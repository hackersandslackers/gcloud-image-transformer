"""Optimize images in a Google Cloud storage bucket CDN."""
from datetime import datetime


def fetch_standard_images(bucket, prefix):
    """List all files in GCP bucket."""
    if prefix is None:
        prefix = datetime.now().strftime('%Y')
    files = bucket.list_blobs(prefix=prefix)
    file_list = [file for file in files if '@2x' not in file.name]
    return file_list


def fetch_retina_images(bucket, prefix):
    """List all files in GCP bucket."""
    if prefix is None:
        prefix = datetime.now().strftime('%Y')
    files = bucket.list_blobs(prefix=prefix)
    file_list = [file for file in files if '@2x' in file.name and 'webp' not in file.nam]
    return file_list
