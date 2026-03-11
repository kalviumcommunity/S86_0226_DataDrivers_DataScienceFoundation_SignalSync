"""
Data Standardization Demo
=========================
This script demonstrates how to standardize column names and data formats in Pandas DataFrames.
Standardization ensures clean, consistent, and analysis-ready data.
"""

import pandas as pd
import numpy as np
import re

print("=" * 80)
print("DATA STANDARDIZATION DEMONSTRATION")
print("=" * 80)
print()

# ============================================================================
# PART 1: Creating a Sample Dataset with Messy Column Names
# ============================================================================

print("PART 1: Creating Sample Dataset with Non-standardized Columns")
print("-" * 80)

# Create a DataFrame with deliberately messy column names
messy_data = {
    'Student Name': ['Alice Johnson', 'BOB SMITH', '  Carol White  ', 'david brown', 'Eve Davis'],
    'Age (Years)': [23, 22, 24, 23, 22],
    'Test Score#1': [85.5, 92.3, 78.9, 88.2, 95.1],
    'Test-Score-2': ['90', '88', '92', '  85  ', '94'],
    'Email Address': ['alice@example.com', 'BOB@EXAMPLE.COM', 'carol@Example.com', 'DAVID@example.com', 'eve@EXAMPLE.COM'],
    'Registration Date': ['2023-01-15', '2023/01/20', '15-01-2023', '2023.01.25', '2023-01-30'],
    'Status!@#': ['Active', 'ACTIVE', 'inactive', '  ACTIVE  ', 'Inactive'],
    'Grade Level': ['A', 'A', 'B', 'A', 'A+']
}

df_messy = pd.DataFrame(messy_data)

print("\n📋 BEFORE STANDARDIZATION:")
print("\nColumn Names:")
print(df_messy.columns.tolist())
print("\nDataFrame Info:")
print(df_messy.info())
print("\nFirst Few Rows:")
print(df_messy.head())
print()

# ============================================================================
# PART 2: Standardizing Column Names
# ============================================================================

print("\n" + "=" * 80)
print("PART 2: Standardizing Column Names")
print("-" * 80)


def standardize_column_names(df):
    """
    Standardize column names by:
    - Converting to lowercase
    - Replacing spaces with underscores
    - Removing special characters
    - Ensuring consistency
    """
    # Create a copy to avoid modifying original
    df_clean = df.copy()

    # Store old names for comparison
    old_names = df_clean.columns.tolist()

    # Apply standardization rules
    new_names = []
    for col in df_clean.columns:
        # Convert to lowercase
        new_col = col.lower()

        # Replace spaces and hyphens with underscores
        new_col = new_col.replace(' ', '_')
        new_col = new_col.replace('-', '_')

        # Remove special characters (keep only alphanumeric and underscores)
        new_col = re.sub(r'[^a-z0-9_]', '', new_col)

        # Remove duplicate underscores
        new_col = re.sub(r'_+', '_', new_col)

        # Remove leading/trailing underscores
        new_col = new_col.strip('_')

        new_names.append(new_col)

    df_clean.columns = new_names

    # Show the transformation
    print("\n🔄 Column Name Transformations:")
    print("-" * 80)
    for old, new in zip(old_names, new_names):
        print(f"  '{old}' → '{new}'")

    return df_clean


df_standardized = standardize_column_names(df_messy)

print("\n✅ Standardized Column Names:")
print(df_standardized.columns.tolist())
print()

# ============================================================================
# PART 3: Standardizing Text Data
# ============================================================================

print("\n" + "=" * 80)
print("PART 3: Standardizing Text Data")
print("-" * 80)

# Standardize student names (proper case)
print("\n📝 Standardizing 'student_name' column:")
print(f"Before: {df_standardized['student_name'].tolist()}")

# Remove whitespace
df_standardized['student_name'] = df_standardized['student_name'].str.strip()
# Proper case
df_standardized['student_name'] = df_standardized['student_name'].str.title()

print(f"After:  {df_standardized['student_name'].tolist()}")

# Standardize email addresses (lowercase)
print("\n📧 Standardizing 'email_address' column:")
print(f"Before: {df_standardized['email_address'].tolist()}")

# All lowercase
df_standardized['email_address'] = df_standardized['email_address'].str.lower()
# Remove whitespace
df_standardized['email_address'] = df_standardized['email_address'].str.strip()

print(f"After:  {df_standardized['email_address'].tolist()}")

# Standardize status column (categorical data)
print("\n🏷️  Standardizing 'status' column:")
print(f"Before: {df_standardized['status'].tolist()}")

# Remove whitespace
df_standardized['status'] = df_standardized['status'].str.strip()
df_standardized['status'] = df_standardized['status'].str.lower()  # Lowercase
# Capitalize first letter
df_standardized['status'] = df_standardized['status'].str.capitalize()

print(f"After:  {df_standardized['status'].tolist()}")

# ============================================================================
# PART 4: Standardizing Numeric Data
# ============================================================================

print("\n" + "=" * 80)
print("PART 4: Standardizing Numeric Data")
print("-" * 80)

# Standardize test score 2 (currently string, convert to numeric)
print("\n🔢 Standardizing 'test_score_2' column:")
print(f"Before: {df_standardized['test_score_2'].tolist()}")
print(f"Data type before: {df_standardized['test_score_2'].dtype}")

# Remove whitespace and convert to numeric
df_standardized['test_score_2'] = df_standardized['test_score_2'].str.strip()
df_standardized['test_score_2'] = pd.to_numeric(
    df_standardized['test_score_2'], errors='coerce')

print(f"After:  {df_standardized['test_score_2'].tolist()}")
print(f"Data type after: {df_standardized['test_score_2'].dtype}")

# Round numeric columns to consistent decimal places
print("\n📊 Rounding numeric scores to 1 decimal place:")
df_standardized['test_score1'] = df_standardized['test_score1'].round(1)
df_standardized['test_score_2'] = df_standardized['test_score_2'].round(1)

# ============================================================================
# PART 5: Standardizing Date Formats
# ============================================================================

print("\n" + "=" * 80)
print("PART 5: Standardizing Date Formats")
print("-" * 80)

print("\n📅 Standardizing 'registration_date' column:")
print(f"Before: {df_standardized['registration_date'].tolist()}")
print(f"Data type before: {df_standardized['registration_date'].dtype}")

# Convert various date formats to standard datetime format
df_standardized['registration_date'] = pd.to_datetime(
    df_standardized['registration_date'],
    infer_datetime_format=True,
    errors='coerce'
)

print(f"After:  {df_standardized['registration_date'].tolist()}")
print(f"Data type after: {df_standardized['registration_date'].dtype}")

# ============================================================================
# PART 6: Final Comparison and Results
# ============================================================================

print("\n" + "=" * 80)
print("PART 6: Final Comparison - Before vs After")
print("=" * 80)

print("\n📋 BEFORE STANDARDIZATION:")
print("-" * 80)
print("Columns:", df_messy.columns.tolist())
print("\nData Types:")
print(df_messy.dtypes)
print("\nSample Data:")
print(df_messy.head())

print("\n" + "=" * 80)
print("\n✅ AFTER STANDARDIZATION:")
print("-" * 80)
print("Columns:", df_standardized.columns.tolist())
print("\nData Types:")
print(df_standardized.dtypes)
print("\nSample Data:")
print(df_standardized.head())

# ============================================================================
# PART 7: Working with Real Dataset - Students Scores
# ============================================================================

print("\n" + "=" * 80)
print("PART 7: Standardizing Real Dataset - Student Scores")
print("=" * 80)

try:
    # Load the students scores dataset
    df_students = pd.read_csv('data/raw/students_scores.csv')

    print("\n📋 Original Student Scores Data:")
    print(df_students.head())
    print("\nColumns:", df_students.columns.tolist())

    # Standardize column names
    df_students_clean = standardize_column_names(df_students)

    # Standardize name column (if exists)
    if 'name' in df_students_clean.columns:
        df_students_clean['name'] = df_students_clean['name'].str.strip(
        ).str.title()

    print("\n✅ Standardized Student Scores Data:")
    print(df_students_clean.head())
    print("\nColumns:", df_students_clean.columns.tolist())

    # Save cleaned data
    df_students_clean.to_csv(
        'data/processed/students_scores_clean.csv', index=False)
    print("\n💾 Cleaned data saved to: data/processed/students_scores_clean.csv")

except FileNotFoundError:
    print("\n⚠️  Student scores file not found, skipping this part.")

# ============================================================================
# PART 8: Save Standardized Data
# ============================================================================

print("\n" + "=" * 80)
print("PART 8: Saving Standardized Data")
print("-" * 80)

# Save the standardized demo data
output_path = 'data/processed/standardized_demo_data.csv'
df_standardized.to_csv(output_path, index=False)
print(f"\n💾 Standardized data saved to: {output_path}")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 80)
print("KEY TAKEAWAYS")
print("=" * 80)
print("""
✅ Column Name Standardization:
   • Use lowercase for all column names
   • Replace spaces with underscores
   • Remove special characters
   • Use snake_case convention
   • Keep names descriptive but concise

✅ Text Data Standardization:
   • Strip extra whitespace
   • Apply consistent casing (lower, upper, or title case)
   • Standardize categorical values
   • Ensure consistency across similar values

✅ Numeric Data Standardization:
   • Convert string numbers to numeric types
   • Handle missing or invalid values
   • Round to consistent decimal places
   • Ensure proper data types

✅ Date Format Standardization:
   • Convert all dates to datetime format
   • Handle multiple date formats
   • Use consistent date representation
   • Enable date-based operations

✅ Why This Matters:
   • Makes code more readable and maintainable
   • Prevents errors in data operations
   • Simplifies merging and joining datasets
   • Improves data quality and reliability
   • Scales better for larger projects
""")

print("=" * 80)
print("STANDARDIZATION COMPLETE!")
print("=" * 80)
