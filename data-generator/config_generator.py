from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api import CONFIG_TYPE


def strip_name(category_path: str, prefix: str, delimiter: str) -> str:
    """Return a stripped version of a category name, from the full path."""
    return category_path.removeprefix(prefix).strip(delimiter)


def extend_config(config: "CONFIG_TYPE", image_paths: list[str | None]) -> "CONFIG_TYPE":
    """Adds image urls and sets thumbnail to first image if none is defined."""
    config.update({"images": image_paths})
    if not config.get("thumbnail"):
        config["thumbnail"] = image_paths[0]  # Default to first image

    return config
