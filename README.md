# AIRFLOW_MLFLOW_DOCKER

- [Background](#background)
- [Tools Overview](#tools_overview)
- [Getting started](#getting_started)
    * [Docker Compose configuration](#docker_config)


<a name="background"/>

## Background
The goal of this project is to create an ecosystem where to run **Data Pipelines** and monitor **Machine Learning Experiments**.

<a name="tools_overview"/>

## Tools Overview

From `Airflow` documentation:
```
Apache Airflow is an open-source platform for developing, scheduling, and monitoring batch-oriented workflows
```

From `MLflow` documentation:
```
MLflow is an open source platform for managing the end-to-end machine learning lifecycle
```

From `Docker` documentation:
```
Docker Compose is a tool for defining and running multi-container Docker applications.
```

<a name="getting_started"/>

## Getting Started
To structure an ecosystem where to run Data Pipelines and monitor ML experiments, the first step to accomplish is define the place of where they should run together: `docker compose`.


<a name="docker_config"/>

### Docker Compose Configuration


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
* [What is Airflow?](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
* [MLflow](https://mlflow.org/docs/latest/index.html)
