def load_file_as_dataframe(file_path, file_format):
    """
    Load content from the specified dataset file as a Pandas DataFrame.

    This method is used to load dataset types that are not natively  managed by MLflow Pipelines
    (datasets that are not in Parquet, Delta Table, or Spark SQL Table format). This method is
    called once for each file in the dataset, and MLflow Pipelines automatically combines the
    resulting DataFrames together.

    :param file_path: The path to the dataset file.
    :param file_format: The file format string, such as "csv".
    :return: A Pandas DataFrame representing the content of the specified file.
    """

    if file_format == "csv":
        _logger.warning(
            "Loading dataset CSV using `pandas.read_csv()` with default arguments, which may not"
            " produce the desired schema. If the schema is not correct, you can adjust it by"
            " modifying the `load_file_as_dataframe()` function in `steps/ingest.py`"
        )
        return pandas.read_csv(file_path)
    else:
        raise NotImplemented
