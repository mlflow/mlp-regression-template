from pandas import DataFrame
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer


def calculate_features(df: DataFrame):
    df.drop(columns=["tpep_pickup_datetime", "tpep_dropoff_datetime"], inplace=True)
    return df


def transformer_fn():
    return Pipeline(
        steps=[
            (
                "calculate_time_and_duration_features",
                FunctionTransformer(calculate_features, feature_names_out="one-to-one"),
            ),
        ]
    )
