"""
EXERCISES: Understanding DataFrame Shapes and Column Data Types

Complete these exercises to demonstrate your understanding of:
- DataFrame shape inspection
- Row and column identification
- Column data type inspection
- Type-related issue detection
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("EXERCISES: DataFrame Shapes and Column Data Types")
print("=" * 80)

# =============================================================================
# EXERCISE 1: INSPECTING SHAPE
# =============================================================================
print("\n" + "=" * 80)
print("EXERCISE 1: Inspecting DataFrame Shape")
print("=" * 80)

# Load the traffic sample dataset
df_traffic = pd.read_csv('traffic_sample.csv')

print("\nTASK: Answer the following questions about the traffic_sample.csv dataset")
print("-" * 80)

# TODO: Print the shape of df_traffic
print("\n1. What is the shape of the dataset?")
# Your code here:
print(f"Shape: {df_traffic.shape}")

# TODO: Print the number of rows
print("\n2. How many traffic records (rows) are in this dataset?")
# Your code here:
print(f"Number of rows: {df_traffic.shape[0]}")

# TODO: Print the number of columns
print("\n3. How many variables (columns) are measured for each record?")
# Your code here:
print(f"Number of columns: {df_traffic.shape[1]}")

# TODO: Print the column names
print("\n4. What are the names of all columns?")
# Your code here:
print(f"Column names: {list(df_traffic.columns)}")

# =============================================================================
# EXERCISE 2: UNDERSTANDING ROWS AND COLUMNS
# =============================================================================
print("\n" + "=" * 80)
print("EXERCISE 2: Understanding Rows and Columns")
print("=" * 80)

# Load the students scores dataset
df_students = pd.read_csv('data/raw/students_scores.csv')

print("\nTASK: Analyze the students_scores.csv dataset structure")
print("-" * 80)

# TODO: Print information about rows
print("\n1. What does each row in this dataset represent?")
# Your answer here:
print("Answer: Each row represents one student's complete academic record")

# TODO: Print information about columns
print("\n2. What does each column in this dataset represent?")
# Your answer here:
print("Answer: Each column represents a specific attribute (ID, name, or subject score)")

# TODO: Calculate and print total data points
print("\n3. How many total data points are in this dataset?")
print("   (Hint: rows × columns)")
# Your code here:
total_data_points = df_students.shape[0] * df_students.shape[1]
print(f"Total data points: {total_data_points}")

# =============================================================================
# EXERCISE 3: INSPECTING DATA TYPES
# =============================================================================
print("\n" + "=" * 80)
print("EXERCISE 3: Inspecting Column Data Types")
print("=" * 80)

print("\nTASK: Examine data types in the students dataset")
print("-" * 80)

# TODO: Print all data types
print("\n1. Display data types for all columns:")
# Your code here:
print(df_students.dtypes)

# TODO: Identify numeric columns
print("\n2. Which columns contain numeric data?")
# Your code here:
numeric_cols = df_students.select_dtypes(include=[np.number]).columns.tolist()
print(f"Numeric columns: {numeric_cols}")

# TODO: Identify non-numeric columns
print("\n3. Which columns contain text/object data?")
# Your code here:
object_cols = df_students.select_dtypes(include=['object']).columns.tolist()
print(f"Object/Text columns: {object_cols}")

# TODO: Use info() method
print("\n4. Display comprehensive information using info():")
# Your code here:
df_students.info()

# =============================================================================
# EXERCISE 4: DETECTING TYPE ISSUES
# =============================================================================
print("\n" + "=" * 80)
print("EXERCISE 4: Detecting Type-Related Issues")
print("=" * 80)

# Create a dataset with type issues
problematic_data = {
    'order_id': ['101', '102', '103', '104', '105'],
    'quantity': ['10', '15', '8', '20', '12'],
    'price': ['25.50', '30.00', '15.75', '40.25', '22.00'],
    'status': ['Delivered', 'Pending', 'Delivered', 'Shipped', 'Pending']
}
df_orders = pd.DataFrame(problematic_data)

print("\nTASK: Identify type issues in this orders dataset")
print("-" * 80)

# TODO: Display the data
print("\n1. Display the first few rows of the dataset:")
# Your code here:
print(df_orders.head())

# TODO: Check data types
print("\n2. Check the data types:")
# Your code here:
print(df_orders.dtypes)

# TODO: Identify problematic columns
print("\n3. Which columns have incorrect data types?")
print("   (Hint: Look for numeric-looking data stored as 'object')")
# Your answer here:
print("Problematic columns:")
print("- order_id: Should be int64, but is object")
print("- quantity: Should be int64, but is object")
print("- price: Should be float64, but is object")

# TODO: Try a numeric operation to confirm the issue
print("\n4. Try to calculate the total quantity:")
# Your code here:
try:
    total = df_orders['quantity'].sum()
    print(f"Total quantity: {total}")
except Exception as e:
    print(f"❌ Error: {type(e).__name__}")
    print("This confirms quantity is not numeric!")

# TODO: Explain why this is a problem
print("\n5. Why is this a problem?")
# Your answer here:
print("Answer: We cannot perform mathematical operations (sum, mean, etc.)")
print("on columns stored as strings/object type, even if they look like numbers.")

# =============================================================================
# EXERCISE 5: COMPREHENSIVE ANALYSIS
# =============================================================================
print("\n" + "=" * 80)
print("EXERCISE 5: Comprehensive Dataset Analysis")
print("=" * 80)

# Load sample traffic data
df_traffic_data = pd.read_csv('data/raw/sample_traffic_data.csv')

print("\nTASK: Perform a complete shape and type analysis")
print("-" * 80)

# TODO: Create a comprehensive report
print("\n--- DATASET ANALYSIS REPORT ---")

print("\n1. SHAPE ANALYSIS:")
# Your code here:
print(f"   - Dataset dimensions: {df_traffic_data.shape}")
print(f"   - Total observations: {df_traffic_data.shape[0]}")
print(f"   - Total variables: {df_traffic_data.shape[1]}")

print("\n2. COLUMN NAMES:")
# Your code here:
for i, col in enumerate(df_traffic_data.columns, 1):
    print(f"   {i}. {col}")

print("\n3. DATA TYPES:")
# Your code here:
print(df_traffic_data.dtypes)

print("\n4. DETAILED INFO:")
# Your code here:
df_traffic_data.info()

print("\n5. DATA TYPE SUMMARY:")
# Your code here:
int_count = len(df_traffic_data.select_dtypes(include=['int64']).columns)
float_count = len(df_traffic_data.select_dtypes(include=['float64']).columns)
object_count = len(df_traffic_data.select_dtypes(include=['object']).columns)

print(f"   - Integer columns: {int_count}")
print(f"   - Float columns: {float_count}")
print(f"   - Object/Text columns: {object_count}")

print("\n6. TYPE APPROPRIATENESS CHECK:")
# Your code here:
print("   Checking if all types are appropriate...")
all_appropriate = True
for col in df_traffic_data.columns:
    if 'volume' in col.lower() or 'hour' in col.lower() or 'temperature' in col.lower():
        if df_traffic_data[col].dtype not in ['int64', 'float64']:
            print(
                f"   ⚠ WARNING: '{col}' should be numeric but is {df_traffic_data[col].dtype}")
            all_appropriate = False

if all_appropriate:
    print("   ✓ All columns have appropriate data types!")

# =============================================================================
# REFLECTION QUESTIONS
# =============================================================================
print("\n" + "=" * 80)
print("REFLECTION QUESTIONS")
print("=" * 80)

print("\nAnswer these questions to solidify your understanding:")
print("-" * 80)

print("\n1. Why is it important to check DataFrame shape before analysis?")
print("Your answer: To understand the size and structure of the data,")
print("know how many records and variables we're working with, and plan")
print("appropriate analysis approaches.")

print("\n2. What problems can occur if column data types are incorrect?")
print("Your answer: Mathematical operations will fail, functions will return")
print("unexpected results, sorting might not work correctly, and analysis")
print("conclusions could be wrong.")

print("\n3. When should you check data types in your workflow?")
print("Your answer: Immediately after loading data, before any operations,")
print("and whenever data behaves unexpectedly.")

print("\n4. What is the difference between 'object' and 'int64' data types?")
print("Your answer: 'object' is typically text/strings, while 'int64' is")
print("whole numbers that support mathematical operations.")

print("\n5. How can you tell if numeric data is mistakenly stored as strings?")
print("Your answer: Check dtypes - if numeric-looking columns show 'object',")
print("or if mathematical operations fail on seemingly numeric data.")

# =============================================================================
# COMPLETION CHECKLIST
# =============================================================================
print("\n" + "=" * 80)
print("COMPLETION CHECKLIST")
print("=" * 80)

print("\n✓ I can inspect DataFrame shape using .shape")
print("✓ I understand what rows represent (observations)")
print("✓ I understand what columns represent (variables)")
print("✓ I can check column data types using .dtypes")
print("✓ I can use .info() for comprehensive inspection")
print("✓ I can identify numeric vs text columns")
print("✓ I can detect when numeric data is stored as strings")
print("✓ I understand why correct data types matter")
print("✓ I check shape and types before any data operations")

print("\n" + "=" * 80)
print("EXERCISES COMPLETE!")
print("=" * 80)
print("\nYou now understand DataFrame shapes and column data types!")
print("This foundation will prevent many common data analysis errors.")
