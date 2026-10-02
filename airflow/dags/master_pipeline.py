from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

with DAG(
    dag_id="master_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["master"],
) as dag:

    bronze_to_silver = TriggerDagRunOperator(
        task_id="trigger_bronze_to_silver",
        trigger_dag_id="bronze_to_silver",
        wait_for_completion=True,
    )

    silver_to_gold = TriggerDagRunOperator(
        task_id="trigger_silver_to_gold",
        trigger_dag_id="silver_to_gold",
        wait_for_completion=True,
    )

    gold_data_quality = TriggerDagRunOperator(
        task_id="trigger_gold_data_quality",
        trigger_dag_id="gold_data_quality",
        wait_for_completion=True,
    )

    bronze_to_silver >> silver_to_gold >> gold_data_quality
