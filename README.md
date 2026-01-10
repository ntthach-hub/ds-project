# Data Science Learning Projects 🎯

This repository contains my small machine learning projects and Kaggle practice notebooks while learning Data Science.

> **New! 🆕** Learn about [Data Engineering vs Data Science roles](docs/DE_vs_DS_Guide.md) - understand what each role does daily, skills needed, and how they work together!
> 
> **Tiếng Việt! 🇻🇳** [Hướng dẫn Data Engineering vs Data Science bằng tiếng Việt](docs/DE_vs_DS_Guide_VI.md) - tìm hiểu công việc hàng ngày, kỹ năng cần thiết, và cách họ làm việc cùng nhau!

## 📁 Repository Structure

```
ds-project/
├── projects/                  # Machine learning project implementations (DS work)
│   ├── iris-classification/   # Iris dataset classification project
│   └── titanic-survival/      # Titanic survival prediction project
├── kaggle-notebooks/          # Kaggle competition practice notebooks (DS work)
│   ├── titanic/              # Titanic: Machine Learning from Disaster
│   └── house-prices/         # House Prices: Advanced Regression Techniques
├── etl/                      # ETL pipelines and data engineering examples (DE work)
│   ├── simple_etl.py         # Basic ETL pipeline example
│   ├── data_validation.py    # Data quality validation
│   └── api_data_collector.py # API data collection example
├── data/                     # Datasets used in projects
│   ├── raw/                  # Raw, immutable datasets
│   └── processed/            # Cleaned and processed datasets
├── docs/                     # Documentation
│   └── DE_vs_DS_Guide.md    # Data Engineering vs Data Science guide
└── requirements.txt          # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ntthach-hub/ds-project.git
cd ds-project
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Navigate to any project or notebook directory and follow the specific instructions in each project's README.

## 📊 Projects

### Data Engineering Examples (ETL/Pipelines)

Learn the fundamentals of Data Engineering - the work that happens BEFORE data science:

1. **Simple ETL Pipeline** (`etl/simple_etl.py`)
   - Extract, Transform, Load data
   - Data cleaning and preprocessing
   - Automated data processing
   - Run: `python etl/simple_etl.py`

2. **Data Validation** (`etl/data_validation.py`)
   - Data quality checks
   - Completeness and consistency validation
   - Automated quality monitoring
   - Run: `python etl/data_validation.py`

3. **API Data Collector** (`etl/api_data_collector.py`)
   - Collect data from external APIs
   - Handle pagination and rate limiting
   - Scheduled data collection
   - Run: `python etl/api_data_collector.py`

### Machine Learning Projects (Data Science)

After data is cleaned by DE, Data Scientists work on these projects:

1. **Iris Classification** (`projects/iris-classification/`)
   - Classic ML project using the Iris dataset
   - Implements multiple classification algorithms
   - Includes data visualization and model comparison

2. **Titanic Survival Prediction** (`projects/titanic-survival/`)
   - Predicts passenger survival on the Titanic
   - Feature engineering and data preprocessing
   - Model training and evaluation

### Kaggle Practice Notebooks

1. **Titanic: Machine Learning from Disaster** (`kaggle-notebooks/titanic/`)
   - Kaggle competition notebook
   - Exploratory data analysis (EDA)
   - Model building and submission

2. **House Prices: Advanced Regression Techniques** (`kaggle-notebooks/house-prices/`)
   - Regression problem
   - Feature engineering
   - Ensemble methods

## 🛠️ Technologies Used

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive computing

## 📚 Learning Resources

Throughout this repository, I'm practicing and implementing concepts from:

**Data Engineering:**
- ETL pipeline development
- Data quality validation
- API data collection
- Database management
- Data pipeline automation

**Data Science:**
- Machine Learning fundamentals
- Data preprocessing and feature engineering
- Model evaluation and validation
- Exploratory Data Analysis (EDA)
- Various ML algorithms (Classification, Regression, Clustering)

**Understanding the Workflow:**
- Read [Data Engineering vs Data Science Guide](docs/DE_vs_DS_Guide.md) to understand:
  - What does a Data Engineer do daily?
  - What does a Data Scientist do daily?
  - How do DE and DS roles work together?
  - What skills are needed for each role?
  - Career paths and learning resources

**📚 Tài liệu Tiếng Việt (Vietnamese Documentation):**
- [Hướng dẫn DE vs DS](docs/DE_vs_DS_Guide_VI.md) - Giải thích chi tiết vai trò và kỹ năng
- [ETL Examples README](etl/README_VI.md) - Giải thích các ví dụ ETL bằng tiếng Việt

## 📝 Notes

This is a learning repository, so code and approaches may not always be optimal. The focus is on learning and experimenting with different data science and data engineering techniques.

The repository demonstrates both Data Engineering (preparing and cleaning data) and Data Science (analyzing data and building models) workflows.

**Ghi chú (Vietnamese Note):** Repository này minh họa cả công việc Data Engineering (chuẩn bị và làm sạch dữ liệu) và Data Science (phân tích dữ liệu và xây dựng mô hình).

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

While this is a personal learning repository, suggestions and feedback are always welcome!

## 📧 Contact

For any questions or feedback, feel free to reach out through GitHub issues.