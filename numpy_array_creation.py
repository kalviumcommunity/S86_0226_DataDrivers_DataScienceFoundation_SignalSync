#!/usr/bin/env python3
"""
Creating NumPy Arrays from Python Lists
========================================
A comprehensive demonstration of converting Python lists to NumPy arrays.

This is the CORE skill for starting with NumPy and data science.

Learning Objectives:
- Import NumPy properly
- Create 1D arrays from lists
- Create 2D arrays from nested lists
- Create multi-dimensional arrays
- Understand array creation patterns
"""

import numpy as np

print("=" * 70)
print("CREATING NUMPY ARRAYS FROM PYTHON LISTS")
print("=" * 70)

# =============================================================================
# SECTION 1: IMPORTING NUMPY
# =============================================================================
print("\n📦 SECTION 1: IMPORTING NUMPY")
print("-" * 70)

print("Standard way to import NumPy:")
print("import numpy as np")
print()
print("✅ 'np' is the standard alias used everywhere")
print("✅ Makes code shorter and more readable")
print("✅ Everyone in data science uses this convention")


# =============================================================================
# SECTION 2: CREATING 1D ARRAYS (ONE-DIMENSIONAL)
# =============================================================================
print("\n\n1️⃣  SECTION 2: CREATING 1D ARRAYS")
print("-" * 70)

print("\n--- Example 1: Basic 1D array from a list ---")
traffic_list = [850, 1200, 450, 980, 1500, 670]
traffic_array = np.array(traffic_list)

print(f"Python list: {traffic_list}")
print(f"NumPy array: {traffic_array}")
print(f"Type: {type(traffic_array)}")
print()

print("--- Example 2: Creating array directly ---")
speeds = np.array([45, 60, 72, 55, 80, 65])
print(f"Speeds array: {speeds}")
print("You can pass the list directly to np.array()")
print()

print("--- Example 3: Different data types ---")
temperatures = np.array([22.5, 24.0, 23.8, 25.2, 21.9])
print(f"Temperatures (floats): {temperatures}")

prices = np.array([100, 250, 150, 300])
print(f"Prices (integers): {prices}")
print()

print("--- Example 4: Creating from range ---")
sequence = np.array(range(10))
print(f"Array from range(10): {sequence}")

even_numbers = np.array(range(0, 20, 2))
print(f"Even numbers: {even_numbers}")


# =============================================================================
# SECTION 3: CREATING 2D ARRAYS (TWO-DIMENSIONAL)
# =============================================================================
print("\n\n2️⃣  SECTION 3: CREATING 2D ARRAYS")
print("-" * 70)

print("\n--- Example 1: 2D array from nested lists ---")
# Traffic data: rows = different locations, columns = hours
traffic_data = [
    [850, 1200, 450],  # Location 1
    [980, 1500, 670],  # Location 2
    [720, 1350, 890]   # Location 3
]
traffic_2d = np.array(traffic_data)

print("Python nested list:")
for row in traffic_data:
    print(f"  {row}")

print(f"\nNumPy 2D array:")
print(traffic_2d)
print()

print("--- Example 2: Temperature readings (3 sensors, 4 time points) ---")
temperatures = np.array([
    [22.5, 23.0, 23.5, 24.0],  # Sensor 1
    [21.8, 22.2, 22.8, 23.1],  # Sensor 2
    [23.1, 23.5, 24.0, 24.5]   # Sensor 3
])
print("Temperature data:")
print(temperatures)
print()

print("--- Example 3: Small matrix ---")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("3x3 matrix:")
print(matrix)


# =============================================================================
# SECTION 4: CREATING 3D ARRAYS (THREE-DIMENSIONAL)
# =============================================================================
print("\n\n3️⃣  SECTION 4: CREATING 3D ARRAYS")
print("-" * 70)

print("\n--- Example: Traffic data across multiple days ---")
# Dimensions: [days, locations, hours]
traffic_3d = np.array([
    # Day 1
    [
        [850, 1200, 450],  # Location 1
        [980, 1500, 670]   # Location 2
    ],
    # Day 2
    [
        [920, 1350, 520],  # Location 1
        [1100, 1600, 720]  # Location 2
    ]
])

print("Shape: 2 days × 2 locations × 3 hours")
print(f"3D array shape: {traffic_3d.shape}")
print("\nData:")
print(traffic_3d)
print()
print("Accessing Day 1 data:")
print(traffic_3d[0])


# =============================================================================
# SECTION 5: ARRAY CREATION PATTERNS
# =============================================================================
print("\n\n🎨 SECTION 5: COMMON ARRAY CREATION PATTERNS")
print("-" * 70)

print("\n--- Pattern 1: From existing Python list ---")
my_list = [10, 20, 30, 40, 50]
my_array = np.array(my_list)
print(f"List: {my_list}")
print(f"Array: {my_array}")
print()

print("--- Pattern 2: Direct inline creation ---")
direct_array = np.array([100, 200, 300, 400])
print(f"Direct: {direct_array}")
print()

print("--- Pattern 3: From list comprehension ---")
squared = np.array([x**2 for x in range(1, 6)])
print(f"Squared [1-5]: {squared}")
print()

print("--- Pattern 4: From multiple lists (2D) ---")
row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]
combined = np.array([row1, row2, row3])
print("Combined rows into 2D array:")
print(combined)


# =============================================================================
# SECTION 6: DATA TYPE HANDLING
# =============================================================================
print("\n\n🔢 SECTION 6: DATA TYPE HANDLING")
print("-" * 70)

print("\n--- Example 1: Integer array ---")
integers = np.array([10, 20, 30, 40])
print(f"Array: {integers}")
print(f"Data type: {integers.dtype}")
print()

print("--- Example 2: Float array ---")
floats = np.array([10.5, 20.3, 30.7, 40.2])
print(f"Array: {floats}")
print(f"Data type: {floats.dtype}")
print()

print("--- Example 3: Mixed numbers (auto-conversion) ---")
mixed = np.array([10, 20.5, 30, 40.7])
print(f"Array: {mixed}")
print(f"Data type: {mixed.dtype}")
print("NumPy converts to float64 to accommodate all values")
print()

print("--- Example 4: Specifying data type explicitly ---")
specified = np.array([10, 20, 30], dtype=float)
print(f"Array: {specified}")
print(f"Data type: {specified.dtype}")


# =============================================================================
# SECTION 7: VERIFYING ARRAY CREATION
# =============================================================================
print("\n\n✅ SECTION 7: VERIFYING ARRAY CREATION")
print("-" * 70)

test_array = np.array([100, 200, 300, 400, 500])

print("\nArray created:")
print(f"Data: {test_array}")
print(f"Type: {type(test_array)}")
print(f"Data type: {test_array.dtype}")
print(f"Shape: {test_array.shape}")
print(f"Number of dimensions: {test_array.ndim}")
print(f"Size (total elements): {test_array.size}")

print("\n✅ All checks confirm this is a NumPy array!")


# =============================================================================
# SECTION 8: COMMON MISTAKES TO AVOID
# =============================================================================
print("\n\n⚠️  SECTION 8: COMMON MISTAKES TO AVOID")
print("-" * 70)

print("\n❌ MISTAKE 1: Forgetting np.array()")
print("Wrong: my_array = [1, 2, 3]")
print("Right: my_array = np.array([1, 2, 3])")
print()

print("❌ MISTAKE 2: Inconsistent 2D array dimensions")
print("This will cause problems:")
print("bad_array = np.array([[1, 2], [3, 4, 5]])")
print("Rows must have the same length!")
print()

print("❌ MISTAKE 3: Using quotes around numbers")
print("Wrong: np.array(['1', '2', '3'])  # strings!")
print("Right: np.array([1, 2, 3])        # numbers")
print()

print("✅ MISTAKE 4: Mixing incompatible types")
print("Be careful with: np.array([1, 2, 'three'])")
mixed_types = np.array([1, 2, 'three'])
print(f"Result: {mixed_types}")
print(f"Type: {mixed_types.dtype}")
print("NumPy converts everything to strings!")


# =============================================================================
# SECTION 9: PRACTICAL EXAMPLES
# =============================================================================
print("\n\n🚦 SECTION 9: PRACTICAL TRAFFIC ANALYSIS EXAMPLES")
print("-" * 70)

print("\n--- Example 1: Daily traffic counts ---")
daily_counts = np.array([1200, 1350, 980, 1500, 1650, 1420, 1100])
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print("Daily traffic volumes:")
for day, count in zip(days, daily_counts):
    print(f"  {day}: {count} vehicles")
print(f"\nWeekly average: {daily_counts.mean():.0f} vehicles/day")
print(f"Peak day: {daily_counts.max()} vehicles")
print()

print("--- Example 2: Speed measurements at different times ---")
speed_data = np.array([
    [45, 60, 55, 50],  # Morning
    [70, 75, 72, 68],  # Afternoon
    [55, 65, 62, 58]   # Evening
])
print("Speed data (3 periods × 4 measurements):")
print(speed_data)
print(f"\nAverage speed: {speed_data.mean():.1f} km/h")
print(f"Highest speed: {speed_data.max()} km/h")
print()

print("--- Example 3: Sensor readings ---")
sensor_readings = np.array([23.5, 24.2, 23.8, 25.1, 24.6])
print(f"Sensor readings: {sensor_readings}")
print(f"Mean: {sensor_readings.mean():.2f}")
print(f"Std dev: {sensor_readings.std():.2f}")


# =============================================================================
# SUMMARY
# =============================================================================
print("\n\n" + "=" * 70)
print("📚 SUMMARY: CREATING NUMPY ARRAYS")
print("=" * 70)

print("""
KEY STEPS:
1. Import NumPy:          import numpy as np
2. Create 1D array:       array_1d = np.array([1, 2, 3])
3. Create 2D array:       array_2d = np.array([[1, 2], [3, 4]])
4. Check properties:      array.shape, array.dtype, array.ndim

REMEMBER:
✅ Use np.array() to convert lists to arrays
✅ Lists → 1D arrays, Nested lists → 2D arrays
✅ All elements become the same data type
✅ NumPy arrays are optimized for numeric operations

NEXT STEPS:
→ Learn to inspect array properties in detail
→ Perform operations on arrays
→ Use arrays for real data analysis
""")

print("=" * 70)
print("🎉 You now know how to create NumPy arrays from Python lists!")
print("=" * 70)
