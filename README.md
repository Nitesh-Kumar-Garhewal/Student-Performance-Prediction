# 🎓 Student Performance Prediction

Machine Learning project that predicts student exam scores based on study habits, attendance, previous scores, and other factors.

## 🚀 Features

- Data preprocessing
- Missing value handling
- Categorical feature encoding
- Random Forest Regression model
- Streamlit web application


## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib


## 📊 Model Performance

- **Model:** Random Forest Regressor
- **Evaluation Metric:** Mean Absolute Error (MAE)
- **Score:** 1.08

## 📂 Project Structure

```text
Student-Performance-Prediction/
│
├── data/
│   └── StudentPerformanceFactors.csv
│
├── models/
│   └── student_model.pkl
│
├── notebooks/
│   └── student_prediction.ipynb
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

## ▶️ Run Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```


## 🎯 Input Features

- Hours Studied
- Attendance
- Previous Scores
- Sleep Hours
- Parental Involvement
- Access to Resources
