import streamlit as st
import joblib
import pandas as pd


model = joblib.load(
    "models/student_model.pkl"
)


st.title("🎓 Student Performance Prediction")


hours = st.number_input(
    "Hours Studied",
    min_value=0
)


attendance = st.number_input(
    "Attendance %",
    min_value=0,
    max_value=100
)


parent = st.selectbox(
    "Parental Involvement",
    ["Low","Medium","High"]
)


resources = st.selectbox(
    "Access to Resources",
    ["Low","Medium","High"]
)


sleep = st.number_input(
    "Sleep Hours"
)


previous = st.number_input(
    "Previous Scores"
)


if st.button("Predict Exam Score"):


    input_data = pd.DataFrame(
        {
            "Hours_Studied":[hours],
            "Attendance":[attendance],
            "Parental_Involvement":[parent],
            "Access_to_Resources":[resources],
            "Extracurricular_Activities":["No"],
            "Sleep_Hours":[sleep],
            "Previous_Scores":[previous],
            "Motivation_Level":["Medium"],
            "Internet_Access":["Yes"],
            "Tutoring_Sessions":[1],
            "Family_Income":["Medium"],
            "Teacher_Quality":["Medium"],
            "School_Type":["Public"],
            "Peer_Influence":["Positive"],
            "Physical_Activity":[3],
            "Learning_Disabilities":["No"],
            "Parental_Education_Level":["College"],
            "Distance_from_Home":["Near"],
            "Gender":["Male"]
        }
    )


    prediction = model.predict(
        input_data
    )


    st.success(
        f"Predicted Exam Score: {prediction[0]:.2f}"
    )