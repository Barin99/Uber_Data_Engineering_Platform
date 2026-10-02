from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="bronze_to_silver",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["dbt", "silver"],
) as dag:

    dbt_run_staging = BashOperator(
        task_id="dbt_run_staging",
        bash_command="""
        cd /opt/airflow/dbt/uber_data_platform &&
        dbt run --select staging
        """
    )

    dbt_test_staging = BashOperator(
        task_id="dbt_test_staging",
        bash_command="""
        cd /opt/airflow/dbt/uber_data_platform &&
        dbt test --select staging
        """
    )

    dbt_run_staging >> dbt_test_staging
