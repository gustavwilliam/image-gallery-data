import os
import boto3
from dotenv import load_dotenv
from .api import get_config, get_categories, get_image_paths

load_dotenv()
PREFIX = os.getenv("PREFIX", "image-gallery/")
DELIMITER = os.getenv("DELIMITER", "/")
try:
    BUCKET_NAME = os.environ["BUCKET_NAME"]
except KeyError:
    raise RuntimeError("The required environment variable `BUCKET_NAME` was not set.")

S3_CLIENT = boto3.client("s3")


if __name__ == "__main__":
    categories = get_categories(S3_CLIENT, BUCKET_NAME, PREFIX, DELIMITER)
    configs = {category: get_config(S3_CLIENT, BUCKET_NAME, category) for category in categories}
    image_paths = {
        category: get_image_paths(S3_CLIENT, BUCKET_NAME, DELIMITER, category)
        for category in configs.keys()
    }
