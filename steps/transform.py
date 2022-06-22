from pandas import DataFrame
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer


def transformer_fn():
    """Returns an UNFITTED transformer with fit() and transform() methods.
    Their input and output signatures should be compatible with sklearn transformers.
    """
    return Pipeline(
        steps=[
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
                            ["trip_distance", "trip_duration"],
                        ),
                    ]
                ),
            ),
        ]
    )
