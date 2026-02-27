"""
Module: train.py
Description:
    This module contains the code for training
    a machine learning model on the Iris dataset.
"""

import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def train_model(
    X_train: pd.DataFrame, y_train: pd.Series, params: dict
) -> RandomForestClassifier:
    """
    Function to train a Random Forest model on the given training data.

    Parameters
    ----------
    X_train : pandas.DataFrame
        The training features.
    y_train : pandas.Series
        The training target variable.
    params : dict
        A dictionary of hyperparameters for the Random Forest model.

    Returns
    -------
    RandomForestClassifier
        The trained Random Forest model.
    """
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    return model


def save_model(model: RandomForestClassifier, model_path: str) -> None:
    """
    Function to save the trained model to a file.

    Parameters
    ----------
    model : RandomForestClassifier
        The trained Random Forest model to be saved.
    model_path : str
        The file path where the model will be saved.
    """
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)


def training(
    X_train: pd.DataFrame, y_train: pd.Series, params: dict, model_path: str
) -> None:
    """
    Function to execute the training pipeline: train the model and save it.

    Parameters
    ----------
    X_train : pandas.DataFrame
        The training features.
    y_train : pandas.Series
        The training target variable.
    params : dict
        A dictionary of hyperparameters for the Random Forest model.
    model_path : str
        The file path where the trained model will be saved.
    """
    model = train_model(X_train, y_train, params)
    save_model(model, model_path)
