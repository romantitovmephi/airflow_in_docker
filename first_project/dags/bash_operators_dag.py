from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

bash_dag = DAG(
    "bash_operators_dag",
    start_date=days_ago(0, 0, 0, 0, 0),
    tags=['bash']
)

operation_1 = BashOperator(
    bash_command="pwd",
    dag=bash_dag,
    task_id='operation_1'
)

operation_2 = BashOperator(
    bash_command="sleep 5",
    dag=bash_dag,
    task_id='operation_2'
)

operation_3 = BashOperator(
    bash_command="sleep 20",
    dag=bash_dag,
    task_id='operation_3'
)

operation_4 = BashOperator(
    bash_command="""echo "completed" """,
    dag=bash_dag,
    task_id='operation_4'
)

operation_1 >> [operation_2, operation_3]

[operation_2, operation_3] >> operation_4
