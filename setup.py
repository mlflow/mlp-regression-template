from setuptools import setup, find_packages

setup(
    name="mlflow-pipeline-examples",
    version="1.0",
    description="Example repo to kickstart integration with mlflow pipelines.",
    author="Databricks",
    url="https://mlflow.org/",
    packages=find_packages(include=["sklearn_regression", "sklearn_regression.*"]),
    license="Apache License 2.0",
    python_requires=">=3.7",
)
