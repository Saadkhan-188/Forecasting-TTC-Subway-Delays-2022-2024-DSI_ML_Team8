<<<<<<< HEAD
# 🚌 DSI_ML_Team8: TTC Delay Data Project

A data science project that uses open datasets from the City of Toronto to analyze and model TTC streetcar and subway delay data. Built with Flask, Python, and a structured ML pipeline.

---

## 📚 Table of Contents

- [Project Structure](#project-structure)
- [Quickstart Instructions](#quickstart-instructions)
- [Step 1: API Setup](#step-1-api-setup)  
  - [1.1 Flask API for Exploring Available Datasets](#11-flask-api-for-exploring-available-datasets)  
  - [1.2 Download TTC Delay Files (Offline)](#12-download-ttc-delay-files-offline)  
- [Step 2: Data Pipeline](#step-2-data-pipeline)  
  - [2.1 Data Cleaning](#21-data-cleaning)  
  - [2.2 Feature Engineering](#22-feature-engineering)  
- [Step 3: EDA and Modeling](#step-3-eda-and-modeling)  
  - [3.1 Summary Statistics](#31-summary-statistics)  
  - [3.2 Trend Analysis](#32-trend-analysis)  
  - [3.3 Delay Duration Modeling](#33-delay-duration-modeling)  
- [Project Team](#project-team)

---

## 🗂 Project Structure
DSI_ML_Team8/
├── data/
│   ├── raw/                                      # Unmodified source data
│   │   ├── ttc-subway-delay-data/                # Folder for raw downloaded files
│   │   └── ttc-subway-delay-data-format_converted/ # Converted XML/XLSX files to CSV          
│   ├── processed/      # Cleaned and engineered datasets
│   │   └── ttc-subway-delay-data-format_converted-clean/  
│   │       
│   └── external/       # External reference files
├── logs/               # Log files for pipeline and API processes
├── notebooks/          # Jupyter notebooks for EDA and modeling
├── models/             # Serialized models and performance metrics
├── visuals/            # Charts and figures for reporting and slides
├── reports/            # Final presentations, summaries, and documentation
├── src/
│   ├── api/            # Flask app + dataset download scripts
│   │   ├── download_data.py
│   │   └── ttc_delay_api.py
│   ├── pipeline/       # Data pipeline scripts: cleaning, feature engineering, orchestration
│   │   ├── __init__.py
│   │   ├── data_cleaning.py
│   │   ├── feature_engineering.py
│   │   ├── pipeline_runner.py
│   │   └── utils.py
│   └── README.src.md    # README specific to src folder
├── .gitignore
└── README.md

---

## ⚡ Quickstart Instructions

```bash
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate     # Windows
source .venv/bin/activate    # macOS/Linux

# Install required packages
pip install -r requirements.txt

# 4. Run Flask API server to explore datasets
python src/api/ttc_delay_api.py

---

## Step 1: API Setup

### 1.1 Flask API for Exploring Available Datasets

Our Flask API exposes endpoints to list and query TTC delay datasets downloaded from the City of Toronto Open Data Portal.

- **Endpoint:** `/get-delays`  
- **Function:** Returns a JSON list of available TTC streetcar and subway delay datasets.  
- **Usage:** Use this endpoint to discover available datasets and their metadata.  
- **Expected Result:**  
  JSON response listing dataset names and details.  
  Copy the `"name"` value of the desired dataset — this is the `PACKAGE_NAME` you’ll use in the downloader script.

---

### 1.2 Download TTC Delay Files (Offline)

We provide a downloader script that fetches CSV resources from the TTC delay dataset package via the City of Toronto CKAN API.

- **Script:** `src/api/download_data.py`  
- **Input:** `PACKAGE_NAME` (e.g., `"ttc-subway-delay-data"`)  
- **Output:** CSV files saved under `data/raw/ttc-subway-delay-data/` folder.  
- **Expected Result:**  
  Local CSV files with TTC delay data ready for ingestion into the pipeline.

---

## Step 2: Data Pipeline

### 2.1 Data Cleaning

Raw CSV files often contain inconsistencies such as missing values, duplicates, encoding errors, and formatting issues.

Our `data_cleaning.py` script handles:

- Removing duplicate rows  
- Trimming whitespace from text fields  
- Standardizing column names (lowercase, snake_case)  
- Fixing encoding issues by trying fallback encodings  
- Logging errors and successes to `logs/data_cleaning.log`  

**Input:** CSV files from `data/raw/ttc-subway-delay-data`  
**Output:** Cleaned CSV files saved to `data/processed/ttc-subway-delay-data`  

This script is designed for robustness and scalability, with proper logging and error handling.

### 2.2 Feature Engineering

After cleaning, we transform data to create meaningful features for modeling:

- Parsing datetime columns and extracting components (year, month, weekday, hour)  
- Encoding categorical variables (e.g., delay codes)  
- Calculating delay durations and flagging anomalies  
- Aggregating data by route, day, or time windows  

These transformations are encapsulated in `feature_engineering.py` and designed for modular extension.

---

## Step 3: EDA and Modeling

### 3.1 Summary Statistics

- Compute basic descriptive statistics to understand the data distribution, e.g., counts, means, medians.  
- Identify missing data patterns and outliers.

### 3.2 Trend Analysis

- Visualize delay frequency by route, time of day, day of week, and month.  
- Detect seasonal patterns or anomalies in delays.

### 3.3 Delay Duration Modeling

- Build regression or classification models to predict delay durations or delay occurrences.  
- Evaluate model performance with appropriate metrics and cross-validation.

All analysis notebooks are located in `notebooks/` with clear documentation and visuals saved in `visuals/`.

---

## Project Team

| Name               | Role                         | Responsibilities                                    |
|--------------------|------------------------------|----------------------------------------------------|
| Saad Khan          | Product Owner / API Integrations | Project leadership, API development, data strategy |
| Saad & Sahil       | EDA + Feature Engineering    | Data cleaning, feature creation, exploration       |
| Sneha & Sucharita  | Modeling + Evaluation        | Model building, validation, and tuning              |
| Val & Faiz         | Visualization + Reporting    | Creating visuals, reports, and presentations        |


=======
# 🚌 DSI_ML_Team8: TTC Delay Data Project

A data science project that uses open datasets from the City of Toronto to analyze and model TTC streetcar and subway delay data. Built with Flask, Python, and a structured ML pipeline.

---

## 📚 Table of Contents

- [Project Structure](#project-structure)
- [Quickstart Instructions](#quickstart-instructions)
- [Step 1: API Setup](#step-1-api-setup)  
  - [1.1 Flask API for Exploring Available Datasets](#11-flask-api-for-exploring-available-datasets)  
  - [1.2 Download TTC Delay Files (Offline)](#12-download-ttc-delay-files-offline)  
- [Step 2: Data Pipeline](#step-2-data-pipeline)  
  - [2.1 Data Cleaning](#21-data-cleaning)  
  - [2.2 Feature Engineering](#22-feature-engineering)  
- [Step 3: EDA and Modeling](#step-3-eda-and-modeling)  
  - [3.1 Summary Statistics](#31-summary-statistics)  
  - [3.2 Trend Analysis](#32-trend-analysis)  
  - [3.3 Delay Duration Modeling](#33-delay-duration-modeling)  
- [Project Team](#project-team)

---

## 🗂 Project Structure
DSI_ML_Team8/
├── data/
│   ├── raw/                                      # Unmodified source data
│   │   ├── ttc-subway-delay-data/                # Folder for raw downloaded files
│   │   └── ttc-subway-delay-data-format_converted/ # Converted XML/XLSX files to CSV          
│   ├── processed/      # Cleaned and engineered datasets
│   │   └── ttc-subway-delay-data-format_converted-clean/  
│   │       
│   └── external/       # External reference files
├── logs/               # Log files for pipeline and API processes
├── notebooks/          # Jupyter notebooks for EDA and modeling
├── models/             # Serialized models and performance metrics
├── visuals/            # Charts and figures for reporting and slides
├── reports/            # Final presentations, summaries, and documentation
├── src/
│   ├── api/            # Flask app + dataset download scripts
│   │   ├── download_data.py
│   │   └── ttc_delay_api.py
│   ├── pipeline/       # Data pipeline scripts: cleaning, feature engineering, orchestration
│   │   ├── __init__.py
│   │   ├── data_cleaning.py
│   │   ├── feature_engineering.py
│   │   ├── pipeline_runner.py
│   │   └── utils.py
│   └── README.src.md    # README specific to src folder
├── .gitignore
└── README.md

---

## ⚡ Quickstart Instructions

```bash
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate     # Windows
source .venv/bin/activate    # macOS/Linux

# Install required packages
pip install -r requirements.txt

# 4. Run Flask API server to explore datasets
python src/api/ttc_delay_api.py

---

## Step 1: API Setup

### 1.1 Flask API for Exploring Available Datasets

Our Flask API exposes endpoints to list and query TTC delay datasets downloaded from the City of Toronto Open Data Portal.

- **Endpoint:** `/get-delays`  
- **Function:** Returns a JSON list of available TTC streetcar and subway delay datasets.  
- **Usage:** Use this endpoint to discover available datasets and their metadata.  
- **Expected Result:**  
  JSON response listing dataset names and details.  
  Copy the `"name"` value of the desired dataset — this is the `PACKAGE_NAME` you’ll use in the downloader script.

---

### 1.2 Download TTC Delay Files (Offline)

We provide a downloader script that fetches CSV resources from the TTC delay dataset package via the City of Toronto CKAN API.

- **Script:** `src/api/download_data.py`  
- **Input:** `PACKAGE_NAME` (e.g., `"ttc-subway-delay-data"`)  
- **Output:** CSV files saved under `data/raw/ttc-subway-delay-data/` folder.  
- **Expected Result:**  
  Local CSV files with TTC delay data ready for ingestion into the pipeline.

---

## Step 2: Data Pipeline

### 2.1 Data Cleaning

Raw CSV files often contain inconsistencies such as missing values, duplicates, encoding errors, and formatting issues.

Our `data_cleaning.py` script handles:

- Removing duplicate rows  
- Trimming whitespace from text fields  
- Standardizing column names (lowercase, snake_case)  
- Fixing encoding issues by trying fallback encodings  
- Logging errors and successes to `logs/data_cleaning.log`  

**Input:** CSV files from `data/raw/ttc-subway-delay-data`  
**Output:** Cleaned CSV files saved to `data/processed/ttc-subway-delay-data`  

This script is designed for robustness and scalability, with proper logging and error handling.

### 2.2 Feature Engineering

After cleaning, we transform data to create meaningful features for modeling:

- Parsing datetime columns and extracting components (year, month, weekday, hour)  
- Encoding categorical variables (e.g., delay codes)  
- Calculating delay durations and flagging anomalies  
- Aggregating data by route, day, or time windows  

These transformations are encapsulated in `feature_engineering.py` and designed for modular extension.

---

## Step 3: EDA and Modeling

### 3.1 Summary Statistics

- Compute basic descriptive statistics to understand the data distribution, e.g., counts, means, medians.  
- Identify missing data patterns and outliers.

### 3.2 Trend Analysis

- Visualize delay frequency by route, time of day, day of week, and month.  
- Detect seasonal patterns or anomalies in delays.

### 3.3 Delay Duration Modeling

- Build regression or classification models to predict delay durations or delay occurrences.  
- Evaluate model performance with appropriate metrics and cross-validation.

All analysis notebooks are located in `notebooks/` with clear documentation and visuals saved in `visuals/`.

---

## Project Team

| Name               | Role                         | Responsibilities                                    |
|--------------------|------------------------------|----------------------------------------------------|
| Saad Khan          | Product Owner / API Integrations | Project leadership, API development, data strategy |
| Saad & Sahil       | EDA + Feature Engineering    | Data cleaning, feature creation, exploration       |
| Sneha & Sucharita  | Modeling + Evaluation        | Model building, validation, and tuning              |
| Val & Faiz         | Visualization + Reporting    | Creating visuals, reports, and presentations        |


>>>>>>> 804fdd5ffc11025b1a7a4ad3a77889966f0e7142
---