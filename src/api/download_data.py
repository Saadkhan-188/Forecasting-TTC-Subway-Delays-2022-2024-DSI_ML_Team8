"""
Step 1.1 — TTC Delay Dataset: Automated Downloader Script
----------------------------------------------------------

📌 PURPOSE:
This script connects to the City of Toronto Open Data API and downloads all relevant
TTC Streetcar Delay data files. The files are saved in `data/raw/` for further use.

🧾 PREREQUISITES:
1. The virtual environment is activated (`.venv` is active).
2. Required Python packages are installed (e.g., `requests`).
3. Directory structure is created and verified:
    - Project root contains: `data/raw/`, `src/api/`, and `README.md`.
    - Run this script from the project root, e.g.:
      ```bash
      python src/api/download_data.py
      ```

✅ VERIFY:
- Ensure `data/raw/` folder gets populated with `.csv` files after script is run.
- Check the terminal logs to confirm download and save success.

"""

# 🧱 Libraries
import os           # for working with file paths
import requests     # to make HTTP requests to Open Data API

# 🌐 Constants
BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca"  # Base API endpoint
PACKAGE_NAME = "ttc-streetcar-delay-data"                     # Dataset name from Toronto Open Data
RAW_DATA_DIR = "data/raw/"                                    # Output directory for downloaded files

# 📁 Ensure target directory exists before saving files
if not os.path.exists(RAW_DATA_DIR):
    print(f"📂 Directory '{RAW_DATA_DIR}' does not exist. Creating it now...")
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
else:
    print(f"📂 Directory '{RAW_DATA_DIR}' already exists. Proceeding with downloads.")

# STEP 1️⃣ — Get dataset (package) metadata from the CKAN API
package_url = f"{BASE_URL}/api/3/action/package_show"
params = { "id": PACKAGE_NAME }
response = requests.get(package_url, params=params)
package = response.json()

# STEP 2️⃣ — Loop through all available resources in the dataset
for resource in package["result"]["resources"]:

    # 🎯 Only download non-database (static file) resources
    if not resource["datastore_active"]:
        resource_id = resource["id"]

        # 📝 Clean up resource name to use as a valid filename
        import re
        resource_name = re.sub(r'[\\/*?:"<>|\t]', '_', resource["name"]).strip()

        # STEP 3️⃣ — Get metadata to extract direct download URL
        resource_meta_url = f"{BASE_URL}/api/3/action/resource_show?id={resource_id}"
        resource_meta = requests.get(resource_meta_url).json()
        file_url = resource_meta["result"]["url"]

        # STEP 4️⃣ — Download the resource file
        print(f"📥 Downloading {resource_name}...")
        file_content = requests.get(file_url).content

        # STEP 5️⃣ — Save the downloaded content to /data/raw/
        file_path = os.path.join(RAW_DATA_DIR, f"{resource_name}.csv")
        with open(file_path, "wb") as f:
            f.write(file_content)

        print(f"✅ Saved to {file_path}")
# This script automates the download of TTC Streetcar Delay data from the City of Toronto's Open Data API.
# It retrieves metadata about the dataset, loops through available resources, and saves each file in the
# `data/raw/` downloaded content to /data/raw/ directory with a cleaned filename.
# It ensures the target directory exists before downloading and provides feedback on the download process.