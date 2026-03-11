# Missing Values Handling - Quick Reference Guide

## 🔍 Detection Methods

```python
# Check for missing values
df.isnull()                    # Boolean DataFrame showing True for missing values
df.isnull().sum()              # Count of missing values per column
df.isnull().sum().sum()        # Total missing values in entire DataFrame

# Missing value percentage
(df.isnull().sum() / len(df)) * 100

# Rows with any missing values
df[df.isnull().any(axis=1)]

# Columns with any missing values
df.columns[df.isnull().any()]
```

## 🗑️ Drop Strategies

```python
# Drop rows with ANY missing value (aggressive)
df.dropna()
df.dropna(how='any')  # Same as above (default)

# Drop rows where ALL values are missing (safe)
df.dropna(how='all')

# Drop rows where specific columns have missing values (targeted)
df.dropna(subset=['column_name'])
df.dropna(subset=['col1', 'col2'])

# Drop columns with missing values
df.dropna(axis=1)

# Drop columns where >50% data is missing
threshold = len(df) * 0.5
df.dropna(thresh=threshold, axis=1)

# Keep original DataFrame (use inplace parameter)
df_clean = df.dropna()  # Returns new DataFrame
df.dropna(inplace=True)  # Modifies original DataFrame
```

## 🎨 Fill Strategies

```python
# Fill with a constant value
df['column'].fillna(0)                    # Fill with 0
df['column'].fillna('Unknown')            # Fill with string
df.fillna(0)                               # Fill all columns with 0

# Fill with statistical measures
df['column'].fillna(df['column'].mean())   # Fill with mean
df['column'].fillna(df['column'].median()) # Fill with median (RECOMMENDED)
df['column'].fillna(df['column'].mode()[0]) # Fill with mode

# Fill with forward/backward propagation (time-series)
df['column'].fillna(method='ffill')       # Forward fill
df['column'].fillna(method='bfill')       # Backward fill

# Fill different columns with different strategies
df['numeric_col'] = df['numeric_col'].fillna(df['numeric_col'].median())
df['category_col'] = df['category_col'].fillna('Unknown')

# Fill using a dictionary (different values per column)
fill_values = {
    'traffic_volume': df['traffic_volume'].median(),
    'temp': df['temp'].median(),
    'weather_main': 'Unknown'
}
df.fillna(fill_values)
```

## 🎯 Decision Tree

```
Is column >70% missing?
├─ YES → DROP COLUMN
└─ NO → Continue

Is this a critical column (e.g., target variable)?
├─ YES → Is row missing this value?
│   ├─ YES → DROP ROW
│   └─ NO → Keep row
└─ NO → Continue

Is missing data <20% of column?
├─ YES → FILL
│   ├─ Numeric data → Use MEDIAN
│   ├─ Categorical data → Use MODE or 'Unknown'
│   └─ Time-series data → Use FORWARD/BACKWARD FILL
└─ NO → Is dataset large?
    ├─ YES → DROP ROWS
    └─ NO → FILL with caution
```

## ⚖️ Drop vs Fill Comparison

| Aspect | Drop | Fill |
|--------|------|------|
| **Data Loss** | High | None |
| **Introduces Bias** | Low | Potentially High |
| **Best When** | Large dataset, <5% missing | Small dataset, <20% missing |
| **Risk** | Losing important patterns | Creating artificial patterns |
| **Complexity** | Simple | Requires justification |

## ✅ Best Practices

### DO:
- ✅ Always identify missing data BEFORE handling
- ✅ Document your strategy and reasoning
- ✅ Verify results after cleaning (check shape, nulls, dtypes)
- ✅ Use median for numeric data (robust to outliers)
- ✅ Use mode for categorical data
- ✅ Consider domain knowledge when choosing strategy
- ✅ Keep filling methods simple and explainable

### DON'T:
- ❌ Drop data without checking the impact on dataset size
- ❌ Fill categorical columns with numeric values
- ❌ Use mean when data has outliers
- ❌ Fill without justifying your choice
- ❌ Mix multiple strategies without documentation
- ❌ Forget to verify cleaned data
- ❌ Assume missing data is always random

## 📊 Common Scenarios

### Scenario 1: Survey Data with Optional Questions
**Problem:** Many columns with 30-50% missing (legitimate skips)
**Solution:** Keep missing as NaN or fill with 'Not Answered', don't drop

### Scenario 2: Sensor Data with Equipment Failure
**Problem:** Critical column (e.g., temperature) missing for some rows
**Solution:** Drop rows where critical data is missing

### Scenario 3: Large Dataset with Sparse Missing Values
**Problem:** <5% rows have any missing values
**Solution:** Drop rows with any missing values if dataset is large enough

### Scenario 4: Small Dataset, Important Analysis
**Problem:** Can't afford to lose rows, but have missing values
**Solution:** Fill with median/mode, document assumptions

### Scenario 5: Time-Series with Gaps
**Problem:** Sequential data with occasional missing points
**Solution:** Forward fill or interpolation

### Scenario 6: Administrative Column 100% Missing
**Problem:** Column exists but has no data
**Solution:** Drop the column entirely

## 🧪 Verification Checklist

After cleaning, always verify:

```python
# 1. Check no missing values remain (or acceptable amount)
print(df.isnull().sum())

# 2. Verify shape is reasonable
print(f"Original shape: {original_shape}")
print(f"Cleaned shape: {df.shape}")
print(f"Rows retained: {df.shape[0]/original_shape[0]*100:.1f}%")

# 3. Check data types are correct
print(df.dtypes)

# 4. Verify statistical properties make sense
print(df.describe())

# 5. Sample a few rows
print(df.head(10))
```

## 🎓 Interview Questions to Consider

When handling missing data, ask yourself:
1. What percentage of data is missing?
2. Is the missing pattern random or systematic?
3. Is this column critical for analysis?
4. Can I afford to lose this data?
5. What assumption am I making by filling?
6. How will this affect downstream analysis?
7. Can I justify this choice to stakeholders?

## 📚 Recommended Reading Order

1. First, learn to **detect** missing values
2. Then, understand **why** data is missing
3. Next, learn **drop** strategies (simpler)
4. Then, learn **fill** strategies (more complex)
5. Finally, practice **decision-making** based on context

## 💡 Remember

> "The best way to handle missing data depends on why it's missing, not just how much is missing."

> "When in doubt, document your assumptions and verify your results."

> "Bad handling can be worse than no handling - always think before you act."

---

**Quick Command Reference:**
- Detect: `df.isnull().sum()`
- Drop rows: `df.dropna()`
- Drop columns: `df.dropna(axis=1)`
- Fill with median: `df.fillna(df.median())`
- Fill with constant: `df.fillna(value)`
- Verify: `df.isnull().sum().sum() == 0`
