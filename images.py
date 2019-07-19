"""Optimize images in a Google Cloud storage bucket CDN."""
from PIL import Image
from google.cloud import storage
import requests
from io import BytesIO
from config import bucketName, bucketURL

storage_client = storage.Client()
bucket = storage_client.get_bucket(bucketName)


def list_files():
    """List all files in GCP bucket."""
    files = bucket.list_blobs(prefix='lynx/lynx26')
    fileList = [file for file in files if '.' in file.name if '@2x' not in file.name]
    return fileList


def create_retina_image(images):
    """Create retina versions of images."""
    affectedImages = []
    for image in images:
        dotPosition = image.name.rfind('.')
        retinaName = image.name[:dotPosition] + '@2x' + image.name[dotPosition:]
        existingRetinaFile = requests.get(bucketURL + retinaName)
        print(existingRetinaFile.status_code, ' = ', bucketURL + retinaName)
        if existingRetinaFile.status_code != 200:
            response = requests.get(bucketURL + image.name)
            im = Image.open(BytesIO(response.content))
            width, height = im.size
            if width > 1000:
                new_blob = bucket.copy_blob(image, bucket, retinaName)
                affectedImages.append(f'Created retina image for {new_blob.name}')
    return affectedImages


def create_webp_image(images):
    """Create webp versions of images."""
    affectedImages = []
    for image in images:
        dotPosition = image.name.rfind('.')
        compressedName = image.name[:dotPosition] + '.webp'
        existingCompressedFile = requests.get(bucketURL + compressedName)
        print(existingCompressedFile.status_code, ' = ', bucketURL + compressedName)
        if existingCompressedFile.status_code != 200:
            new_blob = bucket.copy_blob(image, bucket, compressedName)
            affectedImages.append(f'Created webp image for {new_blob.name}')
    return affectedImages


def optimize_images():
    image_list = list_files()
    response = {
        'retina': create_retina_image(image_list),
        # 'webp': create_webp_image(image_list)
    }
    return response
