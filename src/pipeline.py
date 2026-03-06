"""
Script: pipeline.py
Description:
    This script contains the code for the machine learning pipeline, including
    data preprocessing, model training, and model evaluation.
"""

from loguru import logger

from config.variables import MODEL_PATH
from src.evaluate import evaluate_model
from src.inference import load_model, predict
from src.preprocessing import preprocess_data
from src.train import training

PARAMS = {"n_estimators": 100, "max_depth": 5, "random_state": 42}


def main():
    """
    Main function to execute the machine learning pipeline.
    """

    logger.info("Init the machine learning pipeline...")

    # Load and preprocess the data
    logger.info("Preprocessing the data...")
    X_train, X_test, y_train, y_test = preprocess_data()

    # Train the model and save it
    logger.info("Training the model...")
    training(X_train, y_train, PARAMS, MODEL_PATH)

    # Load the trained model
    logger.info("Loading the trained model...")
    model = load_model(MODEL_PATH)
    logger.debug(f"Model loaded successfully. Model details: {model}")

    # Make predictions on the test set
    logger.info("Making predictions on the test set...")
    y_pred = predict(model, X_test)
    logger.debug(f"Predictions made successfully. Sample predictions: {y_pred[:5]}")

    # Evaluate the model's performance
    logger.info("Evaluating the model's performance...")
    evaluate_model(y_test, y_pred)

    # Log the completion of the pipeline
    logger.info("Machine learning pipeline completed successfully.")


if __name__ == "__main__":
    main()
