🏠 House Price Prediction using Machine Learning
📌 Overview

Dự án này sử dụng Machine Learning để dự đoán giá bán của nhà dựa trên các đặc trưng của ngôi nhà.

Thông qua việc phân tích dữ liệu và huấn luyện mô hình, chương trình có thể ước lượng giá bán của nhà dựa trên các yếu tố như:

Diện tích sinh hoạt (GrLivArea)
Chất lượng tổng thể của nhà (OverallQual)
Sức chứa gara (GarageCars)

Dự án bao gồm các bước chính:

Data preprocessing
Exploratory Data Analysis (EDA)
Model training
Model evaluation
Data visualization
📊 Dataset

Dataset được sử dụng là:

House Prices: Advanced Regression Techniques trên Kaggle
(còn được gọi là Ames Housing Dataset)

Dataset bao gồm:

1460 mẫu dữ liệu
80 thuộc tính (features) mô tả đặc điểm của các ngôi nhà

Các thuộc tính bao gồm thông tin như:

diện tích
chất lượng xây dựng
số phòng
năm xây dựng
diện tích tầng hầm
sức chứa gara
giá bán của nhà

Biến mục tiêu cần dự đoán là:

SalePrice

⚙️ Technologies Used

Các thư viện và công nghệ được sử dụng:

Technology	Purpose
Python	Ngôn ngữ lập trình
Pandas	Xử lý dữ liệu
NumPy	Tính toán số học
Matplotlib	Vẽ biểu đồ
Seaborn	Trực quan hóa dữ liệu
Scikit-learn	Xây dựng mô hình Machine Learning
📁 Project Structure
house-price-prediction
│
├── data
│   └── train.csv
│
├── images
│   ├── price_distribution.png
│   ├── correlation_matrix.png
│   ├── area_vs_price.png
│   ├── prediction_vs_actual.png
│   ├── error_distribution.png
│   └── feature_importance.png
│
├── main.py
├── dubaogianha.py
├── model.pkl
├── requirements.txt
└── README.md
📂 Giải thích các file
data/

Chứa dataset dùng để huấn luyện mô hình.

images/

Chứa các biểu đồ phân tích dữ liệu.

main.py

Chương trình chính thực hiện:

đọc dữ liệu
phân tích dữ liệu
huấn luyện mô hình
đánh giá mô hình
tạo biểu đồ
dubaogianha.py

Chương trình dùng để dự đoán giá nhà dựa trên mô hình đã huấn luyện.

model.pkl

File lưu mô hình Machine Learning đã được huấn luyện.

requirements.txt

Danh sách các thư viện cần thiết để chạy project.

📈 Data Visualization
Distribution of House Prices

Biểu đồ cho thấy phân bố giá nhà trong dataset.

Correlation Matrix

Biểu đồ thể hiện mối tương quan giữa các biến trong dữ liệu.

Living Area vs House Price

Biểu đồ thể hiện mối quan hệ giữa diện tích nhà và giá bán.

Actual vs Predicted Prices

So sánh giá nhà thực tế với giá dự đoán của mô hình.

Prediction Error Distribution

Biểu đồ phân bố sai số của mô hình dự đoán.

Feature Importance

Biểu đồ thể hiện mức độ quan trọng của các đặc trưng trong mô hình Random Forest.

🤖 Machine Learning Models

Dự án sử dụng hai mô hình Machine Learning:

Linear Regression

Mô hình hồi quy tuyến tính cơ bản dùng để dự đoán giá nhà.

Ưu điểm:

đơn giản
dễ hiểu
huấn luyện nhanh
Random Forest Regressor

Random Forest là thuật toán ensemble learning kết hợp nhiều cây quyết định.

Ưu điểm:

độ chính xác cao
giảm overfitting
hoạt động tốt với dữ liệu phức tạp
📊 Model Evaluation

Các mô hình được đánh giá bằng các chỉ số:

MAE (Mean Absolute Error)
RMSE (Root Mean Squared Error)
R² Score

Kết quả thực nghiệm cho thấy:

Random Forest Regressor cho hiệu suất tốt hơn Linear Regression.

🚀 How to Run the Project
1️⃣ Clone repository
git clone https://github.com/thienhavosong1/house-price-prediction.git
2️⃣ Install required libraries
pip install -r requirements.txt
3️⃣ Run the training script
python main.py

Chương trình sẽ:

đọc dữ liệu
huấn luyện mô hình
tạo các biểu đồ phân tích dữ liệu
4️⃣ Run prediction script
python dubaogianha.py

Chương trình sẽ sử dụng mô hình đã huấn luyện để dự đoán giá nhà.

🔧 Source Code Management

Source code được quản lý bằng Git và lưu trữ trên GitHub.

Repository:

https://github.com/thienhavosong1/house-price-prediction

Git giúp:

quản lý phiên bản
theo dõi thay đổi của code
làm việc nhóm hiệu quả
📌 Conclusion

Dự án đã xây dựng thành công mô hình dự đoán giá nhà sử dụng Machine Learning.

Kết quả cho thấy:

Random Forest Regressor có hiệu suất tốt hơn Linear Regression
các đặc trưng như diện tích sinh hoạt (GrLivArea) và chất lượng tổng thể (OverallQual) có ảnh hưởng lớn đến giá nhà

Machine Learning có thể được áp dụng hiệu quả trong lĩnh vực dự đoán giá bất động sản.

👨‍💻 Author

Nhóm 6

Phạm Hữu Bằng – 698346 (Nhóm trưởng)
Lưu Quang Vinh – 698585

Machine Learning Project – House Price Prediction
