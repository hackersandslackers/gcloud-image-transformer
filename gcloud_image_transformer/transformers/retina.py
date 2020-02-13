import sys
from loguru import logger
import requests
from io import BytesIO
from PIL import Image
from .base import BaseImageTransformer


logger.add(sys.stdout, format="{time} {message}", level="INFO")


class RetinaImageTransformer(BaseImageTransformer):

    def __init__(self, bucket, bucket_name, bucket_url, standard_images):
        super().__init__(self, bucket, bucket_name, bucket_url, standard_images)
        self.retina_images_generated = []
        self.bucket = bucket
        self.bucket_name = bucket_name
        self.bucket_url = bucket_url
        self.standard_images = standard_images
        self.num_images_checked = 0
        self.num_images_created = 0

    def transform(self):
        """Find images missing a retina-quality counterpart."""
        for image_blob in self.standard_images:
            self.num_images_checked += 1
            dot_position = image_blob.name.rfind('.')
            new_image_name = image_blob.name[:dot_position] + '@2x' + image_blob.name[dot_position:]
            existing_image_file = self.fetch_image_via_http(new_image_name)
            if existing_image_file is None:
                self.__create_retina_image(image_blob, new_image_name)
        return self.retina_images_generated

    def __create_retina_image(self, image_blob, new_image_name):
        """Create retina versions of standard-res images."""
        original_image = self.fetch_image_via_http(image_blob.name)
        im = Image.open(BytesIO(original_image.content))
        width, height = im.size
        if width > 1000:
            new_blob = self.bucket.copy_blob(image_blob, self.bucket, new_image_name)
            self.retina_images_generated.append(new_blob.name)
            logger.info(f'{self.num_images_created} retina images generated of {self.num_images_checked} checked.')

