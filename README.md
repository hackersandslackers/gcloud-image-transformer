# Google Cloud Storage Image Transformer

![Python](https://img.shields.io/badge/Python-v3.7-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Pillow](https://img.shields.io/badge/Pillow-v6.0.0-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Requests](https://img.shields.io/badge/Requests-v2.22.0-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Google Cloud Functions](https://img.shields.io/badge/Google--Cloud--Functions-v93-blue.svg?longCache=true&logo=google&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/gcloud_image_transformer.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a&logo=Github)](https://github.com/hackersandslackers/gcloud_image_transformer/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/gcloud_image_transformer.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a&logo=Github)](https://github.com/hackersandslackers/gcloud_image_transformer/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/gcloud_image_transformer.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/gcloud_image_transformer/network)

Turn any Google Storage Bucket into a CDN for auto-optimized images. **GCP Image Transformer** ensures that any image added to a GCP bucket has retina, standard definition, webp, and other variants.

## Getting Started

Installation is recommended with Pipenv:

```shell
$ git clone https://github.com/hackersandslackers/gcloud_image_transformer.git
$ cd gcloud-image-transformer
$ pipenv shell
$ pipenv update
$ python3 main.py
```

Alternatively, try installing via `setup.py`:

```shell
$ git clone https://github.com/hackersandslackers/gcloud_image_transformer.git
$ cd gcloud-image-transformer
$ python3 setup.py run
```

The following environment variables are required to run this script:

* `GCP_BUCKET_URL`: Publicly accessible URL of gcloud bucket.
* `GCP_BUCKET_NAME`: Friendly name of bucket.
* `GCP_BUCKET_FOLDER_NAME`: /path/to/images
