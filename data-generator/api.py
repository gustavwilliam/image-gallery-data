from pathlib import Path
import yaml
from .config_generator import strip_name

CONFIG_TYPE = dict[str, str | dict[str, str] | list[str]]


def get_config(client, bucket_name: str, prefix: str, delimiter: str, category_path: str) -> CONFIG_TYPE:
    """Gets the config of a category and returns the corresponding dictionary."""
    Path.mkdir(Path("/tmp/image-gallery-data"), exist_ok=True)
    category_name = strip_name(category_path, prefix, delimiter)
    filename = f"/tmp/image-gallery-data/meta_{category_name}.yaml"

    client.download_file(bucket_name, f"{category_path}meta.yaml", filename)
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
        return [obj["Prefix"] for obj in objects["CommonPrefixes"]]
    except KeyError:
        raise RuntimeError("No categories could be found. Please ensure that the `prefix` ends with the delimiter.")


def get_image_paths(client, bucket_name: str, delimiter: str, category: str) -> list[str | None]:
    """Get a list of paths to images in the S3 category."""
    objects = client.list_objects_v2(
        Bucket=bucket_name,
        Prefix=category,
        Delimiter=delimiter,
    )
    try:
        return [
            obj["Key"]
            for obj in objects["Contents"]  # Return [] if no images are present
            if obj["Key"] != f"{category}meta.yaml"  # Meta files aren't images
        ]
    except KeyError:
        raise RuntimeError(
            f"The category `{category}` either does not exists or is improperly configured. "
            "Please ensure that the `category` ends with the delimiter."
        )
