# 🏥 Smart Healthcare – Chronic Disease Risk Analysis

> **Mentor Review Links**
>
> | Link | URL |
> |------|-----|
> | 🐙 **GitHub Repository** | [https://github.com/YashYK08/Yash-smart-healthcare-project](https://github.com/YashYK08/Yash-smart-healthcare-project) |
> | 🚀 **Live Interactive Demo** | [https://yashyk08.github.io/Yash-smart-healthcare-project/](https://yashyk08.github.io/Yash-smart-healthcare-project/) |
> | 📊 **Tableau Workbook (.twb)** | [Download Smart_Healthcare_Analytics.twb](https://github.com/YashYK08/Yash-smart-healthcare-project/raw/main/Smart_Healthcare_Analytics.twb) |

---

## 📌 Project Overview

This project addresses the growing challenge of **chronic disease identification** — specifically **Heart Disease, Diabetes, and Stroke** — using data analytics and interactive visualizations built on a dataset of **5,000 patients**.

The web application is built with **Flask + Chart.js**, serving as the embedded UI for what would traditionally be Tableau dashboards. It includes:

- ✅ **8 Epics** / **14 Stories** completed
- ✅ **10+ unique visualizations** (bar, line, radar, scatter, doughnut, polar area)
- ✅ **6-scene data story** with narrative insights
- ✅ **KPI metrics** — disease prevalence, risk scores, patient counts
- ✅ **REST API** (`/api/charts`, `/api/kpis`) for data consumption
- ✅ **Responsive design** (mobile-friendly)
- ✅ **Tableau embed placeholder** ready for Tableau Public workbook

---

## 🎯 Scenarios

| Persona | Role | Use Case |
|---------|------|----------|
| 👨‍⚕️ Dr. Michael Carter | Clinical Risk Assessment Officer | Identifies high-risk patients using KPI dashboards and disease-by-age charts |
| 👩‍💻 Emily Rodriguez | Healthcare Data Analyst | Uncovers lifestyle–disease correlations via smoking, alcohol, and exercise charts |
| 🔬 Dr. Priya Nair | Public Health Researcher | Studies population-wide disease patterns and symptom prevalence |

---

## 📊 Dataset

| Feature | Description |
|---------|-------------|
| `age` | Patient age (18–79) |
| `gender` | Male / Female |
| `bmi` | Body Mass Index |
| `exercise_level` | 0 (Sedentary) – 3 (Active) |
| `smoking` | 0 = No, 1 = Yes |
| `alcohol` | 0 = No, 1 = Yes |
| `blood_pressure` | Systolic BP (mmHg) |
| `cholesterol` | mg/dL |
| `glucose` | mg/dL |
| `fatigue` | 0/1 symptom flag |
| `chest_pain` | 0/1 symptom flag |
| `dizziness` | 0/1 symptom flag |
| `heart_disease` | **Target** — 0/1 |
| `diabetes` | **Target** — 0/1 |
| `stroke` | **Target** — 0/1 |
| `health_risk_score` | Composite 0–100 risk score |

**Total records:** 5,000 patients

---

## 🏗️ Technical Architecture

```
smart-healthcare-project/
│
├── app.py                        ← Flask application (routes + data logic)
├── smart_healthcare_dataset.csv  ← Dataset (5,000 patients, 16 features)
├── requirements.txt              ← Python dependencies
│
├── templates/
│   ├── base.html                 ← Shared navbar, footer, Bootstrap 5
│   ├── index.html                ← Landing page with KPIs + project links
│   ├── dashboard.html            ← 10-chart interactive dashboard
│   └── story.html                ← 6-scene data story
│
└── static/
    ├── css/                      ← Custom styles (embedded in base.html)
    └── js/                       ← Chart logic (embedded in templates)
```

**Tech Stack:**
- **Backend:** Python 3.14, Flask 3.x, Pandas, NumPy
- **Frontend:** Bootstrap 5, Chart.js 4, Bootstrap Icons
- **Visualization Tool:** Tableau (Tableau Public for publishing)
- **Version Control:** Git + GitHub

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/YashYK08/Yash-smart-healthcare-project.git
cd Yash-smart-healthcare-project

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Flask app
python app.py

# 4. Open in browser
# http://127.0.0.1:5000
```

### Pages
| Route | Description |
|-------|-------------|
| `/` | Home – KPI cards, project links, scenarios |
| `/dashboard` | Interactive chart dashboard (10 charts) |
| `/story` | 6-scene data narrative |
| `/api/charts` | JSON endpoint – all chart data |
| `/api/kpis` | JSON endpoint – KPI metrics |

---

## 📈 Visualizations Included

| # | Chart Type | Insight |
|---|-----------|---------|
| 1 | Bar Chart | Disease Prevalence by Age Group |
| 2 | Bar Chart | Disease Prevalence by BMI Category |
| 3 | Bar Chart | Smoking vs Disease Rates |
| 4 | Bar Chart | Alcohol vs Disease Rates |
| 5 | Line Chart | Exercise Level vs Avg Risk Score |
| 6 | Doughnut | Symptom Prevalence (Fatigue, Chest Pain, Dizziness) |
| 7 | Bar Chart | Risk Score Distribution |
| 8 | Bar Chart | Disease by Gender |
| 9 | Radar Chart | Clinical Indicators vs Heart Disease |
| 10 | Scatter Plot | Age vs Health Risk Score (500 patients) |

---

## 🔗 Links

| Resource | Link |
|----------|------|
| GitHub Repository | https://github.com/YashYK08/Yash-smart-healthcare-project |
| Tableau Public | https://public.tableau.com/app/profile/yash.kourav |
| Flask Demo | Run locally with `python app.py` |

---

## 📋 Project Completion Checklist

- [x] Data Collection & Extraction from Database
- [x] Connect data with Flask/Python (Pandas)
- [x] Data Preparation for Visualization
- [x] 10+ Unique Visualizations
- [x] Responsive Dashboard Design
- [x] 6-Scene Data Story
- [x] Performance: 5,000 records loaded, data filters, 4 calculation fields
- [x] Web Integration (Flask)
- [x] Dashboard & Story embed UI with Flask
- [x] GitHub Repository published
- [ ] Tableau Public workbook published *(publish .twb to Tableau Public and update link)*
- [ ] Screen recording / explanation video

---

## 👨‍💻 Author

**Yash Kourav**  
GitHub: [@YashYK08](https://github.com/YashYK08)

---

*Smart Healthcare – Chronic Disease Risk Analysis | Healthcare Domain | Individual Project*
