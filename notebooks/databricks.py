# Databricks notebook source

import mlflow.pipelines

help(mlflow.pipelines)

# COMMAND ----------

mlflow.pipelines.clean()

# COMMAND ----------

mlflow.pipelines.ingest()

# COMMAND ----------

mlflow.pipelines.split()

# COMMAND ----------

mlflow.pipelines.transform()

# COMMAND ----------

mlflow.pipelines.train()

# COMMAND ----------

mlflow.pipelines.evaluate()
