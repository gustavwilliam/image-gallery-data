from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api import CONFIG_TYPE


def strip_name(category_path: str, prefix: str, delimiter: str) -> str:
    """Return a stripped version of a category name, from the full path."""
    return category_path.removeprefix(prefix).strip(delimiter)


def extend_config(config: "CONFIG_TYPE", category: str, image_paths: list[str | None]) -> "CONFIG_TYPE":
    """Adds image urls and sets thumbnail to first image if none is defined."""
    config.update({"images": image_paths})
    if config.get("thumbnail"):
        config["thumbnail"] = f"{category}{config['thumbnail']}"
    else:
        try:
            config["thumbnail"] = image_paths[0]  # Default to first image
        except IndexError:
            config["thumbnail"] = None  # No images exist in category

    for key, val in config["dates"].items():
        config["dates"][key] = str(val)  # Convert datetime object to "YYYY-MM-DD" format

    return config
