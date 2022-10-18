# AIRFLOW_MLFLOW_DOCKER

## Table of content
- [Background](#background)
- [Tools Overview](#tools_overview)
- [Getting started](#getting_started)
    * [Docker Compose configuration](#docker_config)
    * [Airflow](#airflow)
    * [MLflow](#mlflow)
- [Connect Airflow to MLflow](#airflow_and_mlflow)
- [References](#references)


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
The first step to structure this project is connecting `Airflow` and `MLflow` together: `docker compose`.


<a name="docker_config"/>

### Docker Compose Configuration
Create `docker-compose.yaml`, which contains the configuration of those docker containers responsible for running `Airflow` and `MLflow` services. 
Each of those services runs on a different container:
* airflow-webserver
* airflow-scheduler
* airflow-worker
* airflow-triggerer
* mlflow 

To create and start multiple container, from terminal run the following command:
```
docker compose up -d
```

<a name="airflow"/>

### Airflow
In order to access to `Airflow server` visit the page: `localhost:8080`

![img](docs/imgs/airflow_home.png)

And take a step into `Airflow` world!

To start creating DAGS initialize an empty folder named `dags` and populate it with as many scripts as you need.
```bash
└── dags
     └── example_dag.py
```

<a name="mlflow"/>

### MLFlow
In order to monitor `MLflow experiments` through its server, visit the page: `localhost:600`

![img](docs/imgs/mlflow_home.png)

<a name="airflow_and_mlflow"/>

## Connect Airflow to MLflow 
To establish a connection between `Airflow` and `MLflow`, define the URI of the `MLflow server`:
```
mlflow.set_tracking_uri('http://mlflow:600')
```

After that, create a new connection on `Airflow` that points to that port.
<img width="1418" alt="image" src="https://user-images.githubusercontent.com/31510474/196529307-3f2df479-a11b-4a0c-bf73-090b82024907.png">


<a name="references"/>

## References
* [Airflow Docker](https://airflow.apache.org/docs/apache-airflow/2.0.1/start/docker.html)
* [What is Airflow?](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
* [MLflow](https://mlflow.org/docs/latest/index.html)
