# MLflow Pipelines Regression Template

## Installation instructions
1. Clone the MLflow Pipelines template repo locally: `git clone https://github.com/mlflow/mlp-regression-template.git`.
2. Enter the root of the template: `cd mlp-regression-template`
3. Install template dendencies: `pip install -r requirements.txt`

## Log to designated MLflow Experiment
To log pipeline runs to a particular MLflow experiment, 
1. Open `profiles/databricks.yaml` or `profiles/local.yaml`, depending on your running environment.
2. Uncomment the `experiment` section, specify the name of the experiment.

## Development Environment -- Databricks
[Sync](https://docs.databricks.com/repos.html) this repo and run `notebooks/databricks` on an DBR 11.x cluster with [workspace files support enabled](https://docs.databricks.com/repos.html#work-with-non-notebook-files-in-a-databricks-repo).

**Note** When making changes to pipelines on Databricks,
it is recommended that you either edit files on your local machine and
use dbx to sync them to Databricks Repos, as demonstrated [here](https://mlflow.org/docs/latest/pipelines.html#usage),
or edit files in Databricks Repos by opening separate browser tabs
for each YAML file or Python code module that you wish to modify.

For the later approach,
we recommend to open at least **3 browser tabs** to facilitate easier development:
- One tab for `pipeline.yaml`
- One tab for changing step function defined in `steps/{step}.py`
- One tab for the driver notebook (`notebooks/databricks`)

### Accessing MLflow Pipeline Runs
You should be able to find experiments and runs on the Databricks ML Experiments page.

## Development Environment -- Local machine
### Jupyter

Launch Jupyter Notebook via command `jupyter notebook`
Open `notebooks/jupyter.ipynb` under the current Python environment.

### CommandLine Interface (CLI)

First `cd` to the template root directory. Then try the following MLflow commands to get started.
Note that `step_name` is optional --
running pipeline commands without specifying the `step_name` parameter will act on the entire pipeline.

```
export MLFLOW_PIPELINES_PROFILE=local
mlflow pipelines --help
mlflow pipelines inspect --step step_name
mlflow pipelines run --step step_name
mlflow pipelines clean --step step_name
```

### Accessing MLflow Pipeline Runs
To check MLflow experiment and runs from pipeline execution,
1. follow the [Running the Javascript Dev Server](https://github.com/mlflow/mlflow/blob/master/CONTRIBUTING.rst#running-the-javascript-dev-server) section
2. enter the root of the template directory `cd mlp-regression-template`.
Then try the following command from the template root directory.

```
mlflow ui --backend-store-uri sqlite:///metadata/mlflow/mlruns.db --default-artifact-root ./metadata/mlflow/mlartifacts --host localhost
```

Then open a browser tab pointing to [http://127.0.0.1:3000](http://127.0.0.1:3000)


