from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def long_task(size=5000000):
    print(f"<<<<<<<<< Starting long task ({size}) >>>>>>>>>>")
    counter = 0
    for i in range(5000000):
        counter = counter + 1
    print(f"Looped: {counter} times")
    print(f"<<<<<<<<< Finished long task ({size}) >>>>>>>>>>")


with DAG(
    "generate_load",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
    num_of_tasks = 100
    num_of_loops = 5000000

    tasks = [
        PythonOperator(
            task_id=f"task{i}",
            python_callable=long_task,
            op_args=[num_of_loops],
        )
        for i in range(num_of_tasks)
    ]
