split_objects = split_train.parquet split_test.parquet split_summary.html

split: $(split_objects)

%_train.parquet %_test.parquet %_summary.html: datasets/autos.parquet
	python -c "from mlflow.pipelines.split_step import run_split_step; run_split_step(input_path='datasets/autos.parquet', summary_path='$*_summary.html', train_output_path='$*_train.parquet', test_output_path='$*_test.parquet')"

transform_objects = transform_transformer.pkl transform_train_transformed.parquet

transform: $(transform_objects)

%_transformer.pkl %_train_transformed.parquet: steps/transform.py steps/transformer_config.yaml split_train.parquet
	python -c "from mlflow.pipelines.transform_step import run_transform_step; run_transform_step(train_data_path='split_train.parquet', transformer_config_path='steps/transformer_config.yaml', transformer_output_path='$*_transformer.pkl', transformed_data_output_path='$*_train_transformed.parquet')"

train_objects = train_pipeline.pkl train_run_id

train: $(train_objects)

%_pipeline.pkl %_run_id: steps/train.py steps/train_config.yaml transform_train_transformed.parquet transform_transformer.pkl
	python -c "from mlflow.pipelines.train_step import run_train_step; run_train_step(transformed_train_data_path='transform_train_transformed.parquet', train_config_path='steps/train_config.yaml', transformer_path='transform_transformer.pkl', tracking_uri='file:/tmp/mlruns', pipeline_output_path='$*_pipeline.pkl', run_id_output_path='$*_run_id')"

evaluate_objects = evaluate_worst_training_examples.parquet evaluate_metrics.json evaluate_explanations.html

evaluate: $(evaluate_objects)

%_worst_training_examples.parquet %_metrics.json %_explanations.html: train_pipeline.pkl split_train.parquet train_run_id
	python -c "from mlflow.pipelines.evaluate_step import run_evaluate_step; run_evaluate_step(pipeline_path='train_pipeline.pkl', tracking_uri='file:/tmp/mlruns', run_id_path='train_run_id', train_data_path='split_train.parquet', test_data_path='split_test.parquet', explanations_output_path='$*_explanations.html', metrics_output_path='$*_metrics.json', worst_train_examples_output_path='$*_worst_training_examples.parquet')"

clean:
	rm -rf $(split_objects) $(transform_objects) $(train_objects) $(evaluate_objects)
