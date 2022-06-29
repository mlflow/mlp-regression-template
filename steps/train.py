"""
This module defines the following routines used by the 'train' step of the regression pipeline:

- ``estimator_fn``: Defines the customizable estimator type and parameters that are used
  during training to produce a model pipeline.
"""

def grid_search_estimator():
  from sklearn.tree import DecisionTreeRegressor
  from sklearn.model_selection import GridSearchCV
  
  param_grid = {
    "max_depth": [3,5,10,None],
    "min_samples_split": [2,5,7,10],
    "min_samples_leaf": [1,2,5]
  }
  return GridSearchCV(DecisionTreeRegressor(random_state=42), param_grid, scoring="roc_auc")


def tree_estimator():
  from sklearn.tree import DecisionTreeRegressor
  
  return DecisionTreeRegressor()


def linear_estimator():
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    from sklearn.linear_model import SGDRegressor
    

    return SGDRegressor(random_state=42)
