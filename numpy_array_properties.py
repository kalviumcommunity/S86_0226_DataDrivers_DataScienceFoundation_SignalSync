#!/usr/bin/env python3
"""
Inspecting NumPy Array Properties and Basic Operations
=======================================================
Learn to understand and work with NumPy array properties.

Learning Objectives:
- Inspect array shape and dimensions
- Understand data types
- Perform basic array operations
- Compare array behavior with lists
"""

import numpy as np

print("=" * 70)
print("INSPECTING NUMPY ARRAY PROPERTIES")
print("=" * 70)

# =============================================================================
# SECTION 1: ARRAY SHAPE
# =============================================================================
print("\n📐 SECTION 1: UNDERSTANDING ARRAY SHAPE")
print("-" * 70)

print("\n--- Example 1: 1D Array Shape ---")
array_1d = np.array([10, 20, 30, 40, 50])
print(f"Array: {array_1d}")
print(f"Shape: {array_1d.shape}")
print(f"Meaning: ({array_1d.shape[0]},) = 5 elements in one dimension")
print()

print("--- Example 2: 2D Array Shape ---")
array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(f"Array:\n{array_2d}")
print(f"Shape: {array_2d.shape}")
print(f"Meaning: {array_2d.shape[0]} rows × {array_2d.shape[1]} columns")
print()

print("--- Example 3: Traffic Data (3 locations × 4 hours) ---")
traffic = np.array([
    [850, 1200, 450, 980],
    [1500, 670, 920, 1100],
    [780, 1350, 890, 1050]
])
print(f"Traffic array:\n{traffic}")
print(f"Shape: {traffic.shape}")
print(f"This is a {traffic.shape[0]}×{traffic.shape[1]} array")
print(f"→ {traffic.shape[0]} locations")
print(f"→ {traffic.shape[1]} time periods")
print()

print("--- Example 4: 3D Array Shape ---")
array_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(f"3D Array shape: {array_3d.shape}")
print(
    f"Meaning: {array_3d.shape[0]} × {array_3d.shape[1]} × {array_3d.shape[2]}")


# =============================================================================
# SECTION 2: ARRAY DIMENSIONS (ndim)
# =============================================================================
print("\n\n📊 SECTION 2: NUMBER OF DIMENSIONS")
print("-" * 70)

# Different dimensional arrays
scalar = np.array(42)
vector = np.array([1, 2, 3, 4])
matrix = np.array([[1, 2], [3, 4], [5, 6]])
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(f"Scalar (single number): {scalar}")
print(f"  Dimensions: {scalar.ndim}D")
print(f"  Shape: {scalar.shape}")
print()

print(f"Vector (1D array): {vector}")
print(f"  Dimensions: {vector.ndim}D")
print(f"  Shape: {vector.shape}")
print()

print(f"Matrix (2D array):\n{matrix}")
print(f"  Dimensions: {matrix.ndim}D")
print(f"  Shape: {matrix.shape}")
print()

print(f"Tensor (3D array):\n{tensor}")
print(f"  Dimensions: {tensor.ndim}D")
print(f"  Shape: {tensor.shape}")


# =============================================================================
# SECTION 3: DATA TYPES (dtype)
# =============================================================================
print("\n\n🔢 SECTION 3: ARRAY DATA TYPES")
print("-" * 70)

print("\n--- Example 1: Integer arrays ---")
int_array = np.array([10, 20, 30, 40])
print(f"Array: {int_array}")
print(f"Data type: {int_array.dtype}")
print(f"Type name: {int_array.dtype.name}")
print()

print("--- Example 2: Float arrays ---")
float_array = np.array([10.5, 20.3, 30.7])
print(f"Array: {float_array}")
print(f"Data type: {float_array.dtype}")
print()

print("--- Example 3: Mixed numbers (auto-conversion) ---")
mixed = np.array([10, 20.5, 30])
print(f"Array: {mixed}")
print(f"Data type: {mixed.dtype}")
print("Note: 10 and 30 are converted to floats")
print()

print("--- Example 4: Boolean arrays ---")
bool_array = np.array([True, False, True, True])
print(f"Array: {bool_array}")
print(f"Data type: {bool_array.dtype}")
print()

print("--- Example 5: String arrays ---")
string_array = np.array(['red', 'yellow', 'green'])
print(f"Array: {string_array}")
print(f"Data type: {string_array.dtype}")


# =============================================================================
# SECTION 4: ARRAY SIZE AND LENGTH
# =============================================================================
print("\n\n📏 SECTION 4: ARRAY SIZE AND LENGTH")
print("-" * 70)

test_array = np.array([
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900],
    [1000, 1100, 1200]
])

print(f"Array:\n{test_array}")
print(f"\nshape: {test_array.shape} → (rows, columns)")
print(f"ndim: {test_array.ndim} → number of dimensions")
print(f"size: {test_array.size} → total number of elements")
print(f"len(): {len(test_array)} → length of first dimension (rows)")
print(f"dtype: {test_array.dtype} → data type of elements")

print("\n📌 Key Difference:")
print(f"  size = {test_array.size} is total elements")
print(f"  len() = {len(test_array)} is number of rows")


# =============================================================================
# SECTION 5: BASIC ARRAY OPERATIONS
# =============================================================================
print("\n\n🔧 SECTION 5: BASIC ARRAY OPERATIONS")
print("-" * 70)

traffic_volumes = np.array([850, 1200, 450, 980, 1500, 670])

print(f"Traffic volumes: {traffic_volumes}")
print()

print("--- Arithmetic Operations (element-wise) ---")
print(f"Original: {traffic_volumes}")
print(f"Add 100: {traffic_volumes + 100}")
print(f"Multiply by 2: {traffic_volumes * 2}")
print(f"Divide by 10: {traffic_volumes / 10}")
print(f"Subtract 200: {traffic_volumes - 200}")
print()

print("--- Statistical Operations ---")
print(f"Sum: {traffic_volumes.sum()}")
print(f"Mean (average): {traffic_volumes.mean():.2f}")
print(f"Median: {np.median(traffic_volumes):.2f}")
print(f"Standard deviation: {traffic_volumes.std():.2f}")
print(f"Minimum: {traffic_volumes.min()}")
print(f"Maximum: {traffic_volumes.max()}")
print(f"Range: {traffic_volumes.max() - traffic_volumes.min()}")
print()

print("--- Comparison Operations ---")
print(f"Values > 1000: {traffic_volumes > 1000}")
print(f"Count > 1000: {(traffic_volumes > 1000).sum()}")
print(f"Values == 850: {traffic_volumes == 850}")


# =============================================================================
# SECTION 6: ARRAY OPERATIONS vs LIST OPERATIONS
# =============================================================================
print("\n\n⚖️  SECTION 6: ARRAYS vs LISTS - OPERATION COMPARISON")
print("-" * 70)

# Create list and array with same data
data_list = [10, 20, 30, 40, 50]
data_array = np.array([10, 20, 30, 40, 50])

print("--- Addition ---")
print(f"List + 5: Not possible directly!")
print(f"Array + 5: {data_array + 5}")
print()

print("--- Multiplication ---")
print(f"List * 2: {data_list * 2}")
print(f"  ^ Repeats the list!")
print(f"Array * 2: {data_array * 2}")
print(f"  ^ Multiplies each element!")
print()

print("--- Sum ---")
print(f"List: sum(data_list) = {sum(data_list)}")
print(f"Array: data_array.sum() = {data_array.sum()}")
print()

print("--- Average ---")
print(f"List: sum(data_list)/len(data_list) = {sum(data_list)/len(data_list)}")
print(f"Array: data_array.mean() = {data_array.mean()}")


# =============================================================================
# SECTION 7: PRACTICAL INSPECTION WORKFLOW
# =============================================================================
print("\n\n🔍 SECTION 7: COMPLETE ARRAY INSPECTION WORKFLOW")
print("-" * 70)

# Create a sample array
sample_array = np.array([
    [22.5, 24.0, 23.8],
    [25.2, 21.9, 23.5],
    [24.1, 23.3, 22.8],
    [23.9, 24.7, 25.0]
])

print("When you receive a new array, inspect it like this:\n")
print("Step 1: Display the array")
print(sample_array)
print()

print("Step 2: Check the shape")
print(
    f"  shape: {sample_array.shape} → {sample_array.shape[0]} rows, {sample_array.shape[1]} columns")
print()

print("Step 3: Check dimensions")
print(f"  ndim: {sample_array.ndim}D array")
print()

print("Step 4: Check data type")
print(f"  dtype: {sample_array.dtype}")
print()

print("Step 5: Check size")
print(f"  size: {sample_array.size} total elements")
print()

print("Step 6: Basic statistics")
print(f"  min: {sample_array.min():.2f}")
print(f"  max: {sample_array.max():.2f}")
print(f"  mean: {sample_array.mean():.2f}")
print(f"  std: {sample_array.std():.2f}")

print("\n✅ Array fully inspected and understood!")


# =============================================================================
# SECTION 8: COMMON OPERATIONS SUMMARY
# =============================================================================
print("\n\n📋 SECTION 8: COMMON OPERATIONS REFERENCE")
print("-" * 70)

demo_array = np.array([100, 200, 300, 400, 500])

print(f"\nArray: {demo_array}\n")
print("Property inspection:")
print(f"  array.shape      → {demo_array.shape}")
print(f"  array.ndim       → {demo_array.ndim}")
print(f"  array.size       → {demo_array.size}")
print(f"  array.dtype      → {demo_array.dtype}")
print(f"  len(array)       → {len(demo_array)}")
print()

print("Statistical operations:")
print(f"  array.sum()      → {demo_array.sum()}")
print(f"  array.mean()     → {demo_array.mean()}")
print(f"  array.std()      → {demo_array.std():.2f}")
print(f"  array.min()      → {demo_array.min()}")
print(f"  array.max()      → {demo_array.max()}")
print()

print("Element-wise math:")
print(f"  array + 10       → {demo_array + 10}")
print(f"  array * 2        → {demo_array * 2}")
print(f"  array / 100      → {demo_array / 100}")
print()

print("Comparisons:")
print(f"  array > 250      → {demo_array > 250}")
print(f"  array == 300     → {demo_array == 300}")


# =============================================================================
# SUMMARY
# =============================================================================
print("\n\n" + "=" * 70)
print("📚 SUMMARY: ARRAY PROPERTIES AND OPERATIONS")
print("=" * 70)

print("""
KEY PROPERTIES:
  .shape    → dimensions (rows, columns, etc.)
  .ndim     → number of dimensions (1D, 2D, 3D, etc.)
  .size     → total number of elements
  .dtype    → data type (int64, float64, etc.)
  len()     → length of first dimension

KEY OPERATIONS:
  .sum()    → sum of all elements
  .mean()   → average value
  .std()    → standard deviation
  .min()    → minimum value
  .max()    → maximum value

ELEMENT-WISE MATH:
  array + n    → add n to every element
  array * n    → multiply every element by n
  array > n    → compare every element with n

REMEMBER:
✅ Always inspect shape and dtype when working with new arrays
✅ NumPy operations work on entire arrays at once (vectorized)
✅ Arrays are homogeneous (all same type)
✅ Element-wise operations are fast and clean
""")

print("=" * 70)
print("🎉 You can now inspect and operate on NumPy arrays!")
print("=" * 70)
