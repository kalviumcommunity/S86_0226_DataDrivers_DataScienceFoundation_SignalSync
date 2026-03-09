"""
DataFrame Inspection Demonstration Script
SignalSync Project - Data Drivers Team

This script demonstrates how to inspect Pandas DataFrames using head(), info(), 
and describe() methods to understand data structure, types, and quality.
"""

import pandas as pd
import os

# Print header
print("=" * 70)
print("PANDAS DATAFRAME INSPECTION DEMONSTRATION")
print("SignalSync Project - Data Drivers Team")
print("=" * 70)
print()

# ==============================================================================
# LOAD SAMPLE DATA
# ==============================================================================
print("LOADING SAMPLE DATA")
print("-" * 70)

csv_file = 'traffic_sample.csv'
if os.path.exists(csv_file):
    print(f"✓ Loading '{csv_file}'...")
    traffic_df = pd.read_csv(csv_file)
    print(f"✓ Data loaded successfully!")
    print()
else:
    print(f"✗ File '{csv_file}' not found")
    print("Please ensure the CSV file is in the same folder as this script.")
    exit()

# ==============================================================================
# PART 1: Inspecting Data with head()
# ==============================================================================
print("=" * 70)
print("PART 1: INSPECTING DATA WITH head()")
print("-" * 70)
print("The head() method shows the first few rows of a DataFrame.")
print("This gives you a quick visual preview of your data.")
print()

# Default head() - first 5 rows
print("1.1 Using head() - Default (first 5 rows):")
print("-" * 70)
print(traffic_df.head())
print()

# Custom number of rows
print("1.2 Using head(3) - First 3 rows:")
print("-" * 70)
print(traffic_df.head(3))
print()

# Custom number of rows
print("1.3 Using head(10) - First 10 rows:")
print("-" * 70)
print(traffic_df.head(10))
print()

print("WHAT head() REVEALS:")
print("  ✓ Column names at the top")
print("  ✓ Sample values in each column")
print("  ✓ Data alignment across columns")
print("  ✓ Basic data patterns at a glance")
print("  ✓ Index values (row numbers)")
print()

print("WHEN TO USE head():")
print("  → After loading data for the first time")
print("  → After data transformations to verify changes")
print("  → To quickly check if data makes sense visually")
print("  → To show examples of your dataset")
print()

# ==============================================================================
# PART 2: Inspecting Structure with info()
# ==============================================================================
print("=" * 70)
print("PART 2: INSPECTING STRUCTURE WITH info()")
print("-" * 70)
print("The info() method provides a concise summary of DataFrame structure.")
print("It shows data types, non-null counts, and memory usage.")
print()

print("2.1 Using info():")
print("-" * 70)
traffic_df.info()
print()

print("WHAT info() REVEALS:")
print("  ✓ Total number of rows (RangeIndex)")
print("  ✓ Total number of columns")
print("  ✓ Column names")
print("  ✓ Data type of each column (int64, float64, object, etc.)")
print("  ✓ Non-null count (how many values are NOT missing)")
print("  ✓ Memory usage of the DataFrame")
print()

print("INTERPRETING DATA TYPES:")
print("  → int64: Integer numbers (whole numbers)")
print("  → float64: Floating-point numbers (decimals)")
print("  → object: Text strings or mixed types")
print("  → datetime64: Date and time values (after conversion)")
print("  → bool: Boolean (True/False) values")
print()

print("WHEN TO USE info():")
print("  → To check if columns loaded with correct data types")
print("  → To identify missing values (non-null count < total rows)")
print("  → To understand memory consumption")
print("  → To plan data type conversions")
print()

# Let's examine data types more closely
print("2.2 Detailed Column Data Types:")
print("-" * 70)
print(traffic_df.dtypes)
print()

# Check for missing values
print("2.3 Checking for Missing Values:")
print("-" * 70)
print("Missing values per column:")
print(traffic_df.isnull().sum())
print()
print(f"Total missing values: {traffic_df.isnull().sum().sum()}")
print()

# ==============================================================================
# PART 3: Summarizing Data with describe()
# ==============================================================================
print("=" * 70)
print("PART 3: SUMMARIZING DATA WITH describe()")
print("-" * 70)
print("The describe() method generates statistical summaries for numeric columns.")
print("It provides key statistics like mean, min, max, and percentiles.")
print()

print("3.1 Using describe():")
print("-" * 70)
print(traffic_df.describe())
print()

print("WHAT describe() REVEALS:")
print("  ✓ count: Number of non-null values")
print("  ✓ mean: Average value")
print("  ✓ std: Standard deviation (spread of data)")
print("  ✓ min: Minimum value")
print("  ✓ 25%: First quartile (25th percentile)")
print("  ✓ 50%: Median (middle value)")
print("  ✓ 75%: Third quartile (75th percentile)")
print("  ✓ max: Maximum value")
print()

print("INTERPRETING THE STATISTICS:")
print("-" * 70)
print(f"Traffic Volume Analysis:")
print(f"  → Average traffic: {traffic_df['traffic_volume'].mean():.2f} vehicles")
print(f"  → Minimum traffic: {traffic_df['traffic_volume'].min()} vehicles")
print(f"  → Maximum traffic: {traffic_df['traffic_volume'].max()} vehicles")
print(f"  → Median traffic: {traffic_df['traffic_volume'].median():.2f} vehicles")
print(f"  → Traffic range: {traffic_df['traffic_volume'].max() - traffic_df['traffic_volume'].min()} vehicles")
print()

print(f"Temperature Analysis:")
print(f"  → Average temperature: {traffic_df['temp'].mean():.2f}°F")
print(f"  → Temperature range: {traffic_df['temp'].min():.2f}°F to {traffic_df['temp'].max():.2f}°F")
print(f"  → Temperature spread (std): {traffic_df['temp'].std():.2f}°F")
print()

print("3.2 Describing All Columns (including non-numeric):")
print("-" * 70)
print(traffic_df.describe(include='all'))
print()

print("WHEN TO USE describe():")
print("  → To understand the distribution of numeric data")
print("  → To spot potential outliers (very high/low values)")
print("  → To check if data ranges make sense")
print("  → To get quick statistical context before analysis")
print()

# ==============================================================================
# PART 4: Knowing When to Use Each Method
# ==============================================================================
print("=" * 70)
print("PART 4: KNOWING WHEN TO USE EACH METHOD")
print("-" * 70)
print("""
Each inspection method answers a different question:

┌──────────────┬──────────────────────────────────────────────────────┐
│ METHOD       │ WHAT IT ANSWERS                                      │
├──────────────┼──────────────────────────────────────────────────────┤
│ head()       │ "What does the data look like?"                      │
│              │ → Shows you actual data values                       │
│              │ → Visual confirmation of structure                   │
│              │ → Quick sanity check                                 │
├──────────────┼──────────────────────────────────────────────────────┤
│ info()       │ "How is the DataFrame structured?"                   │
│              │ → Column names and data types                        │
│              │ → Missing value detection                            │
│              │ → Memory usage                                       │
├──────────────┼──────────────────────────────────────────────────────┤
│ describe()   │ "What are the numeric patterns?"                     │
│              │ → Statistical summary                                │
│              │ → Data distribution overview                         │
│              │ → Outlier detection hints                            │
└──────────────┴──────────────────────────────────────────────────────┘
""")

# ==============================================================================
# PART 5: Complete Inspection Workflow
# ==============================================================================
print("=" * 70)
print("PART 5: COMPLETE INSPECTION WORKFLOW")
print("-" * 70)
print("A complete inspection should include all three methods:")
print()

print("STEP 1: Check Shape")
print(f"  → DataFrame shape: {traffic_df.shape}")
print(f"  → {traffic_df.shape[0]} rows × {traffic_df.shape[1]} columns")
print()

print("STEP 2: Preview with head()")
print(traffic_df.head(3))
print()

print("STEP 3: Check structure with info()")
traffic_df.info()
print()

print("STEP 4: Get statistics with describe()")
print(traffic_df.describe())
print()

print("STEP 5: Additional Checks")
print("-" * 70)
print(f"Column names: {list(traffic_df.columns)}")
print(f"Data types: \n{traffic_df.dtypes}")
print(f"Missing values: {traffic_df.isnull().sum().sum()}")
print(f"Duplicate rows: {traffic_df.duplicated().sum()}")
print()

# ==============================================================================
# PART 6: Practical Example - Detecting Issues
# ==============================================================================
print("=" * 70)
print("PART 6: PRACTICAL EXAMPLE - DETECTING ISSUES")
print("-" * 70)
print("Let's load a problematic dataset and use inspection to find issues:")
print()

# Load the issues dataset
issues_file = 'traffic_issues.csv'
if os.path.exists(issues_file):
    print(f"Loading '{issues_file}' with correct delimiter...")
    issues_df = pd.read_csv(issues_file, delimiter=';')
    print()
    
    print("INSPECTION 1: head()")
    print("-" * 70)
    print(issues_df.head())
    print()
    print("⚠ OBSERVATION: Row 2 has 'Missing Data Row Here' - not actual data!")
    print()
    
    print("INSPECTION 2: info()")
    print("-" * 70)
    issues_df.info()
    print()
    print("⚠ OBSERVATION: traffic_volume has only 4 non-null values (missing 2 values)")
    print("⚠ OBSERVATION: temp has 5 non-null values (missing 1 value)")
    print()
    
    print("INSPECTION 3: describe()")
    print("-" * 70)
    print(issues_df.describe())
    print()
    print("⚠ OBSERVATION: Count shows missing values in numeric columns")
    print()

# ==============================================================================
# KEY TAKEAWAYS
# ==============================================================================
print("=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print("""
1. ALWAYS INSPECT DATA AFTER LOADING:
   → Use head() for visual preview
   → Use info() for structure
   → Use describe() for statistics

2. WHAT EACH METHOD REVEALS:
   → head(): Sample rows and visual confirmation
   → info(): Data types, missing values, memory
   → describe(): Statistical summary of numeric columns

3. INSPECTION WORKFLOW:
   → Check shape first (.shape)
   → Preview data (head())
   → Check structure (info())
   → Get statistics (describe())
   → Look for issues (nulls, types, outliers)

4. COMMON ISSUES TO CATCH:
   → Wrong data types (numbers stored as text)
   → Missing values (NaN, null)
   → Unexpected value ranges
   → Memory problems with large datasets
   → Duplicate rows

5. BEST PRACTICES:
   → Inspect before any transformation
   → Inspect after data loading
   → Inspect after cleaning operations
   → Combine all three methods for complete understanding
   → Document what you observe

6. REMEMBER:
   → Inspection is not optional—it's essential
   → Most analysis errors start with poor inspection
   → Good inspection prevents costly mistakes
   → These methods are used in EVERY real project
""")

print("=" * 70)
print("DATAFRAME INSPECTION DEMONSTRATION COMPLETE")
print("=" * 70)
print()
print("Next Steps:")
print("  1. Practice inspecting different datasets")
print("  2. Build the habit of using all three methods")
print("  3. Learn to spot data quality issues early")
print("  4. Document your inspection findings")
print()
