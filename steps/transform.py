from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer, make_column_selector


def transform_fn():
    transformer = make_column_transformer(
        (
            OneHotEncoder(handle_unknown="ignore"),
            make_column_selector(dtype_include="object"),
        ),
        (
            SimpleImputer(strategy="most_frequent"),
            make_column_selector(dtype_include="number"),
        ),
        remainder="drop",
    )

    return transformer
