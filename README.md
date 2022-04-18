# MLflow Pipelines Demo

### Play with the demo

#### Databricks

[Sync](https://docs.databricks.com/repos.html) this repo and run `notebooks/databricks` on an MLR 10.3+ cluster with [workspace files support enabled](https://docs.databricks.com/repos.html#work-with-non-notebook-files-in-a-databricks-repo).

#### Jupyter

Run `notebooks/jupyter.ipynb` under the current Python environment.

#### CLI

```
cd demo
mlflow pipelines --help
mlflow pipelines clean
mlflow pipelines ingest
mlflow pipelines split
mlflow pipelines transform
mlflow pipelines train
mlflow pipelines evaluate
mlflow pipelines inspect
```

Check MLflow UI

```
cd /tmp/mlruns
mlflow ui
```

Modify `train.py` and run

```
mlflow pipelines evaluate
```

## Apparent gaps

* The `autos.yaml` is not actually used.
* The mlflow experiment folder is hardcoded to `file:/tmp/mlruns`.
* MLflow integration doesn't work on Databricks.
