"""Endpoint for optimizing images."""
from .transform import initialize_transforms


def main():
    """Script entry point."""
    new_retina_images, new_standard_images = initialize_transforms()
    response = {
        'retina': len(new_retina_images),
        'standard': len(new_standard_images)
    }
    print(response)
    return response
