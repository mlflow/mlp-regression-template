# MLflow Pipelines Regression Template
The [MLflow Regression Pipeline](https://mlflow.org/docs/latest/pipelines.html#regression-pipeline)
is an [MLflow Pipeline](https://mlflow.org/docs/latest/pipelines.html) for developing high-quality
regression models. It is designed for developing models using scikit-learn and frameworks that
integrate with scikit-learn, such as the ``XGBRegressor`` API from XGBoost.

For more information about the MLflow Regression Pipeline, check out the documentation at
https://mlflow.org/docs/latest/pipelines.html#regression-pipeline. For more information about MLflow
Pipelines, see https://mlflow.org/docs/latest/pipelines.html.

## Installation instructions
1. Clone the MLflow Pipelines template repo locally: `git clone https://github.com/mlflow/mlp-regression-template.git`.
2. Install MLflow Pipelines via `pip install mlflow[pipelines]`
3. Enter the root of the template: `cd mlp-regression-template`
4. Install template dendencies: `pip install -r requirements.txt`

## Log to the designated MLflow Experiment
To log pipeline runs to a particular MLflow experiment:
1. Open `profiles/databricks.yaml` or `profiles/local.yaml`, depending on your environment.
2. Edit (and uncomment, if necessary) the `experiment` section, specifying the name of the
   desired experiment for logging.

## Development Environment -- Databricks
[Sync](https://docs.databricks.com/repos.html) this repo and run `notebooks/databricks` on a DBR 11.x cluster with [workspace files support enabled](https://docs.databricks.com/repos.html#work-with-non-notebook-files-in-a-databricks-repo).

**Note**: When making changes to pipelines on Databricks,
it is recommended that you either edit files on your local machine and
use dbx to sync them to Databricks Repos, as demonstrated [here](https://mlflow.org/docs/latest/pipelines.html#usage),
or edit files in Databricks Repos by opening separate browser tabs
for each YAML file or Python code module that you wish to modify.

For the latter approach,
we recommend to open at least **3 browser tabs** to facilitate easier development:
- One tab for `pipeline.yaml`
- One tab for changing step function defined in `steps/{step}.py`
- One tab for the driver notebook (`notebooks/databricks`)

### Accessing MLflow Pipeline Runs
You can find MLflow Experiments and MLflow Runs for the pipeline on the
[Databricks ML Experiments page](https://docs.databricks.com/applications/machine-learning/experiments-page.html#experiments).

## Development Environment -- Local machine
### Jupyter

1. Launch the Jupyter Notebook environment via the `jupyter notebook` command.
2. Open `notebooks/jupyter.ipynb` in the Jupyter Notebook environment.

### Command-Line Interface (CLI)

First, enter the template root directory via ``cd mlp-regression-template`. Then, try running the
following [MLflow CLI](https://mlflow.org/docs/latest/cli.html) commands to get started. Note that
the `step_name` argument is optional; pipeline commands that are run without a `step_name` act on
the entire pipeline.

```
export MLFLOW_PIPELINES_PROFILE=local
mlflow pipelines --help
mlflow pipelines inspect --step step_name
mlflow pipelines run --step step_name
mlflow pipelines clean --step step_name
```

### Accessing MLflow Pipeline Runs
To view MLflow Experiments and MLflow Runs from pipeline execution:

1. Enter the template root directory

```
cd mlp-regression-template
```

2. Start the MLflow UI

```
mlflow ui --backend-store-uri sqlite:///metadata/mlflow/mlruns.db --default-artifact-root ./metadata/mlflow/mlartifacts --host localhost
```

3. Open a browser tab pointing to [http://127.0.0.1:5000](http://127.0.0.1:5000)
