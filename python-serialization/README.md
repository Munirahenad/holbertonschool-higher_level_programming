# Python Serialization Examples

This directory includes a set of Python scripts that demonstrate common **serialization** and **deserialization** techniques using widely used data formats.

---

## Contents

### 1) JSON Serialization
- **File:** `task_00_basic_serialization.py`  
- **What it does:**
  - Serializes a Python dictionary into a JSON file
  - Loads the JSON file and deserializes it back into a dictionary
  - Uses UTF-8 encoding with basic error handling
- **Libraries used:** `json`, `os`

---

### 2) Pickling Custom Classes
- **File:** `task_01_pickle.py`  
- **What it does:**
  - Serializes and deserializes objects from a custom Python class
  - Uses the `pickle` module
  - Includes simple type checking after deserialization
- **Libraries used:** `pickle`, `os`

---

### 3) CSV to JSON Conversion
- **File:** `task_02_csv.py`  
- **What it does:**
  - Converts CSV files into JSON format
  - Validates the CSV file before converting
  - Supports Unicode characters
  - Prints basic conversion statistics
- **Libraries used:** `csv`, `json`, `os`

---

### 4) XML Serialization
- **File:** `task_03_xml.py`  
- **What it does:**
  - Serializes a Python dictionary into an XML file
  - Deserializes the XML content back into a dictionary
- **Libraries used:** `xml.etree.ElementTree`

---

## How to Run

Make sure you have **Python 3** installed, then run any script directly:

```bash
python3 filename.py

```
 ## Project Purpose

This project is designed for learning and practice in:

- Serialization and deserialization concepts  
- File handling in Python  
- Error handling  
- Working with multiple formats: **JSON**, **CSV**, **XML**, and **Pickle**
## Authors

- **Munirah Enad** — Holberton School
