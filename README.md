🏠 Dự đoán giá nhà bằng Machine Learning
📌 Tổng quan

Dự án này sử dụng Machine Learning để dự đoán giá bán của nhà dựa trên các đặc trưng của ngôi nhà.

Thông qua việc phân tích dữ liệu và huấn luyện mô hình, chương trình có thể ước lượng giá bán của nhà dựa trên các yếu tố như:

GrLivArea – Diện tích sinh hoạt của ngôi nhà
OverallQual – Chất lượng tổng thể của ngôi nhà
GarageCars – Sức chứa của gara
📊 Dataset

Dataset được sử dụng là Ames Housing Dataset trên Kaggle.

Dataset gồm:

1460 mẫu dữ liệu
80 thuộc tính

Biến mục tiêu cần dự đoán:

SalePrice
⚙️ Công nghệ sử dụng
Công nghệ	Mục đích
Python	Ngôn ngữ lập trình
Pandas	Xử lý dữ liệu
NumPy	Tính toán số học
Matplotlib	Vẽ biểu đồ
Seaborn	Trực quan hóa dữ liệu
Scikit-learn	Xây dựng mô hình Machine Learning
📁 Cấu trúc dự án
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
📈 Trực quan hóa dữ liệu
Phân bố giá nhà

Correlation Matrix

Diện tích nhà và giá nhà

So sánh giá thực tế và giá dự đoán

Phân bố sai số

Feature Importance

🤖 Mô hình Machine Learning

Dự án sử dụng hai mô hình:

Linear Regression

Mô hình hồi quy tuyến tính cơ bản.

Ưu điểm:

đơn giản
dễ hiểu
huấn luyện nhanh
Random Forest Regressor

Thuật toán ensemble learning kết hợp nhiều cây quyết định.

Ưu điểm:

độ chính xác cao
giảm overfitting
xử lý tốt quan hệ phi tuyến
📊 Đánh giá mô hình

Các mô hình được đánh giá bằng:

MAE
RMSE
R² Score

Kết quả cho thấy:

Random Forest Regressor cho hiệu suất tốt hơn Linear Regression.

🚀 Cách chạy chương trình
Clone repository
git clone https://github.com/thienhavosong1/house-price-prediction.git
Cài đặt thư viện
pip install -r requirements.txt
Huấn luyện mô hình
python main.py
Dự đoán giá nhà
python dubaogianha.py
👨‍💻 Tác giả

Nhóm 6

Phạm Hữu Bằng – 698346 (Nhóm trưởng)
Lưu Quang Vinh – 698585
