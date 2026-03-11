"""
Data Standardization Exercises
================================
Practice standardizing column names and data formats.
Complete each exercise to build your data cleaning skills.
"""

import pandas as pd
import re

print("=" * 80)
print("DATA STANDARDIZATION EXERCISES")
print("=" * 80)
print()

# ============================================================================
# EXERCISE 1: Standardize Product Catalog Column Names
# ============================================================================

print("EXERCISE 1: Standardize Product Catalog Column Names")
print("-" * 80)

# Sample product catalog with messy column names
product_data = {
    'Product ID': [101, 102, 103, 104, 105],
    'Product Name!!!': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Price ($)': [999.99, 25.50, 75.00, 350.00, 89.99],
    'Stock-Available': [15, 150, 80, 25, 60],
    'Category Name': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories']
}

df_products = pd.DataFrame(product_data)

print("\nOriginal Columns:")
print(df_products.columns.tolist())
print("\nOriginal DataFrame:")
print(df_products)

# TODO: Standardize the column names
# HINT: Convert to lowercase, replace spaces with underscores, remove special characters
# YOUR CODE HERE:

df_products_clean = df_products.copy()
# df_products_clean.columns = ...

print("\n✅ Expected standardized columns:")
print("['product_id', 'product_name', 'price', 'stock_available', 'category_name']")

# ============================================================================
# EXERCISE 2: Standardize Text Data in Cities Column
# ============================================================================

print("\n" + "=" * 80)
print("EXERCISE 2: Standardize Text Data in Cities Column")
print("-" * 80)

city_data = {
    'city_name': ['  NEW YORK  ', 'los angeles', 'CHICAGO', '  Houston  ', 'phoenix'],
    'population': ['8.3M', '4.0M', '2.7M', '2.3M', '1.7M'],
    'state': ['NY', 'ca', 'IL', 'tx', 'AZ']
}

df_cities = pd.DataFrame(city_data)

print("\nOriginal Data:")
print(df_cities)

# TODO: Standardize the data
# 1. Remove extra whitespace from city_name
# 2. Convert city_name to title case
# 3. Convert state to uppercase
# YOUR CODE HERE:

# df_cities['city_name'] = ...
# df_cities['state'] = ...

print("\n✅ Expected result: city names in Title Case, states in UPPERCASE, no extra spaces")

# ============================================================================
# EXERCISE 3: Standardize Numeric Data
# ============================================================================

print("\n" + "=" * 80)
print("EXERCISE 3: Standardize Numeric Data")
print("-" * 80)

sales_data = {
    'employee_id': [1, 2, 3, 4, 5],
    'sales_amount': ['1500.567', '2300.123', '  1800.999  ', '2100.456', '1900.789'],
    'commission_rate': ['0.05', '0.07', '0.06', '0.08', '0.055']
}

df_sales = pd.DataFrame(sales_data)

print("\nOriginal Data:")
print(df_sales)
print("\nData Types:")
print(df_sales.dtypes)

# TODO: Standardize the numeric columns
# 1. Convert sales_amount to numeric type and round to 2 decimal places
# 2. Convert commission_rate to numeric type and round to 3 decimal places
# YOUR CODE HERE:

# df_sales['sales_amount'] = ...
# df_sales['commission_rate'] = ...

print("\n✅ Expected: All numeric columns should be float type with appropriate rounding")

# ============================================================================
# EXERCISE 4: Standardize Date Formats
# ============================================================================

print("\n" + "=" * 80)
print("EXERCISE 4: Standardize Date Formats")
print("-" * 80)

event_data = {
    'event_name': ['Conference', 'Workshop', 'Seminar', 'Meetup', 'Webinar'],
    'event_date': ['2024-03-15', '15/03/2024', '2024.03.20', 'March 25, 2024', '2024-03-30']
}

df_events = pd.DataFrame(event_data)

print("\nOriginal Data:")
print(df_events)
print("\nData Type of event_date:", df_events['event_date'].dtype)

# TODO: Standardize the date column
# Convert all dates to datetime format
# YOUR CODE HERE:

# df_events['event_date'] = ...

print("\n✅ Expected: All dates should be in datetime format")

# ============================================================================
# EXERCISE 5: Comprehensive Dataset Cleanup
# ============================================================================

print("\n" + "=" * 80)
print("EXERCISE 5: Comprehensive Dataset Cleanup")
print("-" * 80)

messy_employee_data = {
    'Employee ID#': [1001, 1002, 1003, 1004, 1005],
    'Full Name': ['  JOHN DOE  ', 'jane smith', 'BOB WILSON', '  alice brown  ', 'CHARLIE DAVIS'],
    'Email@Address': ['JOHN@COMPANY.COM', 'jane@COMPANY.com', '  bob@company.COM  ', 'alice@Company.com', 'CHARLIE@company.com'],
    'Salary ($)': ['75000.50', '  82000.75  ', '68000.00', '91000.25', '77500.99'],
    'Department Name': ['Sales', 'MARKETING', 'sales', '  HR  ', 'Marketing'],
    'Join-Date': ['2020-01-15', '2020/02/20', '15-03-2020', '2020.04.10', '2020-05-05']
}

df_employees = pd.DataFrame(messy_employee_data)

print("\nOriginal Messy Employee Data:")
print(df_employees)
print("\nOriginal Columns:", df_employees.columns.tolist())
print("\nOriginal Data Types:")
print(df_employees.dtypes)

# TODO: Complete all standardization tasks:
# 1. Standardize column names (lowercase, underscores, no special characters)
# 2. Standardize full names (strip whitespace, title case)
# 3. Standardize email addresses (lowercase, strip whitespace)
# 4. Convert salary to numeric and round to 2 decimal places
# 5. Standardize department names (strip whitespace, title case)
# 6. Convert join dates to datetime format

# YOUR CODE HERE:

df_employees_clean = df_employees.copy()

# Step 1: Standardize column names

# Step 2: Standardize text data

# Step 3: Standardize numeric data

# Step 4: Standardize date data

print("\n" + "=" * 80)
print("✅ Expected Cleaned Employee Data:")
print("-" * 80)
print("Columns: ['employee_id', 'full_name', 'emailaddress', 'salary', 'department_name', 'join_date']")
print("All text properly formatted, numeric columns as float, dates as datetime")

# ============================================================================
# CHALLENGE EXERCISE: Create Your Own Standardization Function
# ============================================================================

print("\n" + "=" * 80)
print("CHALLENGE: Create a Reusable Standardization Function")
print("-" * 80)


def standardize_dataframe(df, text_columns=None, numeric_columns=None, date_columns=None):
    """
    Create a comprehensive function that standardizes a DataFrame.

    Parameters:
    -----------
    df : DataFrame
        The DataFrame to standardize
    text_columns : list
        List of column names to standardize as text (strip, lowercase/title case)
    numeric_columns : list
        List of column names to convert to numeric
    date_columns : list
        List of column names to convert to datetime

    Returns:
    --------
    DataFrame
        Standardized DataFrame
    """
    # TODO: Implement this function
    # YOUR CODE HERE:

    df_clean = df.copy()

    # 1. Standardize all column names

    # 2. Standardize text columns

    # 3. Standardize numeric columns

    # 4. Standardize date columns

    return df_clean


# Test your function
test_data = {
    'Product Name': ['  ITEM A  ', 'item b', 'ITEM C'],
    'Price ($)': ['19.99', '  29.99  ', '39.99'],
    'Launch Date': ['2024-01-01', '2024/02/01', '01-03-2024']
}

df_test = pd.DataFrame(test_data)
print("\nTest Data:")
print(df_test)

# Uncomment to test your function:
# df_test_clean = standardize_dataframe(
#     df_test,
#     text_columns=['product_name'],
#     numeric_columns=['price'],
#     date_columns=['launch_date']
# )
# print("\nStandardized Test Data:")
# print(df_test_clean)

print("\n" + "=" * 80)
print("EXERCISES COMPLETE!")
print("=" * 80)
print("\n💡 Remember:")
print("  • Always standardize early in your data pipeline")
print("  • Be consistent with naming conventions")
print("  • Document your standardization rules")
print("  • Test your standardization on sample data first")
print("=" * 80)
