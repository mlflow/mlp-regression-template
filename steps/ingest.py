import pandas
from mlflow.pipelines.steps import IngestStep


class MyIngestStep(IngestStep):
    def load_file_as_dataframe(file_path: str, file_format: str):
        if file_format == "csv":
            import pandas

            _logger.warning(
                "Loading dataset CSV using `pandas.read_csv()` with default arguments and assumed index"
                " column 0 which may not produce the desired schema. If the schema is not correct, you"
                " can adjust it by modifying the `load_file_as_dataframe()` function in"
                " `steps/ingest.py`"
            )
            return pandas.read_csv(file_path, index_col=0)
        else:
            raise NotImplementedError
