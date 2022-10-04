"""
This module defines the following routines used by the 'train' step of the regression pipeline:

- ``estimator_fn``: Defines the customizable estimator type and parameters that are used
  during training to produce a model pipeline.
"""


def estimator_fn():
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    # FIXME::OPTIONAL: return a scikit-learn-compatible regression estimator with fine-tuned hyperparameters.
    from sklearn.linear_model import SGDRegressor

    return SGDRegressor(random_state=42)
