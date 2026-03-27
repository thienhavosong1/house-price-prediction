🏠 Dự đoán giá nhà bằng Machine Learning
1. Giới thiệu

Dự án này áp dụng các kỹ thuật Machine Learning để dự đoán giá bán của nhà dựa trên một số đặc trưng của ngôi nhà như:

Diện tích sinh hoạt
Chất lượng tổng thể của ngôi nhà
Sức chứa gara

Bằng cách phân tích dữ liệu và huấn luyện các mô hình học máy, chương trình có thể ước lượng giá bán của một căn nhà với độ chính xác tương đối cao.

Các bước chính của dự án gồm:

Phân tích và khám phá dữ liệu (Exploratory Data Analysis)
Trực quan hóa dữ liệu
Huấn luyện mô hình Machine Learning
Đánh giá mô hình
So sánh hiệu suất các mô hình
2. Dataset

Dự án sử dụng bộ dữ liệu House Prices Dataset.

Dataset bao gồm nhiều thông tin về các căn nhà, ví dụ:

diện tích sinh hoạt
chất lượng xây dựng
số phòng
gara
năm xây dựng
giá bán

Biến mục tiêu cần dự đoán là:

SalePrice
3. Công nghệ và thư viện sử dụng

Dự án được xây dựng bằng Python với các thư viện sau:

Thư viện	Mục đích
pandas	xử lý và phân tích dữ liệu
numpy	tính toán số học
matplotlib	vẽ biểu đồ
seaborn	trực quan hóa dữ liệu
scikit-learn	xây dựng mô hình Machine Learning
4. Cấu trúc thư mục dự án
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
Giải thích các file

data/
Chứa dataset dùng để huấn luyện mô hình.

images/
Chứa các biểu đồ trực quan hóa dữ liệu.

main.py
Chương trình chính thực hiện:

đọc dữ liệu
phân tích dữ liệu
huấn luyện mô hình
đánh giá mô hình

dubaogianha.py
Chương trình dùng để dự đoán giá nhà bằng mô hình đã huấn luyện.

model.pkl
File lưu mô hình Machine Learning sau khi huấn luyện.

requirements.txt
Danh sách các thư viện cần thiết để chạy project.

5. Phân tích dữ liệu (EDA)

Trong quá trình phân tích dữ liệu, dự án sử dụng nhiều biểu đồ trực quan để hiểu rõ hơn về dataset.

Distribution of House Prices

Biểu đồ thể hiện phân bố của giá nhà trong dataset.

Correlation Matrix

Biểu đồ thể hiện mối tương quan giữa các biến trong dataset.

Living Area vs Price

Biểu đồ cho thấy diện tích sinh hoạt có ảnh hưởng lớn đến giá nhà.

Actual vs Predicted Prices

Biểu đồ so sánh giá nhà thực tế và giá dự đoán từ mô hình.

Prediction Error Distribution

Biểu đồ thể hiện phân bố sai số của mô hình dự đoán.

Feature Importance

Biểu đồ thể hiện mức độ quan trọng của từng đặc trưng trong mô hình Random Forest.

6. Các mô hình Machine Learning

Dự án sử dụng hai mô hình Machine Learning:

Linear Regression

Linear Regression là mô hình hồi quy tuyến tính đơn giản dùng để dự đoán giá nhà dựa trên mối quan hệ tuyến tính giữa các biến.

Ưu điểm:

đơn giản
dễ hiểu
huấn luyện nhanh
Random Forest Regressor

Random Forest là thuật toán ensemble learning kết hợp nhiều cây quyết định để cải thiện độ chính xác.

Ưu điểm:

độ chính xác cao
giảm overfitting
hoạt động tốt với dữ liệu phức tạp
7. Đánh giá mô hình

Các mô hình được đánh giá bằng các chỉ số:

MAE (Mean Absolute Error)

Sai số trung bình tuyệt đối giữa giá trị dự đoán và giá trị thực.

RMSE (Root Mean Squared Error)

Sai số bình phương trung bình.

R² Score

Đo lường mức độ phù hợp của mô hình với dữ liệu.

Giá trị R² càng gần 1 thì mô hình càng tốt.

8. Hướng dẫn cài đặt
Bước 1: Clone repository
git clone https://github.com/thienhavosong1/house-price-prediction.git
Bước 2: Cài đặt thư viện
pip install -r requirements.txt
Bước 3: Chạy chương trình

Huấn luyện mô hình và tạo biểu đồ:

python main.py
Bước 4: Dự đoán giá nhà
python dubaogianha.py
9. Quản lý mã nguồn

Source code của dự án được quản lý bằng Git và lưu trữ trên GitHub.

Repository:

https://github.com/thienhavosong1/house-price-prediction

Git giúp:

quản lý phiên bản code
theo dõi lịch sử thay đổi
phát triển dự án hiệu quả
10. Kết luận

Dự án đã xây dựng thành công mô hình dự đoán giá nhà bằng Machine Learning.

Kết quả cho thấy:

mô hình Random Forest Regressor cho độ chính xác cao hơn Linear Regression
các yếu tố như diện tích, chất lượng xây dựng và gara có ảnh hưởng lớn đến giá nhà

Machine Learning có thể được ứng dụng hiệu quả trong dự đoán giá bất động sản.

11. Tác giả

Nhóm 6

Phạm Hữu Bằng – 698346
Lưu Quang Vinh - 698585

Machine Learning Project – House Price Prediction
