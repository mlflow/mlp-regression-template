from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer, make_column_selector


def transform_fn():
    #         train_X = cleaned[["pickup_dow", "pickup_hour", "trip_distance", "trip_duration"]]
    ct_pipe = ColumnTransformer(transformers=[
        ('hour_encoder', OneHotEncoder(categories='auto', sparse=False), ["pickup_hour"]),
        ('day_encoder', OneHotEncoder(categories='auto', sparse=False), ["pickup_dow"]),
        ('std_scaler', StandardScaler(), ["trip_distance", "trip_duration"])
    ])

    return transformer
