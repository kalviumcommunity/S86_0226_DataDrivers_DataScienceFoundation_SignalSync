# 📊 COMPARING DISTRIBUTIONS ACROSS COLUMNS - QUICK REFERENCE

## What Is a Distribution Comparison?

A **distribution comparison** analyzes how values are spread across multiple columns to understand:
- How variables differ from each other
- Which columns have similar or different behaviors
- Where patterns and anomalies exist
- How to prioritize analysis efforts

**Purpose**: Understand relationships and differences between variables before diving deeper into analysis or modeling.

---

## Why Compare Distributions?

| Reason | Benefit |
|--------|---------|
| **Understand relationships** | See how variables relate to each other |
| **Identify patterns** | Discover hidden similarities or differences |
| **Guide analysis** | Focus on interesting or unusual columns |
| **Avoid mistakes** | Don't compare "apples to oranges" |
| **Feature selection** | Choose informative variables for modeling |

**Key Insight**: Most real insights come from comparison, not isolation.

---

## Essential Comparison Metrics

### Central Tendency (Typical Values)

| Metric | Method | What It Shows | When to Use |
|--------|--------|---------------|-------------|
| **Mean** | `.mean()` | Average value | Quick comparison of typical values |
| **Median** | `.median()` | Middle value | Robust comparison (less affected by outliers) |

### Spread (Variability)

| Metric | Method | What It Shows | When to Use |
|--------|--------|---------------|-------------|
| **Range** | `max() - min()` | Full spread | Understand boundaries |
| **Std** | `.std()` | Absolute variability | Compare similar-scale columns |
| **CV** | `std / mean` | Relative variability | **Compare different-scale columns** |

### Distribution Shape

| Indicator | How to Check | What It Reveals |
|-----------|--------------|-----------------|
| **Symmetry** | Mean ≈ Median | Balanced distribution |
| **Right Skew** | Mean > Median | High values pulling mean up |
| **Left Skew** | Mean < Median | Low values pulling mean down |

---

## Quick Comparison Workflow

```python
import pandas as pd

# Step 1: Load data
df = pd.read_csv('traffic_sample.csv')

# Step 2: Get all numeric columns
numeric_cols = df.select_dtypes(include=['number']).columns

# Step 3: Get quick overview
print(df[numeric_cols].describe().T)

# Step 4: Compare central tendency
means = df[numeric_cols].mean()
medians = df[numeric_cols].median()
print("\nMean vs Median:")
print(pd.DataFrame({'Mean': means, 'Median': medians}))

# Step 5: Compare variability
stds = df[numeric_cols].std()
cvs = stds / means  # Coefficient of Variation
print("\nVariability (CV):")
print(cvs.sort_values(ascending=False))

# Step 6: Identify patterns
for col in numeric_cols:
    mean = df[col].mean()
    median = df[col].median()
    cv = df[col].std() / mean
    
    print(f"\n{col}:")
    print(f"  Central tendency: {'symmetric' if abs(mean-median)/median < 0.05 else 'skewed'}")
    print(f"  Variability: {'high' if cv > 0.3 else 'low'}")
```

---

## Comparing Central Tendency

### Side-by-Side Mean Comparison

```python
# Compare means across all columns
means = df[['traffic_volume', 'temp']].mean()
print("Means:")
print(means)

# Output:
# traffic_volume    4413.33
# temp                49.27
```

### Mean vs Median Analysis

```python
comparison = pd.DataFrame({
    'Column': ['traffic_volume', 'temp'],
    'Mean': [df['traffic_volume'].mean(), df['temp'].mean()],
    'Median': [df['traffic_volume'].median(), df['temp'].median()],
})

# Add interpretation
comparison['Shape'] = comparison.apply(
    lambda x: 'Symmetric' if abs(x['Mean'] - x['Median'])/x['Median'] < 0.05 
    else ('Right-skewed' if x['Mean'] > x['Median'] else 'Left-skewed'),
    axis=1
)

print(comparison)
```

**Interpretation Rules:**
- **Mean ≈ Median** → Symmetric distribution (balanced)
- **Mean > Median** → Right-skewed (high outliers)
- **Mean < Median** → Left-skewed (low outliers)

---

## Comparing Spread and Variability

### Absolute Spread (Same Scale)

```python
# For columns on similar scales
ranges = df[numeric_cols].max() - df[numeric_cols].min()
stds = df[numeric_cols].std()

print("Range:", ranges)
print("Std:", stds)
```

**Use When**: Columns have similar scales (e.g., both in thousands)

### Relative Spread (Different Scales)

```python
# Coefficient of Variation - works across ANY scale
cvs = df[numeric_cols].std() / df[numeric_cols].mean()

print("CV (Coefficient of Variation):")
print(cvs.sort_values(ascending=False))

# Interpret CV values
for col in numeric_cols:
    cv = df[col].std() / df[col].mean()
    if cv < 0.15:
        print(f"{col}: Very consistent (CV={cv:.3f})")
    elif cv < 0.30:
        print(f"{col}: Moderate variability (CV={cv:.3f})")
    else:
        print(f"{col}: High variability (CV={cv:.3f})")
```

**Use When**: Columns have different scales (e.g., thousands vs degrees)

**CV Interpretation:**
- **CV < 0.15** → Very low variability (highly consistent)
- **CV 0.15-0.30** → Low to moderate variability
- **CV 0.30-0.50** → Moderate to high variability
- **CV > 0.50** → Very high variability

---

## Finding Patterns and Anomalies

### Which Column is Most Variable?

```python
# Using Coefficient of Variation
cvs = df[numeric_cols].std() / df[numeric_cols].mean()
most_variable = cvs.idxmax()
least_variable = cvs.idxmin()

print(f"Most variable: {most_variable} (CV={cvs[most_variable]:.3f})")
print(f"Least variable: {least_variable} (CV={cvs[least_variable]:.3f})")
```

### Which Columns Have Similar Distributions?

```python
# Create distribution profile for each column
profiles = pd.DataFrame({
    'Mean': df[numeric_cols].mean(),
    'Median': df[numeric_cols].median(),
    'CV': df[numeric_cols].std() / df[numeric_cols].mean(),
    'Skew': (df[numeric_cols].mean() - df[numeric_cols].median()) / df[numeric_cols].median()
})

print(profiles)

# Columns with similar CV and Skew have similar distributions
```

### Detecting Unusual Distributions

```python
for col in numeric_cols:
    mean = df[col].mean()
    median = df[col].median()
    std = df[col].std()
    cv = std / mean
    
    # Check for extreme skew
    if mean > 1.2 * median:
        print(f"⚠️  {col}: Highly right-skewed")
    elif mean < 0.8 * median:
        print(f"⚠️  {col}: Highly left-skewed")
    
    # Check for high variability
    if cv > 0.5:
        print(f"⚠️  {col}: Very high variability (CV={cv:.3f})")
    
    # Check for potential outliers
    if df[col].max() > mean + 3 * std:
        print(f"⚠️  {col}: Potential high outliers")
```

---

## Common Comparison Scenarios

### Scenario 1: Which column is more predictable?

```python
# Lower CV = more predictable
cvs = df[numeric_cols].std() / df[numeric_cols].mean()
most_predictable = cvs.idxmin()

print(f"Most predictable: {most_predictable} (CV={cvs[most_predictable]:.3f})")
```

### Scenario 2: Which columns should I focus on?

```python
# Focus on columns with:
# - Unusual distributions (high skew)
# - High variability (high CV)
# - Extreme values (outliers)

summary = pd.DataFrame({
    'Column': numeric_cols,
    'CV': [df[col].std() / df[col].mean() for col in numeric_cols],
    'Skew': [(df[col].mean() - df[col].median()) / df[col].median() 
             for col in numeric_cols]
})

# Sort by "interestingness"
summary['Interest'] = summary['CV'] + abs(summary['Skew'])
summary = summary.sort_values('Interest', ascending=False)

print("Columns ranked by interest:")
print(summary)
```

### Scenario 3: Can I compare these columns directly?

```python
# Check if scales are similar
ranges = df[numeric_cols].max() - df[numeric_cols].min()

if ranges.max() / ranges.min() > 10:
    print("⚠️  Scales differ significantly - use CV, not Std")
    print("Use relative comparisons (CV, percentages)")
else:
    print("✓ Scales are similar - can use Std directly")
    print("Can use absolute comparisons (Std, Range)")
```

---

## Visual Comparison Cheatsheet

```
COMPARING CENTRAL TENDENCY:
├─ Mean → Quick average comparison
├─ Median → Robust comparison
└─ Mean vs Median → Detect skewness

COMPARING SPREAD:
├─ Range → Understand boundaries
├─ Std → Absolute variability (same scale only)
└─ CV → Relative variability (any scale) ★ RECOMMENDED

COMPARING DISTRIBUTIONS:
├─ describe().T → Full statistical overview
├─ Mean/Median ratio → Detect skewness
└─ CV ranking → Find most/least variable
```

---

## Decision Matrix

| Question | Use This | Interpretation |
|----------|----------|----------------|
| Which column has higher average? | Compare **Mean** | Higher mean = higher typical value |
| Which column is more consistent? | Compare **CV** | Lower CV = more consistent |
| Which column has outliers? | Compare **Mean vs Median** | Large difference = outliers present |
| Which column varies more? | Compare **CV** (not Std!) | Higher CV = more variability |
| Are distributions similar? | Compare **CV + Skew** | Similar values = similar distributions |

---

## Best Practices

### ✓ DO

✓ **Use CV for cross-scale comparisons** (not Std)  
✓ **Compare both mean AND median** to understand shape  
✓ **Check variability along with central tendency**  
✓ **Look for patterns across multiple columns**  
✓ **Use comparisons to ask better questions**  
✓ **Consider domain context when interpreting**  

### ✗ DON'T

✗ **Compare only means without checking spread**  
✗ **Use Std to compare different-scale columns**  
✗ **Assume higher values are "better"**  
✗ **Draw conclusions without context**  
✗ **Ignore distribution shape (skewness)**  
✗ **Compare raw values across vastly different scales**  

---

## Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|---------|----------------|------------------|
| Using Std across different scales | Std is absolute, not relative | Use CV (Std/Mean) instead |
| Comparing only means | Ignores spread and outliers | Compare mean, median, and spread |
| Ignoring skewness | Mean can be misleading | Check mean vs median |
| No context | Numbers without meaning | Interpret based on domain |
| Isolated analysis | Missing relationships | Compare multiple columns |

---

## Complete Comparison Template

```python
import pandas as pd
import numpy as np

# 1. Load data
df = pd.read_csv('your_data.csv')
numeric_cols = df.select_dtypes(include=[np.number]).columns

# 2. Quick overview
print("=== DISTRIBUTION OVERVIEW ===")
print(df[numeric_cols].describe().T)

# 3. Central tendency comparison
print("\n=== CENTRAL TENDENCY ===")
central = pd.DataFrame({
    'Mean': df[numeric_cols].mean(),
    'Median': df[numeric_cols].median(),
    'Diff%': ((df[numeric_cols].mean() - df[numeric_cols].median()) / 
              df[numeric_cols].median() * 100)
})
print(central)

# 4. Variability comparison
print("\n=== VARIABILITY ===")
variability = pd.DataFrame({
    'Range': df[numeric_cols].max() - df[numeric_cols].min(),
    'Std': df[numeric_cols].std(),
    'CV': df[numeric_cols].std() / df[numeric_cols].mean()
})
print(variability.sort_values('CV', ascending=False))

# 5. Pattern detection
print("\n=== PATTERNS ===")
for col in numeric_cols:
    mean = df[col].mean()
    median = df[col].median()
    cv = df[col].std() / mean
    
    shape = 'Symmetric' if abs(mean-median)/median < 0.05 else \
            'Right-skewed' if mean > median else 'Left-skewed'
    vary = 'High' if cv > 0.3 else 'Low'
    
    print(f"{col}: {shape}, {vary} variability (CV={cv:.3f})")

# 6. Key insights
print("\n=== KEY INSIGHTS ===")
cvs = df[numeric_cols].std() / df[numeric_cols].mean()
print(f"Most variable: {cvs.idxmax()} (CV={cvs.max():.3f})")
print(f"Most consistent: {cvs.idxmin()} (CV={cvs.min():.3f})")
```

---

## When to Compare Distributions

| Stage | Why Compare | What to Look For |
|-------|-------------|------------------|
| **Data Loading** | Validate data quality | Unusual ranges, unexpected scales |
| **EDA Start** | Understand variables | Central tendency, spread, patterns |
| **Feature Selection** | Choose informative features | High variability, interesting patterns |
| **Before Modeling** | Understand inputs | Scale differences, distributions |
| **Data Validation** | Check consistency | Similar distributions as expected |

---

## Key Takeaways

1. **Distributions describe behavior** - not just single values
2. **Compare both center AND spread** - mean/median + std/CV
3. **Use CV for different scales** - never use Std across scales
4. **Mean vs Median reveals shape** - symmetric vs skewed
5. **Comparison reveals patterns** - isolation hides relationships
6. **Context matters** - interpret numbers with domain knowledge

---

## Related Topics

- Summary Statistics (count, mean, median, std)
- Data Visualization (histograms, box plots)
- Correlation Analysis (relationships between variables)
- Feature Engineering (creating new variables)
- Outlier Detection (identifying unusual values)

---

**Remember**: Comparing distributions is about understanding how variables differ and relate to each other. Always compare multiple metrics (not just mean) and consider both central tendency and spread!
