"""
Summary Statistics Demonstration Script
========================================
SignalSync Project - Data Drivers Team

This script demonstrates how to compute and interpret basic summary statistics
for individual columns in Pandas DataFrames. Summary statistics help you quickly
understand the distribution, central tendency, and spread of your data.

Learning Objectives:
- Understand what summary statistics represent
- Compute basic statistics for numeric columns
- Interpret statistical outputs correctly
- Compare statistics across different columns
- Build intuition about data distributions
"""

import pandas as pd
import numpy as np
import os

# Print header
print("=" * 70)
print("PANDAS SUMMARY STATISTICS DEMONSTRATION")
print("SignalSync Project - Data Drivers Team")
print("=" * 70)
print()

# ==============================================================================
# LOAD SAMPLE DATA
# ==============================================================================
print("LOADING SAMPLE DATA")
print("-" * 70)

csv_file = 'traffic_sample.csv'
if os.path.exists(csv_file):
    print(f"✓ Loading '{csv_file}'...")
    traffic_df = pd.read_csv(csv_file)
    print(f"✓ Data loaded successfully!")
    print()
else:
    print(f"✗ File '{csv_file}' not found")
    print("Please ensure the CSV file is in the same folder as this script.")
    exit()

# Quick preview of the data
print("First 5 rows of the dataset:")
print(traffic_df.head())
print()

# ==============================================================================
# PART 1: Understanding Common Summary Statistics
# ==============================================================================
print("=" * 70)
print("PART 1: UNDERSTANDING COMMON SUMMARY STATISTICS")
print("-" * 70)
print("""
Summary statistics provide a quick numerical overview of your data.
Each statistic tells us something different about the data distribution:

KEY STATISTICS:
- Count: Number of non-missing values
- Mean: Average value (sum ÷ count)
- Median: Middle value when sorted (50th percentile)
- Min: Smallest value in the column
- Max: Largest value in the column
- Std (Standard Deviation): Measure of data spread/variability

WHY THESE MATTER:
- Mean vs Median reveals skewness and outliers
- Min/Max shows the data range
- Std tells us how spread out the values are
- Count reveals missing data issues
""")
print()

# ==============================================================================
# PART 2: Computing Statistics for a Single Column
# ==============================================================================
print("=" * 70)
print("PART 2: COMPUTING STATISTICS FOR A SINGLE COLUMN")
print("-" * 70)
print("Let's analyze the 'traffic_volume' column step by step.\n")

# Select a single column
traffic_volume = traffic_df['traffic_volume']

print("2.1 Computing Individual Statistics")
print("-" * 70)
print(f"Count:  {traffic_volume.count()}")
print(f"Mean:   {traffic_volume.mean():.2f}")
print(f"Median: {traffic_volume.median():.2f}")
print(f"Min:    {traffic_volume.min():.2f}")
print(f"Max:    {traffic_volume.max():.2f}")
print(f"Std:    {traffic_volume.std():.2f}")
print()

print("2.2 Using .describe() for All Statistics at Once")
print("-" * 70)
print("The .describe() method computes all main statistics in one call:\n")
print(traffic_df['traffic_volume'].describe())
print()

print("2.3 Additional Useful Statistics")
print("-" * 70)
print(f"Sum:    {traffic_volume.sum():.2f}")
print(f"Var:    {traffic_volume.var():.2f} (Variance = Std²)")
print(f"25%:    {traffic_volume.quantile(0.25):.2f} (1st Quartile)")
print(f"75%:    {traffic_volume.quantile(0.75):.2f} (3rd Quartile)")
print()

# ==============================================================================
# PART 3: Interpreting Results Correctly
# ==============================================================================
print("=" * 70)
print("PART 3: INTERPRETING RESULTS CORRECTLY")
print("-" * 70)

mean_val = traffic_volume.mean()
median_val = traffic_volume.median()
min_val = traffic_volume.min()
max_val = traffic_volume.max()
std_val = traffic_volume.std()

print("\nINTERPRETATION OF TRAFFIC VOLUME STATISTICS:\n")

print(f"1. Central Tendency:")
print(f"   - Mean:   {mean_val:.2f} vehicles")
print(f"   - Median: {median_val:.2f} vehicles")

if abs(mean_val - median_val) < 100:
    print("   → Mean ≈ Median: Data is fairly symmetric")
elif mean_val > median_val:
    print("   → Mean > Median: Data may be right-skewed (high outliers)")
else:
    print("   → Mean < Median: Data may be left-skewed (low outliers)")
print()

print(f"2. Range:")
print(f"   - Min: {min_val:.2f} vehicles")
print(f"   - Max: {max_val:.2f} vehicles")
print(f"   - Range: {max_val - min_val:.2f} vehicles")
print("   → This shows the full spread of traffic volumes observed")
print()

print(f"3. Variability:")
print(f"   - Std: {std_val:.2f}")
print(f"   → On average, values deviate from the mean by ±{std_val:.2f} vehicles")

if std_val / mean_val < 0.25:
    print("   → Low variability: Traffic volume is relatively consistent")
elif std_val / mean_val > 0.5:
    print("   → High variability: Traffic volume varies significantly")
else:
    print("   → Moderate variability: Some variation in traffic volume")
print()

print(f"4. Typical Range (Mean ± 1 Std):")
print(f"   - Lower: {mean_val - std_val:.2f}")
print(f"   - Upper: {mean_val + std_val:.2f}")
print("   → About 68% of data falls within this range (assuming normal distribution)")
print()

# ==============================================================================
# PART 4: Comparing Columns Using Statistics
# ==============================================================================
print("=" * 70)
print("PART 4: COMPARING COLUMNS USING STATISTICS")
print("-" * 70)
print("Let's compare statistics across different numeric columns.\n")

print("4.1 Statistics for 'temp' (Temperature)")
print("-" * 70)
temp_stats = traffic_df['temp'].describe()
print(temp_stats)
print()

print("4.2 Side-by-Side Comparison")
print("-" * 70)
print("Comparing Traffic Volume vs Temperature:\n")

comparison_df = pd.DataFrame({
    'Statistic': ['Count', 'Mean', 'Median', 'Min', 'Max', 'Std'],
    'Traffic Volume': [
        traffic_volume.count(),
        traffic_volume.mean(),
        traffic_volume.median(),
        traffic_volume.min(),
        traffic_volume.max(),
        traffic_volume.std()
    ],
    'Temperature': [
        traffic_df['temp'].count(),
        traffic_df['temp'].mean(),
        traffic_df['temp'].median(),
        traffic_df['temp'].min(),
        traffic_df['temp'].max(),
        traffic_df['temp'].std()
    ]
})

print(comparison_df.to_string(index=False))
print()

print("4.3 Comparing All Numeric Columns at Once")
print("-" * 70)
print("Using .describe() on the entire DataFrame:\n")
print(traffic_df.describe())
print()

print("INSIGHTS FROM COMPARISON:")
print("-" * 70)
print(f"→ Traffic Volume varies from {traffic_volume.min():.0f} to {traffic_volume.max():.0f}")
print(f"→ Temperature varies from {traffic_df['temp'].min():.1f}°F to {traffic_df['temp'].max():.1f}°F")
print(f"→ Traffic Volume has higher relative variability (Std/Mean)")
print(f"→ Both columns have complete data (count = {len(traffic_df)})")
print()

# ==============================================================================
# PART 5: Identifying Unusual Values Using Statistics
# ==============================================================================
print("=" * 70)
print("PART 5: IDENTIFYING UNUSUAL VALUES USING STATISTICS")
print("-" * 70)
print("Statistics help us identify potential outliers or unusual patterns.\n")

print("5.1 Defining Unusual Values")
print("-" * 70)
print("Values beyond Mean ± 2 Std are considered unusual (occur ~5% of the time)")
print()

lower_bound = mean_val - 2 * std_val
upper_bound = mean_val + 2 * std_val

print(f"For Traffic Volume:")
print(f"  Mean: {mean_val:.2f}")
print(f"  Std:  {std_val:.2f}")
print(f"  Normal range: {lower_bound:.2f} to {upper_bound:.2f}")
print()

unusual_low = traffic_df[traffic_df['traffic_volume'] < lower_bound]
unusual_high = traffic_df[traffic_df['traffic_volume'] > upper_bound]

print(f"  Unusually LOW values:  {len(unusual_low)} records")
print(f"  Unusually HIGH values: {len(unusual_high)} records")

if len(unusual_high) > 0:
    print(f"\nHigh traffic volume outliers:")
    print(unusual_high[['date_time', 'traffic_volume']])
    
if len(unusual_low) > 0:
    print(f"\nLow traffic volume outliers:")
    print(unusual_low[['date_time', 'traffic_volume']])
    
if len(unusual_low) == 0 and len(unusual_high) == 0:
    print("\n✓ No unusual values detected in this dataset")

print()

# ==============================================================================
# PART 6: Best Practices and Common Pitfalls
# ==============================================================================
print("=" * 70)
print("PART 6: BEST PRACTICES AND COMMON PITFALLS")
print("-" * 70)
print("""
BEST PRACTICES:
✓ Always compute summary statistics before analysis
✓ Compare mean vs median to detect skewness
✓ Consider spread (std) alongside central tendency
✓ Check count to identify missing data
✓ Use statistics to guide further investigation

COMMON PITFALLS:
✗ Relying only on mean without checking median and std
✗ Ignoring outliers that heavily influence the mean
✗ Not checking for missing values (look at count)
✗ Comparing statistics without considering scale differences
✗ Making conclusions from statistics alone without context

INTERPRETATION REMINDER:
- Statistics describe data, they don't explain WHY
- Always combine statistics with visual inspection
- Context matters: What's "normal" depends on your domain
- Outliers might be errors OR important insights
""")
print()

# ==============================================================================
# SUMMARY
# ==============================================================================
print("=" * 70)
print("SUMMARY")
print("-" * 70)
print("""
You have learned to:
✓ Understand what each summary statistic represents
✓ Compute statistics for individual columns
✓ Interpret mean, median, min, max, and std correctly
✓ Compare statistics across multiple columns
✓ Identify unusual values using statistical rules
✓ Avoid common interpretation mistakes

KEY TAKEAWAYS:
1. Summary statistics provide a quick numerical overview
2. Mean vs Median reveals data distribution shape
3. Standard deviation shows data variability
4. Always compute statistics BEFORE modeling or analysis
5. Use statistics to ask better questions about your data

NEXT STEPS:
→ Combine statistics with visualizations (histograms, box plots)
→ Investigate unusual values or outliers
→ Use statistics to validate data quality
→ Apply statistical thinking to feature engineering
""")
print()

print("=" * 70)
print("END OF DEMONSTRATION")
print("=" * 70)
