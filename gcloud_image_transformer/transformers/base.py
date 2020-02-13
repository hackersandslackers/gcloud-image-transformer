"""Creates missing image formats in a Google Cloud CDN."""
import sys
import requests
from loguru import logger

logger.add(sys.stdout, format="{time} {message}", level="INFO")


class BaseImageTransformer:

    def __init__(self, bucket, bucket_name, bucket_url, retina_images, standard_images):
        self.bucket = bucket
        self.bucket_name = bucket_name
        self.bucket_url = bucket_url
        self.retina_images = retina_images
        self.standard_images = standard_images

    def fetch_image_via_http(self, url):
        """Determine if image exists via HTTP request."""
        image_request = requests.get(self.bucket_url + url)
        logger.info(f'Checking {self.bucket_url + url}...')
        if image_request.headers['Content-Type'] != 'text/html; charset=UTF-8':
            return image_request.content
        return None

