# Import the necessary libraries
# Flask is used to create the API
# jsonify converts Python dictionaries/lists into JSON format for HTTP responses
from flask import Flask, jsonify

# requests is used to make HTTP requests to the City of Toronto open data API
import requests

# Create a Flask application instance
app = Flask(__name__)

# Base URL for the Toronto Open Data portal
BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

# This is the unique identifier (called "package name") for the TTC Streetcar Delay dataset
PACKAGE_NAME = "ttc-streetcar-delay-data"

# Define an API route (endpoint) at "/get-delays"
# When a user accesses this URL with a GET request, the function below will run
@app.route('/get-delays', methods=['GET'])
def get_delays():
    # Construct the full API endpoint to retrieve metadata about the dataset
    package_url = f"{BASE_URL}/api/3/action/package_show"
    
    # The API expects the package name (dataset name) as a parameter
    params = { "id": PACKAGE_NAME }

    # Make an HTTP GET request to the CKAN API to get the dataset package metadata
    package = requests.get(package_url, params=params).json()

    # Create a list to hold the resource URLs and names
    results = []

    # Loop through each "resource" in the dataset
    # A dataset (package) may contain several files or tables called "resources"
    for resource in package["result"]["resources"]:
        
        # If the resource is NOT "datastore_active", it usually means it's a file (CSV, Excel, etc.)
        if not resource["datastore_active"]:
            # Construct the URL to get more metadata about this specific resource
            resource_url = f"{BASE_URL}/api/3/action/resource_show?id={resource['id']}"

            # Request the metadata
            resource_metadata = requests.get(resource_url).json()

            # Extract the download URL and resource name and add them to the results list
            results.append({
                "name": resource["name"],  # Name of the resource (e.g., "Streetcar Delay Data - 2023")
                "url": resource_metadata["result"]["url"]  # Direct URL to download the file
            })

    # Return the result as a JSON response to the API caller
    return jsonify(results)

# Only run the Flask development server if this file is executed directly
# This block prevents the server from running if the file is imported as a module
if __name__ == "__main__":
    # Start the server in debug mode so you can see real-time errors/logs
    app.run(debug=True)
# This code defines a simple Flask API that retrieves TTC streetcar delay data from the City of Toronto's open data portal.
# It fetches metadata about the dataset and provides download links for the resources available in the dataset.

# The API can be accessed at the "/get-delays" endpoint, which returns a JSON list of resource names and their download URLs.   

# The server runs in debug mode, which is useful for development and testing.   

@app.route('/', methods=['GET'])
def home():
    return "<h2>Welcome to the TTC Delay API</h2><p>Use <code>/get-delays</code> to access delay data.</p>"

# click here http://127.0.0.1:5000/get-delays
