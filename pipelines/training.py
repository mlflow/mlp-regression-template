from mlflow.pipelines.regression.v1 import TrainingPipeline

from steps.ingest import MyIngestStep
from steps.split import MySplitStep
from steps.train import MyTrainStep
from steps.transform import MyTransformStep
from mlflow.pipelines.steps import EvaluateStep, RegisterStep


class MyTrainingPipeline(TrainingPipeline):
    # All step names are required -- their implementations must be provided.
    _STEPS = {
        "ingest": MyIngestStep,
        "split": MySplitStep,
        "transform": MyTransformStep,
        "train": MyTrainStep,
        "evaluate": EvaluateStep,
        "register": RegisterStep,
    }

    def __init__(self, profile, config_file="train.yaml", steps=_STEPS):
        super().__init__(
            profile=profile,
            config_file=config_file,
            steps=steps,
            requirements="requirements/training-requirements.txt",
        )


if __name__ == "__main__":
    MyTrainingPipeline().run()
