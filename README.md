# MLflow Pipelines Regression Template

## Installation instructions
1. Clone the MLflow Pipelines template repo locally: `git clone https://github.com/mlflow/mlp-regression-template.git`.
2. Enter the root of the template: `cd mlp-regression-template`.
3. Install required packages: `pip install mlflow-1.24.1.dev0-py3-none-any.whl && pip install -r requirements.txt`

## Log to designated MLflow Experiment
To log pipeline runs to a particular MLflow experiment, 
1. Open `profiles/databricks.yaml` or `profiles/local.yaml`, depending on your running environment.
2. Uncomment the `experiment` section, specify the name of the experiment.

## Development Environment -- Databricks

[Sync](https://docs.databricks.com/repos.html) this repo and run `notebooks/databricks` on an DBR 11.x cluster with [workspace files support enabled](https://docs.databricks.com/repos.html#work-with-non-notebook-files-in-a-databricks-repo).

**Note** We recommend to open at least **3 browser tabs** to facilitate easier development:
- One tab for pipeline.yaml
- One tab for changing step function defined in steps/{step}.py
- One tab for the driver notebook (notebooks/databricks)

### Accessing MLflow Pipeline Runs
You should be able to find experiments and runs on the Databricks ML Experiments page.

## Development Environment -- Local machine
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

### Accessing MLflow Pipeline Runs
To check MLflow experiment and runs from pipeline execution, try the following command from the template root directory.

```
mlflow ui --backend-store-uri sqlite:///metadata/mlflow/mlruns.db --default-artifact-root ./metadata/mlflow/mlartifacts --host localhost -p 5001
```
Then open a browser tab pointing to [http://127.0.0.1:5001](http://127.0.0.1:5001)


