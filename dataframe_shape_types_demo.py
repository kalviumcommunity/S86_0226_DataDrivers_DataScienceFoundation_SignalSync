"""
Milestone: Understanding Data Shapes and Column Data Types

This script demonstrates:
1. Understanding DataFrame shape
2. Understanding rows and columns
3. Understanding column data types
4. Detecting type-related issues
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("MILESTONE: Understanding DataFrame Shapes and Column Data Types")
print("=" * 80)

# =============================================================================
# 1. UNDERSTANDING DATAFRAME SHAPE
# =============================================================================
print("\n" + "=" * 80)
print("1. UNDERSTANDING DATAFRAME SHAPE")
print("=" * 80)

# Load a sample dataset
df_students = pd.read_csv('data/raw/students_scores.csv')

print("\n--- Loading Students Scores Dataset ---")
print("Dataset preview:")
print(df_students.head())

# Inspect the shape
print("\n--- Inspecting Shape ---")
print(f"DataFrame shape: {df_students.shape}")
print(f"Shape returns a tuple: (rows, columns)")
print(f"Number of rows: {df_students.shape[0]}")
print(f"Number of columns: {df_students.shape[1]}")

print("\n--- What Does Shape Tell Us? ---")
print(
    f"This dataset has {df_students.shape[0]} students (observations/records)")
print(
    f"Each student has {df_students.shape[1]} attributes (features/variables)")
print("Shape gives us the dimensions of our data - how much data we're working with")

# =============================================================================
# 2. UNDERSTANDING ROWS AND COLUMNS
# =============================================================================
print("\n" + "=" * 80)
print("2. UNDERSTANDING ROWS AND COLUMNS")
print("=" * 80)

print("\n--- Rows (Observations) ---")
print(f"Total observations: {df_students.shape[0]}")
print("Each row represents: one student's complete record")
print("Rows are accessed by index (0, 1, 2, ...)")

print("\n--- Columns (Features/Variables) ---")
print(f"Total features: {df_students.shape[1]}")
print("Column names:")
for i, col in enumerate(df_students.columns):
    print(f"  {i}. {col}")
print("\nEach column represents: a specific attribute measured for all students")
print("Columns are accessed by name or index")

# Load traffic data for comparison
df_traffic = pd.read_csv('data/raw/sample_traffic_data.csv')

print("\n--- Comparing Different Dataset Shapes ---")
print(f"Students dataset: {df_students.shape} (rows, columns)")
print(f"Traffic dataset: {df_traffic.shape} (rows, columns)")
print(f"\nInterpretation:")
print(
    f"- Students: {df_students.shape[0]} students with {df_students.shape[1]} attributes each")
print(
    f"- Traffic: {df_traffic.shape[0]} hourly measurements with {df_traffic.shape[1]} variables each")

# =============================================================================
# 3. UNDERSTANDING COLUMN DATA TYPES
# =============================================================================
print("\n" + "=" * 80)
print("3. UNDERSTANDING COLUMN DATA TYPES")
print("=" * 80)

print("\n--- Inspecting Data Types ---")
print("Data types for Students dataset:")
print(df_students.dtypes)

print("\n--- Common Pandas Data Types ---")
print("int64:    Integer numbers (whole numbers)")
print("float64:  Floating-point numbers (decimals)")
print("object:   Text/strings or mixed types")
print("bool:     Boolean (True/False)")
print("datetime64: Date and time values")

print("\n--- Detailed Type Information ---")
print("\nUsing .info() method:")
print(df_students.info())

print("\n--- Why Data Types Matter ---")
print("✓ Numeric types (int64, float64): Can perform mathematical operations")
print("✓ Object types: Typically text, limited to string operations")
print("✓ Correct types enable correct operations")
print("✓ Wrong types cause errors or unexpected behavior")

# Load traffic sample with date_time column
df_traffic_sample = pd.read_csv('traffic_sample.csv')

print("\n--- Inspecting Traffic Sample Data Types ---")
print(df_traffic_sample.dtypes)

print("\n--- Column-by-Column Type Analysis ---")
for col in df_traffic_sample.columns:
    dtype = df_traffic_sample[col].dtype
    print(f"\n{col}:")
    print(f"  Type: {dtype}")
    print(f"  Sample values: {df_traffic_sample[col].head(3).tolist()}")

    if dtype == 'object':
        print(f"  → This is text/categorical data")
    elif dtype in ['int64', 'float64']:
        print(f"  → This is numeric data (can do math)")

# =============================================================================
# 4. DETECTING TYPE-RELATED ISSUES
# =============================================================================
print("\n" + "=" * 80)
print("4. DETECTING TYPE-RELATED ISSUES")
print("=" * 80)

print("\n--- Common Type Issues ---")

# Issue 1: Numeric data stored as strings
print("\n--- Issue 1: Numeric Data Stored as Object (String) ---")
# Create a problematic dataset
problematic_data = {
    # Should be int, but stored as string
    'student_id': ['1', '2', '3', '4', '5'],
    # Should be numeric, but stored as string
    'score': ['85', '92', '78', '95', '88'],
    'grade': ['A', 'A', 'B', 'A', 'B']
}
df_problem = pd.DataFrame(problematic_data)

print("Problematic dataset:")
print(df_problem.head())
print("\nData types:")
print(df_problem.dtypes)

print("\n⚠ PROBLEM DETECTED:")
print("'student_id' and 'score' are stored as 'object' (string) type")
print("They look like numbers but are actually text!")

print("\nWhy this is a problem:")
try:
    avg_score = df_problem['score'].mean()
    print(f"Average score: {avg_score}")
except Exception as e:
    print(f"❌ Error when trying to calculate mean: {type(e).__name__}")
    print("   Cannot perform numeric operations on string data!")

print("\nHow to detect:")
print("- Check dtypes: numeric-looking columns should be int64/float64, not object")
print("- Try operations: if math operations fail, check the type")

# Issue 2: Missing values affecting types
print("\n--- Issue 2: Missing Values Affecting Types ---")
data_with_nulls = {
    'temperature': [22, 20, np.nan, 17, 16],
    'humidity': ['45', '50', '48', 'N/A', '52']  # Mixed numeric and text
}
df_nulls = pd.DataFrame(data_with_nulls)

print("Dataset with missing/invalid values:")
print(df_nulls)
print("\nData types:")
print(df_nulls.dtypes)

print("\n⚠ PROBLEM DETECTED:")
print("'humidity' contains numbers but is object type due to 'N/A' text value")
print("Missing values can force numeric columns to become object type")

# Issue 3: Date stored as string
print("\n--- Issue 3: Date/Time Data Stored as String ---")
print("\nTraffic sample date_time column:")
print(f"Type: {df_traffic_sample['date_time'].dtype}")
print(f"Sample value: {df_traffic_sample['date_time'].iloc[0]}")

print("\n⚠ PROBLEM DETECTED:")
print("'date_time' is stored as object (string), not datetime64")
print("Cannot perform time-based operations (extract month, calculate duration, etc.)")

print("\n--- Early Detection Checklist ---")
print("After loading, ALWAYS check:")
print("✓ DataFrame shape - how much data do you have?")
print("✓ Column data types - are they correct?")
print("✓ Numeric columns - should be int64/float64, not object")
print("✓ Date columns - should be datetime64, not object")
print("✓ Suspicious object types - may contain hidden issues")

# =============================================================================
# 5. BEST PRACTICES SUMMARY
# =============================================================================
print("\n" + "=" * 80)
print("5. BEST PRACTICES SUMMARY")
print("=" * 80)

print("\n--- Essential Commands ---")
print("df.shape          → Get (rows, columns) tuple")
print("df.shape[0]       → Get number of rows")
print("df.shape[1]       → Get number of columns")
print("df.dtypes         → Get all column data types")
print("df.info()         → Get comprehensive type and null info")
print("df[column].dtype  → Get specific column type")

print("\n--- Always Do This After Loading Data ---")
print("1. Check shape: Know how much data you have")
print("2. Check dtypes: Verify columns have correct types")
print("3. Look for object types in numeric columns: Red flag!")
print("4. Use info(): Quick overview of structure and types")
print("5. Inspect sample values: Visual verification")

print("\n--- Why This Matters ---")
print("• Prevents downstream errors and bugs")
print("• Ensures operations behave as expected")
print("• Saves debugging time later")
print("• Enables confident data analysis")
print("• Foundation for all data science work")

print("\n" + "=" * 80)
print("Understanding data shapes and types is the FIRST STEP in any data project!")
print("=" * 80)
