"""Creates missing image formats in a Google Cloud CDN."""
import requests


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
        if image_request.headers['Content-Type'] in ('application/octet-stream', 'image/jpeg'):
            return image_request.content
        return None
