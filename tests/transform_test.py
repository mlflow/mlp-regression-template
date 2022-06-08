from steps.transform import transform_fn


def test_tranform_fn_returns_object_with_correct_spec():
    transformer = transform_fn()
    assert callable(getattr(transformer, "fit", None))
    assert callable(getattr(transformer, "transform", None))
