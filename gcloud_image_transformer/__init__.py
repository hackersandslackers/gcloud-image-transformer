"""Endpoint for optimizing images."""
from .transform import initialize_transforms


def main():
    """Entry point."""
    new_retina_images, new_standard_images, new_webp_images = initialize_transforms()
    response = {
        'retina': len(new_retina_images),
        'webp': len(new_webp_images),
        'standard': len(new_standard_images)
    }
    print(response)
    return response
