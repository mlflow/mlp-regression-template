# MLflow Pipelines Regression Template

### Play with the demo

#### Databricks

[Sync](https://docs.databricks.com/repos.html) this repo and run `notebooks/databricks` on an MLR 10.3+ cluster with [workspace files support enabled](https://docs.databricks.com/repos.html#work-with-non-notebook-files-in-a-databricks-repo).

#### Jupyter

Run `notebooks/jupyter.ipynb` under the current Python environment.

#### CLI

```
mlflow pipelines --help
mlflow pipelines clean
mlflow pipelines ingest
mlflow pipelines run --step step_name --profile profile_name
```

Check MLflow UI

```
cd /tmp/mlruns
mlflow ui
```
