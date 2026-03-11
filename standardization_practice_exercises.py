"""
Standardization Practice Exercises
===================================
Practice standardizing column names and data formats in Pandas DataFrames.

Instructions:
-------------
Complete each exercise by writing code to standardize the data as described.
Run the script to check your work.

Learning Objectives:
- Apply column name standardization techniques
- Standardize text, numeric, and date formats
- Build confidence with data cleaning
"""

import pandas as pd
import numpy as np

print("=" * 70)
print("STANDARDIZATION PRACTICE EXERCISES")
print("=" * 70)

# ============================================================================
# EXERCISE 1: Standardize Column Names
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE 1: Standardize Column Names")
print("=" * 70)

print("""
Task: Clean the column names in this DataFrame.
Convert to lowercase, replace spaces with underscores, and remove special characters.

Expected column names:
['observation_id', 'traffic_count', 'average_speed_mph', 'weather_condition', 'sensor_location']
""")

# Sample data with messy column names
data_ex1 = {
    'Observation-ID': [1, 2, 3, 4, 5],
    'Traffic Count': [1500, 2300, 1800, 2100, 1950],
    'Average Speed (mph)': [65, 58, 62, 70, 68],
    'Weather Condition': ['Clear', 'Rain', 'Cloudy', 'Clear', 'Fog'],
    'Sensor Location%': ['North', 'South', 'East', 'West', 'Central']
}

df_ex1 = pd.DataFrame(data_ex1)

print("\nOriginal column names:")
print(list(df_ex1.columns))

# YOUR CODE HERE
# Hint: Use .str methods on df_ex1.columns
# Solution steps:
# 1. Convert to lowercase
# 2. Replace spaces with underscores
# 3. Remove special characters: -, (), %
# 4. Clean up extra underscores

# Example solution (uncomment to use):
# df_ex1.columns = df_ex1.columns.str.lower()
# df_ex1.columns = df_ex1.columns.str.replace(' ', '_')
# df_ex1.columns = df_ex1.columns.str.replace(r'[()%\-]', '', regex=True)
# df_ex1.columns = df_ex1.columns.str.replace('_+', '_', regex=True)
# df_ex1.columns = df_ex1.columns.str.strip('_')

print("\nYour standardized column names:")
print(list(df_ex1.columns))

# ============================================================================
# EXERCISE 2: Standardize Text Data
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE 2: Standardize Text Data")
print("=" * 70)

print("""
Task: Clean the 'weather' column.
Convert to lowercase and strip whitespace.

Expected result: all values should be lowercase with no extra spaces.
""")

# Sample data with messy text
data_ex2 = {
    'hour': [8, 9, 10, 11, 12],
    'weather': ['  CLEAR  ', 'Rain', '  CLOUDY', 'clear', 'RAIN  '],
    'volume': [1200, 1500, 1300, 1400, 1600]
}

df_ex2 = pd.DataFrame(data_ex2)

print("\nBefore standardization:")
print(df_ex2['weather'].tolist())

# YOUR CODE HERE
# Hint: Use .str.strip() and .str.lower()
# Example: df_ex2['weather'] = ...

print("\nAfter standardization:")
print(df_ex2['weather'].tolist())

# ============================================================================
# EXERCISE 3: Convert String Numbers to Numeric
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE 3: Convert String Numbers to Numeric")
print("=" * 70)

print("""
Task: Convert the 'speed' column from string to numeric type.

Current type: object (string)
Expected type: int64 or float64
""")

# Sample data with string numbers
data_ex3 = {
    'time': ['08:00', '09:00', '10:00', '11:00', '12:00'],
    'speed': ['65', '72', '58', '68', '70'],
    'volume': [1200, 1500, 1300, 1400, 1600]
}

df_ex3 = pd.DataFrame(data_ex3)

print(f"\nBefore conversion - speed type: {df_ex3['speed'].dtype}")
print(df_ex3['speed'].tolist())

# YOUR CODE HERE
# Hint: Use pd.to_numeric()
# Example: df_ex3['speed'] = pd.to_numeric(...)

print(f"\nAfter conversion - speed type: {df_ex3['speed'].dtype}")
print(df_ex3['speed'].tolist())

# Check if you can now do math
try:
    avg_speed = df_ex3['speed'].mean()
    print(f"\nAverage speed: {avg_speed:.2f} mph")
    print("[OK] Speed column is now numeric!")
except TypeError:
    print("\n[ERROR] Speed column is still not numeric. Try again!")

# ============================================================================
# EXERCISE 4: Convert Dates to Datetime
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE 4: Convert Dates to Datetime")
print("=" * 70)

print("""
Task: Convert the 'date' column from string to datetime type.

Current type: object (string)
Expected type: datetime64[ns]
""")

# Sample data with date strings
data_ex4 = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'traffic_volume': [3200, 3600, 4100, 3800, 4300]
}

df_ex4 = pd.DataFrame(data_ex4)

print(f"\nBefore conversion - date type: {df_ex4['date'].dtype}")
print(df_ex4['date'].tolist())

# YOUR CODE HERE
# Hint: Use pd.to_datetime()
# Example: df_ex4['date'] = pd.to_datetime(...)

print(f"\nAfter conversion - date type: {df_ex4['date'].dtype}")
print(df_ex4['date'].tolist())

# Try extracting day of week
try:
    df_ex4['day_of_week'] = df_ex4['date'].dt.day_name()
    print("\nDay of week extraction:")
    print(df_ex4[['date', 'day_of_week']])
    print("[OK] Date column is now datetime!")
except AttributeError:
    print("\n[ERROR] Date column is still not datetime. Try again!")

# ============================================================================
# EXERCISE 5: Complete Standardization Challenge
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE 5: Complete Standardization Challenge")
print("=" * 70)

print("""
Task: Apply complete standardization to this messy DataFrame.

Requirements:
1. Standardize all column names
2. Standardize 'Location Name' text (lowercase, strip whitespace)
3. Convert 'Speed (mph)' from string to numeric
4. Convert 'Date' from string to datetime

This is a comprehensive exercise combining all previous skills.
""")

# Complete messy dataset
data_ex5 = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Traffic Volume (cars)': [3200, 3600, 4100, 3800, 4300],
    'Speed (mph)': ['65', '58', '72', '68', '70'],
    'Location Name': ['  Downtown  ', 'HIGHWAY', '  Suburban  ', 'Rural', 'URBAN  '],
    'Weather%Type': ['Clear', 'Rain', 'Cloudy', 'Clear', 'Fog']
}

df_ex5 = pd.DataFrame(data_ex5)

print("\n--- BEFORE STANDARDIZATION ---")
print("\nColumn names:")
print(list(df_ex5.columns))
print("\nData types:")
print(df_ex5.dtypes)
print("\nFirst 3 rows:")
print(df_ex5.head(3))

# YOUR CODE HERE
# Step 1: Standardize column names
# ...

# Step 2: Standardize 'location_name' text (after column names are fixed)
# ...

# Step 3: Convert 'speed_mph' to numeric
# ...

# Step 4: Convert 'date' to datetime
# ...

print("\n--- AFTER STANDARDIZATION ---")
print("\nColumn names:")
print(list(df_ex5.columns))
print("\nData types:")
print(df_ex5.dtypes)
print("\nFirst 3 rows:")
print(df_ex5.head(3))

# ============================================================================
# BONUS: Create a Standardization Function
# ============================================================================
print("\n" + "=" * 70)
print("BONUS: Create a Standardization Function")
print("=" * 70)

print("""
Challenge: Create a reusable function that standardizes any DataFrame.

Function should:
- Standardize column names
- Accept lists of text columns, numeric columns, and date columns
- Apply appropriate standardization to each column type
- Return the cleaned DataFrame
""")

def standardize_dataframe(df, text_cols=None, numeric_cols=None, date_cols=None):
    """
    Apply complete standardization to a DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input DataFrame to standardize
    text_cols : list, optional
        Original column names to standardize as text (lowercase + strip)
    numeric_cols : list, optional
        Original column names to convert to numeric
    date_cols : list, optional
        Original column names to convert to datetime
    
    Returns:
    --------
    pandas.DataFrame
        Fully standardized DataFrame
    """
    # YOUR CODE HERE
    # Implement the function logic
    
    # Step 1: Standardize column names
    # Step 2: Create a mapping of old names to new names
    # Step 3: Apply text standardization
    # Step 4: Apply numeric conversion
    # Step 5: Apply date conversion
    
    return df  # Replace with your implementation

# Test your function
test_data = {
    'Test Column': ['  VALUE  ', 'data', '  ANOTHER'],
    'Number (units)': ['10', '20', '30'],
    'Date-Time': ['2023-01-01', '2023-01-02', '2023-01-03']
}
df_test = pd.DataFrame(test_data)

print("\nBefore using your function:")
print(df_test)
print("\nColumn types:", df_test.dtypes.tolist())

# Uncomment when your function is ready:
# df_result = standardize_dataframe(
#     df_test,
#     text_cols=['Test Column'],
#     numeric_cols=['Number (units)'],
#     date_cols=['Date-Time']
# )
# print("\nAfter using your function:")
# print(df_result)
# print("\nColumn types:", df_result.dtypes.tolist())

# ============================================================================
# COMPLETION MESSAGE
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE SESSION COMPLETE")
print("=" * 70)
print("""
Review your work:
✓ Did you standardize all column names to snake_case?
✓ Did you clean text data (lowercase + strip whitespace)?
✓ Did you convert string numbers to numeric types?
✓ Did you convert date strings to datetime objects?
✓ Can you now perform calculations on numeric columns?
✓ Can you now extract date components from datetime columns?

Remember:
- Standardization should happen EARLY in your workflow
- Be CONSISTENT across all datasets
- Create REUSABLE functions for common tasks
- Always VERIFY your changes with head() and dtypes

Keep practicing! Clean data is the foundation of good analysis.
""")
