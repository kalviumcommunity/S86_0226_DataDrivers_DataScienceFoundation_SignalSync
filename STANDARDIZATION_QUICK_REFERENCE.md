# Data Standardization Quick Reference

## 🎯 Purpose
Quick reference for standardizing column names and data formats in Pandas DataFrames.

---

## 📋 Column Name Standardization

### Basic Rules
```python
# 1. Convert to lowercase
df.columns = df.columns.str.lower()

# 2. Replace spaces with underscores
df.columns = df.columns.str.replace(' ', '_')

# 3. Remove special characters
df.columns = df.columns.str.replace(r'[()%\-]', '', regex=True)

# 4. Clean up multiple underscores
df.columns = df.columns.str.replace('_+', '_', regex=True)
df.columns = df.columns.str.strip('_')
```

### Complete Function
```python
def standardize_column_names(df):
    """Standardize DataFrame column names to snake_case."""
    df_std = df.copy()
    df_std.columns = df_std.columns.str.lower()
    df_std.columns = df_std.columns.str.replace(' ', '_')
    df_std.columns = df_std.columns.str.replace(r'[()%\-]', '', regex=True)
    df_std.columns = df_std.columns.str.replace('_+', '_', regex=True)
    df_std.columns = df_std.columns.str.strip('_')
    return df_std
```

---

## 📝 Text Data Standardization

### Lowercase Text
```python
# Convert to lowercase
df['column_name'] = df['column_name'].str.lower()
```

### Uppercase Text
```python
# Convert to uppercase
df['column_name'] = df['column_name'].str.upper()
```

### Title Case
```python
# Convert to title case (capitalize first letter)
df['column_name'] = df['column_name'].str.title()
```

### Strip Whitespace
```python
# Remove leading and trailing whitespace
df['column_name'] = df['column_name'].str.strip()
```

### Combined Text Cleaning
```python
# Clean text: strip whitespace and convert to lowercase
df['column_name'] = df['column_name'].str.strip().str.lower()
```

---

## 🔢 Numeric Data Standardization

### Convert to Numeric
```python
# Convert string numbers to numeric type
df['column_name'] = pd.to_numeric(df['column_name'])

# Convert with error handling (invalid values become NaN)
df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')
```

### Check Numeric Type
```python
# Check if column is numeric
print(df['column_name'].dtype)

# Verify conversion worked
print(df.dtypes)
```

---

## 📅 Date Format Standardization

### Convert to Datetime
```python
# Convert to datetime type
df['date_column'] = pd.to_datetime(df['date_column'])

# Convert with error handling
df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')

# Specify date format for faster parsing
df['date_column'] = pd.to_datetime(df['date_column'], format='%Y-%m-%d')
```

### Extract Date Components
```python
# Extract year, month, day
df['year'] = df['date_column'].dt.year
df['month'] = df['date_column'].dt.month
df['day'] = df['date_column'].dt.day

# Extract day of week
df['day_of_week'] = df['date_column'].dt.day_name()
df['weekday_num'] = df['date_column'].dt.weekday  # Monday=0, Sunday=6
```

---

## 🔄 Complete Standardization Workflow

### Step-by-Step
```python
import pandas as pd

# 1. Load data
df = pd.read_csv('data.csv')

# 2. Standardize column names
df = standardize_column_names(df)

# 3. Standardize text columns
text_cols = ['weather', 'location', 'category']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].str.strip().str.lower()

# 4. Standardize numeric columns
numeric_cols = ['speed', 'temperature', 'volume']
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# 5. Standardize date columns
date_cols = ['date', 'timestamp']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# 6. Verify
print(df.head())
print(df.dtypes)
print(df.columns.tolist())
```

---

## ✅ Standardization Checklist

### Column Names
- [ ] All lowercase
- [ ] Underscores instead of spaces
- [ ] No special characters
- [ ] Consistent naming pattern
- [ ] Descriptive but concise

### Text Data
- [ ] Consistent case (lower/upper/title)
- [ ] No leading/trailing whitespace
- [ ] Category values standardized
- [ ] No mixed formats

### Numeric Data
- [ ] Correct data type (int64, float64)
- [ ] No string numbers
- [ ] Consistent units
- [ ] Invalid values handled

### Date Data
- [ ] Converted to datetime type
- [ ] Consistent format
- [ ] Invalid dates handled
- [ ] Ready for date operations

### General
- [ ] Standardize at start of workflow
- [ ] Document standardization rules
- [ ] Verify changes with head() and dtypes
- [ ] Test code with standardized names

---

## 🚨 Common Mistakes to Avoid

### ❌ Don't Do This
```python
# Inconsistent naming
df['Date Time']  # Spaces
df['traffic_volume']  # Underscores
df['Temp_F']  # Mixed case

# Not converting types
speed = df['speed'][0] + 10  # Error if speed is string

# Ignoring whitespace
df[df['weather'] == 'Clear']  # Won't match '  Clear  '
```

### ✅ Do This Instead
```python
# Consistent naming
df['date_time']
df['traffic_volume']
df['temp_f']

# Convert types first
df['speed'] = pd.to_numeric(df['speed'])
speed = df['speed'][0] + 10  # Works!

# Clean text first
df['weather'] = df['weather'].str.strip().str.lower()
df[df['weather'] == 'clear']  # Matches!
```

---

## 📊 Before/After Example

### Before Standardization
```python
# Messy DataFrame
Date Time | Traffic Volume (cars) | Temp_F | Weather Main | Speed (mph)
2023-01-02 | 3600 | 44.5 | CLEAR | "65"
2023-01-03 | 4300 | 46.2 |   Clouds   | "72"
```

### After Standardization
```python
# Clean DataFrame
date_time  | traffic_volume_cars | temp_f | weather_main | speed_mph
2023-01-02 | 3600 | 44.5 | clear | 65
2023-01-03 | 4300 | 46.2 | clouds | 72
```

---

## 🎓 Key Principles

1. **Always standardize early** - Do it right after loading data
2. **Be consistent** - Apply same rules to all datasets
3. **Document choices** - Write down your standardization rules
4. **Automate** - Create reusable functions
5. **Verify** - Always check results with head() and dtypes
6. **Keep it simple** - Don't over-complicate

---

## 🔗 Related Topics

- **Missing Values** - Handle after standardization
- **Data Types** - Verify with df.dtypes
- **String Methods** - df['col'].str methods
- **DataFrame Inspection** - head(), info(), describe()

---

**Remember:** Clean column names lead to clean code!
