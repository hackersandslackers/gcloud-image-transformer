"""Setup file."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Google Cloud Storage Image Transformer',
    version='0.0.1',
    description='Connects to a GCP-hosted image CDN and applies image transformations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hackersandslackers/gcloud_image_transformer',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Google Cloud GCP Image Optimize Pillow Webp Compression Retina',
    packages=find_packages(),
    install_requires=['Flask',
                      'Pillow',
                      'google-cloud-storage',
                      'Requests',
                      'webp-converter',
                      'python-resize-image',
                      'Loguru'],
    entry_points={
        'console_scripts': [
            'run = main:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hackersandslackers/gcloud_image_transformer/issues',
        'Source': 'https://github.com/hackersandslackers/gcloud_image_transformer/',
    },
)
