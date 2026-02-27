"""
Module: evaluate.py
Description:
    This module contains the code for evaluating a trained machine learning model
    on a test dataset and calculating performance metrics.
"""

import pandas as pd
from sklearn.metrics import accuracy_score


def evaluate_model(y_test: pd.Series, y_pred: pd.Series) -> None:
    """
    Function to evaluate a trained machine learning model on a test dataset.

    Parameters
    ----------
    y_test : pd.Series
        The true target values for the test dataset.
    y_pred : pd.Series
        The predicted target values from the model.

    Returns
    -------
    None
    """

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Точность модели: {accuracy:.2f}")
