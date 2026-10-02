🚖 Uber Data Engineering Platform
📌 Project Overview
This project demonstrates an end-to-end Data Engineering pipeline built using modern cloud data engineering tools and Medallion Architecture.

The pipeline ingests Uber trip datasets into Databricks using PySpark, transforms the data through Bronze, Silver, and Gold layers using dbt, and orchestrates the complete workflow using Apache Airflow running on Docker.

The project follows enterprise-level best practices including:

Medallion Architecture
Modular dbt models
Apache Airflow orchestration
Data Quality Testing
Dockerized deployment
Databricks Unity Catalog
Git Version Control
🏗️ Architecture

Source CSV Files
        │
        ▼
Databricks (PySpark)
        │
        ▼
Bronze Layer
        │
        ▼
Airflow DAG-1
Bronze → Silver
        │
        ▼
Silver Layer (dbt)
        │
        ▼
Airflow DAG-2
Silver → Gold
        │
        ▼
Gold Layer
        │
        ▼
Airflow DAG-3
Data Quality
        │
        ▼
Master Pipeline DAG

⚙️ Tech Stack
Technology	Usage
Python	Programming
PySpark	Data Processing
Databricks	Data Engineering Platform
Delta Lake	Storage Layer
dbt	Data Transformation
Apache Airflow	Workflow Orchestration
Docker	Containerization
SQL	Data Analysis
Git & GitHub	Version Control
📁 Project Structure
uber-data-platform/
│
├── airflow/
│   ├── dags/
│   │   ├── dag_bronze_to_silver.py
│   │   ├── dag_silver_to_gold.py
│   │   ├── dag_data_quality.py
│   │   └── master_pipeline.py
│   │
│   ├── Dockerfile
│   ├── docker-compose.yaml
│   └── requirements.txt
│
├── dbt/
│   └── uber_data_platform/
│       ├── models/
│       │   ├── staging/
│       │   ├── dimensions/
│       │   └── facts/
│       │
│       ├── macros/
│       ├── tests/
│       ├── snapshots/
│       ├── seeds/
│       └── dbt_project.yml
│
├── screenshots/
│
├── architecture/
│
├── notebooks/
│
├── README.md
└── .gitignore
🏛️ Medallion Architecture
The project follows the Medallion Architecture.

Bronze Layer
Raw data ingestion
Stores source data without business transformations
Built using Databricks and Delta Tables
Silver Layer
Data cleansing
Standardization
Data type conversion
Null handling
Business-ready staging tables
Implemented using dbt.

Gold Layer
Business-ready analytical tables.

Contains:

Dimension Tables
Fact Tables
Optimized for reporting and analytics.

🔄 End-to-End Pipeline Flow
Source CSV Files
        │
        ▼
Databricks (PySpark)
        │
        ▼
Bronze Layer (Delta Tables)
        │
        ▼
Airflow DAG-1
Bronze → Silver
        │
        ▼
Silver Layer (dbt Staging Models)
        │
        ▼
Airflow DAG-2
Silver → Gold
        │
        ▼
Gold Layer
(Dimensions + Fact Tables)
        │
        ▼
Airflow DAG-3
Data Quality Validation (dbt test)
        │
        ▼
Master Pipeline DAG
🌪️ Airflow DAGs
The project is orchestrated using Apache Airflow running inside Docker.

DAG	Description
bronze_to_silver	Executes dbt staging models to transform Bronze data into Silver
silver_to_gold	Executes dbt dimension and fact models to populate Gold Layer
gold_data_quality	Executes dbt tests to validate transformed datasets
master_pipeline	Orchestrates the complete end-to-end pipeline
✅ Data Quality Checks
The project validates transformed datasets using dbt tests.

Implemented validations include:

Schema Validation
Source Validation
Not Null Checks
Relationship Tests
Accepted Values
Primary Key Validation
This ensures that only trusted and high-quality data reaches the Gold Layer.

📊 Final Data Model
The final Gold Layer contains:

Dimension Tables
dim_city
dim_vehicle_types
dim_vehicle_makes
dim_payment_methods
dim_ride_status
dim_cancellation_reasons
Fact Table
fact_trips
These tables are optimized for reporting and analytical workloads.

📸 Project Screenshots
Airflow
Bronze → Silver DAG
Silver → Gold DAG
Gold Data Quality DAG
Master Pipeline DAG
Databricks
Bronze Schema
Silver Schema
Gold Schema
🚀 How to Run the Project
1. Clone Repository
git clone https://github.com/7798akash/uber-data-platform.git
2. Start Airflow
cd airflow
docker compose up -d
3. Verify dbt Connection
dbt debug
4. Execute Pipeline
Run the Airflow DAGs in the following order:

Bronze → Silver
Silver → Gold
Gold Data Quality
Or simply run:

Master Pipeline DAG
💼 Key Features
End-to-End Data Engineering Pipeline
Medallion Architecture (Bronze, Silver, Gold)
Apache Airflow Orchestration
dbt Transformations
PySpark Data Processing
Delta Lake Storage
Databricks Unity Catalog
Dockerized Airflow Environment
Data Quality Validation using dbt Tests
GitHub Version Control
🔮 Future Enhancements
Email Notifications
Slack Alerts
CI/CD Pipeline using GitHub Actions
Incremental dbt Models
Data Freshness Monitoring
Power BI Dashboard Integration
👨‍💻 Author
Barin Ghosh

Data Engineer | PySpark | SQL | Azure | Databricks | Apache Airflow | dbt

⭐ If you found this project useful, consider giving it a star on GitHub.
