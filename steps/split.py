"""
This module defines the following routines used by the 'split' step of the regression pipeline:

- ``create_dataset_filter``: Defines customizable logic for filtering the training, validation,
  and test datasets produced by the data splitting procedure. Note that arbitrary transformations
  should go into the transform step.
"""

from pandas import DataFrame, Series


def create_dataset_filter(dataset: DataFrame) -> Series(bool):
    """
    Mark rows of the split datasets to be additionally filtered. This function will be called on
    the training, validation, and test datasets.

    :param dataset: The {train,validation,test} dataset produced by the data splitting procedure.
    :return: A Series indicating whether each row should be filtered
    """
    # FIXME::OPTIONAL: implement post-split filtering on the dataframes, such as data cleaning.

    return Series(True, index=dataset.index)
