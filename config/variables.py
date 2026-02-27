"""
Module: variables.py
Description:
    This module contains the configuration variables for the machine learning pipeline.
"""

import os

MODEL_NAME = "random_forest.joblib"
MODEL_PATH = os.path.join("models", MODEL_NAME)
