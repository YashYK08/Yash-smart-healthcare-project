import pandas as pd
df = pd.read_csv('smart_healthcare_dataset.csv')

df['Age Group'] = df['age'].apply(lambda x: 'Teenager' if x<=30 else ('Young Adult' if x<=40 else ('Adult' if x<=50 else ('Middle Age' if x<=60 else ('Senior' if x<=70 else 'Old')))))
df['BMI Category'] = df['bmi'].apply(lambda x: 'Underweight' if x<18.5 else ('Normal' if x<25 else ('Overweight' if x<30 else 'Obese')))
df['Exercise Category'] = df['exercise_level'].map({0:'Sedentary',1:'Moderate',2:'Active'})

print('=== KPIs ===')
print('Total Patients:', len(df))
print('Heart Disease:', df['heart_disease'].sum())
print('Diabetes:', df['diabetes'].sum())
print('Stroke:', df['stroke'].sum())

print('\n=== Avg BP by Age Group ===')
print(df.groupby('Age Group')['blood_pressure'].mean().round(3))

print('\n=== Alcohol+Smoking by Age Group (avg) ===')
print(df.groupby('Age Group')[['smoking','alcohol']].mean().round(4))

print('\n=== Exercise Distribution ===')
print(df['Exercise Category'].value_counts())
print(df['Exercise Category'].value_counts(normalize=True).round(4))

print('\n=== Age Group Distribution ===')
print(df['Age Group'].value_counts())
print(df['Age Group'].value_counts(normalize=True).round(4))

print('\n=== Heart Disease + Diabetes by BMI Category ===')
print(df.groupby('BMI Category')[['heart_disease','diabetes']].mean().round(4))

print('\n=== Heatmap: Heart Disease by BMI x Exercise ===')
print(df.pivot_table('heart_disease','BMI Category','Exercise Category',aggfunc='mean').round(4))

print('\n=== Fatigue by Age Group ===')
print(df.groupby('Age Group')['fatigue'].value_counts().unstack().fillna(0).astype(int))
