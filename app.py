"""
Smart Healthcare Chronic Disease Risk Analysis
Flask Web Application — Dashboard & Story Embed UI
Author: Yash Kourav (YashYK08)
"""

from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import json
import os

app = Flask(__name__)

# ── Load dataset once at startup ─────────────────────────────────────────────
DATA_PATH = os.path.join(os.path.dirname(__file__), "smart_healthcare_dataset.csv")
df = pd.read_csv(DATA_PATH)

# Derived columns
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 30, 45, 60, 100],
    labels=["18–30", "31–45", "46–60", "61+"],
)
df["bmi_category"] = pd.cut(
    df["bmi"],
    bins=[0, 18.5, 25, 30, 100],
    labels=["Underweight", "Normal", "Overweight", "Obese"],
)
df["exercise_label"] = df["exercise_level"].map(
    {0: "Sedentary", 1: "Light", 2: "Moderate", 3: "Active"}
)
df["smoking_label"] = df["smoking"].map({0: "Non-Smoker", 1: "Smoker"})
df["alcohol_label"] = df["alcohol"].map({0: "No Alcohol", 1: "Drinks Alcohol"})


# ── Helper ────────────────────────────────────────────────────────────────────
def to_json(obj):
    return json.dumps(obj, default=str)


# ── KPI Metrics ───────────────────────────────────────────────────────────────
def get_kpis():
    return {
        "total_patients": len(df),
        "heart_disease_pct": round(df["heart_disease"].mean() * 100, 1),
        "diabetes_pct": round(df["diabetes"].mean() * 100, 1),
        "stroke_pct": round(df["stroke"].mean() * 100, 1),
        "avg_risk_score": round(df["health_risk_score"].mean(), 1),
        "high_risk_count": int((df["health_risk_score"] >= 80).sum()),
        "avg_bmi": round(df["bmi"].mean(), 1),
        "avg_age": round(df["age"].mean(), 1),
    }


# ── Chart data helpers ────────────────────────────────────────────────────────
def disease_by_age_group():
    grp = (
        df.groupby("age_group", observed=True)[["heart_disease", "diabetes", "stroke"]]
        .mean()
        .mul(100)
        .round(1)
        .reset_index()
    )
    return grp.to_dict(orient="list")


def disease_by_bmi():
    grp = (
        df.groupby("bmi_category", observed=True)[
            ["heart_disease", "diabetes", "stroke"]
        ]
        .mean()
        .mul(100)
        .round(1)
        .reset_index()
    )
    return grp.to_dict(orient="list")


def lifestyle_correlation():
    """Smoking & alcohol vs disease rates."""
    result = {}
    for lifestyle, label in [("smoking", "Smoking"), ("alcohol", "Alcohol")]:
        tmp = (
            df.groupby(lifestyle)[["heart_disease", "diabetes", "stroke"]]
            .mean()
            .mul(100)
            .round(1)
        )
        result[label] = {
            "labels": ["No", "Yes"],
            "heart_disease": tmp["heart_disease"].tolist(),
            "diabetes": tmp["diabetes"].tolist(),
            "stroke": tmp["stroke"].tolist(),
        }
    return result


def exercise_vs_risk():
    grp = (
        df.groupby("exercise_label", observed=True)["health_risk_score"]
        .mean()
        .round(1)
        .reset_index()
    )
    order = ["Sedentary", "Light", "Moderate", "Active"]
    grp["exercise_label"] = pd.Categorical(grp["exercise_label"], categories=order, ordered=True)
    grp = grp.sort_values("exercise_label")
    return {
        "labels": grp["exercise_label"].tolist(),
        "risk_scores": grp["health_risk_score"].tolist(),
    }


def symptom_prevalence():
    symptoms = ["fatigue", "chest_pain", "dizziness"]
    rates = (df[symptoms].mean() * 100).round(1)
    return {"labels": symptoms, "values": rates.tolist()}


def risk_distribution():
    bins = [0, 20, 40, 60, 80, 100]
    labels = ["0–20", "21–40", "41–60", "61–80", "81–100"]
    counts = pd.cut(df["health_risk_score"], bins=bins, labels=labels).value_counts().sort_index()
    return {"labels": labels, "values": counts.tolist()}


def gender_disease():
    grp = (
        df.groupby("gender")[["heart_disease", "diabetes", "stroke"]]
        .mean()
        .mul(100)
        .round(1)
        .reset_index()
    )
    return grp.to_dict(orient="list")


def age_risk_scatter():
    """Sample 500 points for scatter."""
    sample = df.sample(min(500, len(df)), random_state=42)
    return {
        "age": sample["age"].tolist(),
        "risk": sample["health_risk_score"].tolist(),
        "disease": (sample["heart_disease"] | sample["diabetes"] | sample["stroke"])
        .astype(int)
        .tolist(),
    }


def clinical_averages():
    cols = ["blood_pressure", "cholesterol", "glucose", "bmi"]
    avgs = df.groupby("heart_disease")[cols].mean().round(1)
    return {
        "cols": cols,
        "no_disease": avgs.loc[0].tolist() if 0 in avgs.index else [],
        "with_disease": avgs.loc[1].tolist() if 1 in avgs.index else [],
    }


# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", kpis=get_kpis())


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", kpis=get_kpis())


@app.route("/story")
def story():
    return render_template("story.html", kpis=get_kpis())


@app.route("/api/charts")
def api_charts():
    data = {
        "disease_by_age": disease_by_age_group(),
        "disease_by_bmi": disease_by_bmi(),
        "lifestyle": lifestyle_correlation(),
        "exercise_risk": exercise_vs_risk(),
        "symptoms": symptom_prevalence(),
        "risk_distribution": risk_distribution(),
        "gender_disease": gender_disease(),
        "scatter": age_risk_scatter(),
        "clinical": clinical_averages(),
    }
    return jsonify(data)


@app.route("/api/kpis")
def api_kpis():
    return jsonify(get_kpis())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
