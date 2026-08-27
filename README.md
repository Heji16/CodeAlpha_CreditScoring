# TASK 1: CREDIT SCORING MODEL

## Objective

Predict an individual's creditworthiness and identify the likelihood of serious delinquency using historical financial data.

## Dataset

**Give Me Some Credit** dataset.

After preprocessing, the dataset contained **150,000 records and 11 useful columns**.

## Data Preprocessing

* Removed the unnecessary `Unnamed: 0` column.
* Filled missing `MonthlyIncome` values using the median.
* Filled missing `NumberOfDependents` values using the median.
* Checked for missing values after cleaning.
* Split the data into training and testing sets.
* Addressed the imbalanced target variable during model training.

## Model Used

### Random Forest Classifier

A Random Forest classification model was trained to predict whether a customer would experience serious delinquency within two years.

## Model Performance

| Metric    |  Score |
| --------- | -----: |
| Precision | 0.2208 |
| Recall    | 0.7646 |
| F1-Score  | 0.3426 |
| ROC-AUC   | 0.8653 |

The ROC-AUC score of **0.8466** indicates that the model has good ability to distinguish between customers with and without serious delinquency.

## Feature Importance

The most important features identified by the Random Forest model were:

1. `RevolvingUtilizationOfUnsecuredLines`
2. `DebtRatio`
3. `age`
4. `MonthlyIncome`
5. `NumberOfTimes90DaysLate`

## Confusion Matrix

The final model produced the following confusion matrix on the test data:

```text
[[27021   974]
 [ 1270   735]]
```

This shows the model's predictions for customers with no serious delinquency and customers with serious delinquency.

## Prediction

A prediction script was created:

`predict.py`

The trained model was saved locally as:

`credit_scoring_model.pkl`

The model file is excluded from GitHub using `.gitignore`.

## Project Files

* `credit_scoring_analysis.ipynb` - Complete data analysis, preprocessing, visualization, model training and evaluation.
* `train_model.py` - Script for training the machine learning model.
* `predict.py` - Script for making predictions using the trained model.
* `model_results.csv` - Final model evaluation results.
* `README.md` - Project documentation.

## Conclusion

This project demonstrates how machine learning can be applied to financial data to assess credit risk and predict the likelihood of serious delinquency.

The Random Forest model achieved a **ROC-AUC of 0.8466**, demonstrating good classification ability for distinguishing between customers with and without serious delinquency.
