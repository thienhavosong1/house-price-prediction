import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

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
plt.title("Phân bố giá nhà")
plt.xlabel("SalePrice")
plt.ylabel("Count")
plt.show()


# =========================
# 4. Correlation Matrix
# =========================

plt.figure(figsize=(12,10))
sns.heatmap(data.corr(numeric_only=True), cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()


# =========================
# 5. Diện tích vs giá nhà
# =========================

plt.figure(figsize=(8,5))
sns.scatterplot(x=data["GrLivArea"], y=data["SalePrice"])
plt.title("Diện tích nhà vs Giá nhà")
plt.xlabel("GrLivArea")
plt.ylabel("SalePrice")
plt.show()


# =========================
# 6. Chọn Feature
# =========================

features = ["GrLivArea", "OverallQual", "GarageCars"]

X = data[features]
y = data["SalePrice"]


# =========================
# 7. Chia Train/Test
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


# =========================
# 8. Linear Regression
# =========================

lr_model = LinearRegression()

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

print("\n===== Linear Regression =====")
print("MAE:", mean_absolute_error(y_test, lr_pred))
print("R2 Score:", r2_score(y_test, lr_pred))


# =========================
# 9. Biểu đồ dự đoán
# =========================

plt.figure(figsize=(8,5))
plt.scatter(y_test, lr_pred)
plt.xlabel("Giá thực tế")
plt.ylabel("Giá dự đoán")
plt.title("So sánh giá thực tế và giá dự đoán")
plt.show()


# =========================
# 10. Top Feature Correlation
# =========================

corr = data.corr(numeric_only=True)["SalePrice"].sort_values(ascending=False)

top_corr = corr[1:10]

plt.figure(figsize=(8,6))
sns.barplot(x=top_corr.values, y=top_corr.index)
plt.title("Top Features Affecting House Price")
plt.xlabel("Correlation")
plt.ylabel("Feature")
plt.show()


# =========================
# 11. Phân bố sai số
# =========================

errors = y_test - lr_pred

plt.figure(figsize=(8,5))
sns.histplot(errors, kde=True)
plt.title("Phân bố sai số dự đoán")
plt.xlabel("Error")
plt.savefig("images/error_distribution.png")
plt.show()


# =========================
# 12. Random Forest
# =========================

rf_model = RandomForestRegressor(random_state=42)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

print("\n===== Random Forest =====")
print("MAE:", mean_absolute_error(y_test, rf_pred))
print("R2 Score:", r2_score(y_test, rf_pred))


# =========================
# 13. So sánh mô hình
# =========================

print("\n===== Model Comparison =====")
print("Linear Regression MAE:", mean_absolute_error(y_test, lr_pred))
print("Random Forest MAE:", mean_absolute_error(y_test, rf_pred))