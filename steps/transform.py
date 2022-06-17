from pandas import DataFrame
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer


def compute_features(df: DataFrame):
    df.loc[:, "pickup_dow"] = df["tpep_pickup_datetime"].dt.dayofweek
    df.loc[:, "pickup_hour"] = df["tpep_pickup_datetime"].dt.hour
    trip_duration = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
    df.loc[:, "trip_duration_min"] = trip_duration.map(lambda x: x.total_seconds() / 60.0)
    return df


def transformer_fn():
    """
    Returns an *unfit* transformer that defines ``fit()`` and ``transform()`` methods.
    The transformer's input and output signatures should be compatible with scikit-learn
    transformers.
    """
    return Pipeline(
        steps=[
            ("extra_features", FunctionTransformer(compute_features, validate=False)),
            (
                "encoder",
                ColumnTransformer(
                    transformers=[
                        (
                            "hour_encoder",
                            OneHotEncoder(categories="auto", sparse=False),
                            ["pickup_hour"],
                        ),
                        (
                            "day_encoder",
                            OneHotEncoder(categories="auto", sparse=False),
                            ["pickup_dow"],
                        ),
                        (
                            "std_scaler",
                            StandardScaler(),
                            ["trip_distance", "trip_duration_min"],
                        ),
                    ]
                ),
            ),
        ]
    )
