"""
CSV Data Loading Demonstration Script
SignalSync Project - Data Drivers Team

This script demonstrates how to load CSV files into Pandas DataFrames,
inspect loaded data, and identify common loading issues.
"""

import pandas as pd
import os

# Print header
print("=" * 70)
print("CSV DATA LOADING DEMONSTRATION")
print("SignalSync Project - Data Drivers Team")
print("=" * 70)
print()

# ==============================================================================
# PART 1: Understanding CSV Files
# ==============================================================================
print("PART 1: UNDERSTANDING CSV FILES")
print("-" * 70)
print("CSV (Comma-Separated Values) files contain tabular data where:")
print("  - Each row represents a record")
print("  - Each column represents a field/feature")
print("  - The first row typically contains column headers")
print("  - Values are separated by commas (or other delimiters)")
print()
print("Think of CSV files as simplified spreadsheet tables.")
print()

# ==============================================================================
# PART 2: Loading CSV Files into Pandas
# ==============================================================================
print("PART 2: LOADING CSV FILES INTO PANDAS")
print("-" * 70)

# Check if file exists
csv_file = 'traffic_sample.csv'
if os.path.exists(csv_file):
    print(f"✓ File '{csv_file}' found")
    print()
    
    # Load CSV file into DataFrame
    print(f"Loading '{csv_file}' into a DataFrame...")
    traffic_df = pd.read_csv(csv_file)
    print("✓ CSV loaded successfully!")
    print()
    
else:
    print(f"✗ File '{csv_file}' not found in current directory")
    print("Please ensure the CSV file is in the same folder as this script.")
    print()

# ==============================================================================
# PART 3: Inspecting Loaded Data
# ==============================================================================
print("PART 3: INSPECTING LOADED DATA")
print("-" * 70)
print("Always inspect data after loading to verify it loaded correctly.")
print()

# Show basic information
print("3.1 DataFrame Shape (rows, columns):")
print(f"    Shape: {traffic_df.shape}")
print(f"    → {traffic_df.shape[0]} rows (records)")
print(f"    → {traffic_df.shape[1]} columns (features)")
print()

# Show column names
print("3.2 Column Names:")
print(f"    {list(traffic_df.columns)}")
print()

# Preview first few rows
print("3.3 First 5 Rows (head):")
print(traffic_df.head())
print()

# Preview last few rows
print("3.4 Last 3 Rows (tail):")
print(traffic_df.tail(3))
print()

# Show data types
print("3.5 Data Types of Each Column:")
print(traffic_df.dtypes)
print()

# Show basic statistics
print("3.6 Basic Statistical Summary:")
print(traffic_df.describe())
print()

# Show info summary
print("3.7 DataFrame Info (memory usage, non-null counts):")
print(traffic_df.info())
print()

# ==============================================================================
# PART 4: Recognizing Common Loading Issues
# ==============================================================================
print("\n" + "=" * 70)
print("PART 4: RECOGNIZING COMMON LOADING ISSUES")
print("-" * 70)
print("Loading data without inspection can lead to silent errors.")
print()

# Issue 1: CSV with different delimiter
print("ISSUE 1: Wrong Delimiter (semicolon instead of comma)")
print("-" * 70)
issues_file = 'traffic_issues.csv'
if os.path.exists(issues_file):
    print(f"Loading '{issues_file}' with default comma delimiter...")
    
    # Load incorrectly (wrong delimiter)
    wrong_df = pd.read_csv(issues_file)
    print("DataFrame loaded, but let's check the columns:")
    print(f"Columns: {list(wrong_df.columns)}")
    print()
    print("⚠ PROBLEM: All data is in one column because we used the wrong delimiter!")
    print()
    print("First few rows:")
    print(wrong_df.head())
    print()
    
    # Load correctly with proper delimiter
    print("Now loading with correct delimiter (semicolon):")
    correct_df = pd.read_csv(issues_file, delimiter=';')
    print(f"Columns: {list(correct_df.columns)}")
    print()
    print("✓ FIXED: Data is now properly separated into columns")
    print()
    print("First few rows:")
    print(correct_df.head())
    print()
else:
    print(f"File '{issues_file}' not found")
    print()

# Issue 2: CSV without headers
print("ISSUE 2: CSV File Without Header Row")
print("-" * 70)
no_header_file = 'traffic_no_header.csv'
if os.path.exists(no_header_file):
    print(f"Loading '{no_header_file}' with default settings...")
    
    # Load incorrectly (treats first row as header)
    wrong_header_df = pd.read_csv(no_header_file)
    print("DataFrame loaded, but check the columns:")
    print(f"Columns: {list(wrong_header_df.columns)}")
    print()
    print("⚠ PROBLEM: First data row became column names!")
    print()
    print("First few rows:")
    print(wrong_header_df.head())
    print()
    
    # Load correctly without header
    print("Now loading with header=None and specifying column names:")
    correct_header_df = pd.read_csv(no_header_file, 
                                     header=None, 
                                     names=['date_time', 'traffic_volume', 'temp', 'weather_main'])
    print(f"Columns: {list(correct_header_df.columns)}")
    print()
    print("✓ FIXED: Proper column names assigned, all data rows preserved")
    print()
    print("First few rows:")
    print(correct_header_df.head())
    print()
else:
    print(f"File '{no_header_file}' not found")
    print()

# ==============================================================================
# PART 5: Key Takeaways
# ==============================================================================
print("=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. ALWAYS inspect data after loading
   → Use .head(), .tail(), .info(), .describe()
   → Check shape, columns, and data types

2. COMMON CSV LOADING ISSUES:
   → Wrong delimiter (use delimiter parameter)
   → Missing or incorrect headers (use header parameter)
   → Wrong file path (use os.path.exists() to check)
   → Data type mismatches (inspect with .dtypes)
   → Missing values (check with .info() or .isnull())

3. BEST PRACTICES:
   → Preview the CSV file before loading
   → Verify file path is correct
   → Check column names match expectations
   → Confirm row count is reasonable
   → Look for unexpected null values

4. PANDAS LOADING METHODS:
   → pd.read_csv('file.csv')              # Basic loading
   → pd.read_csv('file.csv', delimiter=';')  # Custom delimiter
   → pd.read_csv('file.csv', header=None)    # No header row
   → pd.read_csv('file.csv', names=[...])    # Custom column names

5. DATA LOADING IS THE FOUNDATION:
   → Most downstream errors begin with incorrect loading
   → Early inspection prevents silent failures
   → Correct loading ensures reliable analysis
""")

print("=" * 70)
print("CSV LOADING DEMONSTRATION COMPLETE")
print("=" * 70)
print()
print("Next Steps:")
print("  1. Practice loading your own CSV files")
print("  2. Always inspect data structure after loading")
print("  3. Handle common issues confidently")
print("  4. Build reliable data pipelines")
print()
