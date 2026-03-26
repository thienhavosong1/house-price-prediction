
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# =========================
# Tạo thư mục lưu hình
# =========================

os.makedirs("images", exist_ok=True)


# =========================
# 1. Đọc dataset
# =========================

data = pd.read_csv("data/train.csv")

print("Dataset Preview:")
print(data.head())

print("\nDataset Info:")
print(data.info())


# =========================
# 2. Xử lý dữ liệu thiếu
# =========================

data.fillna(data.mean(numeric_only=True), inplace=True)


# =========================
# 3. Phân bố giá nhà
# =========================

plt.figure(figsize=(8,5))
sns.histplot(data["SalePrice"], kde=True)
plt.title("Distribution of House Prices")
plt.xlabel("SalePrice")
plt.ylabel("Count")
plt.savefig("images/price_distribution.png")
plt.show()


# =========================
# 4. Correlation Matrix
# =========================

plt.figure(figsize=(12,10))
sns.heatmap(data.corr(numeric_only=True), cmap="coolwarm")
plt.title("Correlation Matrix")
plt.savefig("images/correlation_matrix.png")
plt.show()


# =========================
# 5. Area vs Price
# =========================

plt.figure(figsize=(8,5))
sns.scatterplot(x=data["GrLivArea"], y=data["SalePrice"])
plt.title("Living Area vs House Price")
plt.xlabel("GrLivArea")
plt.ylabel("SalePrice")
plt.savefig("images/area_vs_price.png")
plt.show()


# =========================
# 6. Feature Selection
# =========================

features = [
    "GrLivArea",
    "OverallQual",
    "GarageCars"
]

X = data[features]
y = data["SalePrice"]


# =========================
# 7. Train Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================
# 8. Linear Regression
# =========================

lr_model = LinearRegression()

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)


# Metrics

lr_mae = mean_absolute_error(y_test, lr_pred)
lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
lr_r2 = r2_score(y_test, lr_pred)

print("\n===== Linear Regression =====")
print("MAE:", lr_mae)
print("RMSE:", lr_rmse)
print("R2 Score:", lr_r2)


# =========================
# 9. Actual vs Predicted
# =========================

plt.figure(figsize=(8,5))
plt.scatter(y_test, lr_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Prices")
plt.savefig("images/prediction_vs_actual.png")
plt.show()


# =========================
# 10. Error Distribution
# =========================

errors = y_test - lr_pred

plt.figure(figsize=(8,5))
sns.histplot(errors, kde=True)
plt.title("Prediction Error Distribution")
plt.xlabel("Error")
plt.savefig("images/error_distribution.png")
plt.show()


# =========================
# 11. Random Forest
# =========================

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)


# Metrics

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
rf_r2 = r2_score(y_test, rf_pred)

print("\n===== Random Forest =====")
print("MAE:", rf_mae)
print("RMSE:", rf_rmse)
print("R2 Score:", rf_r2)


# =========================
# 12. Model Comparison
# =========================

print("\n===== Model Comparison =====")

print("Linear Regression MAE:", lr_mae)
print("Random Forest MAE:", rf_mae)


# =========================
# 13. Feature Importance
# =========================

importance = rf_model.feature_importances_

plt.figure(figsize=(8,5))
sns.barplot(x=importance, y=features)
plt.title("Feature Importance (Random Forest)")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.savefig("images/feature_importance.png")
plt.show()

