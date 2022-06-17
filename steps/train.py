def estimator_fn():
    """
    Returns an *unfit* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    from sklearn.linear_model import SGDRegressor

    return SGDRegressor()
