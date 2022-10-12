"""
This DAG is responsible for running the sequence of steps from steps_example_dag.


Author: Fabio Barbazza
Date: Oct, 2022
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging
from steps_example_dag import step1_example_dag

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)



mlflow.set_tracking_uri('http://mlflow:600')

experiment = mlflow.set_experiment("Airflow_Example")


def _task1():
    """
        This method is responsible for running _task1 logic
    """
    try:

        logger.info('taks1')

        step1_example_dag.run_workflow_step1()

    except Exception err:
        logger.exception(err)
        raise err

def _task2():
    """
        This method is responsible for running _task2 logic
    """
    try:

    logger.info('taks2')

    except Exception err:
        logger.exception(err)
        raise err

def _task3():
    """
        This method is responsible for running _task3 logic
    """
    try:

    logger.info('taks3')

    except Exception err:
        logger.exception(err)
        raise err

with mlflow.start_run():
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



    

