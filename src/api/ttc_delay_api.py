<<<<<<< HEAD
"""
TTC_Delay_API.py 🚦
-----------------------------------

✅ PURPOSE:

This is Step 1.1 in the Data Pipeline:

A lightweight Flask API to interact with the TTC Streetcar/Subway Delay datasets
hosted on the City of Toronto Open Data portal.

👥 Intended for: Developers, Analysts, and Data Scientists building tools or pipelines
off Toronto mobility data.

📂 Project Folder Location: `src/api/TTC_Delay_API.py`

-----------------------------------

📌 USER JOURNEY CHECKLIST (How to Use This API)

1️⃣ [Setup] Activate your virtual environment:
    $ source .venv/bin/activate  (Mac/Linux)
    $ .venv\Scripts\activate     (Windows)

2️⃣ [Run API] From project root, start the Flask server:
    $ python src/api/TTC_Delay_API.py

3️⃣ [Access Home] Open a browser:
    👉 http://127.0.0.1:5000/
    🧭 You'll see available endpoints and usage hints

4️⃣  [Search Any Dataset] Use:
    👉 http://127.0.0.1:5000/search?q=ttc
    🔍 Search Toronto Open Data by keyword (e.g., "mobility", "housing", "climate")

    4️⃣.1 Copy the "name" value
    This is the dataset ID you'll pass to the API:
    PACKAGE_NAME = "ttc-subway-delay-data"
-----------------------------------
✅ EXPECTED RESULT:
    You should get JSON responses listing datasets or download links for TTC delays.

💡 NEXT STEP:
    Once you’ve confirmed the API gives correct TTC file URLs,
    1️⃣ Copy the "name" value
    This is the dataset ID you'll pass to the API:
    PACKAGE_NAME = "ttc-subway-delay-data"


    

##🔹 TIP:
Extend this file by adding new routes or wrapping it inside a larger ETL orchestrator.
This is a standalone microservice designed to plug into a modular ML pipeline.

"""

# ------------------------------------------------
# 🔧 Imports
# ------------------------------------------------
from flask import Flask, jsonify, request
import requests

# ------------------------------------------------
# 🌐 Constants
# ------------------------------------------------
BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
PACKAGE_NAME = "ttc-streetcar-delay-data"

# ------------------------------------------------
# 🚀 Initialize Flask app
# ------------------------------------------------
app = Flask(__name__)

# ------------------------------------------------
# 🏠 ROUTE: Home Page (Welcome)
# ------------------------------------------------
@app.route('/', methods=['GET'])
def home():
    return """
    <h2>🚦 TTC Delay Data API</h2>
    <p>Welcome! Use the following endpoints:</p>
    <ul>
        <li><code>/get-delays</code> – List all available TTC delay CSVs</li>
        <li><code>/search?q=your_query</code> – Search any dataset by keyword</li>
    </ul>
    """

# ------------------------------------------------
# 📥 ROUTE: Get delay file download links
# ------------------------------------------------
@app.route('/get-delays', methods=['GET'])
def get_delays():
    package_url = f"{BASE_URL}/api/3/action/package_show"
    params = { "id": PACKAGE_NAME }
    package = requests.get(package_url, params=params).json()

    results = []

    for resource in package["result"]["resources"]:
        if not resource["datastore_active"]:
            resource_url = f"{BASE_URL}/api/3/action/resource_show?id={resource['id']}"
            resource_metadata = requests.get(resource_url).json()
            results.append({
                "name": resource["name"],
                "url": resource_metadata["result"]["url"]
            })

    return jsonify(results)

# ------------------------------------------------
# 🔍 ROUTE: Keyword-based search for other datasets
# ------------------------------------------------
@app.route('/search', methods=['GET'])
def search_dataset():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Please provide a search query using ?q=term"})

    search_url = f"{BASE_URL}/api/3/action/package_search"
    response = requests.get(search_url, params={"q": query})
    results = response.json()["result"]["results"]

    output = []
    for dataset in results:
        output.append({
            "title": dataset.get("title"),
            "name": dataset.get("name"),
            "organization": dataset.get("organization", {}).get("title", "N/A"),
            "num_resources": len(dataset.get("resources", [])),
            "url": f"https://open.toronto.ca/dataset/{dataset.get('name')}/"
        })

    return jsonify(output)

# ------------------------------------------------
# 🧪 Run the Flask server
# ------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)


=======
"""
TTC_Delay_API.py 🚦
-----------------------------------

✅ PURPOSE:

This is Step 1.1 in the Data Pipeline:

A lightweight Flask API to interact with the TTC Streetcar/Subway Delay datasets
hosted on the City of Toronto Open Data portal.

👥 Intended for: Developers, Analysts, and Data Scientists building tools or pipelines
off Toronto mobility data.

📂 Project Folder Location: `src/api/TTC_Delay_API.py`

-----------------------------------

📌 USER JOURNEY CHECKLIST (How to Use This API)

1️⃣ [Setup] Activate your virtual environment:
    $ source .venv/bin/activate  (Mac/Linux)
    $ .venv\Scripts\activate     (Windows)

2️⃣ [Run API] From project root, start the Flask server:
    $ python src/api/TTC_Delay_API.py

3️⃣ [Access Home] Open a browser:
    👉 http://127.0.0.1:5000/
    🧭 You'll see available endpoints and usage hints

4️⃣  [Search Any Dataset] Use:
    👉 http://127.0.0.1:5000/search?q=ttc
    🔍 Search Toronto Open Data by keyword (e.g., "mobility", "housing", "climate")

    4️⃣.1 Copy the "name" value
    This is the dataset ID you'll pass to the API:
    PACKAGE_NAME = "ttc-subway-delay-data"
-----------------------------------
✅ EXPECTED RESULT:
    You should get JSON responses listing datasets or download links for TTC delays.

💡 NEXT STEP:
    Once you’ve confirmed the API gives correct TTC file URLs,
    1️⃣ Copy the "name" value
    This is the dataset ID you'll pass to the API:
    PACKAGE_NAME = "ttc-subway-delay-data"


    

##🔹 TIP:
Extend this file by adding new routes or wrapping it inside a larger ETL orchestrator.
This is a standalone microservice designed to plug into a modular ML pipeline.

"""

# ------------------------------------------------
# 🔧 Imports
# ------------------------------------------------
from flask import Flask, jsonify, request
import requests

# ------------------------------------------------
# 🌐 Constants
# ------------------------------------------------
BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
PACKAGE_NAME = "ttc-streetcar-delay-data"

# ------------------------------------------------
# 🚀 Initialize Flask app
# ------------------------------------------------
app = Flask(__name__)

# ------------------------------------------------
# 🏠 ROUTE: Home Page (Welcome)
# ------------------------------------------------
@app.route('/', methods=['GET'])
def home():
    return """
    <h2>🚦 TTC Delay Data API</h2>
    <p>Welcome! Use the following endpoints:</p>
    <ul>
        <li><code>/get-delays</code> – List all available TTC delay CSVs</li>
        <li><code>/search?q=your_query</code> – Search any dataset by keyword</li>
    </ul>
    """

# ------------------------------------------------
# 📥 ROUTE: Get delay file download links
# ------------------------------------------------
@app.route('/get-delays', methods=['GET'])
def get_delays():
    package_url = f"{BASE_URL}/api/3/action/package_show"
    params = { "id": PACKAGE_NAME }
    package = requests.get(package_url, params=params).json()

    results = []

    for resource in package["result"]["resources"]:
        if not resource["datastore_active"]:
            resource_url = f"{BASE_URL}/api/3/action/resource_show?id={resource['id']}"
            resource_metadata = requests.get(resource_url).json()
            results.append({
                "name": resource["name"],
                "url": resource_metadata["result"]["url"]
            })

    return jsonify(results)

# ------------------------------------------------
# 🔍 ROUTE: Keyword-based search for other datasets
# ------------------------------------------------
@app.route('/search', methods=['GET'])
def search_dataset():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Please provide a search query using ?q=term"})

    search_url = f"{BASE_URL}/api/3/action/package_search"
    response = requests.get(search_url, params={"q": query})
    results = response.json()["result"]["results"]

    output = []
    for dataset in results:
        output.append({
            "title": dataset.get("title"),
            "name": dataset.get("name"),
            "organization": dataset.get("organization", {}).get("title", "N/A"),
            "num_resources": len(dataset.get("resources", [])),
            "url": f"https://open.toronto.ca/dataset/{dataset.get('name')}/"
        })

    return jsonify(output)

# ------------------------------------------------
# 🧪 Run the Flask server
# ------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)


>>>>>>> 804fdd5ffc11025b1a7a4ad3a77889966f0e7142
