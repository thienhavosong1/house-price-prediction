🏠 Dự đoán giá nhà bằng Machine Learning
📌 Tổng quan

Dự án này sử dụng Machine Learning để dự đoán giá bán của nhà dựa trên các đặc trưng của ngôi nhà.

Thông qua việc phân tích dữ liệu và huấn luyện mô hình học máy, hệ thống có thể ước lượng giá bán của nhà dựa trên các yếu tố như:

GrLivArea – Diện tích sinh hoạt của ngôi nhà
OverallQual – Chất lượng tổng thể của ngôi nhà
GarageCars – Sức chứa của gara

Dự án minh họa cách phân tích dữ liệu và áp dụng Machine Learning để giải quyết bài toán dự đoán giá nhà trong thực tế.

📊 Dataset

Dataset được sử dụng trong dự án là Ames Housing Dataset, có trên Kaggle.

Nguồn dataset:
House Prices: Advanced Regression Techniques

https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques

Thông tin về dataset:

1460 mẫu dữ liệu
80 thuộc tính (features) mô tả các đặc điểm của ngôi nhà

Một số đặc trưng trong dataset gồm:

diện tích nhà
chất lượng xây dựng
số phòng
năm xây dựng
diện tích tầng hầm
sức chứa gara
giá bán của nhà

Biến mục tiêu cần dự đoán là:

SalePrice
⚙️ Công nghệ sử dụng
Công nghệ	Mục đích
Python	Ngôn ngữ lập trình
Pandas	Xử lý và phân tích dữ liệu
NumPy	Tính toán số học
Matplotlib	Vẽ biểu đồ
Seaborn	Trực quan hóa dữ liệu
Scikit-learn	Xây dựng mô hình Machine Learning
🔄 Quy trình Machine Learning

Dự án thực hiện theo quy trình Machine Learning cơ bản:

Tiền xử lý dữ liệu (Data preprocessing)
Phân tích dữ liệu khám phá (EDA)
Lựa chọn đặc trưng (Feature selection)
Chia dữ liệu Train/Test
Huấn luyện mô hình
Đánh giá mô hình
Trực quan hóa kết quả
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
📂 Giải thích các file
data/

Thư mục chứa dataset dùng để huấn luyện và kiểm tra mô hình.

images/

Chứa các biểu đồ được tạo ra trong quá trình phân tích dữ liệu và đánh giá mô hình.

main.py

Chương trình chính của dự án, thực hiện các bước:

đọc dataset
tiền xử lý dữ liệu
phân tích dữ liệu (EDA)
lựa chọn feature
huấn luyện mô hình
đánh giá mô hình
tạo các biểu đồ
dubaogianha.py

Chương trình dùng để dự đoán giá nhà bằng mô hình đã được huấn luyện.

model.pkl

File lưu mô hình Machine Learning đã được huấn luyện, giúp sử dụng lại mô hình mà không cần huấn luyện lại từ đầu.

requirements.txt

Danh sách các thư viện Python cần thiết để chạy dự án.

📈 Trực quan hóa dữ liệu
Phân bố giá nhà

Biểu đồ thể hiện phân bố giá nhà trong dataset.

Correlation Matrix

Biểu đồ thể hiện mức độ tương quan giữa các biến trong dữ liệu.

Diện tích nhà và giá nhà

Biểu đồ scatter thể hiện mối quan hệ giữa diện tích nhà và giá bán.

So sánh giá thực tế và giá dự đoán

Biểu đồ so sánh giá nhà thực tế với giá nhà được mô hình dự đoán.

Phân bố sai số dự đoán

Biểu đồ thể hiện phân bố sai số của mô hình.

Mức độ quan trọng của các đặc trưng

Biểu đồ thể hiện mức độ quan trọng của các feature trong mô hình Random Forest.

🤖 Các mô hình Machine Learning

Dự án sử dụng hai mô hình Machine Learning.

Linear Regression

Mô hình hồi quy tuyến tính cơ bản dùng để dự đoán giá nhà.

Ưu điểm:

đơn giản
dễ hiểu
huấn luyện nhanh
Random Forest Regressor

Random Forest là thuật toán ensemble learning, kết hợp nhiều cây quyết định.

Ưu điểm:

độ chính xác cao
giảm hiện tượng overfitting
xử lý tốt các dữ liệu phức tạp
📊 Đánh giá mô hình

Các mô hình được đánh giá bằng các chỉ số:

MAE (Mean Absolute Error)
RMSE (Root Mean Squared Error)
R² Score

Kết quả thực nghiệm cho thấy:

Random Forest Regressor cho hiệu suất tốt hơn Linear Regression.

🚀 Cách chạy chương trình
1️⃣ Clone repository
git clone https://github.com/thienhavosong1/house-price-prediction.git
2️⃣ Cài đặt các thư viện cần thiết
pip install -r requirements.txt
3️⃣ Huấn luyện mô hình
python main.py

Chương trình sẽ:

đọc dữ liệu
huấn luyện mô hình
tạo các biểu đồ
4️⃣ Dự đoán giá nhà
python dubaogianha.py

Chương trình sẽ sử dụng mô hình đã huấn luyện để dự đoán giá nhà.

🔧 Quản lý mã nguồn

Source code của dự án được quản lý bằng Git và lưu trữ trên GitHub.

Repository:

https://github.com/thienhavosong1/house-price-prediction

Git giúp:

quản lý phiên bản mã nguồn
theo dõi lịch sử thay đổi
hỗ trợ làm việc nhóm
📌 Kết luận

Dự án đã xây dựng thành công mô hình dự đoán giá nhà bằng Machine Learning.

Kết quả cho thấy:

Random Forest Regressor cho hiệu suất tốt hơn Linear Regression
các đặc trưng như diện tích sinh hoạt và chất lượng nhà có ảnh hưởng lớn đến giá nhà

Machine Learning có thể được áp dụng hiệu quả trong bài toán dự đoán giá bất động sản.

👨‍💻 Tác giả

Nhóm 6

Phạm Hữu Bằng – 698346 (Nhóm trưởng)
Lưu Quang Vinh – 698585

Machine Learning Project – House Price Prediction
