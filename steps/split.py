from pandas import DataFrame


def process_splits(
    train_df: DataFrame, validation_df: DataFrame, test_df: DataFrame
) -> (DataFrame, DataFrame, DataFrame):
    """
    Perform additional processing on the split datasets.
    """

    def process(df: DataFrame):
        # Drop invalid data points
        cleaned = df.dropna()
        # Filter out invalid fare amounts and trip distance
        cleaned = cleaned[
            (cleaned["fare_amount"] > 0)
            & (cleaned["trip_distance"] < 400)
            & (cleaned["trip_distance"] > 0)
            & (cleaned["fare_amount"] < 1000)
        ]

        cleaned["pickup_dow"] = cleaned["tpep_pickup_datetime"].dt.dayofweek
        cleaned["pickup_hour"] = cleaned["tpep_pickup_datetime"].dt.hour
        trip_duration = (
            cleaned["tpep_dropoff_datetime"] - cleaned["tpep_pickup_datetime"]
        )
        cleaned["trip_duration"] = trip_duration.map(lambda x: x.total_seconds() / 60)

        return cleaned

    return process(train_df), process(validation_df), process(test_df)
