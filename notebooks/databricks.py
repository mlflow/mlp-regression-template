# Databricks notebook source
# MAGIC %md
# MAGIC # MLflow Regression Pipeline Databricks Notebook
# MAGIC This notebook runs the MLflow Regression Pipeline on Databricks and inspects its results.
# MAGIC 
# MAGIC For more information about the MLflow Regression Pipeline, including usage examples,
# MAGIC see the [Regression Pipeline overview documentation](https://mlflow.org/docs/latest/pipelines.html#regression-pipeline)
# MAGIC and the [Regression Pipeline API documentation](https://mlflow.org/docs/latest/python_api/mlflow.pipelines.html#module-mlflow.pipelines.regression.v1.pipeline).

# COMMAND ----------

# MAGIC %pip install git+https://github.com/mlflow/mlflow.git@refs/pull/6147/head
# MAGIC %pip install -r ../requirements.txt

# COMMAND ----------

from mlflow.pipelines import Pipeline

p = Pipeline(profile="databricks")

# COMMAND ----------

p.clean()

# COMMAND ----------

p.inspect()

# COMMAND ----------

p.run("ingest")

# COMMAND ----------

p.run("split")

# COMMAND ----------

p.run("transform")

# COMMAND ----------

p.run("train")

# COMMAND ----------

p.run("evaluate")

# COMMAND ----------

p.run("register")

# COMMAND ----------

p.inspect("train")

# COMMAND ----------

test_data = p.get_artifact("test_data")
test_data.describe()

# COMMAND ----------

trained_model = p.get_artifact("model")
print(trained_model)

# COMMAND ----------

import os
import requests
import numpy as np
import pandas as pd

def create_tf_serving_json(data):
  return {'inputs': {name: data[name].tolist() for name in data.keys()} if isinstance(data, dict) else data.tolist()}

def score_model(dataset):
  url = 'https://e2-dogfood.staging.cloud.databricks.com/model-endpoint/taxi_fare_regressor/57/invocations'
  headers = {'Authorization': f'Bearer {os.environ.get("DATABRICKS_TOKEN")}'}
  data_json = dataset.to_dict(orient='split') if isinstance(dataset, pd.DataFrame) else create_tf_serving_json(dataset)
  response = requests.request(method='POST', headers=headers, url=url, json=data_json)
  if response.status_code != 200:
    raise Exception(f'Request failed with status {response.status_code}, {response.text}')
  return response.json()
