# MLflow Pipelines Regression Template

## Development Environment

### Databricks

[Sync](https://docs.databricks.com/repos.html) this repo and run `notebooks/databricks` on an MLR 10.3+ cluster with [workspace files support enabled](https://docs.databricks.com/repos.html#work-with-non-notebook-files-in-a-databricks-repo).

### Jupyter

Launch Jupyter Lab via command `jupyter-lab`
Open `notebooks/jupyter.ipynb` under the current Python environment.

### CLI

Try the following MLflow commands.
```
mlflow pipelines --help
mlflow pipelines inspect --step step_name
mlflow pipelines run --step step_name
mlflow pipelines clean --step step_name
```

If you develop locally, to check MLflow experiment and runs from pipelines, try the following command from the template root directory.

```
mlflow ui --backend-store-uri sqlite:///metadata/mlflow/mlruns.db --default-artifact-root ./metadata/mlflow/mlartifacts --host localhost
```
