from google.cloud import storage
from config import bucket_name, bucket_URL, bucket_image_folder_prefixes
from .fetch import fetch
from gcloud_image_transformer.images import ImageTransformer


def initialize_transforms():
    """Transform image objects."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    retina_images, standard_images = fetch(bucket, bucket_image_folder_prefixes)
    transformer = ImageTransformer(bucket,
                                   bucket_name,
                                   bucket_URL,
                                   retina_images,
                                   standard_images)
    new_retina_images = transformer.retina_transform()
    new_standard_images = transformer.standard_transform()
    # new_webp_images = transformer.webp_transform()
    return new_retina_images, new_standard_images
