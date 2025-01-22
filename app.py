import streamlit
import numpy
import pandas
import pickle


from import image

#Load the model 
import pickle

# Load the classifier from the pickle file
with open('classifier.rb', 'rb') as pickle_in:
    classifier = pickle.load(pickle_in)


def welcome():
    'welcome All'

    def prediction of Viral load failure(Sex,AGE, Religion,EducationalLevelAttained,CurrentMaritalStatus,ViralLoad_Result,Duration_on_art_Months,Who_Stage,Baseline_CD4_count,Recent_CD4_count,Last_Weight_Recorded,First_Weight_Recorded,Current_regimen,first_regimen, Client_had_Cotrimoxazole_before, Disclosed_Status,functional_status,DaysLate_for_Pharm,Presence_of_OIs,Virology,Month,Date,year ):
    
    prediction=classifier.predict([[Sex,AGE, Religion,EducationalLevelAttained,CurrentMaritalStatus,ViralLoad_Result,Duration_on_art_Months,Who_Stage,Baseline_CD4_count,Recent_CD4_count,Last_Weight_Recorded,First_Weight_Recorded,Current_regimen,first_regimen, Client_had_Cotrimoxazole_before, Disclosed_Status,functional_status,DaysLate_for_Pharm,Presence_of_OIs,Virology,Month,Date,year ]])

    print (prediction)
    return prediction

def main()
    st.title('Prediction of Viral load failure')
    html temp
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hospital Page</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #007BFF; /* Blue background */
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        .container {
            width: 80%;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.8); /* Slightly transparent white */
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }
        .container img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
        }
        h1 {
            color: #007BFF; /* Blue text to contrast the background */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Our Hospital</h1>
        <p>Committed to delivering quality healthcare services.</p>
        <img src="hospital.jpg" alt="Hospital Image">
    </div>
</body>
</html>


import streamlit as st

# Title
st.title("Patient Information Form")

# Input fields for each variable
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
who_stage = st.selectbox(
    "WHO Stage",
    ["Stage 1", "Stage 2", "Stage 3", "Stage 4"],
    index=0
)
baseline_cd4_count = st.number_input("Baseline CD4 Count", min_value=0, step=1)
recent_cd4_count = st.number_input("Recent CD4 Count", min_value=0, step=1)
last_weight = st.number_input("Last Weight Recorded (kg)", min_value=0.0, step=0.1)
first_weight = st.number_input("First Weight Recorded (kg)", min_value=0.0, step=0.1)
current_regimen = st.text_input("Current Regimen")
first_regimen = st.text_input("First Regimen")
cotrimoxazole = st.selectbox(
    "Client had Cotrimoxazole before?",
    ["Yes", "No"],
    index=0
)
disclosed_status = st.selectbox(
    "Disclosed Status",
    ["Yes", "No"],
    index=0
)
functional_status = st.selectbox(
    "Functional Status",
    ["Working", "Ambulatory", "Bedridden"],
    index=0
)
days_late_pharm = st.number_input("Days Late for Pharmacy Pickup", min_value=0, step=1)
presence_of_ois = st.selectbox(
    "Presence of OIs",
    ["Yes", "No"],
    index=0
)
virology = st.text_input("Virology")
month = st.selectbox(
    "Month",
    [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ],
    index=0
)
date = st.date_input("Date")
year = st.number_input("Year", min_value=1900, max_value=2100, step=1)

# Button to submit form
if st.button("Submit"):
    st.write("Form Submitted Successfully!")
    st.write("Collected Information:")
    st.write({
        "Sex": sex,
        "Age": age,
        "Religion": religion,
        "Educational Level Attained": educational_level,
        "Current Marital Status": marital_status,
        "Viral Load Result": viral_load_result,
        "Duration on ART (Months)": duration_on_art,
        "WHO Stage": who_stage,
        "Baseline CD4 Count": baseline_cd4_count,
        "Recent CD4 Count": recent_cd4_count,
        "Last Weight Recorded": last_weight,
        "First Weight Recorded": first_weight,
        "Current Regimen": current_regimen,
        "First Regimen": first_regimen,
        "Client had Cotrimoxazole before": cotrimoxazole,
        "Disclosed Status": disclosed_status,
        "Functional Status": functional_status,
        "Days Late for Pharmacy": days_late_pharm,
        "Presence of OIs": presence_of_ois,
        "Virology": virology,
        "Month": month,
        "Date": date,
        "Year": year,
    })

    date = st.date_input("Date")
year = st.number_input("Year", min_value=1900, max_value=2100, step=1)

# Prediction button
if st.button("Predict"):
    # Prepare input data for prediction
    input_data = [
        sex, age, religion, educational_level, marital_status, viral_load_result,
        duration_on_art, who_stage, baseline_cd4_count, recent_cd4_count, last_weight,
        first_weight, current_regimen, first_regimen, cotrimoxazole, disclosed_status,
        functional_status, days_late_pharm, presence_of_ois, virology, month, date, year
    ]
    # Make prediction
    processed_data = np.array([input_data])  # Convert input data to numpy array (for model compatibility)
    prediction = model.predict(processed_data)
    prediction_proba = model.predict_proba(processed_data)

    # Display the prediction result
    st.write("Prediction:", "High Risk" if prediction[0] == 1 else "Low Risk")
    st.write("Prediction Probability:", prediction_proba)

    if__name=='__main__':
       main()



