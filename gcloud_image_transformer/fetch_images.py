"""Optimize images in a Google Cloud storage bucket CDN."""


def fetch_standard_images(bucket, bucket_image_folder_prefixes):
    """List all files in GCP bucket."""
    images = []
    for prefix in bucket_image_folder_prefixes:
        files = bucket.list_blobs(prefix=prefix)
        file_list = [file for file in files if '@2x' not in file.name]
        images.extend(file_list)
    return images


def fetch_retina_images(bucket, bucket_image_folder_prefixes):
    """List all files in GCP bucket."""
    images = []
    for prefix in bucket_image_folder_prefixes:
        files = bucket.list_blobs(prefix=prefix)
        file_list = [file for file in files if '@2x' in file.name and 'webp' not in file.name]
        images.extend(file_list)
    return images
