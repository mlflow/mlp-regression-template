# MLflow Pipelines Regression Template
The MLflow Regression Pipeline is an [MLflow Pipeline](https://mlflow.org/docs/latest/pipelines.html) for developing
high-quality regression models. 
It is designed for developing models using scikit-learn and frameworks that integrate with scikit-learn, 
such as the `XGBRegressor` API from XGBoost.

This repository is a template for developing production-ready regression models with the MLflow Regression Pipeline.
It provides a pipeline structure for creating models as well as pointers to configurations and code files that should
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
After installing MLflow Pipelines, you can clone this repository to get started. Simply fill in the required values annotated by `FIXME::REQUIRED` comments in the [Pipeline configuration file](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml) 
and in the appropriate profile configuration: [`local.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/profiles/local.yaml) 
(if running locally) or [`databricks.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/profiles/databricks.yaml) 
(if running on Databricks).

The Pipeline will then be in a runnable state, and when run completely, will produce a trained model ready for batch
scoring, along with cards containing detailed information about the results of each step. 
The model will also be registered to the MLflow Model Registry if it meets registration thresholds. 
To iterate and improve your model, follow the [MLflow Pipelines usage guide](https://mlflow.org/docs/latest/pipelines.html#usage). 
Note that iteration will likely involve filling in the optional `FIXME`s in the 
step code files with your own code, in addition to the configuration keys.

## Reference
![image](https://user-images.githubusercontent.com/66143562/195912433-f1e44829-dea5-4fb2-a034-b197c2cebf71.png)

This is a visual overview of the MLflow Regression Pipeline's information flow.

Model develompent consists of the following sequential steps:
```
ingest -> split -> transform -> train -> evaluate -> register
```

The batch scoring workflow consists of the following sequential steps:
```
ingest_scoring -> predict
```
A detailed reference for each step follows.

 * [Reference](#reference)
    + [Step artifacts](#step-artifacts)
    + [Ingest step](#ingest-step)
      - [Data](#data)
    + [Split step](#split-step)
    + [Transform step](#transform-step)
    + [Train step](#train-step)
    + [Evaluate step](#evaluate-step)
    + [Register step](#register-step)
    + [Batch scoring](#batch-scoring)
      - [Ingest Scoring step](#ingest-scoring-step)
      - [Predict step](#predict-step)
    + [MLflow Tracking / Model Registry configuration](#mlflow-tracking--model-registry-configuration)
    + [Metrics](#metrics)
      - [Built-in metrics](#built-in-metrics)
      - [Custom metrics](#custom-metrics)

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
The input dataset is specified by the `data` section in [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml) as follows: 
<details>
<summary><strong><u>Full configuration reference</u></strong></summary>

- `location`: string. Required, unless `format` is `spark_sql`.  
Dataset locations on the local filesystem are supported, as 
well as HTTP(S) URLs and any other remote locations [resolvable by MLflow](https://mlflow.org/docs/latest/tracking.html#artifact-stores).
One may specify multiple data locations by a list of locations as long as they have the same data format (see example below)
<u>Examples</u>:
  ```
  location: ./data/sample.parquet
  ```
  ```
  location: https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet
  ```
  ```
  location: ["./data/sample.parquet", "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet"]
  ```
- `format`: string. Required.  
One of `parquet`, `spark_sql` and `delta`.  


- `custom_loader_method`: string. Optional.  
Fully qualified name of the custom loader function.  
<u>Example</u>: 
  ```
  custom_loader_method: steps.ingest.load_file_as_dataframe
  ```

- `sql`: string. Required if format is `spark_sql`.  
Specifies a SparkSQL statement that identifies the dataset to use.


- `version`: int. Optional.  
If the `delta` format is specified, use this to specify the Delta table version to read from.


- `timestamp`: timestamp. Optional.  
If the `delta` format is specified, use this to specify the timestamp at which to read data.
</details>

**Step artifacts**
- `ingested_data`: The ingested data as a Pandas DataFrame.

### Split step

The split step splits the ingested dataset produced by the ingest step into:
- a training dataset for model training
- a validation dataset for model performance evaluation & tuning, and 
- a test dataset for model performance evaluation.  

The fraction of records allocated to each dataset is defined by the `split_ratios` attribute of the `split` step
definition in [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml). 
The split step also preprocesses the datasets using logic defined in [`steps/split.py`](https://github.com/mlflow/mlp-regression-template/blob/main/steps/split.py).
Subsequent steps use these datasets to develop a model and measure its performance.

The post-split method should be written in `steps/split.py` and should accept three parameters:
- `train_df`: DataFrame. The unprocessed train dataset.
- `validation_df`: DataFrame. The unprocessed validation dataset.
- `test_df`: DataFrame. The unprocessed test dataset.

It should return a triple representing the processed train, validation and test datasets. `steps/split.py` contains an example placeholder function.

The split step is configured by the `steps.split` section in `pipeline.yaml` as follows:
<details>
<summary><strong><u>Full configuration reference</u></strong></summary>

- `split_ratios`: list. Optional.  
A YAML list specifying the ratios by which to split the dataset into training, validation and test sets.  
<u>Example</u>: 
  ```
  split_ratios: [0.75, 0.125, 0.125] # Defaults to this ratio if unspecified
  ```
- `post_split_filter_method`: string. Optional.   
Fully qualified name of the method to use to "post-process" the split datasets. 
This procedure is meant for removing/filtering records, or other cleaning processes. Arbitrary data transformations 
should be done in the transform step.  
<u>Example</u>:
  ```
  post_split_filter_method: steps.split.process_splits
  ```
</details>

**Step artifacts**:
- `training_data`: the training dataset as a Pandas DataFrame.
- `validation_data`: the validation dataset as a Pandas DataFrame.
- `test_data`: the test dataset as a Pandas DataFrame.

### Transform step

The transform step uses the training dataset created by the split step to fit a transformer that performs the 
user-defined transformations. The transformer is then applied to the training dataset and the validation dataset, 
creating transformed datasets that are used by subsequent steps for estimator training and model performance evaluation.

The user-defined transformation function is not required. If absent, an **identity transformer** will be used.
The user-defined function should be written in
[`steps/transform.py`](https://github.com/mlflow/mlp-regression-template/blob/main/steps/transform.py), 
and should return an unfitted estimator that is sklearn-compatible; that is, the returned object should define 
`fit()` and `transform()` methods. `steps/transform.py` contains an example placeholder function.

The transform step is configured by the `steps.transform` section in [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml):
<details>
<summary><strong><u>Full configuration reference</u></strong></summary>

- `transformer_method`: string. Optional.  
Fully qualified name of the method that returns an `sklearn`-compatible transformer which applies feature 
transformation during model training and inference. If absent, an identity transformer with will be used.
<u>Example</u>:
  ```
  transformer_method: steps.split.transformer_fn
  ```

</details>

**Step artifacts**:
- `transformed_training_data`: transformed training dataset as a Pandas DataFrame.
- `transformed_validation_data`: transformed validation dataset as a Pandas DataFrame.
- `transformer`: the sklearn transformer.


### Train step
The train step uses the transformed training dataset output from the transform step to fit an user-defined estimator. 
The estimator is then joined with the fitted transformer output from the transform step to create a model pipeline. 
Finally, this model pipeline is evaluated against the transformed training and validation datasets to compute performance metrics.  

Custom evaluation metrics are computed according to definitions in [`steps/custom_metrics.py`](https://github.com/mlflow/mlp-regression-template/blob/main/steps/custom_metrics.py)
and the `metrics` section of `pipeline.yaml`; see [Custom Metrics](#custom-metrics) section for reference. 

The model pipeline and its associated parameters, performance metrics, and lineage information are logged to [MLflow Tracking](https://www.mlflow.org/docs/latest/tracking.html), producing an MLflow Run.

The user-defined estimator function should be written in [`steps/train.py`](https://github.com/mlflow/mlp-regression-template/blob/main/steps/train.py), 
and should return an unfitted estimator that is `sklearn`-compatible; that is, the returned object should define 
`fit()` and `transform()` methods. `steps/train.py` contains an example placeholder function.

The train step is configured by the `steps.train` section in [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml):
<details>
<summary><strong><u>Full configuration reference</u></strong></summary>

- `estimator_method`: string. Required.  
Fully qualified name of the method that returns an `sklearn`-compatible estimator used for model training.  
<u>Example</u>:
  ```
  estimator_method: steps.train.estimator_fn
  ```

- Tuning configuration reference

   - `enabled`: boolean. Required.  
   Indicates whether or not tuning is enabled.

   - `max_trials`: int. Required.  
   Max tuning trials to run.

   - `algorithm`: string. Optional.  
   Indicates whether or not tuning is enabled.

   - `early_stop_fn`: string. Optional.  
   Early stopping function to be passed to `hyperopt`.

   - `parallelism`: int. Optional.  
   Number of workers to run `hyperopt` across.

   - `sample_fraction`: float. Optional.  
   Sampling fraction in the range `(0, 1.0]` to indicate the amount of data used in tuning.

   - `parameters`: list. Required.  
   `hyperopt` search space in yaml format.

  <u>Example</u>:
  ```
  tuning:
    enabled: True
    algorithm: "hyperopt.rand.suggest"
    max_trials: 5
    early_stop_fn: "hyperopt.early_stop.no_progress_loss(10)"
    parallelism: 1
    sample_fraction: 0.5
    parameters:
        alpha:
          distribution: "uniform"
          low: 0.0
          high: 0.01
        penalty:
          values: ["l1", "l2", "elasticnet"]
  ```

</details>

**Step artifacts**:
- `model`: the [MLflow Model](https://www.mlflow.org/docs/latest/models.html) pipeline created in the train step 
as a [PyFuncModel](https://www.mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.PyFuncModel) instance.


### Evaluate step
The evaluate step evaluates the model pipeline created by the train step on the test dataset output from the 
split step, computing performance metrics and model explanations. 

Performance metrics are compared against configured thresholds to produce a `model_validation_status`, which indicates 
whether or not a model is validated to be registered to the [MLflow Model Registry](https://www.mlflow.org/docs/latest/model-registry.html) 
by the subsequent [register step](#register-step).  
These model performance thresholds are defined in the 
`validation_criteria` section of the `evaluate` step definition in `pipeline.yaml`. 
Custom evaluation metrics are computed according to definitions in [`steps/custom_metrics.py`](https://github.com/mlflow/mlp-regression-template/blob/main/steps/custom_metrics.py)
and the `metrics` section of `pipeline.yaml`; see the [custom metrics section](#custom-metrics) for reference. 

Model performance metrics and explanations are logged to the same MLflow Tracking Run used by the train step.

The evaluate step is configured by the `steps.evaluate` section in [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml):
<details>
<summary><strong><u>Full configuration reference</u></strong></summary>

- `validation_criteria`: list. Optional.  
A list of validation thresholds, each of which a trained model must meet in order to be eligible for 
registration in the [register step](#register-step).
A definition for a validation threshold consists of a metric name
(either a [built-in metric](#built-in-metrics) or a [custom metric](#custom-metrics)), and a threshold value.  
<u>Example</u>:
  ```
  validation_critera:
    - metric: root_mean_squared_error
      threshold: 10
  ```
</details>

**Step artifacts**:
- `run`: the MLflow Tracking Run containing the model pipeline, as well as performance and metrics created during 
the train and evaluate steps.


### Register step
The register step checks the `model_validation_status` output of the preceding [evaluate step](#evaluate-step) and, 
if model validation was successful (if model_validation_status is `'VALIDATED'`), registers the model pipeline created
by the train step to the MLflow Model Registry. If the `model_validation_status` does not indicate that the model 
passed validation checks (if model_validation_status is `'REJECTED'`), the model pipeline is **not** registered to the 
MLflow Model Registry.  
If the model pipeline is registered to the MLflow Model Registry, a `registered_model_version` is produced containing 
the model name and the model version.

The register step is configured by the `steps.register` section in [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml):
<details>
<summary><strong><u>Full configuration reference</u></strong></summary>

- `model_name`: string. Required.  
Specifies the name to use when registering the trained model to the model registry.


- `allow_non_validated_model`: boolean. Required.  
Whether to allow registration of models that fail to meet performance thresholds.

</details>

**Step artifacts**:
- `registered_model_version`: the MLflow Model Registry [ModelVersion](https://mlflow.org/docs/latest/model-registry.html#concepts)
registered in this step.


### Batch scoring
After model training, the regression pipeline provides the capability to score new data with the
trained model.

#### Ingest Scoring step
The ingest scoring step, defined in the `data_scoring` section in [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml), 
specifies the dataset used for batch scoring and has the same API as the [ingest step](#ingest-step).

**Step artifacts**:
- `ingested_scoring_data`: the ingested scoring data as a Pandas DataFrame.

#### Predict step
The predict step uses the model registered by the [register step](#register-step) to score the 
ingested dataset produced by the [ingest scoring step](#ingest-scoring-step) and writes the resulting 
dataset to the specified output format and location. To fix a specific model for use in the predict 
step, provide its model URI as the `model_uri` attribute of the `pipeline.yaml` predict step definition.

The predict step is configured by the `steps.predict` section in [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml):
<details>
<summary><strong><u>Full configuration reference</u></strong></summary>

- `output_format`: string. Required.  
Specifies the output format of the scored data from the predict step. One of `parquet`, `delta`, and 
`table`. The `parquet` format writes the scored data as parquet files under a specified path. The 
`delta` format writes the scored data as a delta table under a specified path. The `table` format 
writes the scored data as delta table and creates a metastore entry for this table with a specified name.


- `output_location`: string. Required.  
For the `parquet` and `delta` output formats, this attribute specifies the output path for writing 
the scored data. In Databricks, this path will be written to be under [DBFS](https://docs.databricks.com/dbfs/index.html), 
e.g. the path `my/special/path` will be written under `/dbfs/my/special/path`. For the `table` output 
format, this attribute specifies the table name that is used to create the metastore entry for the 
written delta table.
<u>Example</u>: 
  ```
  output_location: ./outputs/predictions
  ```


- `model_uri`: string. Optional.  
Specifies the URI of the model to use for batch scoring. If empty, the latest model version produced
by the register step is used. If the register step was cleared, the latest version of the 
registered model specified by the `model_name` attribute of the `pipeline.yaml` [register step](#register-step) 
will be used.  
<u>Example</u>: 
  ```
  model_uri: models/model.pkl
  ```


- `result_type`: string. Optional. Defaults to `double`.  
Specifies the data type for predictions generated by the model. See the 
[MLflow spark_udf API docs](https://www.mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.spark_udf) 
for more information.


- `save_mode`: string. Optional. Defaults to `default`.  
Specifies the save mode used by Spark for writing the scored data. See the 
[PySpark save modes documentation](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#save-modes) 
for more information.
</details>


**Step artifacts**:
- `scored_data`: the scored dataset, with model predictions under the `prediction` column, as a Pandas DataFrame.


### MLflow Tracking / Model Registry configuration
The MLflow Tracking server can be configured to log MLflow runs to a specific server. Tracking information is specified
in the profile configuration files - [`profiles/local.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/profiles/local.yaml)
if running locally and [`profiles/databricks.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/profiles/databricks.yaml) 
if running on Databricks.  

Configuring a tracking server is optional. If this configuration is absent, the default experiment will be used.

Tracking information is configured with the `experiment` section in the profile configuration:
<details>
<summary><strong><u>Full configuration reference</u></strong></summary>

- `name`: string. Required, if configuring tracking.  
Name of the experiment to log MLflow runs to.


- `tracking_uri`: string. Required, if configuring tracking.  
URI of the MLflow tracking server to log runs to. Alternatively, the `MLFLOW_TRACKING_URI` environment variable can be [set to point to a valid tracking server](https://www.mlflow.org/docs/latest/python_api/mlflow.html#mlflow.set_tracking_uri).


- `artifact_location`: string. Optional. 
URI of the location to log run artifacts to.

</details>

To register trained models to the MLflow Model Registry, further configuration may be required. If unspecified, models will be logged to the same server as specified in the tracking URI. 

To register models to a different server, specify the desired server in the `model_registry` section in the profile configuration:
<details>
<summary><strong><u>Full configuration reference</u></strong></summary>

- `uri`: string. Required, if this section is present.  
URI of the model registry server to which to register trained models.

</details>

### Metrics
Evaluation metrics calculate model performance against different datasets. The metrics defined in the pipeline 
will be calculated as part of the training and evaluation steps, and calculated values will be recorded in each 
step’s information card.

This regression pipeline features a set of built-in metrics, and supports user-defined metrics as well.

The **primary evaluation metric** is the one that will be used to select the best performing model in the MLflow UI as
well as in the train and evaluation steps. This can be either a built-in metric or a custom metric (see below).  
Models are ranked by this primary metric.

Metrics are configured under the `metrics` section of [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml), according to the following specification:
<details>
<summary><strong><u>Full configuration reference</u></strong></summary>

- `primary`: string. Required.  
The name of the primary evaluation metric.


- `custom`: string. Optional.  
A list of custom metric configurations.

</details>

Note that each metric specifies a boolean value `greater_is_better`, which indicates whether a higher value for that 
metric is associated with better model performance.

#### Built-in metrics
The following metrics are built-in. Note that `greater_is_better = False` for all these metrics:

- `mean_absolute_error`
- `mean_squared_error`
- `root_mean_squared_error`
- `max_error`
- `mean_absolute_percentage_error`

#### Custom metrics
Custom evaluation metrics define how trained models should be evaluated against custom criteria not captured by 
built-in `sklearn` evaluation metrics.

Custom evaluation metric functions should be defined in [`steps/custom_metrics.py`](https://github.com/mlflow/mlp-regression-template/blob/main/steps/custom_metrics.py). 
Each should accept two parameters:
- `eval_df`: DataFrame.  
A Pandas DataFrame containing two columns:
  - `prediction`: Predictions produced by submitting input data to the model.
  - `target`: Corresponding target truth values.


- `builtin_metrics`: `Dict[str, int]`.  
The built-in metrics calculated during model evaluation. Maps metric names to corresponding scalar values.

The custom metric function should return a `Dict[str, int]`, mapping custom metric names to corresponding scalar metric values.

Custom metrics are specified as a list under the `metrics.custom` key in [`pipeline.yaml`](https://github.com/mlflow/mlp-regression-template/blob/main/pipeline.yaml), specified as follows:
- `name`: string. Required.  
Name of the custom metric. This will be the name by which you refer to this metric when including it in model evaluation or model training.


- `function`: string. Required. Specifies the function this custom metric refers to.


- `greater_is_better`: boolean. Required. Boolean indicating whether a higher metric value indicates better model 
performance.

An example custom metric configuration is as follows:
```
custom:
 - name: weighted_mean_square_error
   function: steps.custom_metrics.get_custom_metrics
   greater_is_better: True
```
