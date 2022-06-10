# MLflow Pipelines Regression Template

## Development Environment

### Databricks

[Sync](https://docs.databricks.com/repos.html) this repo and run `notebooks/databricks` on an MLR 10.3+ cluster with [workspace files support enabled](https://docs.databricks.com/repos.html#work-with-non-notebook-files-in-a-databricks-repo).

**Note** We recommend to open at least **3 browser tabs** to facilitate easier development:
- One tab for pipeline.yaml
- One tab for changing step function defined in steps/{step}.py
- One tab for the driver notebook (notebooks/databricks)

### Jupyter

Launch Jupyter Lab via command `jupyter-lab`
Open `notebooks/jupyter.ipynb` under the current Python environment.

### CommandLine Interface (CLI)

First `cd` to the template root directory. Then try the following MLflow commands to get started.
Note that `step_name` is optional:
running pipeline commands without specifying the `step_name` parameter will act on the entire pipeline.

```
mlflow pipelines --help
mlflow pipelines inspect --step step_name
mlflow pipelines run --step step_name
mlflow pipelines clean --step step_name
```

To check MLflow experiment and runs from pipelines, try the following command from the template root directory.

```
mlflow ui --backend-store-uri sqlite:///metadata/mlflow/mlruns.db --default-artifact-root ./metadata/mlflow/mlartifacts --host localhost
```
If you are using a developer version of mlflow, additional steps need to be taken to launch the MLflow UI.
For details, see
[how to install mlflow developer version locally](https://github.com/mlflow/mlflow/blob/master/CONTRIBUTING.rst#developing-and-testing-mlflow)
and specifically on [how to access local MLflow tracking server via UI](https://github.com/mlflow/mlflow/blob/master/CONTRIBUTING.rst#javascript-and-ui).
