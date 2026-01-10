# Data Engineering và Data Science - Vai trò và Trách nhiệm

## Tổng quan
Tài liệu này giải thích sự khác biệt giữa vai trò Data Engineering (DE) và Data Science (DS), trách nhiệm hàng ngày của họ, kỹ năng cần thiết, và cách họ làm việc cùng nhau trong quy trình dự án dữ liệu.

---

## 🔧 Vai trò Data Engineer (DE)

### Công việc hàng ngày

Công việc hàng ngày của Data Engineer bao gồm:

1. **Phát triển Data Pipeline**
   - Xây dựng các pipeline ETL (Extract, Transform, Load)
   - Tự động hóa thu thập dữ liệu từ nhiều nguồn khác nhau
   - Lập lịch và giám sát luồng dữ liệu

2. **Quản lý Hạ tầng Dữ liệu**
   - Thiết lập và duy trì cơ sở dữ liệu (SQL, NoSQL)
   - Quản lý data warehouse (ví dụ: Snowflake, BigQuery, Redshift)
   - Đảm bảo lưu trữ dữ liệu có khả năng mở rộng và hiệu quả

3. **Kiểm tra Chất lượng & Xác thực Dữ liệu**
   - Triển khai kiểm tra chất lượng dữ liệu
   - Xử lý xác thực dữ liệu và xử lý lỗi
   - Giám sát tình trạng data pipeline

4. **Tích hợp Dữ liệu**
   - Kết nối với API và nguồn dữ liệu bên ngoài
   - Tích hợp dữ liệu từ nhiều nguồn
   - Đảm bảo tính nhất quán của dữ liệu giữa các hệ thống

5. **Tối ưu hóa Hiệu suất**
   - Tối ưu hóa truy vấn và xử lý dữ liệu
   - Cải thiện hiệu suất pipeline
   - Quản lý phân vùng và đánh chỉ mục dữ liệu

### Công việc DE trong Repository này

Trong repository này, các công việc Data Engineering bao gồm:

**Ví dụ DE hiện tại:**
- `data/raw/` - Quản lý lưu trữ dữ liệu thô
- `data/processed/` - Tạo tập dữ liệu đã xử lý/làm sạch
- Tải và xác thực dữ liệu trong các script Python

**Đã thêm vào (công việc DE):**
- ✅ Script ETL pipeline (`etl/` directory)
- ✅ Script xác thực dữ liệu
- ✅ Thu thập dữ liệu tự động
- ✅ Ví dụ kết nối database
- ✅ Kiểm tra chất lượng dữ liệu

### Kỹ năng chính cần học cho DE

**Lập trình:**
- Python (pandas, numpy, SQLAlchemy)
- SQL (PostgreSQL, MySQL, v.v.)
- Bash/Shell scripting

**Công cụ & Công nghệ:**
- **Công cụ ETL**: Apache Airflow, Luigi, Prefect
- **Cơ sở dữ liệu**: PostgreSQL, MySQL, MongoDB, Redis
- **Data Warehouse**: BigQuery, Snowflake, Redshift
- **Nền tảng Cloud**: AWS (S3, Glue, EMR), GCP, Azure
- **Big Data**: Apache Spark, Hadoop, Kafka
- **Containerization**: Docker, Kubernetes

**Khái niệm:**
- Thiết kế và chuẩn hóa cơ sở dữ liệu
- Mô hình hóa dữ liệu (star schema, snowflake schema)
- Distributed computing (điện toán phân tán)
- Versioning và lineage dữ liệu
- CI/CD cho data pipeline

---

## 📊 Vai trò Data Scientist (DS)

### Công việc hàng ngày

Công việc hàng ngày của Data Scientist bao gồm:

1. **Exploratory Data Analysis (EDA) - Phân tích Khám phá Dữ liệu**
   - Hiểu phân phối và mô hình dữ liệu
   - Xác định mối tương quan và mối quan hệ
   - Tạo visualization (trực quan hóa)

2. **Feature Engineering - Kỹ thuật Tính năng**
   - Tạo tính năng mới từ dữ liệu hiện có
   - Chọn các tính năng có liên quan
   - Chuyển đổi tính năng cho các mô hình

3. **Phát triển Mô hình**
   - Huấn luyện các mô hình machine learning
   - Hyperparameter tuning (điều chỉnh siêu tham số)
   - Đánh giá và xác thực mô hình

4. **Thử nghiệm**
   - A/B testing
   - Thử nghiệm các thuật toán khác nhau
   - So sánh hiệu suất mô hình

5. **Giao tiếp**
   - Tạo báo cáo và dashboard
   - Trình bày kết quả cho các stakeholder
   - Tài liệu hóa insights và khuyến nghị

### Công việc DS trong Repository này

Trong repository này, công việc Data Science bao gồm:

**Ví dụ DS hiện tại:**
- `projects/iris-classification/` - Dự án ML hoàn chỉnh
- `projects/titanic-survival/` - Feature engineering và modeling
- `kaggle-notebooks/` - Thực hành competition
- Script huấn luyện, đánh giá và so sánh mô hình

**Các công việc DS được minh họa:**
- ✅ Khám phá và trực quan hóa dữ liệu
- ✅ Feature engineering
- ✅ Huấn luyện và đánh giá mô hình
- ✅ Cross-validation
- ✅ So sánh mô hình
- ✅ Phân tích độ đo hiệu suất

### Kỹ năng chính cần học cho DS

**Lập trình:**
- Python (pandas, numpy, scikit-learn nâng cao)
- R (tùy chọn)
- Thống kê và toán học

**Thư viện ML:**
- **Scikit-learn**: Thuật toán ML truyền thống
- **TensorFlow/Keras**: Deep learning
- **PyTorch**: Deep learning
- **XGBoost, LightGBM**: Gradient boosting
- **Statsmodels**: Mô hình thống kê

**Visualization (Trực quan hóa):**
- Matplotlib, Seaborn, Plotly
- Tableau, Power BI
- Jupyter notebooks

**Khái niệm:**
- Các thuật toán machine learning
- Phân tích thống kê
- Thiết kế thử nghiệm
- Độ đo đánh giá mô hình
- Hiểu biết kinh doanh

---

## 🔄 Quy trình DE → DS

Cách Data Engineer và Data Scientist làm việc cùng nhau:

### 1. Giai đoạn Data Engineer

```
┌─────────────────────────────────────────┐
│  Nguồn Dữ liệu (APIs, Databases, Files) │
└──────────────────┬──────────────────────┘
                   │
                   ▼
         ┌─────────────────┐
         │  ETL Pipeline   │  ← DE xây dựng cái này
         │  - Extract      │
         │  - Transform    │
         │  - Load         │
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │ Data Warehouse  │  ← DE duy trì cái này
         │ (Sạch, Sẵn sàng)│
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │ Kiểm tra Chất   │  ← DE đảm bảo cái này
         │ lượng Dữ liệu   │
         └─────────────────┘
```

**Sản phẩm của DE:**
- Tập dữ liệu sạch, đã xác thực
- Data dictionary/schema
- Tài liệu data pipeline
- Cập nhật dữ liệu theo lịch

### 2. Giai đoạn Data Scientist

```
         ┌─────────────────┐
         │ Dữ liệu Sạch    │  ← Từ DE
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │      EDA        │  ← DS phân tích
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │ Feature         │  ← DS thiết kế
         │ Engineering     │
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │ Huấn luyện      │  ← DS xây dựng
         │ Mô hình         │
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │ Đánh giá        │  ← DS đánh giá
         │ Mô hình         │
         └────────┬────────┘
                  │
                  ▼
         ┌─────────────────┐
         │ Insights &      │  ← DS cung cấp
         │ Dự đoán         │
         └─────────────────┘
```

**Sản phẩm của DS:**
- Báo cáo phân tích
- Mô hình đã được huấn luyện
- Độ đo hiệu suất mô hình
- Khuyến nghị kinh doanh
- Insights dự đoán

---

## 📋 Ví dụ Quy trình Dự án

### Kịch bản: Xây dựng Hệ thống Dự đoán Customer Churn (Khách hàng rời bỏ)

#### Giai đoạn 1: Data Engineering (Tuần 1-2)

**Công việc:**
1. ✅ Kết nối với cơ sở dữ liệu khách hàng
2. ✅ Xây dựng ETL pipeline để trích xuất dữ liệu khách hàng
3. ✅ Làm sạch và xác thực dữ liệu
4. ✅ Tạo bảng data warehouse
5. ✅ Lập lịch cập nhật dữ liệu hàng ngày
6. ✅ Triển khai kiểm tra chất lượng dữ liệu

**Sản phẩm:** Tập dữ liệu khách hàng sạch với các tính năng như:
- Thông tin nhân khẩu học khách hàng
- Lịch sử giao dịch
- Mô hình sử dụng dịch vụ
- Dữ liệu ticket hỗ trợ

#### Giai đoạn 2: Data Science (Tuần 3-4)

**Công việc:**
1. ✅ Khám phá tập dữ liệu sạch (EDA)
2. ✅ Xác định các mô hình trong khách hàng bị churn vs giữ lại
3. ✅ Thiết kế tính năng (ví dụ: xu hướng sử dụng, điểm tương tác)
4. ✅ Huấn luyện mô hình phân loại
5. ✅ Đánh giá hiệu suất mô hình
6. ✅ Tạo dự đoán churn
7. ✅ Tạo insights có thể thực hiện

**Sản phẩm:** 
- Mô hình dự đoán churn
- Danh sách khách hàng có nguy cơ cao
- Các yếu tố chính gây ra churn
- Can thiệp được khuyến nghị

---

## 🎯 Kỹ năng Chồng lấp

Cả hai vai trò đều chia sẻ một số kỹ năng:

**Kỹ năng Chung:**
- Lập trình Python
- SQL
- Xử lý dữ liệu (pandas)
- Git version control
- Hiểu các định dạng dữ liệu (CSV, JSON, Parquet)
- Cơ bản về nền tảng cloud

**Sự khác biệt chính:**
- **DE tập trung vào**: Hạ tầng, khả năng mở rộng, tự động hóa, chất lượng dữ liệu
- **DS tập trung vào**: Phân tích, mô hình hóa, thống kê, insights kinh doanh

---

## 📚 Lộ trình Học tập

### Cho Data Engineering:

1. **Nền tảng (Tháng 1-2)**
   - Python, SQL
   - Cơ bản về cơ sở dữ liệu
   - Linux/Shell scripting

2. **Trung cấp (Tháng 3-4)**
   - Khái niệm và công cụ ETL
   - Apache Airflow
   - Nền tảng cloud (AWS/GCP)
   - Cơ bản về Docker

3. **Nâng cao (Tháng 5-6)**
   - Công cụ Big Data (Spark)
   - Data warehousing
   - Hệ thống phân tán
   - Data governance

### Cho Data Science:

1. **Nền tảng (Tháng 1-2)**
   - Python, pandas, numpy
   - Thống kê và xác suất
   - Trực quan hóa dữ liệu

2. **Trung cấp (Tháng 3-4)**
   - Thuật toán machine learning
   - Scikit-learn
   - Feature engineering
   - Đánh giá mô hình

3. **Nâng cao (Tháng 5-6)**
   - Deep learning
   - Kỹ thuật ML nâng cao
   - MLOps
   - Chuyên môn lĩnh vực

---

## 🔗 Tài nguyên Học tập

**Data Engineering:**
- [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
- [Data Engineering Cookbook](https://github.com/andkret/Cookbook)
- Tài liệu Apache Airflow

**Data Science:**
- [Kaggle Learn](https://www.kaggle.com/learn)
- [Fast.ai](https://www.fast.ai/)
- Tài liệu Scikit-learn

---

## Bước Tiếp theo cho Repository này

Để thể hiện tốt hơn cả hai vai trò, hãy xem xét thêm:

1. **Ví dụ DE:**
   - Script ETL pipeline
   - Ví dụ kết nối database
   - Script xác thực dữ liệu
   - Thu thập dữ liệu tự động

2. **Ví dụ DS:**
   - Mô hình nâng cao hơn
   - Phân tích feature importance
   - Ví dụ triển khai mô hình
   - Kịch bản A/B testing

Xem thư mục `etl/` cho các ví dụ Data Engineering đã được thêm vào repository này.

---

## 💡 Tóm tắt Nhanh

### Data Engineer (DE) làm gì hàng ngày?
- Xây dựng và duy trì data pipeline
- Đảm bảo dữ liệu sạch và chất lượng cao
- Kết nối và tích hợp nhiều nguồn dữ liệu
- Tối ưu hóa hiệu suất và khả năng mở rộng
- Giám sát và sửa lỗi pipeline

### Data Scientist (DS) làm gì hàng ngày?
- Phân tích và khám phá dữ liệu
- Xây dựng và huấn luyện mô hình ML
- Đánh giá và cải thiện mô hình
- Tạo insights và khuyến nghị
- Trình bày kết quả cho stakeholder

### Trong Repository này:
- **Công việc DE**: `etl/` folder (pipeline, validation, API collection)
- **Công việc DS**: `projects/` và `kaggle-notebooks/` (ML models, EDA)

### Sau khi DE hoàn thành:
1. DE cung cấp dữ liệu sạch, đã xác thực
2. DS sử dụng dữ liệu đó để phân tích
3. DS xây dựng và huấn luyện mô hình
4. DS tạo dự đoán và insights
5. Insights được sử dụng để ra quyết định kinh doanh
