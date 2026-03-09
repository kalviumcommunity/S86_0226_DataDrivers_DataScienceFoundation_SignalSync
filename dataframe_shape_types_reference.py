"""
QUICK REFERENCE GUIDE: DataFrame Shapes and Column Data Types

This is your go-to reference for checking DataFrame structure and types.
Keep this handy while working with any dataset!
"""

import pandas as pd

# =============================================================================
# ESSENTIAL COMMANDS REFERENCE
# =============================================================================

print("=" * 80)
print("QUICK REFERENCE: DataFrame Shapes and Data Types")
print("=" * 80)

# Load example dataset
df = pd.read_csv('data/raw/students_scores.csv')

print("\n" + "=" * 80)
print("1. CHECKING SHAPE")
print("=" * 80)

print("\nCommand: df.shape")
print(f"Returns: {df.shape}")
print("Meaning: (number of rows, number of columns)")

print("\nCommand: df.shape[0]")
print(f"Returns: {df.shape[0]}")
print("Meaning: Number of rows (observations)")

print("\nCommand: df.shape[1]")
print(f"Returns: {df.shape[1]}")
print("Meaning: Number of columns (features)")

print("\n" + "=" * 80)
print("2. CHECKING COLUMN NAMES")
print("=" * 80)

print("\nCommand: df.columns")
print(f"Returns: {df.columns.tolist()}")
print("Meaning: List of all column names")

print("\nCommand: len(df.columns)")
print(f"Returns: {len(df.columns)}")
print("Meaning: Count of columns")

print("\n" + "=" * 80)
print("3. CHECKING DATA TYPES")
print("=" * 80)

print("\nCommand: df.dtypes")
print("Returns:")
print(df.dtypes)
print("\nMeaning: Data type of each column")

print("\nCommand: df['column_name'].dtype")
print(f"Example: df['student_id'].dtype")
print(f"Returns: {df['student_id'].dtype}")
print("Meaning: Data type of specific column")

print("\nCommand: df.info()")
print("Returns:")
df.info()
print("\nMeaning: Comprehensive overview with types and null counts")

print("\n" + "=" * 80)
print("4. SELECTING BY TYPE")
print("=" * 80)

print("\nCommand: df.select_dtypes(include=['int64', 'float64'])")
print("Returns: DataFrame with only numeric columns")
numeric_df = df.select_dtypes(include=['int64', 'float64'])
print(f"Numeric columns: {numeric_df.columns.tolist()}")

print("\nCommand: df.select_dtypes(include=['object'])")
print("Returns: DataFrame with only text/object columns")
object_df = df.select_dtypes(include=['object'])
print(f"Object columns: {object_df.columns.tolist()}")

print("\nCommand: df.select_dtypes(exclude=['object'])")
print("Returns: DataFrame excluding text columns (usually numeric)")
non_object_df = df.select_dtypes(exclude=['object'])
print(f"Non-object columns: {non_object_df.columns.tolist()}")

print("\n" + "=" * 80)
print("5. COMMON DATA TYPES IN PANDAS")
print("=" * 80)

print("""
Type         | Description                  | Example Values
-------------|------------------------------|------------------
int64        | Integer numbers              | 1, 42, -10, 1000
float64      | Decimal numbers              | 3.14, -0.5, 2.0
object       | Text/strings or mixed        | "Hello", "A", "123"
bool         | Boolean values               | True, False
datetime64   | Date and time               | 2023-01-01, timestamps
category     | Categorical data             | "Red", "Green", "Blue"
""")

print("\n" + "=" * 80)
print("6. QUICK DIAGNOSTIC WORKFLOW")
print("=" * 80)

print("""
STEP 1: Load data
        df = pd.read_csv('filename.csv')

STEP 2: Check shape
        print(df.shape)
        → Understand data size

STEP 3: View first rows
        print(df.head())
        → See what data looks like

STEP 4: Check types
        print(df.dtypes)
        → Verify column types

STEP 5: Get info
        df.info()
        → Comprehensive overview

STEP 6: Look for issues
        - Numeric columns showing as 'object'?
        - Date columns showing as 'object'?
        - Unexpected null values?
""")

print("\n" + "=" * 80)
print("7. COMMON TYPE ISSUES AND SOLUTIONS")
print("=" * 80)

print("""
ISSUE 1: Numeric column stored as object
Symptom:  df['price'].dtype returns 'object'
Problem:  Cannot do math operations
Check:    print(df['price'].head())
Cause:    Usually has non-numeric characters or missing values

ISSUE 2: Date column stored as object
Symptom:  df['date'].dtype returns 'object'
Problem:  Cannot do time-based operations
Check:    print(df['date'].dtype)
Solution: Use pd.to_datetime(df['date'])

ISSUE 3: Leading zeros removed
Symptom:  '001' becomes 1
Problem:  Integer type drops leading zeros
Solution: Keep as string/object type or use .astype(str)

ISSUE 4: Large integers become floats
Symptom:  Integers have .0 decimal
Cause:    Missing values force int → float
Check:    df.info() for null counts
""")

print("\n" + "=" * 80)
print("8. MEMORY TIPS")
print("=" * 80)

print("""
✓ ALWAYS check shape after loading
✓ ALWAYS check dtypes before analysis
✓ DON'T assume types are correct
✓ DON'T skip this step to save time
✓ USE .info() for quick overview
✓ VERIFY types match your expectations
✓ LOOK for 'object' on numeric columns
✓ CHECK for suspicious data types
""")

print("\n" + "=" * 80)
print("9. EXAMPLE: COMPLETE INSPECTION")
print("=" * 80)

print("\nExample code for inspecting any new dataset:")
print("""
# Load data
df = pd.read_csv('your_data.csv')

# Basic inspection
print("Shape:", df.shape)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# View data
print("\\nFirst 5 rows:")
print(df.head())

# Check types
print("\\nData types:")
print(df.dtypes)

# Comprehensive info
print("\\nDetailed info:")
df.info()

# Type summary
print("\\nNumeric columns:", df.select_dtypes(include='number').columns.tolist())
print("Text columns:", df.select_dtypes(include='object').columns.tolist())
""")

print("\n" + "=" * 80)
print("10. TROUBLESHOOTING CHECKLIST")
print("=" * 80)

print("""
When operations don't work as expected:

□ Did you check the shape?
□ Did you check column names?
□ Did you check data types?
□ Are numeric columns actually numeric?
□ Are there missing values?
□ Did you use .info() to inspect?
□ Did you view sample data with .head()?
□ Is the data format what you expected?

Most issues come from wrong data types!
""")

print("\n" + "=" * 80)
print("REFERENCE COMPLETE")
print("=" * 80)
print("\nBookmark this file for quick reference while working with DataFrames!")
