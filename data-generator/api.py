from pathlib import Path
import yaml

CONFIG_TYPE = dict[str, str | dict[str, str]]


def get_config(client, bucket_name: str, prefix: str, category_name: str) -> CONFIG_TYPE:
    """Gets the config of a category and returns the corresponding dictionary."""
    Path.mkdir(Path("/tmp/image-gallery-data"), exist_ok=True)
    filename = f"/tmp/image-gallery-data/meta_{category_name}.yaml"

    client.download_file(bucket_name, f"{prefix}{category_name}/meta.yaml", filename)
    with open(filename) as f:
        return yaml.load(f, yaml.Loader)


def get_categories(client, bucket_name: str, prefix: str, delimiter: str) -> list[str]:
    """Returns a list of strings corresponding to the categories available in the S3 bucket."""
    objects = client.list_objects_v2(
        Bucket=bucket_name,
        Prefix=prefix,
        Delimiter=delimiter,
    )
    try:
        categories = [obj["Prefix"] for obj in objects["CommonPrefixes"]]
        return [category.removeprefix(prefix).strip("/") for category in categories]
    except KeyError:
        raise RuntimeError("No categories could be found. Please ensure that the `prefix` ends with the delimiter.")
