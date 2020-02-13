import sys
from loguru import logger
from .base import BaseImageTransformer

logger.add(sys.stdout, format="{time} {message}", level="INFO")


class WebpImageTransformer(BaseImageTransformer):

    def __init__(self, bucket, bucket_name, bucket_url, retina_images):
        super().__init__(self, bucket, bucket_name, bucket_url, retina_images)
        self.webp_images_generated = []
        self.bucket = bucket
        self.bucket_name = bucket_name
        self.bucket_url = bucket_url
        self.standard_images = retina_images
        self.num_images_checked = 0
        self.num_images_created = 0

    def transform(self):
        """Find images missing a webp counterpart."""
        for image_blob in self.retina_images:
            new_image_name = image_blob.split('.')[0] + '.webp'
            image_file = self.fetch_image_via_http(new_image_name)
            if image_file is not None:
                new_blob = self.bucket.copy_blob(image_blob, self.bucket, new_image_name)
                self.webp_images_generated.append(new_blob.name)
                logger.info(f'{self.num_images_created} retina images generated of {self.num_images_checked} checked.')
        return self.webp_images_generated

