import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the classifier from the pickle file
with open('Model.pkl', 'rb') as pickle_in:  # Ensure correct file format
    Model= pickle.load(pickle_in)

def predict_viral_load_failure(input_data):
    """
    Predict viral load failure based on user inputs.
    """
    input_array = np.array([input_data])
    prediction = classifier.predict(input_array)[0]
    prediction_proba = classifier.predict_proba(input_array)[0]
    return prediction, prediction_proba

def main():
    # Title of the application
    st.title("Prediction of Viral Load Failure")

    # Input fields
    sex = st.selectbox("Sex", ["Male", "Female", "Other"], index=0)
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    religion = st.text_input("Religion")
    educational_level = st.selectbox(
        "Educational Level Attained", 
        ["None", "Primary", "Secondary", "Tertiary", "Other"], 
        index=0
    )
    marital_status = st.selectbox(
        "Current Marital Status", 
        ["Single", "Married", "Divorced", "Widowed", "Other"], 
        index=0
    )
    viral_load_result = st.number_input("Viral Load Result", min_value=0, step=1)
    duration_on_art = st.number_input("Duration on ART (Months)", min_value=0, step=1)
    who_stage = st.selectbox("WHO Stage", ["Stage 1", "Stage 2", "Stage 3", "Stage 4"], index=0)
    baseline_cd4_count = st.number_input("Baseline CD4 Count", min_value=0, step=1)
    recent_cd4_count = st.number_input("Recent CD4 Count", min_value=0, step=1)
    last_weight = st.number_input("Last Weight Recorded (kg)", min_value=0.0, step=0.1)
    first_weight = st.number_input("First Weight Recorded (kg)", min_value=0.0, step=0.1)
    current_regimen = st.text_input("Current Regimen")
    first_regimen = st.text_input("First Regimen")
    cotrimoxazole = st.selectbox("Client had Cotrimoxazole before?", ["Yes", "No"], index=0)
    disclosed_status = st.selectbox("Disclosed Status", ["Yes", "No"], index=0)
    functional_status = st.selectbox("Functional Status", ["Working", "Ambulatory", "Bedridden"], index=0)
    days_late_pharm = st.number_input("Days Late for Pharmacy Pickup", min_value=0, step=1)
    presence_of_ois = st.selectbox("Presence of OIs", ["Yes", "No"], index=0)
    virology = st.text_input("Virology")
    month = st.selectbox(
        "Month", 
        ["January", "February", "March", "April", "May", "June", 
         "July", "August", "September", "October", "November", "December"], 
        index=0
    )
    date = st.date_input("Date")
    year = st.number_input("Year", min_value=1900, max_value=2100, step=1)

    # Prediction button
    if st.button("Predict"):
        input_data = [
            sex, age, religion, educational_level, marital_status, viral_load_result,
            duration_on_art, who_stage, baseline_cd4_count, recent_cd4_count, 
            last_weight, first_weight, current_regimen, first_regimen, cotrimoxazole, 
            disclosed_status, functional_status, days_late_pharm, presence_of_ois, 
            virology, month, date.year
        ]
        prediction, prediction_proba = predict_viral_load_failure(input_data)

        st.write("Prediction:", "High Risk" if prediction == 1 else "Low Risk")
        st.write("Prediction Probability:", prediction_proba)

if __name__ == "__main__":
    main()
