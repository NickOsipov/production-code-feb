"""
Module: app.py
"""

from flask import Flask, jsonify, request
from loguru import logger
import pandas as pd

from config.variables import MODEL_PATH, IRIS_CLASSES, FEATURE_NAMES
from config.database import ENGINE
from src.inference import load_model, predict


app = Flask(__name__)

logger.info(f"Loading model from {MODEL_PATH}...")
MODEL = load_model(MODEL_PATH)
logger.info("Model loaded successfully.")


@app.route("/")
def healthcheck():
    """
    Healthcheck endpoint.
    """
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def prediction():
    """
    Prediction endpoint.
    Expects a JSON payload with the features for prediction.
    """
    logger.info("Receiving prediction request.")

    try:
        data = request.get_json()
        logger.debug(f"Request data: {data}")
        df = pd.DataFrame(data, index=[0])
        logger.info("DataFrame prepared for prediction.")
        pred = predict(MODEL, df[FEATURE_NAMES])
        logger.info(f"Prediction result: {pred}")
        predicted_class = IRIS_CLASSES[pred[0]]
        logger.info(f"Predicted class: {predicted_class}")

        q = f"""
        INSERT INTO predictions (
            sepal_length, 
            sepal_width, 
            petal_length, 
            petal_width, 
            predicted_class
        )
        VALUES (
            {df['sepal_length'].iloc[0]}, 
            {df['sepal_width'].iloc[0]}, 
            {df['petal_length'].iloc[0]}, 
            {df['petal_width'].iloc[0]}, 
            '{predicted_class}'
        )
        """

        logger.info("Prediction Store process started.")
        with ENGINE.connect() as conn:
            conn.execute(q)
            logger.info("Prediction stored in the database successfully.")

        logger.info("Sending prediction response!")
        return jsonify({"predicted_class": predicted_class})
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 555
