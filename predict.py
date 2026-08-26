import pandas as pd
import joblib


# Load the trained model
model = joblib.load("credit_scoring_model.pkl")


# Example borrower data
borrower = pd.DataFrame([{
    "RevolvingUtilizationOfUnsecuredLines": 0.5,
    "age": 40,
    "NumberOfTime30-59DaysPastDueNotWorse": 0,
    "DebtRatio": 0.3,
    "MonthlyIncome": 5000,
    "NumberOfOpenCreditLinesAndLoans": 8,
    "NumberOfTimes90DaysLate": 0,
    "NumberRealEstateLoansOrLines": 1,
    "NumberOfTime60-89DaysPastDueNotWorse": 0,
    "NumberOfDependents": 1
}])


# Make prediction
prediction = model.predict(borrower)[0]
probability = model.predict_proba(borrower)[0, 1]


# Display result
print("Credit Risk Prediction")
print("----------------------")

if prediction == 1:
    print("Prediction: High Risk")
else:
    print("Prediction: Low Risk")

print("Risk Probability:", round(probability * 100, 2), "%")