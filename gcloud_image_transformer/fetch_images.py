"""Optimize images in a Google Cloud storage bucket CDN."""
import sys
from loguru import logger


logger.add(sys.stdout, format="{time} {message}", level="INFO")


def fetch(bucket, bucket_image_folder_prefixes):
    """Fetch all images from GCP bucket."""
    retina_images = fetch_retina_images(bucket, bucket_image_folder_prefixes)
    standard_images = fetch_standard_images(bucket, bucket_image_folder_prefixes)
    logger.info(f'Checking {len(retina_images)} retina, {len(standard_images)} standard images in {bucket_image_folder_prefixes}')
    return retina_images, standard_images


def fetch_standard_images(bucket, bucket_image_folder_prefixes):
    """List all standard-res images in bucket."""
    images = []
    for prefix in bucket_image_folder_prefixes:
        files = bucket.list_blobs(prefix=prefix)
        file_list = [file for file in files if '@2x' not in file.name]
        images.extend(file_list)
    return images


def fetch_retina_images(bucket, bucket_image_folder_prefixes):
    """List all retina images in bucket."""
    images = []
    for prefix in bucket_image_folder_prefixes:
        files = bucket.list_blobs(prefix=prefix)
        file_list = [file for file in files if '@2x' in file.name and 'webp' not in file.name]
        images.extend(file_list)
    return images
