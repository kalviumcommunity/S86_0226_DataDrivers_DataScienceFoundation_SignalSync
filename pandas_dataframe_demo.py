"""
Pandas DataFrame Fundamentals Demo
===================================
This module demonstrates the creation and inspection of Pandas DataFrames.

Learning Objectives:
1. Understand what a Pandas DataFrame represents
2. Create DataFrames from Python dictionaries
3. Load DataFrames from files (CSV)
4. Inspect DataFrame structure and contents
5. Recognize common patterns and issues
"""

import pandas as pd
import numpy as np
import os

print("=" * 70)
print("PANDAS DATAFRAME FUNDAMENTALS")
print("=" * 70)
print()

# ==============================================================================
# 1. UNDERSTANDING PANDAS DATAFRAMES
# ==============================================================================
print("1. UNDERSTANDING PANDAS DATAFRAMES")
print("-" * 70)
print("A Pandas DataFrame is a two-dimensional labeled data structure.")
print("Think of it as:")
print("  - A spreadsheet or table")
print("  - A SQL database table")
print("  - A collection of Series objects sharing the same index")
print()

print("Key Components of a DataFrame:")
print("  - Rows: Individual records (observations)")
print("  - Columns: Variables or features")
print("  - Index: Row labels (often numeric)")
print("  - Column Names: Headers for each column")
print()

# Creating a simple DataFrame to demonstrate
simple_df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Mumbai', 'Delhi', 'Bangalore']
})

print("Example DataFrame:")
print(simple_df)
print()
print("Structure:")
print("  - 3 rows (index: 0, 1, 2)")
print("  - 3 columns (Name, Age, City)")
print("  - Each column is like a Pandas Series")
print()

# ==============================================================================
# 2. CREATING DATAFRAMES FROM DICTIONARIES
# ==============================================================================
print("=" * 70)
print("2. CREATING DATAFRAMES FROM DICTIONARIES")
print("-" * 70)

# Pattern 1: Dictionary with lists (column-oriented)
print("Pattern 1: Dictionary with Lists (Most Common)")
print("-" * 70)

traffic_data = {
    'hour': [8, 9, 10, 11, 12],
    'traffic_volume': [850, 650, 580, 620, 680],
    'day': ['Monday', 'Monday', 'Monday', 'Monday', 'Monday'],
    'temperature': [23, 25, 27, 28, 29]
}

traffic_df = pd.DataFrame(traffic_data)
print("Traffic Data DataFrame:")
print(traffic_df)
print()
print("Note: Each dictionary key becomes a column name")
print("      Each list becomes the values for that column")
print()

# Pattern 2: List of dictionaries (row-oriented)
print("Pattern 2: List of Dictionaries (Row-Oriented)")
print("-" * 70)

students = [
    {'name': 'Aarav', 'math': 85, 'science': 92},
    {'name': 'Diya', 'math': 92, 'science': 88},
    {'name': 'Arjun', 'math': 78, 'science': 85}
]

students_df = pd.DataFrame(students)
print("Students DataFrame:")
print(students_df)
print()
print("Note: Each dictionary becomes a row")
print("      Keys become column names")
print()

# Pattern 3: Dictionary with custom index
print("Pattern 3: DataFrame with Custom Index")
print("-" * 70)

products_data = {
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'price': [75000, 500, 1200, 15000],
    'stock': [25, 150, 80, 40]
}

products_df = pd.DataFrame(products_data, index=[
                           'P001', 'P002', 'P003', 'P004'])
print("Products DataFrame with Custom Index:")
print(products_df)
print()
print("Note: Custom index labels replace default 0, 1, 2, 3")
print()

# Pattern 4: From NumPy arrays
print("Pattern 4: DataFrame from NumPy Array")
print("-" * 70)

np.random.seed(42)
random_data = np.random.randint(10, 100, size=(4, 3))
random_df = pd.DataFrame(
    random_data,
    columns=['Column_A', 'Column_B', 'Column_C'],
    index=['Row_1', 'Row_2', 'Row_3', 'Row_4']
)

print("Random Data DataFrame:")
print(random_df)
print()
print("Note: Specify both columns and index explicitly")
print()

# ==============================================================================
# 3. LOADING DATAFRAMES FROM FILES
# ==============================================================================
print("=" * 70)
print("3. LOADING DATAFRAMES FROM FILES")
print("-" * 70)

# Determine the correct path to data files
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, 'data', 'raw')

# Loading from CSV
print("Loading DataFrame from CSV File")
print("-" * 70)

csv_file = os.path.join(data_path, 'sample_traffic_data.csv')

if os.path.exists(csv_file):
    traffic_csv_df = pd.read_csv(csv_file)
    print(f"Successfully loaded: {csv_file}")
    print()
    print("First few rows of the loaded data:")
    print(traffic_csv_df.head())
    print()
    print("Key Points:")
    print("  - pd.read_csv() automatically reads the file")
    print("  - First row is used as column names (header)")
    print("  - Index is created automatically (0, 1, 2, ...)")
    print()
else:
    print(f"Note: Sample file not found at {csv_file}")
    print("Creating sample data for demonstration...")
    traffic_csv_df = pd.DataFrame({
        'hour': list(range(24)),
        'traffic_volume': [150, 85, 45, 30, 25, 40, 120, 450, 850, 650,
                           580, 620, 680, 700, 720, 780, 920, 1050,
                           950, 680, 450, 320, 220, 180],
        'day_of_week': ['Monday'] * 24,
        'temperature': [22, 20, 18, 17, 16, 17, 18, 20, 23, 25,
                        27, 28, 29, 30, 29, 28, 27, 26, 24, 22, 21, 20, 19, 18]
    })
    print(traffic_csv_df.head())
    print()

# Common read_csv parameters
print("Common pd.read_csv() Parameters:")
print("-" * 70)
print("""
pd.read_csv('file.csv')                    # Basic usage
pd.read_csv('file.csv', sep=',')           # Specify delimiter
pd.read_csv('file.csv', header=0)          # Header row (default: 0)
pd.read_csv('file.csv', index_col=0)       # Use first column as index
pd.read_csv('file.csv', nrows=100)         # Read only first 100 rows
pd.read_csv('file.csv', skiprows=2)        # Skip first 2 rows
pd.read_csv('file.csv', usecols=['A','B']) # Read specific columns
""")
print()

# ==============================================================================
# 4. INSPECTING DATAFRAME STRUCTURE
# ==============================================================================
print("=" * 70)
print("4. INSPECTING DATAFRAME STRUCTURE")
print("-" * 70)

# Create a sample DataFrame for inspection
inspection_df = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5],
    'name': ['Aarav', 'Diya', 'Arjun', 'Ananya', 'Rohan'],
    'math_score': [85, 92, 78, 95, 88],
    'science_score': [92, 88, 85, 90, 87],
    'english_score': [78, 95, 82, 88, 90]
})

print("Sample DataFrame for Inspection:")
print(inspection_df)
print()
print()

# Method 1: head() and tail()
print("Method 1: View First and Last Rows")
print("-" * 70)
print("df.head() - First 5 rows (default):")
print(inspection_df.head())
print()
print("df.head(3) - First 3 rows:")
print(inspection_df.head(3))
print()
print("df.tail(2) - Last 2 rows:")
print(inspection_df.tail(2))
print()

# Method 2: Shape
print("Method 2: DataFrame Shape")
print("-" * 70)
print(f"df.shape: {inspection_df.shape}")
print(f"  → {inspection_df.shape[0]} rows")
print(f"  → {inspection_df.shape[1]} columns")
print()

# Method 3: Columns
print("Method 3: Column Names")
print("-" * 70)
print(f"df.columns: {inspection_df.columns.tolist()}")
print()

# Method 4: Index
print("Method 4: Index")
print("-" * 70)
print(f"df.index: {inspection_df.index.tolist()}")
print()

# Method 5: Data Types
print("Method 5: Data Types")
print("-" * 70)
print("df.dtypes:")
print(inspection_df.dtypes)
print()
print("Explanation:")
print("  - int64: Integer numbers")
print("  - float64: Decimal numbers")
print("  - object: Strings or mixed types")
print()

# Method 6: info()
print("Method 6: Comprehensive Info")
print("-" * 70)
print("df.info():")
inspection_df.info()
print()
print("Provides:")
print("  - Number of rows and columns")
print("  - Column names and data types")
print("  - Non-null counts (helps identify missing data)")
print("  - Memory usage")
print()

# Method 7: describe()
print("Method 7: Statistical Summary")
print("-" * 70)
print("df.describe() - Summary statistics for numeric columns:")
print(inspection_df.describe())
print()
print("Shows: count, mean, std, min, 25%, 50%, 75%, max")
print()

# Method 8: Accessing specific columns
print("Method 8: Accessing Specific Columns")
print("-" * 70)
print("df['column_name'] - Single column (returns Series):")
print(inspection_df['name'])
print()
print("df[['col1', 'col2']] - Multiple columns (returns DataFrame):")
print(inspection_df[['name', 'math_score']])
print()

# Method 9: Accessing specific rows
print("Method 9: Accessing Specific Rows")
print("-" * 70)
print("df.loc[0] - Row by index label:")
print(inspection_df.loc[0])
print()
print("df.iloc[0] - Row by integer position:")
print(inspection_df.iloc[0])
print()
print("df.loc[0:2] - Multiple rows by label:")
print(inspection_df.loc[0:2])
print()

# ==============================================================================
# 5. COMMON DATAFRAME OPERATIONS
# ==============================================================================
print("=" * 70)
print("5. COMMON DATAFRAME OPERATIONS")
print("-" * 70)

# Adding a new column
print("Adding a New Column:")
print("-" * 70)
inspection_df['total_score'] = (inspection_df['math_score'] +
                                inspection_df['science_score'] +
                                inspection_df['english_score'])
print("df['total_score'] = df['math'] + df['science'] + df['english']")
print(inspection_df)
print()

# Filtering rows
print("Filtering Rows:")
print("-" * 70)
high_performers = inspection_df[inspection_df['total_score'] > 260]
print("Students with total_score > 260:")
print(high_performers)
print()

# Sorting
print("Sorting Data:")
print("-" * 70)
sorted_df = inspection_df.sort_values('total_score', ascending=False)
print("Sorted by total_score (descending):")
print(sorted_df)
print()

# ==============================================================================
# 6. DATAFRAME VS SERIES COMPARISON
# ==============================================================================
print("=" * 70)
print("6. DATAFRAME VS SERIES COMPARISON")
print("-" * 70)

comparison_data = {
    'Aspect': ['Dimensions', 'Structure', 'Indexing', 'Use Case', 'Access'],
    'Series': ['1D', 'Single column', 'Single index', 'Single variable', 'series[index]'],
    'DataFrame': ['2D', 'Multiple columns', 'Row & column', 'Multiple variables', 'df[column][row]']
}
comparison_df = pd.DataFrame(comparison_data)
print(comparison_df.to_string(index=False))
print()

print("Key Insight:")
print("  → A DataFrame is a collection of Series that share the same index")
print("  → Each column in a DataFrame is a Series")
print()

# Demonstrate this
print("Example - Extracting a column as a Series:")
print(f"Type of DataFrame: {type(inspection_df)}")
print(f"Type of a column: {type(inspection_df['name'])}")
print()

# ==============================================================================
# 7. COMMON ISSUES AND SOLUTIONS
# ==============================================================================
print("=" * 70)
print("7. COMMON ISSUES AND SOLUTIONS")
print("-" * 70)

print("""
Issue 1: File Not Found Error
├─ Problem: pd.read_csv('data.csv') fails
└─ Solution: Check file path or use absolute path

Issue 2: Mismatched Dictionary Lengths
├─ Problem: {'A': [1, 2], 'B': [1, 2, 3]} → ValueError
└─ Solution: Ensure all lists have the same length

Issue 3: Wrong Data Types
├─ Problem: Numbers loaded as strings
└─ Solution: Use dtype parameter or convert after loading

Issue 4: Missing Column Names
├─ Problem: First row treated as data instead of header
└─ Solution: Use header=0 parameter or names=['col1', 'col2']

Issue 5: Index Issues
├─ Problem: Unexpected index values after filtering
└─ Solution: Use df.reset_index(drop=True) to reset

Issue 6: Memory Issues with Large Files
├─ Problem: Cannot load entire file into memory
└─ Solution: Use chunksize or nrows parameter
""")

# ==============================================================================
# 8. DATAFRAME CREATION QUICK REFERENCE
# ==============================================================================
print("=" * 70)
print("8. DATAFRAME CREATION QUICK REFERENCE")
print("-" * 70)

print("""
From Dictionary of Lists:
  df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

From List of Dictionaries:
  df = pd.DataFrame([{'A': 1, 'B': 4}, {'A': 2, 'B': 5}])

From NumPy Array:
  df = pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['A', 'B'])

From CSV File:
  df = pd.read_csv('file.csv')

From Excel File:
  df = pd.read_excel('file.xlsx')

With Custom Index:
  df = pd.DataFrame(data, index=['R1', 'R2', 'R3'])

Inspection Methods:
  df.head()          # First 5 rows
  df.tail()          # Last 5 rows
  df.shape           # (rows, columns)
  df.columns         # Column names
  df.dtypes          # Data types
  df.info()          # Summary info
  df.describe()      # Statistics
""")

print("=" * 70)
print("DEMO COMPLETE - You're ready to work with Pandas DataFrames!")
print("=" * 70)
