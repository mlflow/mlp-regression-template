from setuptools import setup, find_packages

setup(
    name="mlflow-pipelines-regression-template",
    version="1.0",
    description="An example use of MLflow pipeline based on a regression model.",
    author="Databricks",
    url="https://mlflow.org/",
    packages=find_packages(),
    install_requires=["mlflow", "scikit-learn", "pandas"],
    license="Apache License 2.0",
    python_requires=">=3.7",
)
