"""
Missing Values Handling Demo
==============================
This script demonstrates strategies for handling missing data in Pandas.
It covers both dropping and filling strategies with clear explanations.

Learning Objectives:
- Understand when to drop vs fill missing values
- Apply drop strategies safely
- Apply fill strategies appropriately
- Make informed decisions based on data context
"""

import pandas as pd
import numpy as np

print("=" * 70)
print("MISSING VALUES HANDLING DEMONSTRATION")
print("=" * 70)

# ============================================================================
# SECTION 1: CREATING A DATASET WITH MISSING VALUES
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 1: Creating Sample Data with Missing Values")
print("=" * 70)

# Create a realistic traffic dataset with missing values
data = {
    'date_time': [
        '2023-01-02 08:00:00', '2023-01-02 09:00:00', '2023-01-02 10:00:00',
        '2023-01-02 11:00:00', '2023-01-02 12:00:00', '2023-01-02 13:00:00',
        '2023-01-02 14:00:00', '2023-01-02 15:00:00', '2023-01-02 16:00:00',
        '2023-01-02 17:00:00', '2023-01-02 18:00:00', '2023-01-02 19:00:00'
    ],
    'traffic_volume': [3600, 4300, np.nan, 3700, np.nan, 4600, 5100, np.nan, 5800, 6200, 5900, 4800],
    'temp': [44.5, 46.2, 48.1, 49.8, 51.5, 52.9, 54.2, np.nan, 55.8, 54.3, 52.1, 49.6],
    'weather_main': ['Clear', 'Clouds', 'Rain', 'Clear', 'Rain', 'Clear', 'Clouds', 'Clear', np.nan, 'Clear', 'Clouds', 'Rain'],
    'sensor_id': [101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101],
    'maintenance_notes': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}

df_original = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df_original)
print(f"\nDataset Shape: {df_original.shape}")
print(f"Total cells: {df_original.shape[0] * df_original.shape[1]}")

# ============================================================================
# SECTION 2: IDENTIFYING MISSING VALUES
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 2: Identifying Missing Values")
print("=" * 70)

print("\nMissing values per column:")
missing_count = df_original.isnull().sum()
print(missing_count)

print("\nMissing values percentage per column:")
missing_percentage = (df_original.isnull().sum() / len(df_original)) * 100
print(missing_percentage.round(2))

print("\nTotal missing values in dataset:", df_original.isnull().sum().sum())

# Visualize missing data pattern
print("\nMissing data pattern (True = Missing):")
print(df_original.isnull())

# ============================================================================
# SECTION 3: STRATEGY 1 - DROPPING MISSING VALUES
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 3: DROPPING MISSING VALUES")
print("=" * 70)

# 3.1 Drop rows with ANY missing value
print("\n--- Strategy 3.1: Drop rows with ANY missing values ---")
df_drop_any = df_original.dropna()
print(f"Original shape: {df_original.shape}")
print(f"After dropping rows with ANY missing values: {df_drop_any.shape}")
print(f"Rows removed: {df_original.shape[0] - df_drop_any.shape[0]}")
print(f"Data retained: {(df_drop_any.shape[0] / df_original.shape[0]) * 100:.1f}%")
print("\nResult:")
print(df_drop_any)

print("\n⚠️  CAUTION: Dropped {}/{} rows ({:.1f}% data loss)".format(
    df_original.shape[0] - df_drop_any.shape[0],
    df_original.shape[0],
    ((df_original.shape[0] - df_drop_any.shape[0]) / df_original.shape[0]) * 100
))
print("This is too aggressive for this dataset!")

# 3.2 Drop rows with ALL values missing
print("\n--- Strategy 3.2: Drop rows where ALL values are missing ---")
df_drop_all = df_original.dropna(how='all')
print(f"Original shape: {df_original.shape}")
print(f"After dropping rows where ALL values are missing: {df_drop_all.shape}")
print(f"Rows removed: {df_original.shape[0] - df_drop_all.shape[0]}")
print("✅ This is safer - only removes completely empty rows")

# 3.3 Drop rows with missing values in specific columns
print("\n--- Strategy 3.3: Drop rows with missing values in CRITICAL columns ---")
# For traffic analysis, traffic_volume is critical
df_drop_subset = df_original.dropna(subset=['traffic_volume'])
print(f"Dropping rows where 'traffic_volume' is missing")
print(f"Original shape: {df_original.shape}")
print(f"After dropping: {df_drop_subset.shape}")
print(f"Rows removed: {df_original.shape[0] - df_drop_subset.shape[0]}")
print("\nResult:")
print(df_drop_subset)
print("\n✅ Better strategy: Only drop rows where critical data is missing")

# 3.4 Drop columns with excessive missing data
print("\n--- Strategy 3.4: Drop columns with EXCESSIVE missing values ---")
# maintenance_notes has 100% missing data
missing_percentage_by_col = (df_original.isnull().sum() / len(df_original)) * 100
print(f"\nColumns with >50% missing data:")
columns_to_drop = missing_percentage_by_col[missing_percentage_by_col > 50].index.tolist()
print(columns_to_drop)

df_drop_cols = df_original.drop(columns=columns_to_drop)
print(f"\nOriginal shape: {df_original.shape}")
print(f"After dropping columns: {df_drop_cols.shape}")
print(f"Columns removed: {columns_to_drop}")
print("\n✅ Removed columns with no useful data")

# ============================================================================
# SECTION 4: STRATEGY 2 - FILLING MISSING VALUES
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 4: FILLING MISSING VALUES")
print("=" * 70)

# 4.1 Fill with a constant
print("\n--- Strategy 4.1: Fill with a CONSTANT value ---")
df_fill_constant = df_original.copy()
df_fill_constant['weather_main'] = df_fill_constant['weather_main'].fillna('Unknown')
print("Filled 'weather_main' missing values with 'Unknown'")
print("\nBefore:")
print(df_original['weather_main'])
print("\nAfter:")
print(df_fill_constant['weather_main'])
print("\n✅ Good for categorical data where 'Unknown' is meaningful")

# 4.2 Fill numeric columns with mean
print("\n--- Strategy 4.2: Fill numeric columns with MEAN ---")
df_fill_mean = df_original.copy()
mean_traffic = df_fill_mean['traffic_volume'].mean()
df_fill_mean['traffic_volume'] = df_fill_mean['traffic_volume'].fillna(mean_traffic)
print(f"Filled 'traffic_volume' missing values with mean: {mean_traffic:.2f}")
print("\nBefore:")
print(df_original['traffic_volume'])
print("\nAfter:")
print(df_fill_mean['traffic_volume'])
print("\n⚠️  Note: Mean can be affected by outliers")

# 4.3 Fill numeric columns with median
print("\n--- Strategy 4.3: Fill numeric columns with MEDIAN ---")
df_fill_median = df_original.copy()
median_traffic = df_fill_median['traffic_volume'].median()
df_fill_median['traffic_volume'] = df_fill_median['traffic_volume'].fillna(median_traffic)
print(f"Filled 'traffic_volume' missing values with median: {median_traffic:.2f}")
print("\nBefore:")
print(df_original['traffic_volume'])
print("\nAfter:")
print(df_fill_median['traffic_volume'])
print("\n✅ Median is more robust to outliers than mean")

# 4.4 Fill categorical columns with mode
print("\n--- Strategy 4.4: Fill categorical columns with MODE (most frequent) ---")
df_fill_mode = df_original.copy()
mode_weather = df_fill_mode['weather_main'].mode()[0]
df_fill_mode['weather_main'] = df_fill_mode['weather_main'].fillna(mode_weather)
print(f"Filled 'weather_main' missing values with mode: '{mode_weather}'")
print("\nBefore:")
print(df_original['weather_main'].value_counts())
print("\nAfter:")
print(df_fill_mode['weather_main'].value_counts())
print("\n✅ Mode is appropriate for categorical data")

# 4.5 Fill with forward fill (propagate last valid value)
print("\n--- Strategy 4.5: Forward Fill (propagate last valid value) ---")
df_fill_forward = df_original.copy()
df_fill_forward['temp'] = df_fill_forward['temp'].fillna(method='ffill')
print("Forward filled 'temp' column")
print("\nBefore:")
print(df_original['temp'])
print("\nAfter:")
print(df_fill_forward['temp'])
print("\n✅ Good for time-series data where values change gradually")

# 4.6 Fill with backward fill
print("\n--- Strategy 4.6: Backward Fill (propagate next valid value) ---")
df_fill_backward = df_original.copy()
df_fill_backward['temp'] = df_fill_backward['temp'].fillna(method='bfill')
print("Backward filled 'temp' column")
print("\nBefore:")
print(df_original['temp'])
print("\nAfter:")
print(df_fill_backward['temp'])
print("\n✅ Alternative for time-series data")

# ============================================================================
# SECTION 5: COMPREHENSIVE CLEANING STRATEGY
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 5: COMPREHENSIVE CLEANING STRATEGY")
print("=" * 70)

print("\nApplying a thoughtful, combined strategy:")
df_cleaned = df_original.copy()

# Step 1: Drop columns with >50% missing data
print("\nStep 1: Drop columns with excessive missing data (>50%)")
df_cleaned = df_cleaned.drop(columns=columns_to_drop)
print(f"   Dropped columns: {columns_to_drop}")

# Step 2: Fill numeric columns with median (more robust than mean)
print("\nStep 2: Fill numeric columns with median")
df_cleaned['traffic_volume'] = df_cleaned['traffic_volume'].fillna(df_cleaned['traffic_volume'].median())
df_cleaned['temp'] = df_cleaned['temp'].fillna(df_cleaned['temp'].median())
print("   Filled 'traffic_volume' and 'temp' with their medians")

# Step 3: Fill categorical columns with mode
print("\nStep 3: Fill categorical columns with mode")
df_cleaned['weather_main'] = df_cleaned['weather_main'].fillna(df_cleaned['weather_main'].mode()[0])
print("   Filled 'weather_main' with mode")

# Verify no missing values remain
print("\nFinal missing values check:")
print(df_cleaned.isnull().sum())

print("\n✅ Dataset is now clean and ready for analysis!")
print(f"\nOriginal shape: {df_original.shape}")
print(f"Cleaned shape: {df_cleaned.shape}")
print(f"Data retained: 100% of rows, {df_cleaned.shape[1]}/{df_original.shape[1]} columns")

print("\nCleaned Dataset:")
print(df_cleaned)

# ============================================================================
# SECTION 6: COMPARING STRATEGIES
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 6: COMPARING DROP vs FILL STRATEGIES")
print("=" * 70)

print("\n📊 COMPARISON TABLE:")
print("-" * 70)

strategies = {
    'Original': df_original,
    'Drop ANY missing': df_drop_any,
    'Drop subset (traffic_volume)': df_drop_subset,
    'Fill with mean': df_fill_mean,
    'Fill with median': df_fill_median,
    'Comprehensive strategy': df_cleaned
}

comparison_data = []
for name, df in strategies.items():
    comparison_data.append({
        'Strategy': name,
        'Rows': df.shape[0],
        'Columns': df.shape[1],
        'Total Cells': df.shape[0] * df.shape[1],
        'Missing Values': df.isnull().sum().sum(),
        'Data Retained': f"{(df.shape[0] / df_original.shape[0]) * 100:.1f}%"
    })

comparison_df = pd.DataFrame(comparison_data)
print(comparison_df.to_string(index=False))

# ============================================================================
# SECTION 7: DECISION GUIDELINES
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 7: DECISION GUIDELINES")
print("=" * 70)

print("""
When to DROP missing values:
✓ Column has >70% missing data (little useful information)
✓ Row is completely empty
✓ Missing data is in a critical column (e.g., target variable)
✓ Dataset is large enough to afford data loss
✓ Missing data pattern seems non-random (systematically missing)

When to FILL missing values:
✓ Missing data is <20% of column
✓ Column is important for analysis
✓ Dataset is small and can't afford data loss
✓ Missing values appear randomly
✓ You can justify the filling method

How to CHOOSE filling method:
→ Use MEDIAN for numeric data (robust to outliers)
→ Use MODE for categorical data
→ Use FORWARD/BACKWARD FILL for time-series data
→ Use CONSTANT (e.g., 0, 'Unknown') when it makes domain sense
→ AVOID using MEAN if data has outliers

Common MISTAKES to avoid:
✗ Dropping data without checking impact
✗ Filling categorical data with numeric values
✗ Using mean when median is more appropriate
✗ Filling without documenting your decision
✗ Not verifying the cleaned data
""")

# ============================================================================
# SECTION 8: VERIFICATION
# ============================================================================
print("\n" + "=" * 70)
print("SECTION 8: FINAL VERIFICATION")
print("=" * 70)

print("\n✅ Verification Checklist:")
print(f"1. No missing values remain: {df_cleaned.isnull().sum().sum() == 0}")
print(f"2. Shape is reasonable: {df_cleaned.shape}")
print(f"3. Data types preserved correctly:")
print(df_cleaned.dtypes)
print(f"\n4. Summary statistics look reasonable:")
print(df_cleaned[['traffic_volume', 'temp']].describe())

print("\n" + "=" * 70)
print("✅ MISSING VALUES HANDLING DEMONSTRATION COMPLETE")
print("=" * 70)
print("\nKey Takeaway:")
print("Always make INTENTIONAL decisions about missing data.")
print("Document your choices and verify the results.")
print("=" * 70)
