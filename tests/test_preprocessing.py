"""
Module: test_preprocessing.py
Description:
    This module contains unit tests for the
    preprocessing functions defined in preprocessing.py.
"""

import pandas as pd

from src.preprocessing import load_data


def test_load_data():
    df = load_data()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (150, 5)
    assert set(df.columns) == {
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "target",
    }
