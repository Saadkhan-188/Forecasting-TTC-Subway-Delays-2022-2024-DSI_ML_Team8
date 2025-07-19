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
│   ├── raw/            # Unmodified source data
│   │   ├── ttc-subway-delay-data/                  # Folder for raw downloaded files
│   │   │   ├── TTC_Subway_Delay_Data_since_2025.csv
│   │   │   ├── Code_Descriptions.xml
│   │   │   ├── ttc-subway-delay-codes.xlsx
│   │   │   └── ... (other raw CSV, XML, XLSX files)
│   │   └── ttc-subway-delay-data-format_converted/ # Converted XML/XLSX files to CSV
│   │       ├── TTC_Subway_Delay_Data_since_2025.csv
│   │       ├── Code_Descriptions.csv
│   │       └── ... (converted CSV files)
│   ├── processed/      # Cleaned and engineered datasets
│   │   └── ttc-subway-delay-data-format_converted-clean/  
│   │       ├── TTC_Subway_Delay_Data_since_2025_clean.csv
│   │       ├── Code_Descriptions_clean.csv
│   │       └── ... (cleaned CSV files)
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


