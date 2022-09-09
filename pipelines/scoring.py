from mlflow.pipelines.regression.v1 import ScoringPipeline

from steps.ingest import MyIngestStep
from mlflow.pipelines.steps import PredictStep


class MyScoringPipeline(ScoringPipeline):
    # All step names are required -- their implementations must be provided.
    _STEPS = {
        "ingest": MyIngestStep,
        "predict": PredictStep,
    }

    def __init__(self, profile, config_file="scoring.yaml", steps=_STEPS):
        super().__init__(
            profile=profile,
            config_file=config_file,
            steps=steps,
            requirements="requirements/scoring-requirements.txt",
        )


if __name__ == "__main__":
    MyScoringPipeline().run()
