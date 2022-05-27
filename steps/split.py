from pandas import DataFrame


def process_splits(
    train_df: DataFrame, validation_df: DataFrame, test_df: DataFrame
) -> (DataFrame, DataFrame, DataFrame):
    """
    Perform additional processing on the split datasets.
    """
    def process(ds):
        # Drop invalid data points
        cleaned = ds.dropna()
        # Filter out invalid fare amounts, trip distance, tip amounts, passenger counts
        cleaned = cleaned[(cleaned["fare_amount"] > 0) & (cleaned["trip_distance"] < 400) & (cleaned["trip_distance"] > 0) &
                      (cleaned["tip_amount"] >= 0) & (cleaned["passenger_count"] > 0) & (cleaned["fare_amount"] < 1000)]

        # Locations 264 and 265 map to unknown. Filter them out
        cleaned = cleaned[(cleaned["PULocationID"] < 264) & (cleaned["DOLocationID"] < 264)]

        return cleaned
    return process(train_df), process(validation_df), process(test_df)

