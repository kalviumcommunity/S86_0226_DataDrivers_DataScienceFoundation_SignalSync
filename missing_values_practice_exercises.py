"""
Missing Values Handling - Practice Exercises
==============================================
Complete these exercises to reinforce your understanding of handling missing data.

Work through each exercise step by step.
Document your decisions and reasoning.
"""

import pandas as pd
import numpy as np

print("=" * 70)
print("MISSING VALUES HANDLING - PRACTICE EXERCISES")
print("=" * 70)

# ============================================================================
# EXERCISE 1: CREATE A DATASET WITH MISSING VALUES
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE 1: Create and Inspect Dataset")
print("=" * 70)

# TODO: Create a DataFrame with the following data:
# - 15 rows
# - Columns: student_id, name, age, grade, attendance_rate, test_score
# - Include missing values in age (2 missing), grade (3 missing), and test_score (1 missing)

# Your code here:
# data = {
#     'student_id': [...],
#     'name': [...],
#     'age': [...],
#     'grade': [...],
#     'attendance_rate': [...],
#     'test_score': [...]
# }
# df = pd.DataFrame(data)

# TASK 1.1: Print the DataFrame
print("\nTask 1.1: Display the DataFrame")
# Your code here

# TASK 1.2: Count missing values per column
print("\nTask 1.2: Count missing values per column")
# Your code here

# TASK 1.3: Calculate missing value percentage per column
print("\nTask 1.3: Calculate missing percentage per column")
# Your code here

# ============================================================================
# EXERCISE 2: PRACTICE DROP STRATEGIES
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE 2: Apply Drop Strategies")
print("=" * 70)

# TASK 2.1: Drop rows with ANY missing values
print("\nTask 2.1: Drop rows with ANY missing values")
# Your code here
# df_drop_any = ...
# print(f"Original shape: {df.shape}")
# print(f"After dropping: {df_drop_any.shape}")

# TASK 2.2: Drop rows where 'test_score' is missing
print("\nTask 2.2: Drop rows where 'test_score' is missing")
# Your code here
# df_drop_subset = ...
# print(f"Original shape: {df.shape}")
# print(f"After dropping: {df_drop_subset.shape}")

# TASK 2.3: Calculate what percentage of data you would lose
print("\nTask 2.3: Calculate data loss percentage")
# Your code here
# loss_percentage = ...
# print(f"Data loss: {loss_percentage:.1f}%")

# QUESTION: Which drop strategy is better for this dataset? Why?
print("\nQUESTION: Document your answer here")
# Your answer: 

# ============================================================================
# EXERCISE 3: PRACTICE FILL STRATEGIES
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE 3: Apply Fill Strategies")
print("=" * 70)

# TASK 3.1: Fill 'age' with the median age
print("\nTask 3.1: Fill 'age' with median")
# Your code here
# df_filled = df.copy()
# df_filled['age'] = ...

# TASK 3.2: Fill 'grade' with the mode (most common grade)
print("\nTask 3.2: Fill 'grade' with mode")
# Your code here
# df_filled['grade'] = ...

# TASK 3.3: Fill 'test_score' with the mean score
print("\nTask 3.3: Fill 'test_score' with mean")
# Your code here
# df_filled['test_score'] = ...

# TASK 3.4: Verify no missing values remain
print("\nTask 3.4: Verify no missing values")
# Your code here
# print(df_filled.isnull().sum())

# QUESTION: Why did we use median for age, mode for grade, and mean for test_score?
print("\nQUESTION: Document your reasoning here")
# Your answer:

# ============================================================================
# EXERCISE 4: COMPARISON CHALLENGE
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE 4: Compare Strategies")
print("=" * 70)

# TASK 4.1: Create three versions of the dataset:
#   - Version A: Drop all rows with any missing values
#   - Version B: Fill all numeric columns with median, categorical with mode
#   - Version C: Drop rows where test_score is missing, fill others

print("\nTask 4.1: Create three versions")
# Your code here
# df_version_a = ...
# df_version_b = ...
# df_version_c = ...

# TASK 4.2: Compare the shape of all three versions
print("\nTask 4.2: Compare shapes")
# Your code here
# print(f"Version A shape: {df_version_a.shape}")
# print(f"Version B shape: {df_version_b.shape}")
# print(f"Version C shape: {df_version_c.shape}")

# TASK 4.3: Calculate average test_score for each version
print("\nTask 4.3: Compare average test scores")
# Your code here
# print(f"Version A avg score: {df_version_a['test_score'].mean():.2f}")
# print(f"Version B avg score: {df_version_b['test_score'].mean():.2f}")
# print(f"Version C avg score: {df_version_c['test_score'].mean():.2f}")

# QUESTION: Which version would you choose and why?
print("\nQUESTION: Document your choice and reasoning")
# Your answer:

# ============================================================================
# EXERCISE 5: REAL-WORLD SCENARIO
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE 5: Real-World Scenario - Traffic Analysis")
print("=" * 70)

# Scenario: You have traffic data with missing values
# - traffic_volume: 15% missing (sensor malfunction)
# - temp: 5% missing (weather station offline)
# - weather_main: 3% missing (API errors)
# - road_conditions: 80% missing (new feature, not yet collected)

# Create this scenario dataset:
traffic_data = {
    'timestamp': pd.date_range('2023-01-01', periods=100, freq='H'),
    'traffic_volume': [np.random.randint(100, 1000) if np.random.rand() > 0.15 else np.nan for _ in range(100)],
    'temp': [np.random.uniform(30, 80) if np.random.rand() > 0.05 else np.nan for _ in range(100)],
    'weather_main': [np.random.choice(['Clear', 'Rain', 'Snow']) if np.random.rand() > 0.03 else np.nan for _ in range(100)],
    'road_conditions': [np.nan] * 100  # 100% missing
}
df_traffic = pd.DataFrame(traffic_data)

print("\nTraffic Dataset Created")
print(df_traffic.head(10))
print("\nMissing values:")
print(df_traffic.isnull().sum())

# TASK 5.1: Decide what to do with each column
print("\nTask 5.1: Make a cleaning plan")
# Document your plan:
# - road_conditions: [Your decision]
# - traffic_volume: [Your decision]
# - temp: [Your decision]
# - weather_main: [Your decision]

# TASK 5.2: Implement your cleaning strategy
print("\nTask 5.2: Implement your strategy")
# Your code here
# df_traffic_clean = df_traffic.copy()
# ... apply your strategy ...

# TASK 5.3: Verify your results
print("\nTask 5.3: Verify cleaned data")
# Your code here
# print("Missing values after cleaning:")
# print(df_traffic_clean.isnull().sum())
# print(f"\nOriginal shape: {df_traffic.shape}")
# print(f"Cleaned shape: {df_traffic_clean.shape}")
# print(f"Data retained: {(df_traffic_clean.shape[0]/df_traffic.shape[0])*100:.1f}%")

# TASK 5.4: Justify your decisions
print("\nTask 5.4: Document your reasoning")
# Your justification:
# Road conditions: [Why did you drop/fill/keep it?]
# Traffic volume: [Why did you choose this approach?]
# Temperature: [What was your reasoning?]
# Weather: [Why this strategy?]

# ============================================================================
# EXERCISE 6: MISTAKE IDENTIFICATION
# ============================================================================
print("\n" + "=" * 70)
print("EXERCISE 6: Find the Mistakes")
print("=" * 70)

# The following code has several mistakes. Find and fix them.

sample_data = {
    'product': ['A', 'B', 'C', 'D', 'E'],
    'price': [10.5, np.nan, 25.0, np.nan, 15.5],
    'category': ['Electronics', 'Books', np.nan, 'Electronics', 'Books'],
    'stock': [100, 50, np.nan, 25, 80]
}
df_sample = pd.DataFrame(sample_data)

print("\nOriginal data:")
print(df_sample)

# MISTAKE 1: Filling categorical data with mean
df_sample['category'] = df_sample['category'].fillna(df_sample['category'].mean())

# MISTAKE 2: Using mean for price when it should be median
df_sample['price'] = df_sample['price'].fillna(df_sample['price'].mean())

# MISTAKE 3: Dropping entire dataset because one column has missing values
df_sample = df_sample.dropna()

# TASK 6.1: Identify all mistakes
print("\nTask 6.1: List all mistakes you found")
# Your answer:
# 1. 
# 2. 
# 3. 

# TASK 6.2: Write corrected code
print("\nTask 6.2: Write corrected version")
# Your code here:

# ============================================================================
# BONUS CHALLENGE: ADVANCED SCENARIO
# ============================================================================
print("\n" + "=" * 70)
print("BONUS CHALLENGE: Multiple Missing Patterns")
print("=" * 70)

# Create a complex dataset:
np.random.seed(42)
complex_data = {
    'id': range(1, 51),
    'age': [np.random.randint(20, 60) if np.random.rand() > 0.1 else np.nan for _ in range(50)],
    'income': [np.random.randint(30000, 100000) if np.random.rand() > 0.2 else np.nan for _ in range(50)],
    'education': [np.random.choice(['HS', 'BS', 'MS', 'PhD']) if np.random.rand() > 0.15 else np.nan for _ in range(50)],
    'city': [np.random.choice(['NYC', 'LA', 'CHI']) if np.random.rand() > 0.05 else np.nan for _ in range(50)],
    'optional_survey': [np.nan] * 50
}
df_complex = pd.DataFrame(complex_data)

print("\nComplex Dataset:")
print(df_complex.head())
print("\nMissing values summary:")
print(df_complex.isnull().sum())
print("\nMissing percentages:")
print((df_complex.isnull().sum() / len(df_complex) * 100).round(2))

# CHALLENGE: Design a comprehensive cleaning strategy that:
# 1. Handles each column appropriately
# 2. Retains at least 80% of rows
# 3. Ensures no missing values in critical columns (age, income, city)
# 4. Documents all decisions
# 5. Verifies the final result

print("\nBONUS CHALLENGE: Implement your comprehensive strategy")
# Your code here:

print("\n" + "=" * 70)
print("END OF EXERCISES")
print("=" * 70)

# ============================================================================
# SELF-ASSESSMENT CHECKLIST
# ============================================================================
print("\n📋 SELF-ASSESSMENT CHECKLIST:")
print("Did you:")
print("□ Identify missing values before handling them?")
print("□ Choose appropriate strategies for each column type?")
print("□ Consider the percentage of missing data?")
print("□ Document your decisions and reasoning?")
print("□ Verify results after cleaning?")
print("□ Understand why each strategy was chosen?")
print("□ Avoid common mistakes (mean for outliers, dropping blindly, etc.)?")
print("□ Check data retention percentage?")
print("□ Ensure cleaned data is analysis-ready?")
print("□ Learn something new from each exercise?")

print("\n🎯 Next Steps:")
print("1. Review any exercises where you struggled")
print("2. Compare your answers with the demonstration script")
print("3. Try creating your own scenarios")
print("4. Practice with real-world datasets")
print("5. Record your video walkthrough!")

print("\n" + "=" * 70)
