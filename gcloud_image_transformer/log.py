import sys
from functools import wraps
from loguru import logger


logger.add(sys.stdout, format="{time} {message}", level="INFO")


def log_progress(func):
    wraps(func)

    def wrapper(self, *args, **kwargs):
        logger.info(f'{self.num_images_created} images generated of {len(self.image_blobs)} total.')
