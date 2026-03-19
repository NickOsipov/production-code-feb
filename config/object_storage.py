"""
Module: object_storage.py
Description: Client for object storage services, such as Amazon S3.
"""

from boto3.session import Session

from config.variables import S3_ACCESS_KEY, S3_SECRET_KEY, S3_ENDPOINT_URL

session = Session()

S3_CLIENT = session.client(
    service_name='s3',
    endpoint_url=S3_ENDPOINT_URL,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY
)
