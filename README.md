# AIRFLOW_MLFLOW_DOCKER

## Background
The goal of this project is to create an ecosystem where to run **Data Pipelines** and monitor **Machine Learning Experiments**.

## Getting started

### Docker
Create `docker-compose.yaml`, which is responsible for running `Airflow` and `MLflow` components. Each of them running on a different container:
* airflow-webserver
* airflow-scheduler
* airflow-worker
* airflow-triggerer
* mlflow 

Then, from terminal run the following command:
```
docker compose up -d
```

### Airflow
After running docker containers, visit the page: `localhost:8080`
![img](docs/imgs/airflow_home.png)

And take a step into the Airflow world!

The, create a folder named `dags` and populate it with as many DAGS as you need.


### MLFlow
On the `docker-compose.yaml` includes the `mlflow` container in the `services` section.
This container is responsible for running the `MLFlow server`, which is exposed on the `localhost:600`.
![img](docs/imgs/mlflow_home.png)

#### Connect Airflow to MLflow 
Open the `example_dag.py` and set the URI of the current MLFlow server(localhost:600)
```
mlflow.set_tracking_uri('http://mlflow:600')
```

After updating the URI of the MLFlow server, create a new connection on `Airflow`.

### Tech Stack
* Airflow
* MLflow
* Docker
* Python


### References
* [Airflow Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
