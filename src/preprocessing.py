"""
Module: preprocessing.py
Description: This module contains functions for loading and preprocessing the Iris dataset.
"""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def load_data() -> pd.DataFrame:
    # Загрузка данных
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Создание DataFrame
    df = pd.DataFrame(X, columns=iris.feature_names)
    df["target"] = y

    # Переименование столбцов для удобства
    df = df.rename(
        columns={
            "sepal length (cm)": "sepal_length",
            "sepal width (cm)": "sepal_width",
            "petal length (cm)": "petal_length",
            "petal width (cm)": "petal_width",
        }
    )

    return df


def split_data(
    df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42
) -> tuple:
    """
    Function to split the dataset into training and testing sets.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame containing the features and target variable.
    test_size : float, optional
        The proportion of the dataset to include in the test split (default is 0.2)
    random_state : int, optional
        Controls the randomness of the split (default is 42)

    Returns
    -------
    tuple
        A tuple containing the training and testing sets: (X_train, X_test, y_train, y_test)
    """

    # Разделение данных на признаки и целевую переменную
    X = df.drop("target", axis=1)
    y = df["target"]

    # Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    return X_train, X_test, y_train, y_test


def save_data(df: pd.DataFrame, file_path: str) -> None:
    """
    Function to save the DataFrame to a Parquet file.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to be saved.
    file_path : str
        The path where the Parquet file will be saved.
    """
    df.to_parquet(file_path, index=False)


def preprocess_data() -> tuple:
    """
    Function to load, preprocess, and save the Iris dataset.
    """
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)
    return X_train, X_test, y_train, y_test
