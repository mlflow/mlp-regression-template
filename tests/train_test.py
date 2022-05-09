from examples.pipelines.sklearn_regression.steps.train import train_fn


def test_user_function_returns_object_with_correct_spec():
    regressor = train_fn()
    assert(callable(getattr(regressor, 'fit', None)))
    assert(callable(getattr(regressor, 'predict', None)))