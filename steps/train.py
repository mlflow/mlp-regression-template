def train_fn():
    # from sklearn.linear_model import ElasticNet
    # return ElasticNet()

    from sklearn.linear_model import SGDRegressor

    return SGDRegressor()
