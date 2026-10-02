from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="silver_to_gold",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["dbt", "gold"],
) as dag:

    dbt_run_gold = BashOperator(
        task_id="dbt_run_gold",
        bash_command="""
        cd /opt/airflow/dbt/uber_data_platform &&
        dbt run --select dimensions facts
        """
    )

    dbt_test_gold = BashOperator(
        task_id="dbt_test_gold",
        bash_command="""
        cd /opt/airflow/dbt/uber_data_platform &&
        dbt test --select dimensions facts
        """
    )

    dbt_run_gold >> dbt_test_gold
