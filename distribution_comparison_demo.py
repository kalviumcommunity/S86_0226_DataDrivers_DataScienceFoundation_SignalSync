"""
Distribution Comparison Demonstration Script
=============================================
SignalSync Project - Data Drivers Team

This script demonstrates how to compare distributions across multiple columns
in Pandas DataFrames. Comparing distributions reveals patterns and relationships
that single-column analysis cannot show.

Learning Objectives:
- Understand what a data distribution represents
- Compare central tendency across columns
- Compare spread and variability across columns
- Identify differences and similarities between variables
- Build intuition for multi-column analysis
"""

import pandas as pd
import numpy as np
import os

# Print header
print("=" * 70)
print("COMPARING DISTRIBUTIONS ACROSS MULTIPLE COLUMNS")
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
print(f"Dataset has {len(traffic_df)} rows and {len(traffic_df.columns)} columns")
print(f"Numeric columns: {list(traffic_df.select_dtypes(include=[np.number]).columns)}")
print()

# ==============================================================================
# PART 1: Understanding Distributions Across Columns
# ==============================================================================
print("=" * 70)
print("PART 1: UNDERSTANDING DISTRIBUTIONS ACROSS COLUMNS")
print("-" * 70)
print("""
WHAT IS A DISTRIBUTION?
A distribution describes how values are spread across a column:
- Where the center is (mean, median)
- How spread out the values are (range, std)
- Whether there are outliers or unusual patterns

WHY COMPARE DISTRIBUTIONS?
- Understand how variables differ from each other
- Identify patterns and relationships
- Make informed analysis decisions
- Avoid comparing "apples to oranges"

KEY INSIGHT:
Don't just look at raw values - understand how each column behaves!
""")
print()

# ==============================================================================
# PART 2: Comparing Central Tendency Across Columns
# ==============================================================================
print("=" * 70)
print("PART 2: COMPARING CENTRAL TENDENCY ACROSS COLUMNS")
print("-" * 70)
print("Central tendency = 'typical' or 'average' value\n")

# Get all numeric columns
numeric_cols = traffic_df.select_dtypes(include=[np.number]).columns.tolist()

print("2.1 Computing Mean for All Numeric Columns")
print("-" * 70)
means = traffic_df[numeric_cols].mean()
print(means)
print()

print("2.2 Computing Median for All Numeric Columns")
print("-" * 70)
medians = traffic_df[numeric_cols].median()
print(medians)
print()

print("2.3 Side-by-Side Comparison of Central Tendency")
print("-" * 70)
central_comparison = pd.DataFrame({
    'Column': numeric_cols,
    'Mean': [traffic_df[col].mean() for col in numeric_cols],
    'Median': [traffic_df[col].median() for col in numeric_cols]
})
print(central_comparison.to_string(index=False))
print()

print("INTERPRETATION:")
print("-" * 70)
for col in numeric_cols:
    mean_val = traffic_df[col].mean()
    median_val = traffic_df[col].median()
    diff_pct = abs(mean_val - median_val) / median_val * 100 if median_val != 0 else 0
    
    print(f"\n{col}:")
    print(f"  Mean:   {mean_val:.2f}")
    print(f"  Median: {median_val:.2f}")
    print(f"  Difference: {diff_pct:.1f}%")
    
    if diff_pct < 5:
        print("  → Nearly symmetric distribution")
    elif mean_val > median_val:
        print("  → Right-skewed (high values pulling mean up)")
    else:
        print("  → Left-skewed (low values pulling mean down)")

print()

# ==============================================================================
# PART 3: Comparing Spread and Variability Across Columns
# ==============================================================================
print("=" * 70)
print("PART 3: COMPARING SPREAD AND VARIABILITY ACROSS COLUMNS")
print("-" * 70)
print("Spread = how much variation exists in the data\n")

print("3.1 Computing Range for All Numeric Columns")
print("-" * 70)
ranges = traffic_df[numeric_cols].max() - traffic_df[numeric_cols].min()
print(ranges)
print()

print("3.2 Computing Standard Deviation for All Numeric Columns")
print("-" * 70)
stds = traffic_df[numeric_cols].std()
print(stds)
print()

print("3.3 Comprehensive Spread Comparison")
print("-" * 70)
spread_comparison = pd.DataFrame({
    'Column': numeric_cols,
    'Min': [traffic_df[col].min() for col in numeric_cols],
    'Max': [traffic_df[col].max() for col in numeric_cols],
    'Range': [traffic_df[col].max() - traffic_df[col].min() for col in numeric_cols],
    'Std': [traffic_df[col].std() for col in numeric_cols]
})
print(spread_comparison.to_string(index=False))
print()

print("3.4 Coefficient of Variation (CV) - Relative Variability")
print("-" * 70)
print("CV = Std / Mean (allows comparison across different scales)")
print()

cv_comparison = pd.DataFrame({
    'Column': numeric_cols,
    'Mean': [traffic_df[col].mean() for col in numeric_cols],
    'Std': [traffic_df[col].std() for col in numeric_cols],
    'CV': [traffic_df[col].std() / traffic_df[col].mean() if traffic_df[col].mean() != 0 else 0 
           for col in numeric_cols]
})
print(cv_comparison.to_string(index=False))
print()

print("INTERPRETATION:")
print("-" * 70)
for col in numeric_cols:
    mean_val = traffic_df[col].mean()
    std_val = traffic_df[col].std()
    cv = std_val / mean_val if mean_val != 0 else 0
    
    print(f"\n{col}:")
    print(f"  CV: {cv:.3f}")
    
    if cv < 0.15:
        print("  → Very low variability (highly consistent)")
    elif cv < 0.30:
        print("  → Low to moderate variability")
    elif cv < 0.50:
        print("  → Moderate to high variability")
    else:
        print("  → High variability (values spread widely)")

print()

# ==============================================================================
# PART 4: Identifying Patterns and Anomalies
# ==============================================================================
print("=" * 70)
print("PART 4: IDENTIFYING PATTERNS AND ANOMALIES")
print("-" * 70)
print("Look for unusual behavior or interesting differences\n")

print("4.1 Complete Statistical Summary for All Columns")
print("-" * 70)
print(traffic_df[numeric_cols].describe().T)
print()

print("4.2 Identifying Columns with Extreme Characteristics")
print("-" * 70)

# Find column with highest variability
cv_values = {col: traffic_df[col].std() / traffic_df[col].mean() 
             for col in numeric_cols if traffic_df[col].mean() != 0}
highest_cv_col = max(cv_values, key=cv_values.get)
lowest_cv_col = min(cv_values, key=cv_values.get)

print(f"✓ Column with HIGHEST variability: {highest_cv_col} (CV = {cv_values[highest_cv_col]:.3f})")
print(f"✓ Column with LOWEST variability:  {lowest_cv_col} (CV = {cv_values[lowest_cv_col]:.3f})")
print()

# Find column with largest range
range_values = {col: traffic_df[col].max() - traffic_df[col].min() for col in numeric_cols}
largest_range_col = max(range_values, key=range_values.get)
smallest_range_col = min(range_values, key=range_values.get)

print(f"✓ Column with LARGEST range:  {largest_range_col} (Range = {range_values[largest_range_col]:.2f})")
print(f"✓ Column with SMALLEST range: {smallest_range_col} (Range = {range_values[smallest_range_col]:.2f})")
print()

print("4.3 Comparing Scales Across Columns")
print("-" * 70)
print("Different columns often have different scales (e.g., volume in thousands, temp in degrees)")
print()

scale_comparison = pd.DataFrame({
    'Column': numeric_cols,
    'Min': [traffic_df[col].min() for col in numeric_cols],
    'Max': [traffic_df[col].max() for col in numeric_cols],
    'Mean': [traffic_df[col].mean() for col in numeric_cols],
    'Scale': ['Large' if traffic_df[col].mean() > 1000 else 'Small' for col in numeric_cols]
})
print(scale_comparison.to_string(index=False))
print()

print("⚠️  IMPORTANT: When comparing columns with different scales,")
print("   use relative measures like CV, not absolute measures like Std")
print()

# ==============================================================================
# PART 5: Practical Comparison Scenarios
# ==============================================================================
print("=" * 70)
print("PART 5: PRACTICAL COMPARISON SCENARIOS")
print("-" * 70)

print("\n5.1 Scenario: Which column is more predictable?")
print("-" * 70)
print("Answer: The column with LOWER coefficient of variation (CV)")
print()

for col in numeric_cols:
    cv = traffic_df[col].std() / traffic_df[col].mean() if traffic_df[col].mean() != 0 else 0
    print(f"{col:20s} → CV = {cv:.3f}")

most_predictable = min(cv_values, key=cv_values.get)
print(f"\n✓ Most predictable column: {most_predictable}")
print()

print("\n5.2 Scenario: Which columns have similar distributions?")
print("-" * 70)
print("Look at CV, skewness (mean vs median), and relative spread")
print()

for col in numeric_cols:
    mean_val = traffic_df[col].mean()
    median_val = traffic_df[col].median()
    cv = traffic_df[col].std() / mean_val if mean_val != 0 else 0
    skew_indicator = "symmetric" if abs(mean_val - median_val) / median_val < 0.05 else "skewed"
    
    print(f"{col:20s} → CV={cv:.3f}, {skew_indicator}")

print()

print("\n5.3 Scenario: Are there unusual patterns?")
print("-" * 70)

for col in numeric_cols:
    mean_val = traffic_df[col].mean()
    median_val = traffic_df[col].median()
    min_val = traffic_df[col].min()
    max_val = traffic_df[col].max()
    
    # Check for extreme skew
    if mean_val > 1.2 * median_val:
        print(f"⚠️  {col}: Highly right-skewed (mean >> median)")
    elif mean_val < 0.8 * median_val:
        print(f"⚠️  {col}: Highly left-skewed (mean << median)")
    
    # Check for potential outliers
    std_val = traffic_df[col].std()
    if max_val > mean_val + 3 * std_val:
        print(f"⚠️  {col}: Potential high outliers detected")
    if min_val < mean_val - 3 * std_val:
        print(f"⚠️  {col}: Potential low outliers detected")

if not any([traffic_df[col].mean() > 1.2 * traffic_df[col].median() or 
            traffic_df[col].mean() < 0.8 * traffic_df[col].median() 
            for col in numeric_cols]):
    print("✓ No major distribution anomalies detected")

print()

# ==============================================================================
# PART 6: Best Practices for Distribution Comparison
# ==============================================================================
print("=" * 70)
print("PART 6: BEST PRACTICES FOR DISTRIBUTION COMPARISON")
print("-" * 70)
print("""
BEST PRACTICES:
✓ Always compare multiple statistics, not just mean
✓ Use relative measures (CV) when scales differ
✓ Compare mean vs median to understand skewness
✓ Consider both central tendency AND spread
✓ Look for patterns, not just individual values
✓ Use comparisons to ask better questions

COMMON PITFALLS:
✗ Comparing only means without checking spread
✗ Comparing absolute std across different scales
✗ Assuming higher values are "better" or "worse"
✗ Drawing conclusions without understanding context
✗ Ignoring the shape of the distribution

DECISION GUIDE:
- Use MEAN/MEDIAN to compare typical values
- Use STD/RANGE to compare spread
- Use CV to compare relative variability
- Use MIN/MAX to understand boundaries
- Use DESCRIBE() for quick overview

WHEN TO COMPARE DISTRIBUTIONS:
→ Before combining datasets
→ Before feature selection
→ When understanding relationships
→ When validating data quality
→ Before making modeling decisions
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
✓ Understand what distributions represent
✓ Compare central tendency across columns (mean, median)
✓ Compare spread and variability (range, std, CV)
✓ Identify patterns and anomalies across columns
✓ Use comparisons to guide deeper analysis

KEY TAKEAWAYS:
1. Distributions describe how values are spread in a column
2. Compare both central tendency AND spread, not just averages
3. Use CV (Coefficient of Variation) for cross-scale comparisons
4. Mean vs Median reveals distribution shape
5. Comparison reveals patterns that isolation cannot show

NEXT STEPS:
→ Visualize distributions (histograms, box plots)
→ Explore relationships between columns (correlation)
→ Investigate unusual distributions or outliers
→ Use distribution insights for feature engineering
→ Apply comparisons to guide modeling decisions
""")
print()

print("=" * 70)
print("END OF DEMONSTRATION")
print("=" * 70)
