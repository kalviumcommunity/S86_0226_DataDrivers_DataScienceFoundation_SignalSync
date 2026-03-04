#!/usr/bin/env python3
"""
NumPy Arrays vs Python Lists - Understanding the Difference
============================================================
This file demonstrates why NumPy arrays are preferred over Python lists
for numerical computing in data science.

Learning Objectives:
- Understand the limitations of Python lists for numeric data
- See the benefits of NumPy arrays
- Compare performance and functionality
- Learn when to use arrays vs lists
"""

import numpy as np
import time

print("=" * 70)
print("NUMPY ARRAYS vs PYTHON LISTS")
print("=" * 70)

# =============================================================================
# PART 1: PYTHON LISTS - LIMITATIONS FOR NUMERIC DATA
# =============================================================================
print("\n📋 PART 1: PYTHON LISTS FOR NUMERIC DATA")
print("-" * 70)

# Creating a Python list of traffic volumes
traffic_volumes_list = [850, 1200, 450, 980, 1500, 670, 920]

print("Python List:")
print(f"Data: {traffic_volumes_list}")
print(f"Type: {type(traffic_volumes_list)}")

# Problem 1: Element-wise operations don't work
print("\n❌ PROBLEM 1: Cannot do direct math on lists")
print("Trying to multiply all values by 2:")
print("traffic_volumes_list * 2")
print(f"Result: {traffic_volumes_list * 2}")
print("^ This just repeats the list, doesn't multiply each element!")

# Problem 2: Need loops for element-wise operations
print("\n❌ PROBLEM 2: Need loops for simple operations")
print("To multiply each element, you need a loop:")
doubled_list = [x * 2 for x in traffic_volumes_list]
print(f"Result: {doubled_list}")
print("This is slow and verbose!")

# Problem 3: Lists can contain mixed types (not ideal for numeric data)
print("\n❌ PROBLEM 3: Lists allow mixed types")
mixed_list = [100, "hello", 3.14, True]
print(f"Mixed list: {mixed_list}")
print("This can cause errors in numeric computations!")

# Problem 4: No built-in statistical functions
print("\n❌ PROBLEM 4: Limited built-in functions")
print("For statistics, you need to import or write your own:")
print(f"Sum: {sum(traffic_volumes_list)}")
print(f"Length: {len(traffic_volumes_list)}")
print(f"Average: {sum(traffic_volumes_list) / len(traffic_volumes_list)}")
print("No built-in mean(), std(), max() directly on the list!")


# =============================================================================
# PART 2: NUMPY ARRAYS - DESIGNED FOR NUMERIC DATA
# =============================================================================
print("\n\n🔢 PART 2: NUMPY ARRAYS FOR NUMERIC DATA")
print("-" * 70)

# Creating a NumPy array from the same data
traffic_volumes_array = np.array([850, 1200, 450, 980, 1500, 670, 920])

print("NumPy Array:")
print(f"Data: {traffic_volumes_array}")
print(f"Type: {type(traffic_volumes_array)}")

# Benefit 1: Element-wise operations work directly
print("\n✅ BENEFIT 1: Direct element-wise math")
print("Multiplying all values by 2:")
print("traffic_volumes_array * 2")
print(f"Result: {traffic_volumes_array * 2}")
print("^ Each element is multiplied - no loop needed!")

# Benefit 2: Fast and efficient
print("\n✅ BENEFIT 2: Built for performance")
print("Operations are vectorized and optimized in C")
print("Much faster than Python loops on large data")

# Benefit 3: Homogeneous data (all same type)
print("\n✅ BENEFIT 3: Enforces consistent data types")
mixed_array = np.array([100, 3.14, 5, 7.5])
print(f"Array with mixed numbers: {mixed_array}")
print(f"Data type: {mixed_array.dtype}")
print("NumPy automatically converts to compatible type (float)")

# Benefit 4: Rich set of built-in functions
print("\n✅ BENEFIT 4: Powerful built-in functions")
print(f"Mean: {traffic_volumes_array.mean():.2f}")
print(f"Standard deviation: {traffic_volumes_array.std():.2f}")
print(f"Min: {traffic_volumes_array.min()}")
print(f"Max: {traffic_volumes_array.max()}")
print(f"Sum: {traffic_volumes_array.sum()}")
print("All built-in and optimized!")


# =============================================================================
# PART 3: SIDE-BY-SIDE COMPARISON
# =============================================================================
print("\n\n⚖️  PART 3: DIRECT COMPARISON")
print("-" * 70)

# Example: Calculate average of values above 1000
print("Task: Calculate average of values > 1000\n")

# Using Python list
print("PYTHON LIST approach:")
print("values_above_1000 = [x for x in traffic_volumes_list if x > 1000]")
print("average = sum(values_above_1000) / len(values_above_1000)")
values_above_1000 = [x for x in traffic_volumes_list if x > 1000]
average_list = sum(values_above_1000) / len(values_above_1000)
print(f"Result: {average_list:.2f}")
print("Lines of code: 2-3, requires loop comprehension\n")

# Using NumPy array
print("NUMPY ARRAY approach:")
print("average = traffic_volumes_array[traffic_volumes_array > 1000].mean()")
average_array = traffic_volumes_array[traffic_volumes_array > 1000].mean()
print(f"Result: {average_array:.2f}")
print("Lines of code: 1, clean and readable!")


# =============================================================================
# PART 4: PERFORMANCE COMPARISON
# =============================================================================
print("\n\n⚡ PART 4: PERFORMANCE COMPARISON")
print("-" * 70)

# Create larger datasets
size = 100000
large_list = list(range(size))
large_array = np.array(large_list)

print(f"Testing with {size:,} elements\n")

# Time list operation
start = time.time()
result_list = [x * 2 + 5 for x in large_list]
time_list = time.time() - start

# Time array operation
start = time.time()
result_array = large_array * 2 + 5
time_array = time.time() - start

print(f"Python List time: {time_list*1000:.4f} ms")
print(f"NumPy Array time: {time_array*1000:.4f} ms")
print(f"Speed improvement: {time_list/time_array:.1f}x faster with NumPy!")


# =============================================================================
# PART 5: WHEN TO USE WHAT
# =============================================================================
print("\n\n🎯 PART 5: WHEN TO USE LISTS vs ARRAYS")
print("-" * 70)

print("\n✅ USE PYTHON LISTS when:")
print("  • Storing mixed data types (strings, numbers, objects)")
print("  • Working with small datasets")
print("  • Need dynamic resizing frequently")
print("  • Data is not primarily numeric")
print("  • Example: ['user1', 'user2', 'user3']")

print("\n✅ USE NUMPY ARRAYS when:")
print("  • Working with numeric data")
print("  • Need mathematical operations")
print("  • Processing large datasets")
print("  • Performing statistical analysis")
print("  • Example: [850, 1200, 450, 980] (traffic volumes)")


# =============================================================================
# SUMMARY
# =============================================================================
print("\n\n" + "=" * 70)
print("📊 SUMMARY: WHY NUMPY FOR DATA SCIENCE")
print("=" * 70)

print("\nPython Lists:")
print("  ❌ Slow for numeric operations")
print("  ❌ No element-wise math")
print("  ❌ Limited statistical functions")
print("  ❌ Not optimized for numerical computing")

print("\nNumPy Arrays:")
print("  ✅ Fast and memory-efficient")
print("  ✅ Element-wise operations built-in")
print("  ✅ Rich mathematical functions")
print("  ✅ Foundation for Pandas, SciPy, ML libraries")

print("\n🎯 KEY TAKEAWAY:")
print("NumPy arrays are THE standard for numerical computing in Python.")
print("Every data science library (Pandas, SciPy, scikit-learn, TensorFlow)")
print("is built on top of NumPy arrays.")

print("\n" + "=" * 70)
print("Next: Learn how to CREATE NumPy arrays from Python lists!")
print("=" * 70)
