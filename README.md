# Google Cloud Storage Image Transformer

![Python](https://img.shields.io/badge/Python-v3.7-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Pillow](https://img.shields.io/badge/Pillow-v6.0.0-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Requests](https://img.shields.io/badge/Requests-v2.22.0-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Google Cloud Functions](https://img.shields.io/badge/Google--Cloud--Functions-v93-blue.svg?longCache=true&logo=google&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/gcloud_image_transformer.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a&logo=Github)](https://github.com/hackersandslackers/gcloud_image_transformer/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/gcloud_image_transformer.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a&logo=Github)](https://github.com/hackersandslackers/gcloud_image_transformer/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/gcloud_image_transformer.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b&logo=Github)](https://github.com/hackersandslackers/gcloud_image_transformer/network)

Script to optimize image files being served from a live CDN. Walks through a bucket to create *retina* and *webp* variations of images where needed.

## Getting Started

Installation is recommended with Pipenv:

```shell
$ git clone https://github.com/hackersandslackers/gcloud_image_transformer.git
$ cd gcloud_image_transformer
$ pipenv shell
$ pipenv update
$ python3 main.py
```

Alternatively, try installing via `setup.py`:

```shell
$ git clone https://github.com/hackersandslackers/gcloud_image_transformer.git
$ cd gcloud_image_transformer
$ python3 setup.py run
```

The following environment variables are required to run this script:

* `GCP_BUCKET_URL`: Publically accesible URL of gcloud bucket.
* `GCP_BUCKET_NAME`: Friendly name of bucket.
* `GCP_BUCKET_FOLDER_NAME`: /path/to/images


-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
