# Databricks notebook source
# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# MAGIC %md
# MAGIC # MLflow Regression Pipeline Notebook
# MAGIC 
# MAGIC This notebook runs the MLflow Regression Pipeline on Databricks and inspects its results. For more information about the MLflow Regression Pipeline, including usage examples, see the [Regression Pipeline overview documentation](https://mlflow.org/docs/latest/pipelines.html#regression-pipeline) the [Regression Pipeline API documentation](https://mlflow.org/docs/latest/python_api/mlflow.pipelines.html#module-mlflow.pipelines.regression.v1.pipeline).

# COMMAND ----------

from mlflow.pipelines import Pipeline

p = Pipeline(profile="local")

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

training_data = p.get_artifact("training_data")
training_data.describe()

# COMMAND ----------

trained_model = p.get_artifact("model")
print(trained_model)
