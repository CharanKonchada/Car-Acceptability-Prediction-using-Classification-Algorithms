Absolutely, Charan! Here's a professional and clean `README.md` you can use for your **Car Acceptancy Prediction** GitHub repository:

---

# 🚗 Car Acceptancy Prediction using Machine Learning

This project predicts car acceptability based on various features like buying price, maintenance cost, number of doors, person capacity, luggage boot size, and safety rating using multiple classification algorithms. The final model, trained using **XGBoost**, achieved high accuracy and was deployed via a **Flask web application**.

---

## 📊 Dataset

* Source: [Kaggle - Car Evaluation Data Set]
* Type: Structured
* Task: Classification
* Target: `class` (unacc, acc, good, vgood)

## 🧠 Models Used

* Logistic Regression
* Ridge Classifier
* K-Nearest Neighbors
* Decision Tree
* Random Forest
* Gradient Boosting
* **XGBoost (Best Performer)**

---

## 🔧 Techniques

* **Ordinal Encoding** for categorical variables  
* **Standard Scaling** for distance-based models (KNN, Logistic)
* **Hyperparameter Tuning** using `GridSearchCV`
* **Model Evaluation** using Accuracy & Cross-Validation Scores

---

## ✅ Best Model - XGBoost

* **Train Accuracy**: 100%
* **Test Accuracy**: 98.55%
* **Cross-Validation Score**: 99.2%

---


## 🧪 Prediction Classes Explained

| Class   | Description  |
| ------- | ------------ |
| `unacc` | Unacceptable |
| `acc`   | Acceptable   |
| `good`  | Good         |
| `vgood` | Very Good    |

---


