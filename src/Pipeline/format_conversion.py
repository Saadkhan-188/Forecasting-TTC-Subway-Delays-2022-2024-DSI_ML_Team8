"""
Step 2: Data Pipeline  


====================================
Step 2.1: Format Conversion Script to Data > Raw > [Package-format_converted]
====================================



Converts raw XML and Excel files downloaded from CKAN
into CSV files for easier processing downstream.

Files are read from:
  data/raw/<package_name>/

Converted CSV files are saved to:
  data/raw/<package_name>-format_converted/

This script supports:
- XML files using pandas.read_xml (requires lxml or xml engine)
- Excel files (.xls, .xlsx) - converts first sheet to CSV

Developer Notes:
- Ensure dependencies installed: pandas, lxml, openpyxl
- Add support for multi-sheet Excel export if needed
"""

from pathlib import Path
import pandas as pd

# Configuration
RAW_DIR = Path("data/raw/ttc-subway-delay-data")
CONVERTED_DIR = Path(str(RAW_DIR) + "-format_converted")
CONVERTED_DIR.mkdir(parents=True, exist_ok=True)

print(f"Files found in raw folder:")
files = list(RAW_DIR.glob("*"))
for f in files:
    print(f" - {f.name} (extension: {f.suffix})")

# XML conversion function with fallback parser
def convert_xml_to_csv(xml_file: Path, output_dir: Path):
    try:
        # Try lxml parser first
        df = pd.read_xml(xml_file, parser="lxml")
    except ImportError:
        print(f"⚠️ lxml not found. Falling back to etree parser for {xml_file.name}")
        df = pd.read_xml(xml_file, parser="etree")
    except Exception as e:
        raise RuntimeError(f"Failed to parse XML {xml_file.name}: {e}")

    output_file = output_dir / (xml_file.stem + ".csv")
    df.to_csv(output_file, index=False)
    print(f"✅ Converted '{xml_file.name}' → '{output_file.name}'")

# Excel conversion function with explicit engine
def convert_excel_to_csv(excel_file: Path, output_dir: Path):
    try:
        if excel_file.suffix.lower() == ".xls":
            df = pd.read_excel(excel_file, engine="xlrd")
        else:  # .xlsx and others
            df = pd.read_excel(excel_file, engine="openpyxl")
    except Exception as e:
        raise RuntimeError(f"Failed to parse Excel {excel_file.name}: {e}")

    output_file = output_dir / (excel_file.stem + ".csv")
    df.to_csv(output_file, index=False)
    print(f"✅ Converted '{excel_file.name}' → '{output_file.name}'")

# Main processing loop
xml_files = [f for f in files if f.suffix.lower() == ".xml"]
excel_files = [f for f in files if f.suffix.lower() in [".xls", ".xlsx"]]

print(f"\nConverting {len(xml_files)} XML files to CSV:")
for xml_file in xml_files:
    try:
        convert_xml_to_csv(xml_file, CONVERTED_DIR)
    except Exception as e:
        print(f"❌ {e}")

print(f"\nConverting {len(excel_files)} Excel files to CSV:")
for excel_file in excel_files:
    try:
        convert_excel_to_csv(excel_file, CONVERTED_DIR)
    except Exception as e:
        print(f"❌ {e}")

print("\nFormat conversion step completed.")