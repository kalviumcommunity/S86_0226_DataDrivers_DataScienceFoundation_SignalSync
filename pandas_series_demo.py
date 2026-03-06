"""
Pandas Series Fundamentals Demo
================================
This module demonstrates the creation and manipulation of Pandas Series.

Learning Objectives:
1. Understand what a Pandas Series is
2. Create a Series from Python lists
3. Create a Series from NumPy arrays
4. Understand index and values in a Series
5. Compare Series behavior with NumPy arrays
"""

import pandas as pd
import numpy as np

print("=" * 70)
print("PANDAS SERIES FUNDAMENTALS")
print("=" * 70)
print()

# ==============================================================================
# 1. UNDERSTANDING PANDAS SERIES
# ==============================================================================
print("1. UNDERSTANDING PANDAS SERIES")
print("-" * 70)
print("A Pandas Series is a one-dimensional labeled array.")
print("It consists of two main components:")
print("  - Values: The actual data")
print("  - Index: Labels for each value")
print()

# Creating a simple Series to demonstrate
simple_series = pd.Series([10, 20, 30, 40, 50])
print("Example Series:")
print(simple_series)
print()
print("Notice the two columns:")
print("  - Left column: Index (0, 1, 2, 3, 4)")
print("  - Right column: Values (10, 20, 30, 40, 50)")
print("  - Bottom line: Data type (int64)")
print()

# ==============================================================================
# 2. CREATING A SERIES FROM PYTHON LISTS
# ==============================================================================
print("=" * 70)
print("2. CREATING A SERIES FROM PYTHON LISTS")
print("-" * 70)

# Example 1: Numeric list
temperatures = [23, 25, 27, 26, 24, 22, 21]
temp_series = pd.Series(temperatures)
print("Series from numeric list (Daily temperatures in °C):")
print(temp_series)
print()

# Example 2: String list
cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai']
cities_series = pd.Series(cities)
print("Series from string list (Indian cities):")
print(cities_series)
print()

# Example 3: Mixed numeric types
scores = [85.5, 92.0, 78.5, 88.0, 95.5]
scores_series = pd.Series(scores)
print("Series from float list (Student scores):")
print(scores_series)
print()

# Automatic index creation
print("Key Observation:")
print("  → Pandas automatically creates an index starting from 0")
print("  → Index increases by 1 for each element")
print("  → This is called the 'default integer index'")
print()

# ==============================================================================
# 3. CREATING A SERIES FROM NUMPY ARRAYS
# ==============================================================================
print("=" * 70)
print("3. CREATING A SERIES FROM NUMPY ARRAYS")
print("-" * 70)

# Example 1: 1D NumPy array
array_data = np.array([100, 200, 300, 400, 500])
array_series = pd.Series(array_data)
print("Series from NumPy array:")
print(array_series)
print()

# Example 2: Array with specific dtype
float_array = np.array([1.5, 2.5, 3.5, 4.5], dtype=np.float64)
float_series = pd.Series(float_array)
print("Series from NumPy float array:")
print(float_series)
print()

# Example 3: Using NumPy functions
random_data = np.random.randint(10, 100, size=5)
random_series = pd.Series(random_data)
print("Series from randomly generated NumPy array:")
print(random_series)
print()

# Data type preservation
print("Data Type Preservation:")
print(f"  NumPy array dtype: {array_data.dtype}")
print(f"  Pandas Series dtype: {array_series.dtype}")
print("  → Data types are preserved when converting from NumPy to Pandas")
print()

# ==============================================================================
# 4. UNDERSTANDING INDEX AND VALUES
# ==============================================================================
print("=" * 70)
print("4. UNDERSTANDING INDEX AND VALUES")
print("-" * 70)

# Create a sample Series
sample_data = pd.Series([45, 67, 89, 91, 78])
print("Sample Series:")
print(sample_data)
print()

# Accessing the index
print("Accessing the Index:")
print(f"  series.index → {sample_data.index}")
print(f"  Type: {type(sample_data.index)}")
print()

# Accessing the values
print("Accessing the Values:")
print(f"  series.values → {sample_data.values}")
print(f"  Type: {type(sample_data.values)}")
print("  Note: values returns a NumPy array!")
print()

# Creating a Series with custom index
print("Creating a Series with Custom Index:")
custom_series = pd.Series(
    data=[95, 87, 92, 88, 90],
    index=['Math', 'Science', 'English', 'History', 'Geography']
)
print(custom_series)
print()
print(f"Custom index: {custom_series.index.tolist()}")
print()

# Positional vs Label-based access
print("Positional Access (using integer position):")
print(f"  custom_series.iloc[0] → {custom_series.iloc[0]}")
print(f"  custom_series.iloc[2] → {custom_series.iloc[2]}")
print()

print("Label-based Access (using index labels):")
print(f"  custom_series['Math'] → {custom_series['Math']}")
print(f"  custom_series['English'] → {custom_series['English']}")
print()

print("Key Insight:")
print("  → Index labels add MEANING to your data")
print("  → You can access data by position OR by label")
print("  → This makes data more intuitive and self-documenting")
print()

# ==============================================================================
# 5. COMPARING SERIES BEHAVIOR WITH NUMPY ARRAYS
# ==============================================================================
print("=" * 70)
print("5. COMPARING SERIES BEHAVIOR WITH NUMPY ARRAYS")
print("-" * 70)

# Create comparable data structures
numpy_arr = np.array([10, 20, 30, 40, 50])
pandas_ser = pd.Series([10, 20, 30, 40, 50])

print("NumPy Array:")
print(numpy_arr)
print()

print("Pandas Series:")
print(pandas_ser)
print()

# Similarity: Vectorization
print("Similarity: Both support vectorized operations")
print(f"  NumPy: {numpy_arr} * 2 = {numpy_arr * 2}")
print(f"  Pandas: {pandas_ser.values} * 2 = ")
print(pandas_ser * 2)
print()

# Difference: Indexing
print("Difference: Indexing capabilities")
labeled_series = pd.Series(
    [10, 20, 30, 40, 50],
    index=['A', 'B', 'C', 'D', 'E']
)
print("Series with labels:")
print(labeled_series)
print(f"\nAccess by label: labeled_series['C'] = {labeled_series['C']}")
print("  → NumPy arrays cannot do this!")
print()

# Difference: Alignment
print("Difference: Automatic alignment in operations")
series1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])
print("Series 1:")
print(series1)
print("\nSeries 2:")
print(series2)
print("\nSeries 1 + Series 2 (note alignment by index):")
print(series1 + series2)
print("  → Pandas aligns data by index labels automatically")
print("  → NaN appears when labels don't match")
print()

# ==============================================================================
# 6. SIMPLE OPERATIONS ON A SERIES
# ==============================================================================
print("=" * 70)
print("6. SIMPLE OPERATIONS ON A SERIES")
print("-" * 70)

# Create a sample Series for operations
prices = pd.Series([250, 450, 380, 520, 290],
                   index=['Item_A', 'Item_B', 'Item_C', 'Item_D', 'Item_E'])
print("Product Prices (in ₹):")
print(prices)
print()

# Arithmetic operations
print("Arithmetic Operations:")
print(f"  Add 50 to all prices: \n{prices + 50}\n")
print(f"  Apply 10% discount: \n{prices * 0.9}\n")

# Statistical operations
print("Statistical Operations:")
print(f"  Mean price: ₹{prices.mean():.2f}")
print(f"  Median price: ₹{prices.median():.2f}")
print(f"  Max price: ₹{prices.max()}")
print(f"  Min price: ₹{prices.min()}")
print(f"  Standard deviation: ₹{prices.std():.2f}")
print()

# Boolean indexing
print("Boolean Indexing (Filter products > ₹400):")
expensive_items = prices[prices > 400]
print(expensive_items)
print()

# Summary statistics
print("Summary Statistics:")
print(prices.describe())
print()

# ==============================================================================
# 7. WHY SERIES ARE USEFUL - SUMMARY
# ==============================================================================
print("=" * 70)
print("7. WHY PANDAS SERIES ARE USEFUL")
print("-" * 70)
print("""
Key Benefits of Pandas Series:

1. LABELED DATA
   → Each value has a meaningful label (index)
   → Makes data self-documenting and intuitive

2. ALIGNMENT
   → Operations automatically align data by labels
   → Prevents common data misalignment errors

3. INTEGRATION
   → Works seamlessly with DataFrames
   → Foundation for more complex data structures

4. FLEXIBILITY
   → Can hold any data type (int, float, string, objects)
   → Custom indexing for domain-specific needs

5. RICH FUNCTIONALITY
   → Built-in statistical methods
   → Easy filtering and selection
   → Handles missing data gracefully

Series = NumPy Array + Labels + Extra Features
""")

print("=" * 70)
print("DEMO COMPLETE - You're ready to work with Pandas Series!")
print("=" * 70)
