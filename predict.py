import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# tạo thư mục images nếu chưa có
os.makedirs("images", exist_ok=True)

# đọc dữ liệu
data = pd.read_csv("data/train.csv")

print(data.head())
print(data.info())

# xử lý dữ liệu thiếu
data.fillna(data.mean(numeric_only=True), inplace=True)

# biểu đồ phân bố giá nhà
plt.figure(figsize=(8,5))
sns.histplot(data["SalePrice"], kde=True)
plt.title("Distribution of House Prices")
plt.savefig("images/price_distribution.png")
plt.show()

# correlation matrix
plt.figure(figsize=(12,10))
sns.heatmap(data.corr(numeric_only=True), cmap="coolwarm")
plt.title("Correlation Matrix")
plt.savefig("images/correlation_matrix.png")
plt.show()

# diện tích vs giá nhà
plt.figure(figsize=(8,5))
sns.scatterplot(x=data["GrLivArea"], y=data["SalePrice"])
plt.title("Living Area vs Price")
plt.savefig("images/area_vs_price.png")
plt.show()

# chọn feature
features = ["GrLivArea", "OverallQual", "GarageCars"]
X = data[features]
y = data["SalePrice"]

# chia train test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

print("Linear Regression MAE:", mean_absolute_error(y_test, lr_pred))

# Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

print("Random Forest MAE:", mean_absolute_error(y_test, rf_pred))

# actual vs predicted
plt.figure(figsize=(8,5))
plt.scatter(y_test, rf_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted")
plt.savefig("images/prediction_vs_actual.png")
plt.show()

# feature importance
importance = rf.feature_importances_

plt.figure(figsize=(8,5))
sns.barplot(x=importance, y=features)
plt.title("Feature Importance")
plt.savefig("images/feature_importance.png")
plt.show()
