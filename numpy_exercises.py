#!/usr/bin/env python3
"""
Practice Exercises: Creating NumPy Arrays from Python Lists
============================================================
Complete these exercises to master NumPy array creation and operations.

Instructions:
- Each exercise tests your understanding of NumPy arrays
- Follow the TODO comments to complete each section
- Solutions are provided for learning
- Run the file to test your work
"""

import numpy as np

print("=" * 70)
print("PRACTICE EXERCISES: NUMPY ARRAYS FROM PYTHON LISTS")
print("=" * 70)

# =============================================================================
# EXERCISE 1: Create a Simple 1D Array
# =============================================================================
print("\n📝 EXERCISE 1: Create a 1D Array")
print("-" * 70)
print("Task: Convert the Python list to a NumPy array\n")

# Given list
vehicle_counts = [150, 200, 175, 220, 190]

# TODO: Create a NumPy array from the list
# YOUR CODE HERE:
vehicle_array = np.array(vehicle_counts)

# Display results
print(f"Original list: {vehicle_counts}")
print(f"NumPy array: {vehicle_array}")
print(f"Type: {type(vehicle_array)}")
print(f"Array shape: {vehicle_array.shape}")
print("✅ Exercise 1 Complete!\n")


# =============================================================================
# EXERCISE 2: Create a 2D Array
# =============================================================================
print("\n📝 EXERCISE 2: Create a 2D Array from Nested Lists")
print("-" * 70)
print("Task: Create a 2D array from traffic data\n")

# Given nested list (3 locations × 4 time periods)
traffic_data = [
    [850, 1200, 450, 980],
    [920, 1350, 670, 1100],
    [780, 1050, 890, 1200]
]

# TODO: Create a 2D NumPy array
# YOUR CODE HERE:
traffic_array = np.array(traffic_data)

# Display results
print("Traffic data (3 locations × 4 time periods):")
print(traffic_array)
print(f"\nShape: {traffic_array.shape}")
print(f"Dimensions: {traffic_array.ndim}D")
print(f"Total elements: {traffic_array.size}")
print("✅ Exercise 2 Complete!\n")


# =============================================================================
# EXERCISE 3: Inspect Array Properties
# =============================================================================
print("\n📝 EXERCISE 3: Inspect Array Properties")
print("-" * 70)
print("Task: Create an array and inspect all its properties\n")

# Create array from this list
temperatures = [22.5, 24.0, 23.8, 25.2, 21.9, 23.5, 24.6]

# TODO: Create array and inspect properties
# YOUR CODE HERE:
temp_array = np.array(temperatures)

print(f"Array: {temp_array}")
print(f"\nProperties:")
print(f"  Shape: {temp_array.shape}")
print(f"  Dimensions: {temp_array.ndim}")
print(f"  Size: {temp_array.size}")
print(f"  Data type: {temp_array.dtype}")
print(f"  Length: {len(temp_array)}")
print("✅ Exercise 3 Complete!\n")


# =============================================================================
# EXERCISE 4: Perform Basic Operations
# =============================================================================
print("\n📝 EXERCISE 4: Perform Basic Array Operations")
print("-" * 70)
print("Task: Calculate statistics on the array\n")

# Given array
speed_data = np.array([45, 60, 72, 55, 80, 65, 58, 70])

# TODO: Calculate various statistics
# YOUR CODE HERE:
total = speed_data.sum()
average = speed_data.mean()
minimum = speed_data.min()
maximum = speed_data.max()
std_dev = speed_data.std()

print(f"Speed data: {speed_data}")
print(f"\nStatistics:")
print(f"  Total: {total}")
print(f"  Average: {average:.2f} km/h")
print(f"  Minimum: {minimum} km/h")
print(f"  Maximum: {maximum} km/h")
print(f"  Std deviation: {std_dev:.2f}")
print("✅ Exercise 4 Complete!\n")


# =============================================================================
# EXERCISE 5: Element-wise Operations
# =============================================================================
print("\n📝 EXERCISE 5: Element-wise Arithmetic")
print("-" * 70)
print("Task: Perform element-wise operations on an array\n")

# Given array of prices
prices = np.array([100, 250, 150, 300, 200])

# TODO: Apply operations to the array
# YOUR CODE HERE:
increased_10_percent = prices * 1.10
discount_20 = prices - 20
doubled = prices * 2

print(f"Original prices: {prices}")
print(f"Increased by 10%: {increased_10_percent}")
print(f"$20 discount: {discount_20}")
print(f"Doubled: {doubled}")
print("✅ Exercise 5 Complete!\n")


# =============================================================================
# EXERCISE 6: Create Array from Range
# =============================================================================
print("\n📝 EXERCISE 6: Create Array from Range")
print("-" * 70)
print("Task: Create arrays using range()\n")

# TODO: Create array of numbers 1 to 10
# YOUR CODE HERE:
numbers_1_to_10 = np.array(range(1, 11))

# TODO: Create array of even numbers 0 to 20
# YOUR CODE HERE:
even_numbers = np.array(range(0, 21, 2))

print(f"Numbers 1-10: {numbers_1_to_10}")
print(f"Even numbers 0-20: {even_numbers}")
print("✅ Exercise 6 Complete!\n")


# =============================================================================
# EXERCISE 7: Array Comparisons
# =============================================================================
print("\n📝 EXERCISE 7: Boolean Comparisons")
print("-" * 70)
print("Task: Use comparison operations on arrays\n")

# Given traffic volume data
volumes = np.array([850, 1200, 450, 980, 1500, 670, 920])
threshold = 1000

# TODO: Find volumes above threshold
# YOUR CODE HERE:
above_threshold = volumes > threshold
count_above = above_threshold.sum()
high_volumes = volumes[above_threshold]

print(f"Traffic volumes: {volumes}")
print(f"Threshold: {threshold}")
print(f"Above threshold (boolean): {above_threshold}")
print(f"Count above threshold: {count_above}")
print(f"High volumes: {high_volumes}")
print("✅ Exercise 7 Complete!\n")


# =============================================================================
# EXERCISE 8: Create Multi-dimensional Array
# =============================================================================
print("\n📝 EXERCISE 8: Create and Analyze 2D Array")
print("-" * 70)
print("Task: Create a 2D array and calculate row/column statistics\n")

# Create a 2D array of sensor readings (4 sensors × 3 time points)
sensor_data = [
    [22.5, 23.0, 23.5],  # Sensor 1
    [21.8, 22.2, 22.8],  # Sensor 2
    [23.1, 23.5, 24.0],  # Sensor 3
    [22.0, 22.5, 23.0]   # Sensor 4
]

# TODO: Create 2D array and analyze
# YOUR CODE HERE:
sensor_array = np.array(sensor_data)
overall_mean = sensor_array.mean()
overall_max = sensor_array.max()
overall_min = sensor_array.min()

print("Sensor readings (4 sensors × 3 time points):")
print(sensor_array)
print(f"\nShape: {sensor_array.shape}")
print(f"Overall mean: {overall_mean:.2f}")
print(f"Overall max: {overall_max:.2f}")
print(f"Overall min: {overall_min:.2f}")
print("✅ Exercise 8 Complete!\n")


# =============================================================================
# EXERCISE 9: Data Type Handling
# =============================================================================
print("\n📝 EXERCISE 9: Understanding Data Types")
print("-" * 70)
print("Task: Create arrays with different data types\n")

# TODO: Create integer array
# YOUR CODE HERE:
int_array = np.array([10, 20, 30, 40, 50])

# TODO: Create float array
# YOUR CODE HERE:
float_array = np.array([10.5, 20.5, 30.5, 40.5, 50.5])

# TODO: Create boolean array
# YOUR CODE HERE:
bool_array = np.array([True, False, True, True, False])

print(f"Integer array: {int_array}")
print(f"  Data type: {int_array.dtype}")
print()
print(f"Float array: {float_array}")
print(f"  Data type: {float_array.dtype}")
print()
print(f"Boolean array: {bool_array}")
print(f"  Data type: {bool_array.dtype}")
print("✅ Exercise 9 Complete!\n")


# =============================================================================
# EXERCISE 10: Real-world Application
# =============================================================================
print("\n📝 EXERCISE 10: Real-world Traffic Analysis")
print("-" * 70)
print("Task: Analyze weekly traffic data\n")

# Weekly traffic counts
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
morning_traffic = [1200, 1350, 1280, 1400, 1450, 900, 750]
evening_traffic = [1500, 1600, 1550, 1650, 1700, 950, 800]

# TODO: Create arrays and perform analysis
# YOUR CODE HERE:
morning_array = np.array(morning_traffic)
evening_array = np.array(evening_traffic)

morning_avg = morning_array.mean()
evening_avg = evening_array.mean()
busiest_morning_idx = morning_array.argmax()
busiest_evening_idx = evening_array.argmax()
total_weekly = morning_array.sum() + evening_array.sum()

print("Weekly Traffic Analysis:")
print(f"\nMorning traffic: {morning_array}")
print(f"Morning average: {morning_avg:.0f} vehicles")
print(
    f"Busiest morning: {days[busiest_morning_idx]} ({morning_array[busiest_morning_idx]} vehicles)")
print()
print(f"Evening traffic: {evening_array}")
print(f"Evening average: {evening_avg:.0f} vehicles")
print(
    f"Busiest evening: {days[busiest_evening_idx]} ({evening_array[busiest_evening_idx]} vehicles)")
print()
print(f"Total weekly traffic: {total_weekly:,} vehicles")

# Compare morning vs evening
difference = evening_array - morning_array
print(f"\nEvening - Morning difference: {difference}")
print(f"Average difference: {difference.mean():.0f} more vehicles in evening")
print("✅ Exercise 10 Complete!\n")


# =============================================================================
# BONUS EXERCISE: Array Creation Patterns
# =============================================================================
print("\n🌟 BONUS EXERCISE: Various Creation Methods")
print("-" * 70)
print("Task: Create arrays using different methods\n")

# Method 1: From list
arr1 = np.array([1, 2, 3, 4, 5])
print(f"From list: {arr1}")

# Method 2: From range
arr2 = np.array(range(10, 51, 10))
print(f"From range: {arr2}")

# Method 3: From list comprehension
arr3 = np.array([x**2 for x in range(1, 6)])
print(f"From comprehension: {arr3}")

# Method 4: Nested lists to 2D
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D array:\n{arr4}")

# Method 5: With explicit dtype
arr5 = np.array([1, 2, 3], dtype=float)
print(f"With explicit dtype: {arr5} ({arr5.dtype})")

print("\n✅ Bonus Exercise Complete!\n")


# =============================================================================
# CONGRATULATIONS!
# =============================================================================
print("=" * 70)
print("🎉 ALL EXERCISES COMPLETED!")
print("=" * 70)

print("""
You have practiced:
  ✅ Creating 1D arrays from lists
  ✅ Creating 2D arrays from nested lists
  ✅ Inspecting array properties (shape, dtype, ndim, size)
  ✅ Performing basic operations (sum, mean, min, max, std)
  ✅ Element-wise arithmetic operations
  ✅ Creating arrays from range
  ✅ Boolean comparisons and filtering
  ✅ Working with multi-dimensional arrays
  ✅ Understanding data types
  ✅ Real-world traffic data analysis

KEY SKILLS MASTERED:
  1. Converting Python lists to NumPy arrays
  2. Understanding array structure and properties
  3. Performing vectorized operations
  4. Applying arrays to real-world problems

NEXT STEPS:
  → Learn advanced indexing and slicing
  → Explore more NumPy functions
  → Use arrays with Pandas DataFrames
  → Apply to real datasets

🚀 You're ready to work with NumPy arrays in data science projects!
""")

print("=" * 70)
