from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# DAG 기본 설정
default_args = {
    'owner': 'ryan',
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 29),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'hello_airflow_dag',
    default_args=default_args,
    description="our first time practice airflow",
    schedule_interval=timedelta(days=1),
)

# 실행할 함수 정의
def print_word(word):
    print(word) # test

# 동적 태스크 생성
sentence = "hello airflow dag. test task star"
prev_task = None

for i, word in enumerate(sentence.split()):
    task = PythonOperator(
        task_id=f'print_world_{i}',
        python_callable=print_word,
        op_kwargs={'word': word},
        dag=dag,
    )
    if prev_task:
        prev_task >> task
    prev_task = task