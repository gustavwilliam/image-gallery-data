import json
import os
from pathlib import Path

import boto3
from dotenv import load_dotenv
from .api import get_config, get_categories, get_image_paths
from .config_generator import extend_config, strip_name
from .publish import publish_data

load_dotenv()
PREFIX = os.getenv("PREFIX", "image-gallery/")
DELIMITER = os.getenv("DELIMITER", "/")
try:
    BUCKET_NAME = os.environ["BUCKET_NAME"]
except KeyError:
    raise RuntimeError("The required environment variable `BUCKET_NAME` was not set.")

S3_CLIENT = boto3.client("s3")

categories = get_categories(S3_CLIENT, BUCKET_NAME, PREFIX, DELIMITER)
configs = {category: get_config(S3_CLIENT, BUCKET_NAME, PREFIX, DELIMITER, category) for category in categories}
image_paths = {
    category: get_image_paths(S3_CLIENT, BUCKET_NAME, DELIMITER, category)
    for category in configs.keys()
}
gallery_data = {
    strip_name(name, PREFIX, DELIMITER):
    extend_config(config, name, image_paths[name])
    for name, config in configs.items()
}

if __name__ == "__main__":
    Path.mkdir(Path("/tmp/image-gallery-data"), exist_ok=True)
    filepath = "/tmp/image-gallery-data/data.json"

    with open(filepath, "w") as f:
        json.dump(gallery_data, f)

    publish_data(S3_CLIENT, BUCKET_NAME, filepath, f"{PREFIX}data.json")
