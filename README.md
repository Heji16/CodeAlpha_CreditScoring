TASK 1: CREDIT SCORING MODEL



Objective

Predict an individual's creditworthiness using past financial data.



Dataset

Give Me Some Credit dataset

150,000 records and 11 useful columns after cleaning.



Data Preprocessing

\- Removed the unnecessary Unnamed: 0 column.

\- Filled missing MonthlyIncome values with the median.

\- Filled missing NumberOfDependents values with the median.

\- Checked for missing values after cleaning.



Models Used

1\. Logistic Regression

2\. Random Forest Classifier



Random Forest Performance

Precision: 0.2208

Recall: 0.7646

F1-Score: 0.3426

ROC-AUC: 0.8653



Feature Importance

The most important features were:

1\. RevolvingUtilizationOfUnsecuredLines

2\. NumberOfTimes90DaysLate

3\. NumberOfTime30-59DaysPastDueNotWorse

4\. NumberOfTime60-89DaysPastDueNotWorse

5\. age



Prediction

The trained Random Forest model was saved as:

credit\_scoring\_model.pkl



A prediction script was created as:

predict.py



Conclusion

The Random Forest model achieved a ROC-AUC of 0.8653 and showed good ability to identify customers at higher credit risk.

