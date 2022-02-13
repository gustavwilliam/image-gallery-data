import os
import boto3
from dotenv import load_dotenv

load_dotenv()

try:
    BUCKET_NAME = os.environ["BUCKET_NAME"]
except KeyError:
    raise RuntimeError("The required environment variable `BUCKET_NAME` was not set.")

s3 = boto3.resource("s3")
bucket = s3.Bucket(BUCKET_NAME)
