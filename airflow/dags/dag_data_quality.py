from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="gold_data_quality",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["dbt", "quality"],
) as dag:

    dbt_test = BashOperator(
        task_id="dbt_test_gold",
        bash_command="""
        cd /opt/airflow/dbt/uber_data_platform &&
        dbt test --select dimensions facts
        """
    )

    dbt_test
