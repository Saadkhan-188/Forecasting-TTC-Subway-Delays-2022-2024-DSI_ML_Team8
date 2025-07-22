<<<<<<< HEAD
"""
🔧 ### 1.2 Download TTC Delay Files (Offline) to Data > Raw > [Package]

Description:
This script handles the cleaning of TTC Subway Delay datasets downloaded from the City of Toronto Open Data Portal.

Supported File Formats:
- .csv
- .xls
- .xlsx

Main Cleaning Tasks:
- Remove duplicate rows
- Standardize column names (lowercase, snake_case)
- Handle bad lines and encoding issues
- Log all successes and failures to: logs/data_cleaning.log

Input:
- Folder: data/raw/ttc-subway-delay-data
- Files: Mixed-format TTC delay data files (.csv/.xls/.xlsx)

Output:
- Folder: data/processed/ttc-subway-delay-data
- Files: Cleaned `.csv` files, named identically to source but standardized

Usage:
Run this file directly as a standalone script:

```bash
python src/pipeline/data_cleaning.py
```

Author: DSI Team 8 | Maintainer: Saad Khan
"""

import requests
from pathlib import Path

def download_ckan_package_resources(package_name: str, base_url: str = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show"):
    """
    Downloads all resources from a CKAN package by package_name.

    Args:
        package_name (str): The CKAN package ID to download resources from.
        base_url (str): CKAN API endpoint for package_show.

    Saves:
        Files are saved under data/raw/<package_name>/ directory with original filenames.
    """
    # Prepare directories
    output_dir = Path("data/raw") / package_name
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"📥 Downloading resources for package: {package_name}")
    print(f"➡️ Saving files to: {output_dir}")

    # Fetch package metadata
    response = requests.get(base_url, params={"id": package_name})
    response.raise_for_status()
    package_data = response.json()

    if not package_data.get("success"):
        raise Exception(f"Failed to fetch package info for {package_name}")

    resources = package_data["result"]["resources"]
    print(f"🔍 Found {len(resources)} resources to download.")

    for resource in resources:
        resource_name = resource.get("name")
        resource_url = resource.get("url")
        resource_format = resource.get("format")

        if not resource_url:
            print(f"⚠️ Skipping resource '{resource_name}' because it has no URL.")
            continue

        # Determine output file path
        file_name = resource_name.strip().replace(" ", "_") + "." + resource_format.lower()
        file_path = output_dir / file_name

        # Check if file exists
        if file_path.exists():
            user_input = input(f"File '{file_name}' already exists. Overwrite? (y/n): ").strip().lower()
            if user_input != "y":
                print(f"Skipping '{file_name}'")
                continue

        # Download the file
        try:
            print(f"Downloading '{file_name}' from {resource_url}...")
            r = requests.get(resource_url, stream=True)
            r.raise_for_status()

            with open(file_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"✅ Saved '{file_name}'")
        except Exception as e:
            print(f"❌ Failed to download '{file_name}': {e}")

if __name__ == "__main__":
    # Replace PACKAGE_NAME with the dataset id you want to download
    PACKAGE_NAME = "ttc-subway-delay-data"
    download_ckan_package_resources(PACKAGE_NAME)
=======
"""
🔧 ### 1.2 Download TTC Delay Files (Offline) to Data > Raw > [Package]

Description:
This script handles the cleaning of TTC Subway Delay datasets downloaded from the City of Toronto Open Data Portal.

Supported File Formats:
- .csv
- .xls
- .xlsx

Main Cleaning Tasks:
- Remove duplicate rows
- Standardize column names (lowercase, snake_case)
- Handle bad lines and encoding issues
- Log all successes and failures to: logs/data_cleaning.log

Input:
- Folder: data/raw/ttc-subway-delay-data
- Files: Mixed-format TTC delay data files (.csv/.xls/.xlsx)

Output:
- Folder: data/processed/ttc-subway-delay-data
- Files: Cleaned `.csv` files, named identically to source but standardized

Usage:
Run this file directly as a standalone script:

```bash
python src/pipeline/data_cleaning.py
```

Author: DSI Team 8 | Maintainer: Saad Khan
"""

import requests
from pathlib import Path

def download_ckan_package_resources(package_name: str, base_url: str = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show"):
    """
    Downloads all resources from a CKAN package by package_name.

    Args:
        package_name (str): The CKAN package ID to download resources from.
        base_url (str): CKAN API endpoint for package_show.

    Saves:
        Files are saved under data/raw/<package_name>/ directory with original filenames.
    """
    # Prepare directories
    output_dir = Path("data/raw") / package_name
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"📥 Downloading resources for package: {package_name}")
    print(f"➡️ Saving files to: {output_dir}")

    # Fetch package metadata
    response = requests.get(base_url, params={"id": package_name})
    response.raise_for_status()
    package_data = response.json()

    if not package_data.get("success"):
        raise Exception(f"Failed to fetch package info for {package_name}")

    resources = package_data["result"]["resources"]
    print(f"🔍 Found {len(resources)} resources to download.")

    for resource in resources:
        resource_name = resource.get("name")
        resource_url = resource.get("url")
        resource_format = resource.get("format")

        if not resource_url:
            print(f"⚠️ Skipping resource '{resource_name}' because it has no URL.")
            continue

        # Determine output file path
        file_name = resource_name.strip().replace(" ", "_") + "." + resource_format.lower()
        file_path = output_dir / file_name

        # Check if file exists
        if file_path.exists():
            user_input = input(f"File '{file_name}' already exists. Overwrite? (y/n): ").strip().lower()
            if user_input != "y":
                print(f"Skipping '{file_name}'")
                continue

        # Download the file
        try:
            print(f"Downloading '{file_name}' from {resource_url}...")
            r = requests.get(resource_url, stream=True)
            r.raise_for_status()

            with open(file_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"✅ Saved '{file_name}'")
        except Exception as e:
            print(f"❌ Failed to download '{file_name}': {e}")

if __name__ == "__main__":
    # Replace PACKAGE_NAME with the dataset id you want to download
    PACKAGE_NAME = "ttc-subway-delay-data"
    download_ckan_package_resources(PACKAGE_NAME)
>>>>>>> 804fdd5ffc11025b1a7a4ad3a77889966f0e7142
