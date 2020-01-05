"""Endpoint for optimizing images."""
from flask import Flask, jsonify, make_response
from google.cloud import storage
from config import bucket_name, bucket_URL
from .fetch_images import fetch_standard_images, fetch_retina_images
from .transformer import ImageTransformer


def main():
    image_transformer = initialize_remote_image_transformer()
    new_standard_images, new_retina_images, new_webp_images = transform_images(image_transformer)
    response = {
        'retina': new_retina_images,
        'webp': new_webp_images,
        'standard': new_standard_images
    }
    return response


def initialize_remote_image_transformer():
    """Create transformer object."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    retina_images = fetch_retina_images(bucket)
    standard_images = fetch_standard_images(bucket)
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
