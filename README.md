# 🚖 Uber Data Engineering Platform

An end-to-end **Data Engineering project** that demonstrates how raw Uber trip data can be ingested, transformed, validated, and organized into analytics-ready datasets using modern data engineering technologies.

The project follows **Medallion Architecture (Bronze, Silver, Gold)** and combines **Databricks, PySpark, Delta Lake, dbt, Apache Airflow, Docker, SQL, and Git** to build an automated and modular data pipeline.

---

## 📌 Project Overview

The pipeline processes Uber trip datasets through multiple stages:

**Source CSV Files → Databricks/PySpark → Bronze → Silver → Gold → Data Quality Validation**

The complete workflow is orchestrated using **Apache Airflow**, while **dbt** is used for SQL-based transformations and testing.

### Key Engineering Practices

* Medallion Architecture
* Modular dbt transformations
* Apache Airflow orchestration
* PySpark-based data processing
* Delta Lake storage
* Data quality testing
* Dockerized development environment
* Git/GitHub version control
* Dimensional data modeling
* Automated pipeline execution

---

# 🏗️ Architecture

```text
                 Source CSV Files
                       │
                       ▼
              ┌─────────────────┐
              │    Databricks   │
              │     PySpark     │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Bronze Layer   │
              │  Raw Delta Data │
              └────────┬────────┘
                       │
                 Airflow DAG
                       │
                       ▼
              ┌─────────────────┐
              │  Silver Layer   │
              │ Cleaned &       │
              │ Standardized    │
              └────────┬────────┘
                       │
                 Airflow DAG
                       │
                       ▼
              ┌─────────────────┐
              │   Gold Layer    │
              │ Facts &         │
              │ Dimensions      │
              └────────┬────────┘
                       │
                 Airflow DAG
                       │
                       ▼
              ┌─────────────────┐
              │ Data Quality    │
              │   Validation    │
              └─────────────────┘
```

---

# ⚙️ Technology Stack

| Technology         | Purpose                                  |
| ------------------ | ---------------------------------------- |
| **Python**         | Programming and pipeline logic           |
| **PySpark**        | Distributed data processing              |
| **Databricks**     | Data engineering and processing platform |
| **Delta Lake**     | Reliable storage and table management    |
| **dbt**            | SQL transformations and data modeling    |
| **Apache Airflow** | Workflow orchestration                   |
| **Docker**         | Containerized Airflow environment        |
| **SQL**            | Data transformation and analysis         |
| **Git & GitHub**   | Version control                          |

---

# 🏛️ Medallion Architecture

The project follows the **Bronze → Silver → Gold** data architecture pattern.

## 🥉 Bronze Layer

The Bronze layer stores the raw source data with minimal transformation.

### Responsibilities

* Ingest source CSV files
* Preserve source information
* Store raw datasets
* Create Delta tables
* Maintain the initial structure of incoming data

**Technology:** Databricks + PySpark + Delta Lake

---

## 🥈 Silver Layer

The Silver layer converts raw data into clean and standardized datasets.

### Transformations

* Data cleansing
* Data type conversion
* Null handling
* Standardization
* Invalid-value handling
* Column transformations
* Business-rule preparation

**Technology:** dbt + SQL

---

## 🥇 Gold Layer

The Gold layer contains business-ready analytical datasets optimized for reporting and analysis.

The model follows a dimensional data-modeling approach consisting of:

### Dimension Tables

* `dim_city`
* `dim_vehicle_types`
* `dim_vehicle_makes`
* `dim_payment_methods`
* `dim_ride_status`
* `dim_cancellation_reasons`

### Fact Table

* `fact_trips`

The `fact_trips` table stores measurable trip-level information and connects to the relevant dimension tables.

---

# 🔄 End-to-End Pipeline

```text
CSV Source Data
      │
      ▼
Databricks + PySpark
      │
      ▼
Bronze Delta Tables
      │
      ▼
Airflow: Bronze → Silver
      │
      ▼
dbt Staging Models
      │
      ▼
Silver Layer
      │
      ▼
Airflow: Silver → Gold
      │
      ▼
dbt Dimension & Fact Models
      │
      ▼
Gold Layer
      │
      ▼
Airflow: Data Quality
      │
      ▼
dbt Tests
```

---

# 🌪️ Apache Airflow DAGs

Apache Airflow is used to orchestrate the different stages of the pipeline.

| DAG                 | Description                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| `bronze_to_silver`  | Executes dbt staging models and transforms Bronze data into Silver datasets |
| `silver_to_gold`    | Executes dbt dimension and fact models to build the Gold layer              |
| `gold_data_quality` | Executes dbt tests to validate Gold-layer datasets                          |
| `master_pipeline`   | Coordinates the complete end-to-end workflow                                |

### Master Pipeline

The complete pipeline can be executed through the master DAG:

```text
Bronze → Silver → Gold → Data Quality
```

This reduces the need to manually execute individual pipeline stages.

---

# ✅ Data Quality

Data quality checks are implemented using **dbt tests** to ensure that reliable data reaches the Gold layer.

### Implemented Checks

* Not-null validation
* Primary-key validation
* Relationship tests
* Accepted-value validation
* Schema validation
* Source validation
* Data consistency checks

These tests help identify data-quality problems before datasets are used for analytical workloads.

---

# 📊 Gold Data Model

The final analytical model contains:

```text
                    dim_city
                       │
                       │
dim_vehicle_types ────┤
                       │
dim_vehicle_makes ────┤
                       │
dim_payment_methods ──┤
                       │
dim_ride_status ──────┤
                       │
dim_cancellation ─────┤
                       │
                       ▼
                  fact_trips
```

The dimensional model allows analytical queries to combine trip-level metrics with descriptive information such as:

* City
* Vehicle type
* Vehicle make
* Payment method
* Ride status
* Cancellation reason

---

# 📁 Project Structure

```text
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
├── notebooks/
│
├── architecture/
│
├── screenshots/
│
├── README.md
│
└── .gitignore
```

---

# 📸 Project Screenshots

The repository contains screenshots demonstrating:

### Airflow

* Bronze → Silver DAG
* Silver → Gold DAG
* Gold Data Quality DAG
* Master Pipeline DAG

### Databricks

* Bronze layer
* Silver layer
* Gold layer

### Data Model

* Fact tables
* Dimension tables
* Architecture diagrams

---

# 💼 Key Features

* End-to-end Data Engineering pipeline
* Medallion Architecture
* PySpark data processing
* Databricks integration
* Delta Lake storage
* dbt-based transformations
* Apache Airflow orchestration
* Dockerized development environment
* Dimensional data modeling
* Data quality validation
* Git/GitHub version control

---

# 🔮 Future Enhancements

Potential future improvements include:

* Email notifications for pipeline failures
* Slack alerts
* GitHub Actions CI/CD
* Incremental dbt models
* Data freshness monitoring
* Pipeline failure monitoring
* Power BI dashboard integration
* Additional data-quality rules
* Automated documentation generation

---

# 📚 What This Project Demonstrates

This project demonstrates practical knowledge of:

* ETL/ELT pipeline development
* Data ingestion
* Batch data processing
* PySpark
* SQL transformations
* Data warehousing
* Medallion Architecture
* Dimensional modeling
* Workflow orchestration
* Data quality engineering
* Containerization
* Version control

---

# 👨‍💻 Author

**Barin Ghosh**

B.Tech Computer Science & Engineering | Data Engineering Enthusiast

**Skills:** SQL | Python | PySpark | Databricks | Apache Airflow | dbt | Docker | Data Warehousing | Git

---

⭐ If you find this project useful, consider giving the repository a star.
