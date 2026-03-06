"""
Pandas Series Practice Exercises
=================================
Complete these exercises to solidify your understanding of Pandas Series.

Instructions:
- Write your code below each exercise prompt
- Run the file to test your solutions
- Uncomment the print statements to verify your answers
"""

import pandas as pd
import numpy as np

print("=" * 70)
print("PANDAS SERIES PRACTICE EXERCISES")
print("=" * 70)
print()

# ==============================================================================
# EXERCISE 1: Create Series from Lists
# ==============================================================================
print("EXERCISE 1: Create Series from Lists")
print("-" * 70)
print("Task: Create a Series from the following list of student ages:")
print("      [18, 19, 20, 18, 21, 19, 22]")
print()

# TODO: Create the Series here
# student_ages = pd.Series([...])

# Uncomment to test:
# print("Student Ages Series:")
# print(student_ages)
print()

# ==============================================================================
# EXERCISE 2: Create Series from NumPy Array
# ==============================================================================
print("EXERCISE 2: Create Series from NumPy Array")
print("-" * 70)
print("Task: Create a NumPy array of 6 random integers between 50 and 100,")
print("      then convert it to a Pandas Series.")
print()

# TODO: Create NumPy array and convert to Series
# np.random.seed(42)  # for reproducibility
# random_array = np.random.randint(...)
# random_series = pd.Series(...)

# Uncomment to test:
# print("Random Scores Series:")
# print(random_series)
print()

# ==============================================================================
# EXERCISE 3: Custom Index
# ==============================================================================
print("EXERCISE 3: Custom Index")
print("-" * 70)
print("Task: Create a Series with the following data and custom index:")
print("      Data: [100, 200, 300, 400, 500]")
print("      Index: ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']")
print()

# TODO: Create Series with custom index
# quarterly_sales = pd.Series(...)

# Uncomment to test:
# print("Quarterly Sales:")
# print(quarterly_sales)
print()

# ==============================================================================
# EXERCISE 4: Access Index and Values
# ==============================================================================
print("EXERCISE 4: Access Index and Values")
print("-" * 70)
print("Task: Given the Series below, extract and print:")
print("      a) The index")
print("      b) The values")
print("      c) The data type")
print()

physics_scores = pd.Series([88, 92, 76, 85, 90])

# TODO: Extract index, values, and dtype
# index_result = ...
# values_result = ...
# dtype_result = ...

# Uncomment to test:
# print(f"Index: {index_result}")
# print(f"Values: {values_result}")
# print(f"Data Type: {dtype_result}")
print()

# ==============================================================================
# EXERCISE 5: Label-based Access
# ==============================================================================
print("EXERCISE 5: Label-based Access")
print("-" * 70)
print("Task: Create a Series of temperatures with day names as index,")
print("      then access the temperature for 'Wednesday'")
print()

# TODO: Create temperature Series and access Wednesday's temperature
# temperatures = pd.Series(
#     data=[...],
#     index=[...]
# )
# wednesday_temp = ...

# Uncomment to test:
# print("Temperature Series:")
# print(temperatures)
# print(f"\nWednesday's temperature: {wednesday_temp}°C")
print()

# ==============================================================================
# EXERCISE 6: Arithmetic Operations
# ==============================================================================
print("EXERCISE 6: Arithmetic Operations")
print("-" * 70)
print("Task: Given product prices, calculate:")
print("      a) Prices after 15% discount")
print("      b) Prices after adding ₹50 shipping")
print()

product_prices = pd.Series([500, 750, 1200, 300, 950],
                           index=['Product_A', 'Product_B', 'Product_C',
                                  'Product_D', 'Product_E'])

# TODO: Perform calculations
# discounted_prices = ...
# prices_with_shipping = ...

# Uncomment to test:
# print("Original Prices:")
# print(product_prices)
# print("\nAfter 15% discount:")
# print(discounted_prices)
# print("\nAfter adding ₹50 shipping:")
# print(prices_with_shipping)
print()

# ==============================================================================
# EXERCISE 7: Statistical Operations
# ==============================================================================
print("EXERCISE 7: Statistical Operations")
print("-" * 70)
print("Task: Calculate mean, median, max, min for the test scores below")
print()

test_scores = pd.Series([85, 92, 78, 88, 95, 82, 90, 87])

# TODO: Calculate statistics
# mean_score = ...
# median_score = ...
# max_score = ...
# min_score = ...

# Uncomment to test:
# print("Test Scores Statistics:")
# print(f"Mean: {mean_score}")
# print(f"Median: {median_score}")
# print(f"Maximum: {max_score}")
# print(f"Minimum: {min_score}")
print()

# ==============================================================================
# EXERCISE 8: Boolean Indexing
# ==============================================================================
print("EXERCISE 8: Boolean Indexing")
print("-" * 70)
print("Task: Filter employees with salary > 50000 from the Series below")
print()

salaries = pd.Series([45000, 55000, 62000, 48000, 71000, 52000],
                     index=['Emp1', 'Emp2', 'Emp3', 'Emp4', 'Emp5', 'Emp6'])

# TODO: Filter high salaries
# high_salaries = ...

# Uncomment to test:
# print("Original Salaries:")
# print(salaries)
# print("\nEmployees with salary > ₹50,000:")
# print(high_salaries)
print()

# ==============================================================================
# EXERCISE 9: Series from Dictionary
# ==============================================================================
print("EXERCISE 9: Series from Dictionary")
print("-" * 70)
print("Task: Create a Series from a dictionary of city populations")
print()

# TODO: Create dictionary and convert to Series
# city_population = {
#     'Mumbai': 20_000_000,
#     'Delhi': 30_000_000,
#     'Bangalore': 12_000_000,
#     'Hyderabad': 10_000_000
# }
# population_series = pd.Series(...)

# Uncomment to test:
# print("City Populations:")
# print(population_series)
print()

# ==============================================================================
# EXERCISE 10: Series Alignment
# ==============================================================================
print("EXERCISE 10: Series Alignment")
print("-" * 70)
print("Task: Add two Series with different indexes and observe alignment")
print()

january_sales = pd.Series([100, 150, 200], index=['A', 'B', 'C'])
february_sales = pd.Series([120, 180, 160], index=['B', 'C', 'D'])

# TODO: Add the two Series
# total_sales = ...

# Uncomment to test:
# print("January Sales:")
# print(january_sales)
# print("\nFebruary Sales:")
# print(february_sales)
# print("\nTotal Sales (notice NaN for mismatched indexes):")
# print(total_sales)
print()

# ==============================================================================
# SOLUTIONS
# ==============================================================================
print("=" * 70)
print("Uncomment the solution section below to check your answers")
print("=" * 70)

# SOLUTION 1
student_ages = pd.Series([18, 19, 20, 18, 21, 19, 22])

# SOLUTION 2
np.random.seed(42)
random_array = np.random.randint(50, 101, size=6)
random_series = pd.Series(random_array)

# SOLUTION 3
quarterly_sales = pd.Series([100, 200, 300, 400, 500],
                            index=['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])

# SOLUTION 4
index_result = physics_scores.index
values_result = physics_scores.values
dtype_result = physics_scores.dtype

# SOLUTION 5
temperatures = pd.Series(
    data=[22, 24, 26, 25, 23, 21, 20],
    index=['Monday', 'Tuesday', 'Wednesday', 'Thursday',
           'Friday', 'Saturday', 'Sunday']
)
wednesday_temp = temperatures['Wednesday']

# SOLUTION 6
discounted_prices = product_prices * 0.85
prices_with_shipping = product_prices + 50

# SOLUTION 7
mean_score = test_scores.mean()
median_score = test_scores.median()
max_score = test_scores.max()
min_score = test_scores.min()

# SOLUTION 8
high_salaries = salaries[salaries > 50000]

# SOLUTION 9
city_population = {
    'Mumbai': 20_000_000,
    'Delhi': 30_000_000,
    'Bangalore': 12_000_000,
    'Hyderabad': 10_000_000
}
population_series = pd.Series(city_population)

# SOLUTION 10
total_sales = january_sales + february_sales

print("\n✓ Solutions are defined. Uncomment print statements to verify!")
