"""
Module: inference.py
Description:
    This module contains the code for loading a trained machine learning model
    and making predictions on new data.
"""

import joblib


def load_model(model_path: str):
    """
    Function to load a trained model from a file.

    Parameters
    ----------
    model_path : str
        The file path where the model is saved.

    Returns
    -------
    The loaded model.
    """
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        print(
            f"Model file not found at {model_path}. Please check the path and try again."
        )
        raise


def predict(model, array):
    """
    Function to make predictions using the loaded model.

    Parameters
    ----------
    model : The loaded machine learning model.
    array : array-like
        The input features for which to make predictions.

    Returns
    -------
    array-like
        The predicted target values.
    """
    return model.predict(array)
