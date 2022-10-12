from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging
from steps import step1

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def _task1():
    logger.info('taks1')
    step1.run_workflow_step1()

def _task2():
    logger.info('taks2')

def _task3():
    logger.info('taks3')


with DAG(dag_id='dag_example', start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:

    t1 = PythonOperator(
        task_id='t1',
        op_kwargs=dag.default_args,
        provide_context=True,
        python_callable=_task1
    )


    t2 = PythonOperator(
        task_id='t2',
        op_kwargs=dag.default_args,
        provide_context=True,
        python_callable=_task2
    )

    t3 = PythonOperator(
        task_id='t3',
        op_kwargs=dag.default_args,
        provide_context=True,
        python_callable=_task3
    )

    t1 >> [t2, t3]



    

