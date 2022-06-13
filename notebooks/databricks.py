# Databricks notebook source

# Pipeline and steps are the main concepts one interacts with MLflow Pipelines.
# To create a Pipeline, simply do p = Pipeline() within this pipeline template directory.
#
# There are 5 major steps within a Pipeline:
# - "ingest":    through this step all data about an ML problem is ingested. To run it, call
#                p.run("ingest"). After running this step. You can fetch the ingested data via
#                p.get_artifact("ingested_data"). By default ingest support Parquet file and Spark
#                SQL commands. For other data formats, modify {template_root}/steps/ingest.py. We
#                have provided an example there for CSV files.
#
# - "split":     In this step, we split the ingested dataset into 3 subsets, namely, "training",
#                "validation" and "test". You can specify the split ratio in pipeline.yaml. If you
#                want to do additional data processing such as cleaning, see
#                {template_root}/steps/split.py for example.
#
# - "transform": This is the place to do feature transformation. Here we require an unfitted
#                transformer to be returned by the user. See
#                {template_root}/steps/transform.py for examples.
#
# - "train":     This is the step to train an estimator. We require an unfitted sklearn estimator
#                to be returned by the user. See {template_root}/steps/train.py for examples.
#
# - "evaluate":  In this step, we evaluate the model via mlflow.evaluate() on the test dataset.
#                If you have custom metrics to be evaluated, specify them in pipeline.yaml and
#                {template_root}/steps/custom_metrics.py.
#
# - "register":  We provide an option to register the model after training and evaluation at this
#                step.

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
