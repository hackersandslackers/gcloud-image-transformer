"""Google Cloud Storage Configuration."""
from os import environ


# Google Cloud Storage
bucket_URL = environ.get('GCP_BUCKET_URL')
bucket_name = environ.get('GCP_BUCKET_NAME')
bucket_folder = environ.get('GCP_BUCKET_FOLDER_NAME')
