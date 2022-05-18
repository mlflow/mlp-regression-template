from sklearn.metrics import mean_squared_error


def weighted_mean_squared_error(eval_df, builtin_metrics):
    return {
        "weighted_mean_squared_error": mean_squared_error(
            eval_df["prediction"], eval_df["target"], sample_weight=1 / eval_df["prediction"].values
        )
    }
