from pandas import DataFrame


def process_splits(
    train_df: DataFrame, validation_df: DataFrame, test_df: DataFrame
) -> (DataFrame, DataFrame, DataFrame):
    """
    Perform additional processing on the split datasets.
    """
    def process(ds: DataFrame):
        # Drop invalid data points
        cleaned = ds.dropna()
        # Filter out invalid fare amounts, trip distance, tip amounts, passenger counts
        cleaned = cleaned[(cleaned["fare_amount"] > 0) & (cleaned["trip_distance"] < 400) & (cleaned["trip_distance"] > 0) &
                      (cleaned["tip_amount"] >= 0) & (cleaned["passenger_count"] > 0) & (cleaned["fare_amount"] < 1000)]

        # Locations 264 and 265 map to unknown. Filter them out
        cleaned = cleaned[(cleaned["PULocationID"] < 264) & (cleaned["DOLocationID"] < 264)]

        cleaned["pickup_dow"] = cleaned["tpep_pickup_datetime"].dt.dayofweek
        cleaned["pickup_hour"] = cleaned["tpep_pickup_datetime"].dt.hour
        trip_duration = cleaned["tpep_dropoff_datetime"] - cleaned["tpep_pickup_datetime"]
        cleaned["trip_duration"] = trip_duration.map(lambda x: x.total_seconds() / 60)

        # Large dataset. Take first 10%
        length = ds.size
        return cleaned.head(int(length/10))
    return process(train_df), process(validation_df), process(test_df)

