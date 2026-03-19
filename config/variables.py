"""
Module: variables.py
Description:
    This module contains the configuration variables for the machine learning pipeline.
"""

import os

MODEL_NAME = "random_forest.joblib"
MODEL_PATH = os.path.join("models", MODEL_NAME)

IRIS_CLASSES = ["setosa", "versicolor", "virginica"]
FEATURE_NAMES = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL")
