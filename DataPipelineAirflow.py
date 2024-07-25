# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

default_args = {
  'owner': 'Shrish Maharjan',
  'start_date': days_ago(0),
  'email': ['maharjanshrish8@gmail.com']
}

dag = DAG(
  'process_web_log',
  default_args=default_args,
  description='Capstime Data pipeline using Airflow',
  schedule_interval=timedelta(days=1),
)

extract_data = BashOperator(
  task_id='extract_data',
  bash_command='cut -d" " -f1 /home/shrish/airflow/dags/capstone/accesslog.txt > /home/shrish/airflow/dags/capstone/extracted_data.txt',
  dag=dag,
)

transform_data = BashOperator(
  task_id='transform_data',
  bash_command='cat /home/shrish/airflow/dags/capstone/extracted_data.txt | grep "198.46.149.143" > /home/shrish/airflow/dags/capstone/transformed_data.txt',
  dag=dag,
)

load_data = BashOperator(
  task_id='load_data',
  bash_command='tar -cvf /home/shrish/airflow/dags/capstone/weblog.tar /home/shrish/airflow/dags/capstone/transformed_data.txt',
  dag=dag,
)

#task pipeline
extract_data >> transform_data >> load_data