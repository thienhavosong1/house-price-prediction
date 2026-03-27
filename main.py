

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

np.random.seed(42)


# =========================
# 2. Create folder for images
# =========================

os.makedirs("images", exist_ok=True)


# =========================
# 3. Load Dataset
# =========================

print("Loading dataset...")

data = pd.read_csv("data/train.csv")

print("\nDataset Preview:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nDataset Statistics:")
print(data.describe())


# =========================
# 4. Handle Missing Values
# =========================

print("\nHandling missing values...")

data.fillna(data.mean(numeric_only=True), inplace=True)


# =========================
# 5. Exploratory Data Analysis
# =========================

# Distribution of house prices

plt.figure(figsize=(8,5))

sns.histplot(data["SalePrice"], kde=True)

plt.title("Distribution of House Prices")

plt.xlabel("SalePrice")

plt.ylabel("Count")

plt.savefig("images/price_distribution.png")

plt.show()



# =========================
# 6. Correlation Matrix
# =========================

corr = data.corr(numeric_only=True)

plt.figure(figsize=(12,10))

sns.heatmap(corr, cmap="coolwarm", center=0)

plt.title("Correlation Matrix")

plt.savefig("images/correlation_matrix.png")

plt.show()



# =========================
# 7. Living Area vs Price
# =========================

plt.figure(figsize=(8,5))

sns.scatterplot(
    x=data["GrLivArea"],
    y=data["SalePrice"]
)

plt.title("Living Area vs House Price")

plt.xlabel("GrLivArea")

plt.ylabel("SalePrice")

plt.savefig("images/area_vs_price.png")

plt.show()



# =========================
# 8. Feature Selection
# =========================

print("\nSelecting important features...")

features = [
    "GrLivArea",
    "OverallQual",
    "GarageCars"
]

X = data[features]

y = data["SalePrice"]



# =========================
# 9. Train-Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# =========================
# 10. Linear Regression Model
# =========================

print("\nTraining Linear Regression...")

lr_model = LinearRegression()

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)



# =========================
# 11. Evaluate Linear Regression
# =========================

lr_mae = mean_absolute_error(y_test, lr_pred)

lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))

lr_r2 = r2_score(y_test, lr_pred)


print("\n===== Linear Regression Results =====")

print("MAE:", lr_mae)

print("RMSE:", lr_rmse)

print("R2 Score:", lr_r2)



# =========================
# 12. Actual vs Predicted
# =========================

plt.figure(figsize=(8,5))

plt.scatter(y_test, lr_pred, alpha=0.6)

plt.xlabel("Actual Price")

plt.ylabel("Predicted Price")

plt.title("Actual vs Predicted Prices")

plt.savefig("images/prediction_vs_actual.png")

plt.show()



# =========================
# 13. Error Distribution
# =========================

errors = y_test - lr_pred

plt.figure(figsize=(8,5))

sns.histplot(errors, kde=True)

plt.title("Prediction Error Distribution")

plt.xlabel("Error")

plt.savefig("images/error_distribution.png")

plt.show()



# =========================
# 14. Random Forest Model
# =========================

print("\nTraining Random Forest...")

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)



# =========================
# 15. Evaluate Random Forest
# =========================

rf_mae = mean_absolute_error(y_test, rf_pred)

rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))

rf_r2 = r2_score(y_test, rf_pred)


print("\n===== Random Forest Results =====")

print("MAE:", rf_mae)

print("RMSE:", rf_rmse)

print("R2 Score:", rf_r2)



# =========================
# 16. Model Comparison
# =========================

print("\n===== Model Comparison =====")

print("\nLinear Regression")

print("MAE:", lr_mae)

print("RMSE:", lr_rmse)

print("R2:", lr_r2)


print("\nRandom Forest")

print("MAE:", rf_mae)

print("RMSE:", rf_rmse)

print("R2:", rf_r2)



# =========================
# 17. Feature Importance
# =========================

importance = rf_model.feature_importances_

importance_df = pd.DataFrame({

    "Feature": features,

    "Importance": importance

}).sort_values(by="Importance", ascending=False)


plt.figure(figsize=(8,5))

sns.barplot(
    x="Importance",
    y="Feature",
    data=importance_df
)

plt.title("Feature Importance (Random Forest)")

plt.savefig("images/feature_importance.png")

plt.show()




print("\nProject Completed Successfully!")


