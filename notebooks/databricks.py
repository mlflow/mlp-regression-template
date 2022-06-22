# Databricks notebook source
# Pipeline and steps are the main concepts one interacts with MLflow Pipelines.
# To create a Pipeline, simply do p = Pipeline() within this pipeline template directory.
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
