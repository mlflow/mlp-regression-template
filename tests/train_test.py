from examples.pipelines.sklearn_regression.steps.train import train_fn
from sklearn.utils.estimator_checks import check_estimator


def test_user_train_returns_object_with_correct_spec():
    regressor = train_fn()
    assert callable(getattr(regressor, "fit", None))
    assert callable(getattr(regressor, "predict", None))


def test_user_train_passes_check_estimator():
    regressor = train_fn()
    check_estimator(regressor)


def test_user_train_on_fake_data():
    from sklearn import datasets
    iris = datasets.load_iris()
    parameters = {"kernel": ("linear", "rbf"), "C": [1, 10]}
    svc = svm.SVC()
    clf = GridSearchCV(svc, parameters)

    clf.fit(iris.data, iris.target)
    run_id = mlflow.last_active_run().info.run_id

    # show data logged in the parent run
    print("========== parent run ==========")
    for key, data in fetch_logged_data(run_id).items():
        print("\n---------- logged {} ----------".format(key))
        pprint(data)

    # show data logged in the child runs
    filter_child_runs = "tags.mlflow.parentRunId = '{}'".format(run_id)
    runs = mlflow.search_runs(filter_string=filter_child_runs)
    param_cols = ["params.{}".format(p) for p in parameters.keys()]
    metric_cols = ["metrics.mean_test_score"]

    print("\n========== child runs ==========\n")
    pd.set_option("display.max_columns", None)  # prevent truncating columns
    print(runs[["run_id", *param_cols, *metric_cols]])
