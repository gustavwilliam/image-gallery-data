def publish_data(client, bucket: str, config_path: str, output_path: str) -> None:
    """Uploads the gallery config to the S3 bucket."""
    client.upload_file(config_path, bucket, output_path)
