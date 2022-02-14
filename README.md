# Image Gallery Data

The data for my [Image Gallery](https://github.com/gustavwilliam/image-gallery) project.

This repo contains scripts for automatically building a `data.json` file with all the information required by the Image Gallery.
The source images are hosted in an [AWS S3](https://aws.amazon.com/s3/) bucket.

## Installation

Clone the repo and enter the directory.

```zsh
git clone https://github.com/gustavwilliam/image-gallery-data
cd image-gallery-data
```

Create a virtual environment and install the dependencies.

```zsh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Environment variables

In order to access your AWS S3 bucket, you must provide a `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
Read more about generating the credentials [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey).

Create a `.env` file at the root of the project directory:

```
# Required
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
BUCKET_NAME=

# Optional
PREFIX=         # Defaults to "image-gallery"
DELIMITER=      # Defaults to "/"
```

<details>

<summary>Example .env file</summary>

```
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
BUCKET_NAME=cdn.godi.se

PREFIX=image-gallery/
DELIMITER=/
```

</details>
