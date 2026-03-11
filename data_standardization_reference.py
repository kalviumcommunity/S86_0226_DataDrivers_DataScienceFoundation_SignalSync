"""
Data Standardization Reference Guide
======================================
Complete solutions and best practices for data standardization.
"""

import pandas as pd
import numpy as np
import re
from datetime import datetime

print("=" * 80)
print("DATA STANDARDIZATION REFERENCE GUIDE")
print("=" * 80)
print()

# ============================================================================
# SECTION 1: Column Name Standardization Function
# ============================================================================


def standardize_column_names(df):
    """
    Standardize DataFrame column names using snake_case convention.

    Rules applied:
    - Convert to lowercase
    - Replace spaces and hyphens with underscores
    - Remove special characters
    - Remove duplicate underscores
    - Strip leading/trailing underscores

    Parameters:
    -----------
    df : DataFrame
        Input DataFrame with any column names

    Returns:
    --------
    DataFrame
        DataFrame with standardized column names
    """
    df_clean = df.copy()

    new_columns = []
    for col in df_clean.columns:
        # Convert to string and lowercase
        new_col = str(col).lower()

        # Replace spaces, hyphens, periods with underscores
        new_col = new_col.replace(' ', '_')
        new_col = new_col.replace('-', '_')
        new_col = new_col.replace('.', '_')

        # Remove special characters (keep only alphanumeric and underscores)
        new_col = re.sub(r'[^a-z0-9_]', '', new_col)

        # Remove duplicate underscores
        new_col = re.sub(r'_+', '_', new_col)

        # Strip leading/trailing underscores
        new_col = new_col.strip('_')

        # Ensure column name is not empty
        if not new_col:
            new_col = f'column_{len(new_columns)}'

        new_columns.append(new_col)

    df_clean.columns = new_columns
    return df_clean

# ============================================================================
# SECTION 2: Text Data Standardization Functions
# ============================================================================


def standardize_text_lowercase(series):
    """Standardize text to lowercase and strip whitespace."""
    return series.str.strip().str.lower()


def standardize_text_uppercase(series):
    """Standardize text to uppercase and strip whitespace."""
    return series.str.strip().str.upper()


def standardize_text_titlecase(series):
    """Standardize text to title case and strip whitespace."""
    return series.str.strip().str.title()


def standardize_text_capitalize(series):
    """Standardize text to capitalize first letter only and strip whitespace."""
    return series.str.strip().str.capitalize()


def standardize_categorical(series, categories_map=None):
    """
    Standardize categorical values with optional mapping.

    Parameters:
    -----------
    series : Series
        Column with categorical data
    categories_map : dict, optional
        Mapping of old values to new standardized values

    Returns:
    --------
    Series
        Standardized categorical series
    """
    # Strip whitespace and lowercase
    series_clean = series.str.strip().str.lower()

    # Apply mapping if provided
    if categories_map:
        # Convert map keys to lowercase for matching
        lowercase_map = {k.lower(): v for k, v in categories_map.items()}
        series_clean = series_clean.map(lowercase_map).fillna(series_clean)
    else:
        # Default: capitalize first letter
        series_clean = series_clean.str.capitalize()

    return series_clean

# ============================================================================
# SECTION 3: Numeric Data Standardization Functions
# ============================================================================


def standardize_numeric(series, decimal_places=2, fill_value=None):
    """
    Standardize numeric column.

    Parameters:
    -----------
    series : Series
        Column to standardize
    decimal_places : int
        Number of decimal places to round to
    fill_value : float, optional
        Value to use for NaN entries

    Returns:
    --------
    Series
        Standardized numeric series
    """
    # Strip whitespace if string
    if series.dtype == 'object':
        series = series.str.strip()

    # Convert to numeric
    series_numeric = pd.to_numeric(series, errors='coerce')

    # Round to specified decimal places
    series_numeric = series_numeric.round(decimal_places)

    # Fill NaN values if specified
    if fill_value is not None:
        series_numeric = series_numeric.fillna(fill_value)

    return series_numeric


def remove_currency_symbols(series, currency_symbols=['$', '€', '£', '¥']):
    """Remove currency symbols from strings before converting to numeric."""
    if series.dtype == 'object':
        for symbol in currency_symbols:
            series = series.str.replace(symbol, '', regex=False)
        series = series.str.strip()
    return series


def remove_percentage_signs(series):
    """Remove percentage signs and convert to decimal (e.g., '50%' -> 0.50)."""
    if series.dtype == 'object':
        series = series.str.replace('%', '', regex=False)
        series = pd.to_numeric(series, errors='coerce') / 100
    return series

# ============================================================================
# SECTION 4: Date Standardization Functions
# ============================================================================


def standardize_dates(series, date_format=None):
    """
    Standardize date column to datetime format.

    Parameters:
    -----------
    series : Series
        Column with date strings
    date_format : str, optional
        Specific date format to parse (e.g., '%Y-%m-%d')

    Returns:
    --------
    Series
        Standardized datetime series
    """
    if date_format:
        return pd.to_datetime(series, format=date_format, errors='coerce')
    else:
        return pd.to_datetime(series, infer_datetime_format=True, errors='coerce')


def format_date_string(series, output_format='%Y-%m-%d'):
    """Convert datetime series to standardized string format."""
    return pd.to_datetime(series).dt.strftime(output_format)

# ============================================================================
# SECTION 5: Complete Standardization Pipeline
# ============================================================================


def standardize_dataframe_complete(df, column_config):
    """
    Complete standardization pipeline for a DataFrame.

    Parameters:
    -----------
    df : DataFrame
        Input DataFrame to standardize
    column_config : dict
        Configuration dictionary specifying how to handle each column type
        Example:
        {
            'text_lowercase': ['email', 'username'],
            'text_titlecase': ['name', 'city'],
            'text_uppercase': ['country_code', 'state'],
            'numeric': {'price': 2, 'quantity': 0},  # column: decimal_places
            'dates': ['registration_date', 'last_login']
        }

    Returns:
    --------
    DataFrame
        Fully standardized DataFrame
    """
    # Step 1: Standardize column names
    df_clean = standardize_column_names(df)

    # Step 2: Standardize text columns
    if 'text_lowercase' in column_config:
        for col in column_config['text_lowercase']:
            if col in df_clean.columns:
                df_clean[col] = standardize_text_lowercase(df_clean[col])

    if 'text_uppercase' in column_config:
        for col in column_config['text_uppercase']:
            if col in df_clean.columns:
                df_clean[col] = standardize_text_uppercase(df_clean[col])

    if 'text_titlecase' in column_config:
        for col in column_config['text_titlecase']:
            if col in df_clean.columns:
                df_clean[col] = standardize_text_titlecase(df_clean[col])

    # Step 3: Standardize numeric columns
    if 'numeric' in column_config:
        for col, decimals in column_config['numeric'].items():
            if col in df_clean.columns:
                df_clean[col] = standardize_numeric(
                    df_clean[col], decimal_places=decimals)

    # Step 4: Standardize date columns
    if 'dates' in column_config:
        for col in column_config['dates']:
            if col in df_clean.columns:
                df_clean[col] = standardize_dates(df_clean[col])

    return df_clean

# ============================================================================
# DEMONSTRATION EXAMPLES
# ============================================================================


print("=" * 80)
print("DEMONSTRATION: Using Standardization Functions")
print("=" * 80)

# Example 1: Basic column name standardization
print("\n1. Column Name Standardization")
print("-" * 80)

sample_df = pd.DataFrame({
    'First Name': ['John', 'Jane'],
    'Last-Name': ['Doe', 'Smith'],
    'Age (years)': [30, 25],
    'Email@Address': ['john@test.com', 'jane@test.com']
})

print("Before:")
print(sample_df.columns.tolist())

sample_df_clean = standardize_column_names(sample_df)

print("After:")
print(sample_df_clean.columns.tolist())

# Example 2: Text standardization
print("\n2. Text Standardization")
print("-" * 80)

df_text = pd.DataFrame({
    'name': ['  JOHN DOE  ', 'jane smith', 'BOB WILSON'],
    'email': ['JOHN@TEST.COM', '  jane@TEST.com  ', 'bob@test.COM'],
    'status': ['Active', 'INACTIVE', '  active  ']
})

print("Before:")
print(df_text)

df_text['name'] = standardize_text_titlecase(df_text['name'])
df_text['email'] = standardize_text_lowercase(df_text['email'])
df_text['status'] = standardize_text_capitalize(df_text['status'])

print("\nAfter:")
print(df_text)

# Example 3: Numeric standardization
print("\n3. Numeric Standardization")
print("-" * 80)

df_numeric = pd.DataFrame({
    'price': ['  $19.99  ', '$29.999', '39.50'],
    'discount': ['10%', '15%', '5%']
})

print("Before:")
print(df_numeric)
print(df_numeric.dtypes)

df_numeric['price'] = remove_currency_symbols(df_numeric['price'])
df_numeric['price'] = standardize_numeric(
    df_numeric['price'], decimal_places=2)
df_numeric['discount'] = remove_percentage_signs(df_numeric['discount'])

print("\nAfter:")
print(df_numeric)
print(df_numeric.dtypes)

# Example 4: Date standardization
print("\n4. Date Standardization")
print("-" * 80)

df_dates = pd.DataFrame({
    'event_date': ['2024-01-15', '15/01/2024', 'January 20, 2024']
})

print("Before:")
print(df_dates)
print("Type:", df_dates['event_date'].dtype)

df_dates['event_date'] = standardize_dates(df_dates['event_date'])

print("\nAfter:")
print(df_dates)
print("Type:", df_dates['event_date'].dtype)

# Example 5: Complete pipeline
print("\n5. Complete Standardization Pipeline")
print("-" * 80)

messy_df = pd.DataFrame({
    'Employee ID#': [1, 2, 3],
    'Full Name': ['  JOHN DOE  ', 'jane smith', 'BOB WILSON'],
    'Email Address': ['JOHN@COMPANY.COM', 'jane@company.COM', 'bob@Company.com'],
    'Salary ($)': ['75000.50', '82000', '  68000.99  '],
    'Start Date': ['2020-01-15', '2020/02/20', 'March 15, 2020']
})

print("Before:")
print(messy_df)
print("\nColumns:", messy_df.columns.tolist())
print("\nData types:")
print(messy_df.dtypes)

# Configure standardization
config = {
    'text_titlecase': ['full_name'],
    'text_lowercase': ['email_address'],
    'numeric': {'salary': 2},
    'dates': ['start_date']
}

# Apply complete standardization
clean_df = standardize_dataframe_complete(messy_df, config)

print("\n\nAfter:")
print(clean_df)
print("\nColumns:", clean_df.columns.tolist())
print("\nData types:")
print(clean_df.dtypes)

# ============================================================================
# BEST PRACTICES
# ============================================================================

print("\n" + "=" * 80)
print("BEST PRACTICES SUMMARY")
print("=" * 80)
print("""
✅ COLUMN NAMING CONVENTIONS:
   • Use snake_case (recommended for Python)
   • Alternatives: camelCase, PascalCase (less common in data science)
   • Be consistent across all datasets
   • Avoid abbreviations unless widely understood
   • Keep names concise but descriptive
   • Examples: user_id, first_name, created_at, total_sales

✅ TEXT STANDARDIZATION:
   • Remove leading/trailing whitespace
   • Choose appropriate casing:
     - lowercase: emails, usernames, URLs
     - UPPERCASE: country codes, state abbreviations
     - Title Case: names, cities, titles
     - Sentence case: descriptions, notes
   • Standardize categorical values before analysis
   • Handle missing values consistently

✅ NUMERIC STANDARDIZATION:
   • Convert strings to appropriate numeric types
   • Remove currency symbols and percentage signs
   • Round to appropriate decimal places
   • Handle missing values (NaN, None, empty strings)
   • Ensure consistent units across dataset
   • Validate ranges (e.g., age between 0-120)

✅ DATE STANDARDIZATION:
   • Convert to datetime format as early as possible
   • Use consistent date format (ISO 8601: YYYY-MM-DD recommended)
   • Handle timezone information if relevant
   • Validate date ranges
   • Consider extracting components (year, month, day) if needed

✅ WORKFLOW INTEGRATION:
   • Standardize immediately after loading data
   • Document standardization rules in code comments
   • Create reusable functions for common patterns
   • Validate data after standardization
   • Save cleaned data for reproducibility
   • Keep original data unchanged (work on copies)

✅ COMMON PITFALLS TO AVOID:
   • Modifying original data (always work on copies)
   • Inconsistent standardization across similar columns
   • Over-standardizing (losing important information)
   • Not handling missing values
   • Ignoring data type conversions
   • Not validating results after standardization

✅ PERFORMANCE TIPS:
   • Use vectorized operations (str methods, apply)
   • Avoid loops when possible
   • Process in chunks for large datasets
   • Cache standardized data
   • Use appropriate data types to save memory
""")

print("=" * 80)
print("REFERENCE GUIDE COMPLETE")
print("=" * 80)
