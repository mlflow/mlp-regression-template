def estimator_fn():
    """Returns an UNFITTED estimator that contains fit() and predict() method.
    Their input and output signatures should be compatible with sklearn estimators.
    """
    from sklearn.linear_model import SGDRegressor

    return SGDRegressor()
