from gcloud_image_transformer.log import log_progress
from .base import BaseImageTransformer


class WebpImageTransformer(BaseImageTransformer):

    def __init__(self, bucket, bucket_name, bucket_url, image_blobs):
        super().__init__(self, bucket, bucket_name, bucket_url, image_blobs)
        self.images_generated = []
        self.bucket = bucket
        self.bucket_name = bucket_name
        self.bucket_url = bucket_url
        self.image_blobs = image_blobs
        self.num_images_checked = 0
        self.num_images_created = 0

    def transform(self):
        """Find images missing a webp counterpart."""
        for image_blob in self.image_blobs:
            self.num_images_checked += 1
            print(self.num_images_checked, ' of ', len(self.image_blobs))
            new_image_name = image_blob.name.split('.')[0] + '.webp'
            image_file = self.fetch_image_via_http(new_image_name)
            if image_file is not None:
                new_blob = self.bucket.copy_blob(image_blob, self.bucket, new_image_name)
                self.images_generated.append(new_blob.name)
