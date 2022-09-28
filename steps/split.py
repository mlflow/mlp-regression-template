"""
This module defines the following routines used by the 'split' step of the regression pipeline:

- ``mark_to_be_filtered``: Defines customizable logic for filtering the training, validation,
  and test datasets produced by the data splitting procedure. Note that arbitrary transformations
  should go into the transform step.
"""

from pandas import DataFrame, Series


def mark_to_be_filtered(dataset: DataFrame) -> Series(bool):
    """
    Mark rows of the split datasets to be additionally filtered. This function will be called on
    the training, validation, and test datasets.

    :param dataset: The {train,validation,test} dataset produced by the data splitting procedure.
    :return: A Series indicating whether each row should be filtered
    """
    return (
        (dataset["fare_amount"] > 0)
        & (dataset["trip_distance"] < 400)
        & (dataset["trip_distance"] > 0)
        & (dataset["fare_amount"] < 1000)
    ) | (~dataset.isna().any(axis=1))
