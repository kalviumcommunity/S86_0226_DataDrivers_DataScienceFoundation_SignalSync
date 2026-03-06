"""
Pandas DataFrame Practice Exercises
====================================
Complete these exercises to solidify your understanding of Pandas DataFrames.

Instructions:
- Write your code below each exercise prompt
- Run the file to test your solutions
- Uncomment the print statements to verify your answers
"""

import pandas as pd
import numpy as np
import os

print("=" * 70)
print("PANDAS DATAFRAME PRACTICE EXERCISES")
print("=" * 70)
print()

# ==============================================================================
# EXERCISE 1: Create DataFrame from Dictionary (Column-Oriented)
# ==============================================================================
print("EXERCISE 1: Create DataFrame from Dictionary")
print("-" * 70)
print("Task: Create a DataFrame with the following data:")
print("      Columns: 'city', 'population', 'area'")
print("      Data: Mumbai (20M, 603 km²), Delhi (30M, 1484 km²),")
print("            Bangalore (12M, 741 km²)")
print()

# TODO: Create the DataFrame here
# cities_data = {
#     'city': [...],
#     'population': [...],
#     'area': [...]
# }
# cities_df = pd.DataFrame(...)

# Uncomment to test:
# print("Cities DataFrame:")
# print(cities_df)
print()

# ==============================================================================
# EXERCISE 2: Create DataFrame from List of Dictionaries
# ==============================================================================
print("EXERCISE 2: Create DataFrame from List of Dictionaries")
print("-" * 70)
print("Task: Create a DataFrame where each dictionary represents a product:")
print("      [{'name': 'Laptop', 'price': 75000, 'stock': 25},")
print("       {'name': 'Mouse', 'price': 500, 'stock': 150},")
print("       {'name': 'Keyboard', 'price': 1200, 'stock': 80}]")
print()

# TODO: Create the DataFrame here
# products_list = [...]
# products_df = pd.DataFrame(...)

# Uncomment to test:
# print("Products DataFrame:")
# print(products_df)
print()

# ==============================================================================
# EXERCISE 3: Create DataFrame with Custom Index
# ==============================================================================
print("EXERCISE 3: Create DataFrame with Custom Index")
print("-" * 70)
print("Task: Create a DataFrame of daily temperatures with custom index:")
print("      Data: [22, 24, 26, 25, 23, 21, 20]")
print("      Index: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']")
print("      Column name: 'temperature'")
print()

# TODO: Create the DataFrame here
# temp_df = pd.DataFrame(...)

# Uncomment to test:
# print("Temperature DataFrame:")
# print(temp_df)
print()

# ==============================================================================
# EXERCISE 4: Load DataFrame from CSV
# ==============================================================================
print("EXERCISE 4: Load DataFrame from CSV")
print("-" * 70)
print("Task: Load the students_scores.csv file from data/raw/")
print()

# TODO: Load the CSV file
# script_dir = os.path.dirname(os.path.abspath(__file__))
# csv_path = os.path.join(script_dir, 'data', 'raw', 'students_scores.csv')
# students_df = pd.read_csv(...)

# Uncomment to test:
# print("Students DataFrame:")
# print(students_df)
print()

# ==============================================================================
# EXERCISE 5: Inspect DataFrame Shape and Columns
# ==============================================================================
print("EXERCISE 5: Inspect DataFrame Shape and Columns")
print("-" * 70)
print("Task: Given the DataFrame below, extract:")
print("      a) Number of rows and columns")
print("      b) List of column names")
print()

sample_df = pd.DataFrame({
    'employee_id': [101, 102, 103, 104, 105],
    'name': ['Raj', 'Priya', 'Amit', 'Neha', 'Vikram'],
    'department': ['IT', 'HR', 'Sales', 'IT', 'Sales'],
    'salary': [75000, 60000, 55000, 80000, 62000]
})

# TODO: Extract shape and columns
# num_rows, num_cols = ...
# column_list = ...

# Uncomment to test:
# print(f"Shape: {num_rows} rows, {num_cols} columns")
# print(f"Columns: {column_list}")
print()

# ==============================================================================
# EXERCISE 6: Use head() and tail()
# ==============================================================================
print("EXERCISE 6: Use head() and tail()")
print("-" * 70)
print("Task: Display the first 3 rows and last 2 rows of sample_df")
print()

# TODO: Display head and tail
# first_three = ...
# last_two = ...

# Uncomment to test:
# print("First 3 rows:")
# print(first_three)
# print("\nLast 2 rows:")
# print(last_two)
print()

# ==============================================================================
# EXERCISE 7: Check Data Types
# ==============================================================================
print("EXERCISE 7: Check Data Types")
print("-" * 70)
print("Task: Display the data types of all columns in sample_df")
print()

# TODO: Get data types
# dtypes_info = ...

# Uncomment to test:
# print("Data Types:")
# print(dtypes_info)
print()

# ==============================================================================
# EXERCISE 8: Access Specific Columns
# ==============================================================================
print("EXERCISE 8: Access Specific Columns")
print("-" * 70)
print("Task: From sample_df, extract:")
print("      a) 'name' column as a Series")
print("      b) 'name' and 'salary' columns as a DataFrame")
print()

# TODO: Extract columns
# names_series = ...
# name_salary_df = ...

# Uncomment to test:
# print("Names (Series):")
# print(names_series)
# print(f"Type: {type(names_series)}")
# print("\nName and Salary (DataFrame):")
# print(name_salary_df)
# print(f"Type: {type(name_salary_df)}")
print()

# ==============================================================================
# EXERCISE 9: Filter DataFrame Rows
# ==============================================================================
print("EXERCISE 9: Filter DataFrame Rows")
print("-" * 70)
print("Task: From sample_df, filter employees with salary > 60000")
print()

# TODO: Filter rows
# high_salary_df = ...

# Uncomment to test:
# print("Employees with salary > 60000:")
# print(high_salary_df)
print()

# ==============================================================================
# EXERCISE 10: Add New Column
# ==============================================================================
print("EXERCISE 10: Add New Column")
print("-" * 70)
print("Task: Add a 'bonus' column to sample_df (10% of salary)")
print()

# TODO: Add new column
# sample_df['bonus'] = ...

# Uncomment to test:
# print("DataFrame with Bonus Column:")
# print(sample_df)
print()

# ==============================================================================
# EXERCISE 11: Sort DataFrame
# ==============================================================================
print("EXERCISE 11: Sort DataFrame")
print("-" * 70)
print("Task: Sort sample_df by salary in descending order")
print()

# TODO: Sort DataFrame
# sorted_df = ...

# Uncomment to test:
# print("Sorted by Salary (Descending):")
# print(sorted_df)
print()

# ==============================================================================
# EXERCISE 12: Get Summary Statistics
# ==============================================================================
print("EXERCISE 12: Get Summary Statistics")
print("-" * 70)
print("Task: Display summary statistics for numeric columns in sample_df")
print()

# TODO: Get summary statistics
# stats = ...

# Uncomment to test:
# print("Summary Statistics:")
# print(stats)
print()

# ==============================================================================
# EXERCISE 13: Create DataFrame from NumPy Array
# ==============================================================================
print("EXERCISE 13: Create DataFrame from NumPy Array")
print("-" * 70)
print("Task: Create a 4x3 DataFrame from a random NumPy array")
print("      Columns: ['Feature_1', 'Feature_2', 'Feature_3']")
print("      Index: ['Sample_1', 'Sample_2', 'Sample_3', 'Sample_4']")
print()

# TODO: Create DataFrame from NumPy array
# np.random.seed(42)
# array_data = np.random.randint(10, 100, size=(4, 3))
# numpy_df = pd.DataFrame(...)

# Uncomment to test:
# print("DataFrame from NumPy Array:")
# print(numpy_df)
print()

# ==============================================================================
# EXERCISE 14: Use info() Method
# ==============================================================================
print("EXERCISE 14: Use info() Method")
print("-" * 70)
print("Task: Display comprehensive information about sample_df")
print()

# TODO: Display info
# print("DataFrame Info:")
# sample_df.info()
print()

# ==============================================================================
# EXERCISE 15: Reset Index
# ==============================================================================
print("EXERCISE 15: Reset Index")
print("-" * 70)
print("Task: Create a filtered DataFrame and reset its index")
print()

it_employees = sample_df[sample_df['department'] == 'IT']
print("IT Employees (before reset):")
print(it_employees)
print()

# TODO: Reset index
# it_employees_reset = it_employees.reset_index(drop=True)

# Uncomment to test:
# print("IT Employees (after reset):")
# print(it_employees_reset)
print()

# ==============================================================================
# SOLUTIONS
# ==============================================================================
print("=" * 70)
print("Uncomment the solution section below to check your answers")
print("=" * 70)

# SOLUTION 1
cities_data = {
    'city': ['Mumbai', 'Delhi', 'Bangalore'],
    'population': [20_000_000, 30_000_000, 12_000_000],
    'area': [603, 1484, 741]
}
cities_df = pd.DataFrame(cities_data)

# SOLUTION 2
products_list = [
    {'name': 'Laptop', 'price': 75000, 'stock': 25},
    {'name': 'Mouse', 'price': 500, 'stock': 150},
    {'name': 'Keyboard', 'price': 1200, 'stock': 80}
]
products_df = pd.DataFrame(products_list)

# SOLUTION 3
temp_df = pd.DataFrame(
    {'temperature': [22, 24, 26, 25, 23, 21, 20]},
    index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
)

# SOLUTION 4
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'data', 'raw', 'students_scores.csv')
try:
    students_df = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"Note: CSV file not found at {csv_path}")
    students_df = pd.DataFrame()

# SOLUTION 5
num_rows, num_cols = sample_df.shape
column_list = sample_df.columns.tolist()

# SOLUTION 6
first_three = sample_df.head(3)
last_two = sample_df.tail(2)

# SOLUTION 7
dtypes_info = sample_df.dtypes

# SOLUTION 8
names_series = sample_df['name']
name_salary_df = sample_df[['name', 'salary']]

# SOLUTION 9
high_salary_df = sample_df[sample_df['salary'] > 60000]

# SOLUTION 10
sample_df['bonus'] = sample_df['salary'] * 0.10

# SOLUTION 11
sorted_df = sample_df.sort_values('salary', ascending=False)

# SOLUTION 12
stats = sample_df.describe()

# SOLUTION 13
np.random.seed(42)
array_data = np.random.randint(10, 100, size=(4, 3))
numpy_df = pd.DataFrame(
    array_data,
    columns=['Feature_1', 'Feature_2', 'Feature_3'],
    index=['Sample_1', 'Sample_2', 'Sample_3', 'Sample_4']
)

# SOLUTION 14
# sample_df.info() - already completed in the exercise

# SOLUTION 15
it_employees_reset = it_employees.reset_index(drop=True)

print("\n✓ Solutions are defined. Uncomment print statements to verify!")
