"""Endpoint for optimizing images."""
from google.cloud import storage
from config import bucket_name, bucket_URL, bucket_image_folder_prefixes
from .fetch_images import fetch_standard_images, fetch_retina_images
from .transformer import ImageTransformer


def main():
    """Entry point."""
    image_transformer = initialize_remote_image_transformer()
    new_standard_images, new_retina_images, new_webp_images = transform_images(image_transformer)
    response = {
        'retina': len(new_retina_images),
        'webp': len(new_webp_images),
        'standard': len(new_standard_images)
    }
    print(response)


def initialize_remote_image_transformer():
    """Create transformer object."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    retina_images = fetch_retina_images(bucket, bucket_image_folder_prefixes)
    standard_images = fetch_standard_images(bucket, bucket_image_folder_prefixes)
    image_transformer = ImageTransformer(bucket,
                                         bucket_name,
                                         bucket_URL,
                                         retina_images,
                                         standard_images)
    return image_transformer


def transform_images(image_transformer):
    """Connect to GCP bucket and apply image transforms."""
    new_standard_images = image_transformer.create_standard_def_image()
    new_retina_images = image_transformer.create_retina_image()
    new_webp_images = image_transformer.create_webp_image()
    return new_standard_images, new_retina_images, new_webp_images
