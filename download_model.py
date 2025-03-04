from typing import Literal
import os
import requests
import zipfile
import fire


def download_file(url: str, dest_path: str) -> None:
    """Download a file from a URL and save it to a destination path."""
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Raise an error for bad status
        with open(dest_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive chunks
                    f.write(chunk)
    print(f"Downloaded file saved to {dest_path}")


def extract_zip(zip_path: str, extract_to: str) -> None:
    """Extract a zip file to a given directory."""
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {zip_path} to {extract_to}")


def download_and_extract(
    asset: Literal["enzh", "enja", "zhen", "jaen"] = "enzh",
    output_dir: str = "./models",
) -> None:
    """
    Download and extract a model asset.

    Args:
        asset (str): The key of the asset to download. Options are: enzh, enja, zhen, jaen.
        output_dir (str): The directory where the zip contents should be extracted.

    https://github.com/mozilla/firefox-translations-models/blob/main/scripts/pull_models.sh
    """
    # Base URL for the GitHub release assets
    base_url = "https://github.com/xxnuo/MTranServer/releases/download/models"
    # Map asset keys to file names
    assets = {
        "enzh": "enzh.zip",  # English-to-Chinese model
        "enja": "enja.zip",  # English-to-Japanese model
        "zhen": "zhen.zip",  # Chinese-to-English model
        "jaen": "jaen.zip",  # Japanese-to-English model
    }

    if asset not in assets:
        print(
            f"Asset '{asset}' not recognized. Available assets: {', '.join(assets.keys())}"
        )
        return

    file_name = assets[asset]
    download_url = f"{base_url}/{file_name}"
    local_zip = file_name  # Local temporary file name

    print(f"Downloading {download_url} ...")
    download_file(download_url, local_zip)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    print(f"Extracting {local_zip} to {output_dir} ...")
    extract_zip(local_zip, output_dir)

    # Optionally, remove the zip file after extraction
    os.remove(local_zip)
    print("Cleanup complete. Download and extraction finished.")


if __name__ == "__main__":
    fire.Fire(download_and_extract)
