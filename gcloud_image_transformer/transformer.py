"""Creates missing image formats in a Google Cloud CDN."""
import sys
import requests
from io import BytesIO
from PIL import Image
from loguru import logger

logger.add('logs/info_{time}.log', format="{time} {message}", level="INFO")


class ImageTransformer:

    def __init__(self, bucket, bucket_name, bucket_url, retina_images, standard_images):
        self.bucket = bucket
        self.bucket_name = bucket_name
        self.bucket_url = bucket_url
        self.retina_images = retina_images
        self.standard_images = standard_images

    def create_retina_image(self):
        """Create retina versions of standard def images."""
        affected_images = []
        for image in self.standard_images:
            dot_position = image.name.rfind('.')
            retina_name = image.name[:dot_position] + '@2x' + image.name[dot_position:]
            existing_retina_file = requests.get(self.bucket_url + retina_name)
            logger.info(f"Checking if {image.name} needs retina.")
            if existing_retina_file.status_code != 200:
                response = requests.get(self.bucket_url + image.name)
                im = Image.open(BytesIO(response.content))
                width, height = im.size
                if width > 1000:
                    new_blob = self.bucket.copy_blob(image, self.bucket, retina_name)
                    affected_images.append(new_blob.name)
        return affected_images

    def create_standard_def_image(self):
        """Create non-retina images where retina images exist but standard does not."""
        affected_images = []
        for image in self.retina_images:
            if '@2x' in image.name:
                standard_def_name = image.name.replace('@2x', '')
                existing_file = requests.get(self.bucket_url + standard_def_name)
                logger.info(f"Checking if {image.name} needs standard image.")
                if existing_file.status_code != 200:
                    new_blob = self.bucket.copy_blob(image, self.bucket, standard_def_name)
                    affected_images.append(new_blob.name)
        return affected_images

    def create_webp_image(self):
        """Create webp versions of images."""
        affected_images = []
        for image in self.retina_images:
            dot_position = image.name.rfind('.')
            compressed_name = image.name[:dot_position] + '.webp'
            existing_compressed_file = requests.get(self.bucket_url + compressed_name)
            logger.info(f"Checking if {image.name} needs webp.")
            if existing_compressed_file.status_code != 200:
                new_blob = self.bucket.copy_blob(image, self.bucket, compressed_name)
                affected_images.append(new_blob.name)
        return affected_images
