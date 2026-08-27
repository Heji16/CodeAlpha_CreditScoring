# Credit Scoring Model

A machine learning project developed as part of the **CodeAlpha Machine Learning Internship – Task 1**. The project predicts the credit risk of individuals using historical financial information and a **Random Forest Classifier**.

## 📌 Project Overview

Credit scoring is the process of assessing an individual's credit risk based on financial and credit-related information.

This project uses historical borrower data to build a classification model that predicts whether an individual is likely to represent a higher credit risk.

The workflow includes:

* Data cleaning and preprocessing
* Exploratory data analysis
* Feature preparation
* Model training
* Model evaluation
* Credit-risk prediction

## 🎯 Objective

The main objectives of this project are to:

* Analyze historical credit-related data
* Preprocess financial and demographic features
* Train a machine learning classification model
* Evaluate the model using appropriate classification metrics
* Identify the model's ability to distinguish between different credit-risk classes
* Build a reusable prediction script for new borrower data

## 📊 Dataset

The project uses the **Give Me Some Credit** dataset, which contains historical borrower information and credit-risk indicators.

Important features include:

| Feature                                | Description                                 |
| -------------------------------------- | ------------------------------------------- |
| `RevolvingUtilizationOfUnsecuredLines` | Ratio of credit utilization                 |
| `age`                                  | Borrower's age                              |
| `NumberOfTime30-59DaysPastDueNotWorse` | Number of times payment was 30–59 days late |
| `DebtRatio`                            | Debt-to-income ratio                        |
| `MonthlyIncome`                        | Monthly income                              |
| `NumberOfOpenCreditLinesAndLoans`      | Number of open credit accounts and loans    |
| `NumberOfTimes90DaysLate`              | Number of times payments were 90+ days late |
| `NumberRealEstateLoansOrLines`         | Number of real-estate loans or credit lines |
| `NumberOfTime60-89DaysPastDueNotWorse` | Number of times payment was 60–89 days late |
| `NumberOfDependents`                   | Number of dependents                        |

The target variable represents the borrower's credit-risk status.

> **Note:** The original dataset is not included in this repository.

## 🔄 Machine Learning Workflow

### 1. Data Preprocessing

The data preparation process includes:

* Handling missing values
* Selecting relevant features
* Preparing the target variable
* Splitting the dataset into training and testing sets
* Addressing class imbalance during model training

### 2. Model Training

The project uses a **Random Forest Classifier** for credit-risk classification.

The model is configured with:

* `n_estimators = 100`
* `max_depth = 10`
* `class_weight = "balanced"`
* Stratified train-test split
* Test size: **20%**

The trained model is saved as:

```text
credit_scoring_model.pkl
```

### 3. Model Evaluation

The model is evaluated using:

* Precision
* Recall
* F1-score
* ROC-AUC

## 📈 Model Performance

The final model achieved the following results on the evaluation data:

| Metric    |      Score |
| --------- | ---------: |
| Precision | **0.2208** |
| Recall    | **0.7646** |
| F1-score  | **0.3426** |
| ROC-AUC   | **0.8653** |

### Interpretation

The model achieved a **ROC-AUC of 0.8653**, indicating good ability to distinguish between the two credit-risk classes.

The relatively high recall shows that the model identifies a large proportion of the positive-risk cases, while the lower precision indicates that some predicted positive cases are false positives.

## 🔮 Making Predictions

The `predict.py` script loads the trained model and uses borrower information to generate a credit-risk prediction.

Example borrower information includes:

```text
Age: 40
Monthly Income: 5000
Debt Ratio: 0.3
Credit Utilization: 0.5
Number of Open Credit Lines: 8
Number of Dependents: 1
```

The script produces:

* Credit-risk prediction
* Risk probability

Run the prediction script with:

```bash
python predict.py
```

## 📁 Project Structure

```text
CodeAlpha_CreditScoring/
│
├── credit_scoring_analysis.ipynb
├── train_model.py
├── predict.py
├── model_results.csv
├── credit_scoring_model.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

| File                            | Purpose                                                    |
| ------------------------------- | ---------------------------------------------------------- |
| `credit_scoring_analysis.ipynb` | Data analysis and exploratory work                         |
| `train_model.py`                | Trains and evaluates the Random Forest model               |
| `predict.py`                    | Generates predictions for new borrower data                |
| `model_results.csv`             | Stores model evaluation results                            |
| `credit_scoring_model.pkl`      | Saved trained machine learning model                       |
| `requirements.txt`              | Python dependencies                                        |
| `.gitignore`                    | Prevents unnecessary or sensitive files from being tracked |
| `README.md`                     | Project documentation                                      |

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Heji16/CodeAlpha_CreditScoring.git
cd CodeAlpha_CreditScoring
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Usage

### Train the model

```bash
python train_model.py
```

This trains the Random Forest classifier, displays the evaluation metrics, and saves the trained model.

### Generate a prediction

```bash
python predict.py
```

The prediction script loads the saved model and evaluates the example borrower data.

### Explore the analysis

Open:

```text
credit_scoring_analysis.ipynb
```

with Jupyter Notebook to view the exploratory analysis and modelling workflow.

## 🛠️ Technologies Used

* **Python 3**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Joblib**
* **Jupyter Notebook**
* **Matplotlib / Seaborn** for data visualization

## ⚠️ Limitations

This project is intended for educational and internship purposes.

The model's predictions should not be treated as actual financial or lending decisions. Credit-risk modelling in real-world applications requires additional validation, domain-specific considerations, fairness analysis, monitoring, and regulatory compliance.

## 🏁 Conclusion

This project demonstrates an end-to-end machine learning workflow for credit-risk classification, from data preprocessing and exploratory analysis to model training, evaluation, and prediction.

The Random Forest model achieved a **ROC-AUC of 0.8653**, demonstrating good overall discriminatory performance on the evaluation data.

## 👩🏻 Author

**Heji16**

Developed as part of the **CodeAlpha Machine Learning Internship – Task 1**.

## 📄 License

This project is intended for educational and internship purposes.
