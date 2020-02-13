"""Connect to remote GCP bucket containing images."""
from config import bucket_name
from google.cloud import storage


def connect_to_bucket():
    """Return a GCP bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    return bucket
