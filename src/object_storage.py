"""
Module: object_storage.py
Description: This module provides functionality for interacting with 
    object storage services, such as Amazon S3.
"""

from boto3.session import Session

from config.object_storage import S3_CLIENT
from config.variables import S3_BUCKET_NAME


def upload_model_to_s3(
    model_path: str, 
    object_name: str,
    client: Session = S3_CLIENT,
    bucket_name: str = S3_BUCKET_NAME    
) -> None:
    """
    Uploads a model file to the specified S3 bucket.

    Parameters
    ----------
    model_path : str
        The local file path of the model to be uploaded.

    object_name : str
        The name of the object in the S3 bucket (including any desired path).
    """
    try:
        client.upload_file(model_path, bucket_name, object_name)
        print(f"Model uploaded successfully to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading model to S3: {e}")
