"""
🚦 ## Step 2: Data Pipeline

### 2.1 Data Cleaning to Data > Raw > [Package-format_converted-cleaned]

Location: src/pipeline/data_cleaning.py

This script:
- Reads CSV files from converted raw folder: data/raw/<package_name>-format_converted/
- Cleans data by removing duplicates, trimming whitespace, standardizing column names
- Handles errors robustly with logging
- Saves cleaned CSV files to processed folder: data/processed/<package_name>/

Ensure you update PACKAGE_NAME before running.
"""

import os
from pathlib import Path
import pandas as pd

def clean_data_file(input_path: Path, output_path: Path):
    """
    Basic cleaning:
    - Remove duplicates
    - Strip whitespace from string columns
    - Standardize columns to lowercase snake_case (example)
    - Save cleaned CSV
    """
    print(f"Cleaning file: {input_path.name}")

    df = pd.read_csv(input_path)

    # Drop duplicates
    df = df.drop_duplicates()

    # Strip whitespace from string columns
    str_cols = df.select_dtypes(include=['object']).columns
    for col in str_cols:
        df[col] = df[col].str.strip()

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Save cleaned file
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned file to: {output_path}")

def run_data_cleaning():
    raw_dir = Path("data/raw")
    processed_dir = Path("data/processed")

    # Look for all folders matching *-format_converted under raw_dir
    for raw_subdir in raw_dir.glob("*-format_converted"):
        package_name = raw_subdir.name  # e.g. 'ttc-subway-delay-data-format_converted'
        print(f"\nProcessing package folder: {package_name}")

        # Define processed output folder, e.g. data/processed/ttc-subway-delay-data-format_converted-clean
        processed_subdir = processed_dir / f"{package_name}-clean"
        if not processed_subdir.exists():
            processed_subdir.mkdir(parents=True)
            print(f"Created processed folder: {processed_subdir}")
        else:
            print(f"Processed folder already exists: {processed_subdir}")

        # Process each CSV file in raw_subdir
        for csv_file in raw_subdir.glob("*.csv"):
            output_file = processed_subdir / csv_file.name

            if output_file.exists():
                # Ask user to overwrite
                answer = input(f"Cleaned file '{output_file.name}' exists. Overwrite? (y/n): ").strip().lower()
                if answer != 'y':
                    print(f"Skipping {output_file.name}")
                    continue

            try:
                clean_data_file(csv_file, output_file)
            except Exception as e:
                print(f"Error cleaning file {csv_file.name}: {e}")

if __name__ == "__main__":
    run_data_cleaning()
# Ensure you have the required packages installed
# conda install pandas scikit-learn