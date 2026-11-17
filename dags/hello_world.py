"""Small DAG used to confirm git-sync is loading this repo."""

from datetime import datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG

with DAG(
    dag_id="hello_world",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["example"],
) as dag:
    BashOperator(
        task_id="print_hello",
        bash_command="echo hello from airflow-dags",
    )
