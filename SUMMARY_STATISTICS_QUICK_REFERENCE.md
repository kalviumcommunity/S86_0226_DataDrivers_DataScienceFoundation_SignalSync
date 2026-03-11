# 📊 SUMMARY STATISTICS QUICK REFERENCE

## What Are Summary Statistics?

Summary statistics are numerical measures that describe the key characteristics of your data:
- **Central Tendency**: Where the "center" of your data is (mean, median)
- **Spread**: How spread out your data is (std, variance, range)
- **Boundaries**: The extreme values (min, max)
- **Distribution**: How many values you have (count)

**Purpose**: Get a quick numerical snapshot of your data before diving into analysis.

---

## Essential Statistics and Their Meanings

| Statistic | Method | Meaning | When to Use |
|-----------|---------|---------|-------------|
| **Count** | `.count()` | Number of non-missing values | Check for missing data |
| **Mean** | `.mean()` | Average value (sum ÷ count) | Understand typical value |
| **Median** | `.median()` | Middle value when sorted | Robust to outliers |
| **Min** | `.min()` | Smallest value | Find lower boundary |
| **Max** | `.max()` | Largest value | Find upper boundary |
| **Std** | `.std()` | Standard deviation (spread) | Measure variability |
| **Var** | `.var()` | Variance (std²) | Theoretical calculations |
| **25%/75%** | `.quantile()` | Quartiles | Understand distribution |

---

## Computing Statistics

### For a Single Column

```python
# Individual statistics
traffic_df['traffic_volume'].count()    # Non-missing count
traffic_df['traffic_volume'].mean()     # Average
traffic_df['traffic_volume'].median()   # Middle value
traffic_df['traffic_volume'].min()      # Minimum
traffic_df['traffic_volume'].max()      # Maximum
traffic_df['traffic_volume'].std()      # Standard deviation
traffic_df['traffic_volume'].sum()      # Total sum
```

### Using .describe() - All at Once

```python
# Get all statistics in one call
traffic_df['traffic_volume'].describe()

# Output:
# count    15.000000
# mean      4413.33
# std       1019.01
# min       2800.00
# 25%       3700.00
# 50%       4200.00    ← This is the median
# 75%       5000.00
# max       6200.00
```

### For All Numeric Columns

```python
# Describe all numeric columns at once
traffic_df.describe()

# Transpose for better readability
traffic_df.describe().T
```

---

## Interpreting Statistics Correctly

### Mean vs Median

| Relationship | Interpretation | What It Means |
|--------------|----------------|---------------|
| Mean ≈ Median | Symmetric distribution | Data is evenly distributed |
| Mean > Median | Right-skewed | High values pulling mean up |
| Mean < Median | Left-skewed | Low values pulling mean down |

**Rule**: When mean and median differ significantly, investigate outliers.

### Standard Deviation (Std)

```python
std = traffic_df['traffic_volume'].std()
mean = traffic_df['traffic_volume'].mean()

# Typical range (68% of data)
lower = mean - std
upper = mean + std

# Most values fall between lower and upper
```

**Rule**: Higher std = more variability in data.

### Coefficient of Variation (CV)

```python
cv = std / mean
# CV < 0.25 → Low variability
# CV 0.25-0.5 → Moderate variability
# CV > 0.5 → High variability
```

---

## Comparing Columns

### Side-by-Side Comparison

```python
import pandas as pd

comparison = pd.DataFrame({
    'Traffic Volume': traffic_df['traffic_volume'].describe(),
    'Temperature': traffic_df['temp'].describe()
})

print(comparison)
```

### Identify Which Column Has More Variability

```python
# Method 1: Compare standard deviations
print(traffic_df[['traffic_volume', 'temp']].std())

# Method 2: Compare coefficient of variation
cv_traffic = traffic_df['traffic_volume'].std() / traffic_df['traffic_volume'].mean()
cv_temp = traffic_df['temp'].std() / traffic_df['temp'].mean()

print(f"CV Traffic: {cv_traffic:.2f}")
print(f"CV Temp: {cv_temp:.2f}")
```

---

## Identifying Unusual Values

### Using the 2-Sigma Rule

```python
mean = traffic_df['traffic_volume'].mean()
std = traffic_df['traffic_volume'].std()

# Define normal range
lower_bound = mean - 2 * std
upper_bound = mean + 2 * std

# Find unusual values
unusual_low = traffic_df[traffic_df['traffic_volume'] < lower_bound]
unusual_high = traffic_df[traffic_df['traffic_volume'] > upper_bound]

print(f"Unusual low: {len(unusual_low)} records")
print(f"Unusual high: {len(unusual_high)} records")
```

**Rule**: Values beyond Mean ± 2×Std are unusual (occur ~5% of the time).

### Using Quartiles (IQR Method)

```python
Q1 = traffic_df['traffic_volume'].quantile(0.25)
Q3 = traffic_df['traffic_volume'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier boundaries
lower_outlier = Q1 - 1.5 * IQR
upper_outlier = Q3 + 1.5 * IQR

# Find outliers
outliers = traffic_df[
    (traffic_df['traffic_volume'] < lower_outlier) | 
    (traffic_df['traffic_volume'] > upper_outlier)
]
```

---

## Common Patterns and What They Mean

| Pattern | Interpretation | Action |
|---------|----------------|--------|
| Mean >> Median | Right skew, high outliers | Investigate high values |
| Mean << Median | Left skew, low outliers | Investigate low values |
| High Std/Mean ratio | High variability | Understand causes of variance |
| Count < Total rows | Missing values present | Handle missing data |
| Min or Max extreme | Potential data errors | Validate extreme values |

---

## Best Practices

### ✓ DO

✓ **Compute statistics FIRST** before any analysis or modeling  
✓ **Compare mean and median** to understand distribution shape  
✓ **Check count** to identify missing values  
✓ **Consider spread (std)** alongside central tendency  
✓ **Use statistics to guide** further investigation  
✓ **Combine with visual inspection** (histograms, box plots)  

### ✗ DON'T

✗ **Rely only on mean** without checking median and std  
✗ **Ignore outliers** that heavily influence the mean  
✗ **Skip the count check** (missing data can distort statistics)  
✗ **Compare statistics** without considering scale differences  
✗ **Make conclusions** from statistics alone without context  

---

## Quick Decision Guide

```
START: Want to understand a numeric column
  │
  ├─→ Compute .describe() for quick overview
  │
  ├─→ Compare Mean vs Median
  │   ├─ If similar → Symmetric distribution
  │   └─ If different → Check for outliers
  │
  ├─→ Check Std (spread)
  │   ├─ High → Investigate why variability is high
  │   └─ Low → Data is consistent
  │
  ├─→ Look at Min/Max
  │   └─ If extreme → Validate data quality
  │
  └─→ Compare Count vs Total Rows
      └─ If different → Handle missing values
```

---

## Example Workflow

```python
import pandas as pd

# Step 1: Load data
df = pd.read_csv('traffic_sample.csv')

# Step 2: Get overview of all numeric columns
print(df.describe())

# Step 3: Focus on a specific column
col = 'traffic_volume'
print(f"\nAnalyzing {col}:")
print(f"Mean:   {df[col].mean():.2f}")
print(f"Median: {df[col].median():.2f}")
print(f"Std:    {df[col].std():.2f}")

# Step 4: Interpret
mean_val = df[col].mean()
median_val = df[col].median()
if mean_val > median_val:
    print("→ Right-skewed: Check for high outliers")
elif mean_val < median_val:
    print("→ Left-skewed: Check for low outliers")
else:
    print("→ Symmetric distribution")

# Step 5: Check for unusual values
std_val = df[col].std()
lower = mean_val - 2 * std_val
upper = mean_val + 2 * std_val
unusual = df[(df[col] < lower) | (df[col] > upper)]
print(f"Unusual values: {len(unusual)}")
```

---

## Common Mistakes to Avoid

| Mistake | Why It's Wrong | Correct Approach |
|---------|----------------|------------------|
| "Mean is enough" | Ignores spread and outliers | Check mean, median, and std |
| "This value is wrong" | Might be a real outlier | Investigate before removing |
| Ignoring count | Missing data distorts stats | Always check count first |
| No context | Numbers without meaning | Interpret based on domain |
| Statistics only | Missing visual patterns | Combine with plots |

---

## When Each Statistic Matters Most

| Use Case | Most Important Statistics |
|----------|--------------------------|
| **Finding typical value** | Mean (if symmetric), Median (if skewed) |
| **Understanding variability** | Std, Min, Max, Range |
| **Checking data quality** | Count, Min, Max |
| **Comparing columns** | Mean, Std, CV (Coefficient of Variation) |
| **Finding outliers** | Mean, Std, Quartiles (Q1, Q3) |
| **Understanding distribution** | Mean, Median, Std, Quartiles |

---

## Practice Exercises

1. **Load a dataset and compute statistics for all numeric columns**
   ```python
   df = pd.read_csv('your_data.csv')
   print(df.describe())
   ```

2. **Compare mean vs median for a column and interpret**
   ```python
   col = 'your_column'
   print(f"Mean: {df[col].mean():.2f}")
   print(f"Median: {df[col].median():.2f}")
   ```

3. **Find the typical range (Mean ± Std)**
   ```python
   mean = df[col].mean()
   std = df[col].std()
   print(f"Typical range: {mean-std:.2f} to {mean+std:.2f}")
   ```

4. **Identify unusual values**
   ```python
   unusual = df[(df[col] < mean-2*std) | (df[col] > mean+2*std)]
   print(unusual[[col]])
   ```

---

## Key Takeaways

1. **Summary statistics** provide a quick numerical overview of data
2. **Mean vs Median** reveals if data is skewed
3. **Standard deviation** shows how spread out your data is
4. **Always compute statistics BEFORE modeling**
5. **Combine statistics with visual inspection** for best results

---

## Related Topics

- Data Visualization (box plots, histograms)
- Data Cleaning (handling outliers)
- Feature Engineering
- Correlation Analysis
- Hypothesis Testing

---

**Remember**: Summary statistics describe your data, but they don't explain WHY the patterns exist. Always combine numerical summaries with domain knowledge and visual exploration.
