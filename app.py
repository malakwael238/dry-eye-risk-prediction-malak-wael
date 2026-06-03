import streamlit as st
import joblib
import numpy as np

model = joblib.load("dry_eye_model.pkl")

st.set_page_config(page_title="Dry Eye Risk Predictor", layout="centered")

st.title("Dry Eye Risk Predictor")
st.write("Prepared by: Malak Wael")
st.write("This app predicts the risk of Dry Eye Disease using lifestyle, health, and eye-symptom factors.")

gender = st.selectbox("Gender", ["Female", "Male"])
age = st.slider("Age", 18, 45, 25)
sleep_duration = st.slider("Sleep Duration (hours)", 4.0, 10.0, 7.0)
sleep_quality = st.slider("Sleep Quality", 1, 5, 3)
stress_level = st.slider("Stress Level", 1, 5, 3)

heart_rate = st.slider("Heart Rate", 60, 100, 75)
daily_steps = st.slider("Daily Steps", 1000, 20000, 8000)
physical_activity = st.slider("Physical Activity", 0, 180, 60)

height = st.slider("Height (cm)", 150, 200, 165)
weight = st.slider("Weight (kg)", 50, 100, 70)

sleep_disorder = st.selectbox("Sleep Disorder", ["No", "Yes"])
wake_night = st.selectbox("Wake Up During Night", ["No", "Yes"])
sleepy_day = st.selectbox("Feel Sleepy During Day", ["No", "Yes"])
caffeine = st.selectbox("Caffeine Consumption", ["No", "Yes"])
alcohol = st.selectbox("Alcohol Consumption", ["No", "Yes"])
smoking = st.selectbox("Smoking", ["No", "Yes"])
medical_issue = st.selectbox("Medical Issue", ["No", "Yes"])
medication = st.selectbox("Ongoing Medication", ["No", "Yes"])
smart_device = st.selectbox("Smart Device Before Bed", ["No", "Yes"])

screen_time = st.slider("Average Screen Time", 1.0, 10.0, 5.0)
blue_filter = st.selectbox("Blue Light Filter", ["No", "Yes"])
eye_strain = st.selectbox("Discomfort / Eye Strain", ["No", "Yes"])
redness = st.selectbox("Redness in Eye", ["No", "Yes"])
irritation = st.selectbox("Itchiness / Irritation in Eye", ["No", "Yes"])

systolic_bp = st.slider("Systolic Blood Pressure", 90, 150, 120)
diastolic_bp = st.slider("Diastolic Blood Pressure", 60, 100, 80)

def yes_no(value):
    return 1 if value == "Yes" else 0

gender_val = 1 if gender == "Male" else 0

screen_sleep_ratio = screen_time / sleep_duration
bmi = weight / ((height / 100) ** 2)
lifestyle_risk_score = stress_level + screen_time - sleep_quality

input_data = np.array([[
    gender_val,
    age,
    sleep_duration,
    sleep_quality,
    stress_level,
    heart_rate,
    daily_steps,
    physical_activity,
    height,
    weight,
    yes_no(sleep_disorder),
    yes_no(wake_night),
    yes_no(sleepy_day),
    yes_no(caffeine),
    yes_no(alcohol),
    yes_no(smoking),
    yes_no(medical_issue),
    yes_no(medication),
    yes_no(smart_device),
    screen_time,
    yes_no(blue_filter),
    yes_no(eye_strain),
    yes_no(redness),
    yes_no(irritation),
    systolic_bp,
    diastolic_bp,
    screen_sleep_ratio,
    bmi,
    lifestyle_risk_score
]])

if st.button("Predict Dry Eye Risk"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("High Risk of Dry Eye Disease")
        st.write("The result suggests higher risk. Reducing screen time, improving sleep quality, and using eye-care habits may help.")
    else:
        st.success("Low Risk of Dry Eye Disease")
        st.write("The result suggests lower risk, but maintaining healthy lifestyle and screen habits is still recommended.")