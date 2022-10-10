# MLflow Pipelines Regression Template
The MLflow Regression Pipeline is an [MLflow Pipeline](https://mlflow.org/docs/latest/pipelines.html) for developing
high-quality regression models. 
It is designed for developing models using scikit-learn and frameworks that integrate with scikit-learn, 
such as the `XGBRegressor` API from XGBoost.

This repository is a template for developing production-ready regression models with the MLflow Regression Pipeline.
It provides a pipeline structure for creating models, and pointers to configurations and code files that should
be filled in to produce a working pipeline.

Code developed with this template should be run with [MLflow Pipelines](https://mlflow.org/docs/latest/pipelines.html). 
An example implementation of this template can be found in the [MLP Regression Example repo](https://github.com/mlflow/mlp-regression-example), 
which targets the NYC taxi dataset for its training problem.

**Note**: [MLflow Pipelines](https://mlflow.org/docs/latest/pipelines.html)
is an experimental feature in [MLflow](https://mlflow.org).
If you observe any issues,
please report them [here](https://github.com/mlflow/mlflow/issues).
For suggestions on improvements,
please file a discussion topic [here](https://github.com/mlflow/mlflow/discussions).
Your contribution to MLflow Pipelines is greatly appreciated by the community!

## Key Features
- Deterministic data splitting
- Reproducible data transformations
- Hyperparameter tuning support
- Model registration for use in production
- Starter code for ingest, split, transform and train steps
- Cards containing step results, including dataset profiles, model leaderboard, performance plots and more

## Installation
Follow the [MLflow Pipelines installation guide](https://mlflow.org/docs/latest/pipelines.html#installation). 
You may need to install additional libraries for extra features:
- [Hyperopt](https://pypi.org/project/hyperopt/)  is required for hyperparameter tuning.
- [PySpark](https://pypi.org/project/pyspark/)  is required for distributed training or to ingest Spark tables.
- [Delta](https://pypi.org/project/delta-spark/) is required to ingest Delta tables.
These libraries are available natively in the [Databricks Runtime for Machine Learning](https://docs.databricks.com/runtime/mlruntime.html).

## Get started
After installing MLflow Pipelines, you can clone this repository to get started.  
Simply fill in the required values in the [Pipeline configuration file](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml) 
and in the appropriate profile configuration: [`local.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/profiles/local.yaml) 
(if running locally) or [`databricks.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/profiles/databricks.yaml) 
(if running on Databricks).  
The Pipeline will then be in a runnable state, and when run completely, will produce a trained model ready for batch
scoring, along with cards containing detailed information about the results of each step. 
The model will also be registered to the MLflow Model Registry if it meets registration thresholds. 
To iterate and improve your model, follow the [MLflow Pipelines usage guide](https://mlflow.org/docs/latest/pipelines.html#usage). 
Note that iteration will likely involve filling in the FIXMEs in the 
step code files with your own code, in addition to the configuration keys.

## Reference
TODO INSERT IMAGE

This is a visual overview of the MLflow Regression Pipeline's information flow.

Model develompent consists of the following sequential steps:
```
ingest -> split -> transform -> train -> evaluate -> register
```

The batch scoring workflow consists of the following sequential steps:
```
ingest -> predict
```
A detailed reference for each step follows.
### Step artifacts
Each of the steps in the pipeline produces artifacts after completion. These artifacts consist of cards containing
detailed execution information, as well as other step-specific information.
The [`Pipeline.inspect()`](https://mlflow.org/docs/latest/python_api/mlflow.pipelines.html#mlflow.pipelines.regression.v1.pipeline.RegressionPipeline.inspect)
API is used to view step cards. The [`get_artifact`](https://mlflow.org/docs/latest/python_api/mlflow.pipelines.html#mlflow.pipelines.regression.v1.pipeline.RegressionPipeline.get_artifact)
API is used to load all other step artifacts by name.  
Per-step artifacts are further detailed in the following step references.

### Ingest step
The ingest step resolves the dataset specified by the `data` section in [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml)
and converts it to parquet format, leveraging the custom loader code specified in the `data` section if necessary.  
**Note**: If you make changes to the dataset referenced by the ingest step (e.g. by adding new records or columns), 
you must manually re-run the ingest step in order to use the updated dataset in the pipeline. 
The ingest step does not automatically detect changes in the dataset.

The custom loader function allows use of datasets in other formats, such as `csv`. 
The function should be defined in [`steps/ingest.py`](https://github.com/mlflow/mlp-regression-template/blob/main/steps/ingest.py),
and should accept two parameters:
- `file_path`: `str`. Path to the dataset file.
- `file_format`: `str`. The file format string, such as `"csv"`.

It should return a Pandas DataFrame representing the content of the specified file. [`steps/ingest.py`](https://github.com/mlflow/mlp-regression-template/blob/main/steps/ingest.py) contains an example placeholder function.

#### Data
The input dataset is specified by the `data` section in [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml). 
The reference for the keys under `data` is as follows:
<details>
<summary>Reference</summary>

- `location`: string. Required, unless `format` is `spark_sql`.  
Dataset locations on the local filesystem are supported, as 
well as HTTP(S) URLs and any other remote locations [resolvable by MLflow](https://mlflow.org/docs/latest/tracking.html#artifact-stores).  
Examples: 
```
location: ./data/sample.parquet
```
```
location: https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet
```
- `format`: string. Required.  
One of `parquet`, `spark_sql` and `delta`.  


- `custom_loader_method`: string. Optional.  
Fully qualified name of the custom loader function.  
Example using the default placeholder method in `steps/ingest.py`: 
```
custom_loader_method: steps.ingest.load_file_as_dataframe
```

- `sql`: string. Required if format is `spark_sql`. In that case, this key specifies a SparkSQL statement that identifies the dataset to use.
- `version`: int. Optional. If the `delta` format is specified, use this to specify the Delta table version to read from.
- `timestamp`: timestamp. Optional. If the `delta` format is specified, use this to specify the timestamp at which to read data.
</details>


## Adapt the template to your ML problem
This template is not directly runnable. For runnable examples,
please checkout [this](https://github.com/mlflow/mlr-regression-example) repository.
To adapt this template to your specific ML problem at hand,
1. Find all **FIXME::REQUIRED** fields in *pipeline.yaml* and *profiles/\*.yaml*,
follow the instructions inline to supply valid values to those fields.
2. Run the pipeline via *notebooks/databricks.py* or *notebooks/jupyter.ipynb*.
3. Improve the model quality by finding all **FIXME::OPTIONAL** fields,
modifying them accordingly, and iterating through various pipeline steps in the notebook.

## Log to the designated MLflow Experiment
To log pipeline runs to a particular MLflow experiment:
1. Open `profiles/databricks.yaml` or `profiles/local.yaml`, depending on your environment.
2. Edit (and uncomment, if necessary) the `experiment` section, specifying the name of the
   desired experiment for logging.

## Development Environment -- Databricks
[Sync](https://docs.databricks.com/repos.html) this repository with
[Databricks Repos](https://docs.databricks.com/repos.html) and run the `notebooks/databricks`
notebook on a Databricks Cluster running version 11.0 or greater of the
[Databricks Runtime](https://docs.databricks.com/runtime/dbr.html) or the
[Databricks Runtime for Machine Learning](https://docs.databricks.com/runtime/mlruntime.html)
with [workspace files support enabled](https://docs.databricks.com/repos.html#work-with-non-notebook-files-in-a-databricks-repo).

**Note**: When making changes to pipelines on Databricks,
it is recommended that you edit files on your local machine and
use [dbx](https://docs.databricks.com/dev-tools/dbx.html) to sync them to Databricks Repos, as
demonstrated [here](https://mlflow.org/docs/latest/pipelines.html#usage)

**Note**: data profiles display in step cards are not visually compatible with dark theme.
Please avoid using the dark theme if possible.

### Accessing MLflow Pipeline Runs
You can find MLflow Experiments and MLflow Runs created by the pipeline on the
[Databricks ML Experiments page](https://docs.databricks.com/applications/machine-learning/experiments-page.html#experiments).

## Development Environment -- Local machine
### Jupyter
1. Launch the Jupyter Notebook environment via the `jupyter notebook` command.
2. Open and run the `notebooks/jupyter.ipynb` notebook in the Jupyter environment.

**Note**: data profiles display in step cards are not visually compatible with dark theme.
Please avoid using the dark theme if possible.

### Command-Line Interface (CLI)

First, enter the template root directory and set the profile via environment variable
```
cd mlp-regression-template
```
```
export MLFLOW_PIPELINES_PROFILE=local
```

Then, try running the
following [MLflow Pipelines CLI](https://mlflow.org/docs/latest/cli.html#mlflow-pipelines)
commands to get started.
Note that the `--step` argument is optional.
Pipeline commands without a `--step` specified act on the entire pipeline instead.

Available step names are: `ingest`, `split`, `transform`, `train`, `evaluate` and `register`.

- Display the help message:
```
mlflow pipelines --help
```

- Run a pipeline step or the entire pipeline:
```
mlflow pipelines run --step step_name
```

- Inspect a step card or the pipeline dependency graph:
```
mlflow pipelines inspect --step step_name
```

- Clean a step cache or all step caches:
```
mlflow pipelines clean --step step_name
```

**Note**: a short cut to `mlflow pipelines` is installed as `mlp`.
For example, to run the ingest step,
instead of issuing `mlflow pipelines run --step ingest`, you may type
```
mlp -s ingest
```

### Accessing MLflow Pipeline Runs
To view MLflow Experiments and MLflow Runs created by the pipeline:

1. Enter the template root directory: `cd mlp-regression-template`

2. Start the MLflow UI

```sh
mlflow ui \
   --backend-store-uri sqlite:///metadata/mlflow/mlruns.db \
   --default-artifact-root ./metadata/mlflow/mlartifacts \
   --host localhost
```

3. Open a browser tab pointing to [http://127.0.0.1:5000](http://127.0.0.1:5000)
