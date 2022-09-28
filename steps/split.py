"""
This module defines the following routines used by the 'split' step of the regression pipeline:

- ``process_splits``: Defines customizable logic for processing & cleaning the training, validation,
  and test datasets produced by the data splitting procedure. Note that arbitrary transformations
  should go into the transform step.
"""

from typing import Tuple
from pandas import DataFrame, Series


def process_splits(
    train_df: DataFrame, validation_df: DataFrame, test_df: DataFrame
) -> (DataFrame, DataFrame, DataFrame):
    """
    Perform additional processing on the split datasets.

    :param train_df: The training dataset produced by the data splitting procedure.
    :param validation_df: The validation dataset produced by the data splitting procedure.
    :param test_df: The test dataset produced by the data splitting procedure.
    :return: A tuple containing, in order: the processed training dataset, the processed
             validation dataset, and the processed test dataset.
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

        return cleaned

    # return process(train_df), process(validation_df), process(test_df)
    train_df['to_filter'] = mark_to_be_filtered(train_df)
    validation_df['to_filter'] = mark_to_be_filtered(validation_df)
    test_df['to_filter'] = mark_to_be_filtered(test_df)
    return (
        train_df[train_df.to_filter == True],
        validation_df[validation_df.to_filter == True],
        test_df[test_df.to_filter == True]
    )


def mark_to_be_filtered(dataset: DataFrame) -> Series(bool):
    """
    Mark rows of the split datasets to be additionally filtered. This function will be called on
    the training, validation, and test datasets.

    :param dataset: The {train,validation,test} dataset produced by the data splitting procedure.
    :return: A Series indicating whether each row should be filtered
    """
    return (dataset["fare_amount"] > 0) & (dataset["trip_distance"] < 400) & (
        dataset["trip_distance"] > 0
    ) & (dataset["fare_amount"] < 1000) or dataset.isna().any(axis=1)
