# Databricks notebook source

# MAGIC %md
# MAGIC # MLflow Regression Pipeline Databricks Notebook
# MAGIC This notebook runs the MLflow Regression Pipeline on Databricks and inspects its results.
# MAGIC
# MAGIC For more information about the MLflow Regression Pipeline, including usage examples,
# MAGIC see the [Regression Pipeline overview documentation](https://mlflow.org/docs/latest/pipelines.html#regression-pipeline)
# MAGIC and the [Regression Pipeline API documentation](https://mlflow.org/docs/latest/python_api/mlflow.pipelines.html#module-mlflow.pipelines.regression.v1.pipeline).

# COMMAND ----------

# MAGIC %pip install mlflow[pipelines]
# MAGIC %pip install -r ../requirements.txt

# COMMAND ----------

# MAGIC %md ### Create a new pipeline with "databricks" profile:

# COMMAND ----------

from mlflow.pipelines import Pipeline

p = Pipeline(profile="databricks")

# COMMAND ----------

# MAGIC %md ### Inspect a newly created pipeline using a graphical representation:

# COMMAND ----------

p.inspect()

# COMMAND ----------

# MAGIC %md ### Ingest the dataset into the pipeline:

# COMMAND ----------

p.run("ingest")

# COMMAND ----------

# MAGIC %md ### Split the dataset in train, validation and test data profiles:

# COMMAND ----------

p.run("split")

# COMMAND ----------

training_data = p.get_artifact("training_data")
training_data.describe()

# COMMAND ----------

p.run("transform")

# COMMAND ----------

# MAGIC %md ### Using training data profile, train the model:

# COMMAND ----------

p.run("train")

# COMMAND ----------

trained_model = p.get_artifact("model")
print(trained_model)

# COMMAND ----------

# MAGIC %md ### Evaluate the resulting model using validation data profile:

# COMMAND ----------


p.run("evaluate")

# COMMAND ----------

# MAGIC %md ### Register the trained model in the registry:

# COMMAND ----------

p.run("register")
