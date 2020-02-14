"""Endpoint for optimizing images."""
from google.cloud import storage
from config import bucket_name, bucket_URL, bucket_image_folder_prefixes
from .fetch_images import fetch_standard_images, fetch_retina_images
from gcloud_image_transformer.transformers import (
    RetinaImageTransformer,
    StandardImageTransformer,
    WebpImageTransformer
)


def main():
    """Entry point."""
    new_retina_images, new_standard_images, new_webp_images = initialize_transforms()
    response = {
        'retina': len(new_retina_images),
        'webp': len(new_webp_images),
        'standard': len(new_standard_images)
    }
    print(response)


def initialize_transforms():
    """Create transformer objects."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    retina_images, standard_images = fetch_remote_images(bucket)
    retina_transformer, standard_transformer, webp_transformer = create_transformers(bucket, bucket_name,
                                                                                     bucket_URL,
                                                                                     retina_images,
                                                                                     standard_images)
    new_retina_images, new_standard_images, new_webp_images = transform_images(retina_transformer,
                                                                               standard_transformer,
                                                                               webp_transformer)
    return new_retina_images, new_standard_images, new_webp_images


def fetch_remote_images(bucket):
    """Fetch all images from GCP bucket."""
    retina_images = fetch_retina_images(bucket, bucket_image_folder_prefixes)
    standard_images = fetch_standard_images(bucket, bucket_image_folder_prefixes)
    return retina_images, standard_images


def create_transformers(bucket, bucket_name, bucket_URL, retina_images, standard_images):
    """Connect to GCP bucket and apply image transforms."""
    retina_transformer = RetinaImageTransformer(bucket,
                                                bucket_name,
                                                bucket_URL,
                                                standard_images)
    standard_transformer = StandardImageTransformer(bucket,
                                                    bucket_name,
                                                    bucket_URL,
                                                    retina_images)
    webp_transformer = WebpImageTransformer(bucket,
                                            bucket_name,
                                            bucket_URL,
                                            retina_images)
    return retina_transformer, standard_transformer, webp_transformer


def transform_images(retina_transformer, standard_transformer, webp_transformer):
    """Perform image transforms."""
    retina_transformer.transform()
    standard_transformer.transform()
    webp_transformer.transform()
    return retina_transformer.images_generated, standard_transformer.images_generated, webp_transformer.images_generated
