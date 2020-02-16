"""Google Cloud Storage Configuration."""
from os import environ
import datetime


# Google Cloud Storage
bucket_URL = environ.get('GCP_BUCKET_URL')
bucket_name = environ.get('GCP_BUCKET_NAME')
bucket_folder = environ.get('GCP_BUCKET_FOLDER_NAME')

# Current month/year
dt = datetime.datetime.today()
year = dt.year
month = dt.strftime('%m')
bucket_image_folder_prefixes = [f'{year}/{month}']
