import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error as mae

data = pd.read_csv("data/train.csv")
print(data.head())
print(data.info())

plt.figure(figsize=(8,5))
sns.histplot(data["SalePrice"], kde = True)
plt.title("Phân bố giá nhà ")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x=data["GrLivArea"] , y = data["SalePrice"])
plt.title("Diện tích nhà vs Giá nhà ")
plt.show()

features = ["GrLivArea" , "OverallQual" , "GarageCars"]
X= data[features]
y = data["SalePrice"]

X_train , X_test , y_train , y_test = train_test_split(
   X,y,test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train , y_train)

y_pred = model.predict(X_test)
print("MAE:", mae(y_test , y_pred))

plt.figure(figsize=(8,5))
plt.scatter(y_test , y_pred)
plt.xlabel("Giá thực tế ")
plt.ylabel("Giá dự đoán ")
plt.title("So sánh giá thực tế và giá dự đoán ")
plt.show()


errors = y_test - y_pred
plt.figure(figsize=(8,5))
sns.histplot(errors , kde = True)
plt.title("Phân bố sai số dự đoán ")
plt.xlabel("Error")
plt.show()




