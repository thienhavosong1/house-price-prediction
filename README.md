# 🏠 House Price Prediction using Machine Learning

This project predicts house prices using Machine Learning models based on housing features such as living area, overall quality, and garage capacity.

The goal of this project is to build a regression model that can estimate the selling price of a house using data analysis and machine learning techniques.

---

## 📊 Project Overview

House prices depend on many factors such as area, quality of construction, and available facilities.
In this project, we analyze housing data and apply machine learning algorithms to predict house prices.

Two regression models are implemented and compared:

* Linear Regression
* Random Forest Regressor

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 📂 Project Structure

```
house-price-prediction
│
├── data/
│   └── train.csv
│
├── images/
│   ├── price_distribution.png
│   ├── correlation_matrix.png
│   └── house_price_vs_area.png
│
├── main.py
├── dubaoianha.py
├── model.pkl
├── requirements.txt
└── README.md
```

---

## 📈 Data Analysis

The project includes several visualizations to understand the dataset:

* Distribution of house prices
* Correlation matrix of numerical features
* Relationship between living area and price
* Prediction error distribution

These visualizations help identify important features affecting house prices.

---

## 🤖 Machine Learning Models

### 1. Linear Regression

A basic regression model used as a baseline to understand the relationship between features and house prices.

### 2. Random Forest Regressor

An ensemble learning model that improves prediction performance by combining multiple decision trees.

---

## 📊 Model Evaluation

Models are evaluated using the following metrics:

* **MAE (Mean Absolute Error)**
* **RMSE (Root Mean Squared Error)**
* **R² Score**

Random Forest generally provides better prediction performance compared to Linear Regression.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/thienhavosong1/house-price-prediction.git
```

### 2️⃣ Install required libraries

```
pip install -r requirements.txt
```

### 3️⃣ Run the training script

```
python main.py
```

### 4️⃣ Run prediction script

```
python dubaoianha.py
```

---

## 📌 Features Used in Prediction

The main features used for training the model include:

* **GrLivArea** – Above ground living area
* **OverallQual** – Overall quality of the house
* **GarageCars** – Garage capacity

These features show strong correlation with house prices.

---

## 📚 Dataset

The dataset used in this project is a housing dataset containing information about houses and their selling prices.

---

## 👨‍💻 Author

**Nhóm 6 - Phạm Hữu Bằng (698346) "

Machine Learning Project – House Price Prediction
