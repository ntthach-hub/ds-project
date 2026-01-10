# Ví dụ ETL - Data Engineering

Thư mục này chứa các ví dụ về công việc Data Engineering, đặc biệt là các pipeline ETL (Extract, Transform, Load) và script xử lý dữ liệu.

## Nội dung

1. **`simple_etl.py`** - Ví dụ ETL pipeline cơ bản
2. **`data_validation.py`** - Script xác thực chất lượng dữ liệu
3. **`api_data_collector.py`** - Ví dụ thu thập dữ liệu từ API

## ETL là gì?

**ETL (Extract, Transform, Load)** là quy trình cốt lõi trong data engineering:

- **Extract (Trích xuất)**: Thu thập dữ liệu từ nhiều nguồn khác nhau (API, database, file)
- **Transform (Chuyển đổi)**: Làm sạch, xác thực và tái cấu trúc dữ liệu
- **Load (Tải)**: Lưu trữ dữ liệu đã xử lý vào đích đến (database, data warehouse)

## Chạy các Ví dụ

Mỗi script có thể chạy độc lập:

```bash
# ETL pipeline đơn giản
python simple_etl.py

# Xác thực dữ liệu
python data_validation.py

# Thu thập dữ liệu từ API
python api_data_collector.py
```

## Data Engineering vs Data Science

**Vai trò của Data Engineer:**
- Xây dựng và duy trì các pipeline ETL này
- Đảm bảo chất lượng và độ tin cậy của dữ liệu
- Tự động hóa thu thập và xử lý dữ liệu
- Tối ưu hóa lưu trữ và truy xuất dữ liệu

**Vai trò của Data Scientist:**
- Sử dụng dữ liệu sạch do DE tạo ra
- Thực hiện phân tích khám phá dữ liệu
- Xây dựng mô hình machine learning
- Tạo insights và dự đoán

## Giải thích chi tiết các Script

### 1. simple_etl.py - Pipeline ETL cơ bản

Script này minh họa một quy trình ETL hoàn chỉnh:

**Extract (Trích xuất):**
- Tạo dữ liệu mẫu giao dịch khách hàng
- Trong thực tế, đây sẽ là việc đọc từ database, API, hoặc file

**Transform (Chuyển đổi):**
- Xử lý giá trị thiếu
- Loại bỏ bản sao
- Chuyển đổi kiểu dữ liệu
- Tạo tính năng mới (feature engineering)
- Xác thực dữ liệu
- Tạo thống kê tóm tắt

**Load (Tải):**
- Lưu dữ liệu đã xử lý vào file CSV
- Lưu metadata về quá trình ETL
- Trong thực tế, đây sẽ là việc ghi vào database hoặc data warehouse

**Output:**
- File: `../data/processed/customer_transactions_clean.csv`
- Metadata: `../data/processed/customer_transactions_clean_metadata.json`

### 2. data_validation.py - Xác thực chất lượng dữ liệu

Script này kiểm tra chất lượng dữ liệu:

**Các kiểm tra bao gồm:**
- **Completeness (Tính đầy đủ)**: Kiểm tra giá trị thiếu
- **Uniqueness (Tính duy nhất)**: Phát hiện bản sao
- **Data Types (Kiểu dữ liệu)**: Xác thực kiểu dữ liệu đúng
- **Range Validation (Xác thực phạm vi)**: Kiểm tra giá trị trong phạm vi hợp lệ
- **Categorical Validation (Xác thực phân loại)**: Kiểm tra giá trị category hợp lệ
- **Consistency (Tính nhất quán)**: Kiểm tra logic nhất quán

**Output:**
- Báo cáo xác thực chi tiết
- Danh sách lỗi và cảnh báo
- Tỷ lệ thành công của kiểm tra

### 3. api_data_collector.py - Thu thập dữ liệu từ API

Script này minh họa cách thu thập dữ liệu từ API:

**Tính năng:**
- Thu thập dữ liệu cơ bản từ API
- Xử lý pagination (phân trang)
- Tuân thủ rate limiting (giới hạn tốc độ)
- Xử lý lỗi và retry logic
- Lưu dữ liệu thô từ API

**Ví dụ sử dụng API:**
- JSONPlaceholder (API test công khai)
- Trong thực tế: Twitter API, Stripe API, Google Analytics API, v.v.

**Output:**
- File JSON với dữ liệu thô từ API
- File CSV với dữ liệu đã chuyển đổi

## Công cụ Data Engineering phổ biến

### ETL Tools (Công cụ ETL)
- **Apache Airflow**: Điều phối workflow, lập lịch pipeline
- **Luigi**: Framework pipeline của Spotify
- **Prefect**: Orchestration hiện đại
- **dbt**: Transformation tool cho data warehouse

### Data Quality Tools (Công cụ chất lượng dữ liệu)
- **Great Expectations**: Framework xác thực dữ liệu Python
- **Apache Griffin**: Giám sát chất lượng dữ liệu
- **Deequ**: Thư viện unit test cho dữ liệu lớn

### Databases & Warehouses
- **PostgreSQL, MySQL**: Relational databases
- **MongoDB, Redis**: NoSQL databases
- **Snowflake, BigQuery, Redshift**: Data warehouses

## Kỹ năng cần học

### Cơ bản
1. **Python**: pandas, numpy cho xử lý dữ liệu
2. **SQL**: Truy vấn và quản lý database
3. **Shell scripting**: Tự động hóa công việc

### Trung cấp
4. **Apache Airflow**: Điều phối pipeline
5. **Docker**: Containerization
6. **Cloud platforms**: AWS, GCP, hoặc Azure
7. **Data modeling**: Thiết kế schema

### Nâng cao
8. **Apache Spark**: Xử lý dữ liệu lớn
9. **Kafka**: Streaming dữ liệu real-time
10. **Kubernetes**: Orchestration container

## Lộ trình học Data Engineering

### Tháng 1-2: Nền tảng
- Python cơ bản và nâng cao
- SQL và database design
- Git version control
- Linux command line

### Tháng 3-4: ETL & Pipelines
- Xây dựng ETL pipeline
- Apache Airflow
- Data validation
- API integration

### Tháng 5-6: Production & Scale
- Cloud platforms (AWS/GCP)
- Docker và containerization
- Big data tools (Spark)
- Monitoring và logging

## Tài nguyên học tập

**Khóa học miễn phí:**
- [DataCamp: Introduction to Data Engineering](https://www.datacamp.com/)
- [Coursera: Data Engineering on Google Cloud](https://www.coursera.org/)
- [Apache Airflow Tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html)

**Sách:**
- "Fundamentals of Data Engineering" - Joe Reis & Matt Housley
- "Data Engineering with Python" - Paul Crickard

**GitHub Resources:**
- [Awesome Data Engineering](https://github.com/igorbarinov/awesome-data-engineering)
- [Data Engineering Cookbook](https://github.com/andkret/Cookbook)

## Best Practices

### 1. Idempotency (Tính nhất quán)
Pipeline nên cho cùng kết quả khi chạy nhiều lần với cùng input

### 2. Monitoring (Giám sát)
- Log tất cả các bước quan trọng
- Thiết lập alert cho lỗi
- Theo dõi metrics hiệu suất

### 3. Data Quality (Chất lượng dữ liệu)
- Xác thực dữ liệu tại mọi bước
- Tài liệu hóa các quy tắc chất lượng
- Kiểm tra tự động

### 4. Error Handling (Xử lý lỗi)
- Retry logic cho lỗi tạm thời
- Ghi log chi tiết lỗi
- Fail gracefully

### 5. Documentation (Tài liệu)
- Tài liệu hóa pipeline và dependencies
- Giữ schema documentation cập nhật
- Code comments rõ ràng

## Câu hỏi thường gặp

**Q: Khác biệt giữa ETL và ELT là gì?**
A: 
- **ETL**: Transform trước khi Load (phù hợp cho data warehouse truyền thống)
- **ELT**: Load trước rồi mới Transform (phù hợp cho cloud data warehouse hiện đại như BigQuery)

**Q: Khi nào nên sử dụng Airflow?**
A: Khi bạn có nhiều pipeline phức tạp cần lập lịch, theo dõi dependencies, và monitoring

**Q: Data Engineer khác Software Engineer như thế nào?**
A: DE tập trung vào dữ liệu (pipelines, quality, storage) trong khi SE tập trung vào ứng dụng

**Q: Cần học Big Data tools ngay từ đầu không?**
A: Không, hãy bắt đầu với Python, SQL, và ETL cơ bản trước. Big Data tools cần khi xử lý dữ liệu rất lớn (TB/PB)

## Bước tiếp theo

Sau khi hiểu ETL, bạn có thể:

1. **Thực hành**: Modify các script này để xử lý dữ liệu của riêng bạn
2. **Mở rộng**: Thêm database connection, cloud storage
3. **Tự động hóa**: Sử dụng Airflow để lập lịch pipeline
4. **Tối ưu**: Cải thiện hiệu suất cho dữ liệu lớn

**Xem thêm:**
- [Hướng dẫn DE vs DS chi tiết](../docs/DE_vs_DS_Guide_VI.md)
- [English version](README.md)
