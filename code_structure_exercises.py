#!/usr/bin/env python3
"""
Practice Exercises: Code Structure and Organization
====================================================
Complete these exercises to practice structuring Python code for readability
and reuse.

Instructions:
- Each exercise builds your understanding of code organization
- Follow the TODO comments to complete each section
- Focus on structure, not complexity
- Run the file to test your solutions
"""

print("=" * 70)
print("PRACTICE EXERCISES: CODE STRUCTURE AND ORGANIZATION")
print("=" * 70)

# =============================================================================
# EXERCISE 1: Organizing Code into Sections
# =============================================================================
print("\n📝 EXERCISE 1: Organize Code into Logical Sections")
print("-" * 70)
print("Task: Restructure the messy code below into clear sections")
print()

# MESSY CODE (Don't modify - just observe):
# vehicles = [100, 200, 150]
# def calc(v): return sum(v) / len(v)
# THRESHOLD = 150
# result = calc(vehicles)
# def check(val): return "High" if val > THRESHOLD else "Low"
# print(check(result))

# YOUR STRUCTURED VERSION:
# TODO: Organize the above code into clear sections following this template:

# ---- SECTION 1: CONSTANTS ----
# TODO: Define THRESHOLD here
THRESHOLD = 150

# ---- SECTION 2: FUNCTIONS ----
# TODO: Define calc() function here (with proper name and docstring)


def calculate_average(values):
    """Calculate average of a list of values.

    Args:
        values (list): List of numeric values

    Returns:
        float: Average value
    """
    return sum(values) / len(values)


# TODO: Define check() function here (with proper name and docstring)
def classify_value(value, threshold=THRESHOLD):
    """Classify value as High or Low based on threshold.

    Args:
        value (float): Value to classify
        threshold (float): Threshold for classification

    Returns:
        str: "High" or "Low"
    """
    return "High" if value > threshold else "Low"


# ---- SECTION 3: MAIN EXECUTION ----
# TODO: Put execution code here
vehicles = [100, 200, 150]
result = calculate_average(vehicles)
classification = classify_value(result)
print(
    f"Exercise 1 Result: Average = {result:.1f}, Classification = {classification}")
print("✅ Exercise 1 Complete: Code is now organized!\n")


# =============================================================================
# EXERCISE 2: Eliminating Code Duplication with Functions
# =============================================================================
print("\n📝 EXERCISE 2: Use Functions to Eliminate Duplication")
print("-" * 70)
print("Task: Replace repeated code with a reusable function")
print()

# DUPLICATED CODE (Don't modify - just observe):
# hour1 = 8
# if 7 <= hour1 <= 9 or 17 <= hour1 <= 19:
#     print(f"Hour {hour1}: Peak time")
# else:
#     print(f"Hour {hour1}: Off-peak")
#
# hour2 = 18
# if 7 <= hour2 <= 9 or 17 <= hour2 <= 19:
#     print(f"Hour {hour2}: Peak time")
# else:
#     print(f"Hour {hour2}: Off-peak")
#
# hour3 = 13
# if 7 <= hour3 <= 9 or 17 <= hour3 <= 19:
#     print(f"Hour {hour3}: Peak time")
# else:
#     print(f"Hour {hour3}: Off-peak")

# YOUR SOLUTION:
# TODO: Create a reusable function to check if hour is peak time


def is_peak_hour(hour):
    """Check if given hour is during peak traffic times.

    Peak times are 7-9 AM and 5-7 PM (17-19 in 24-hour format).

    Args:
        hour (int): Hour in 24-hour format (0-23)

    Returns:
        bool: True if peak hour, False otherwise
    """
    is_morning_peak = 7 <= hour <= 9
    is_evening_peak = 17 <= hour <= 19
    return is_morning_peak or is_evening_peak


# TODO: Use the function to check multiple hours without duplication
hours_to_check = [8, 18, 13]
for hour in hours_to_check:
    if is_peak_hour(hour):
        print(f"Hour {hour}: Peak time")
    else:
        print(f"Hour {hour}: Off-peak")

print("✅ Exercise 2 Complete: Duplication eliminated!\n")


# =============================================================================
# EXERCISE 3: Separating Logic from Execution
# =============================================================================
print("\n📝 EXERCISE 3: Separate Logic from Execution")
print("-" * 70)
print("Task: Organize code with functions defined first, then executed")
print()

# MIXED CODE (Don't modify - just observe):
# data = [50, 75, 125, 90]
# def analyze(values): return max(values)
# peak = analyze(data)
# def format_result(val): return f"Peak: {val}"
# print(format_result(peak))

# YOUR SOLUTION:
# TODO: Define ALL functions first (logic layer)


def find_peak(values):
    """Find the maximum value in a list.

    Args:
        values (list): List of numeric values

    Returns:
        int/float: Maximum value
    """
    return max(values)


def format_peak_result(value):
    """Format peak value as a readable string.

    Args:
        value (int/float): Peak value

    Returns:
        str: Formatted result string
    """
    return f"Peak: {value}"


# TODO: Then execute using those functions (execution layer)
data = [50, 75, 125, 90]
peak = find_peak(data)
formatted_result = format_peak_result(peak)
print(formatted_result)
print("✅ Exercise 3 Complete: Logic separated from execution!\n")


# =============================================================================
# EXERCISE 4: Creating a Complete Structured Script
# =============================================================================
print("\n📝 EXERCISE 4: Build a Complete Structured Program")
print("-" * 70)
print("Task: Create a fully structured traffic signal timing calculator")
print()

# REQUIREMENTS:
# - Calculate optimal signal timing based on vehicle count
# - Light traffic (<500): 30 seconds
# - Medium traffic (500-1000): 45 seconds
# - Heavy traffic (>1000): 60 seconds

# TODO: Section 1 - Define constants
LIGHT_TRAFFIC_MAX = 500
MEDIUM_TRAFFIC_MAX = 1000
LIGHT_TIMING = 30
MEDIUM_TIMING = 45
HEAVY_TIMING = 60

# TODO: Section 2 - Define helper functions


def calculate_signal_timing(vehicle_count):
    """Calculate optimal signal timing based on traffic volume.

    Args:
        vehicle_count (int): Number of vehicles per hour

    Returns:
        int: Signal timing in seconds
    """
    if vehicle_count < LIGHT_TRAFFIC_MAX:
        return LIGHT_TIMING
    elif vehicle_count < MEDIUM_TRAFFIC_MAX:
        return MEDIUM_TIMING
    else:
        return HEAVY_TIMING


def get_traffic_category(vehicle_count):
    """Get traffic category description.

    Args:
        vehicle_count (int): Number of vehicles per hour

    Returns:
        str: Traffic category description
    """
    if vehicle_count < LIGHT_TRAFFIC_MAX:
        return "Light"
    elif vehicle_count < MEDIUM_TRAFFIC_MAX:
        return "Medium"
    else:
        return "Heavy"


# TODO: Section 3 - Define main analysis function
def analyze_signal_timing(intersections):
    """Analyze signal timing needs for multiple intersections.

    Args:
        intersections (dict): Dict mapping intersection name to vehicle count

    Returns:
        dict: Dict mapping intersection name to timing recommendation
    """
    recommendations = {}
    for location, count in intersections.items():
        timing = calculate_signal_timing(count)
        category = get_traffic_category(count)
        recommendations[location] = {
            'timing': timing,
            'category': category,
            'vehicles': count
        }
    return recommendations


# TODO: Section 4 - Execute the program
print("Signal Timing Analysis:")
intersections = {
    "Main St & 1st Ave": 450,
    "Highway 101 Exit": 1200,
    "Downtown Center": 780
}

results = analyze_signal_timing(intersections)

for location, info in results.items():
    print(f"  {location}:")
    print(
        f"    Traffic: {info['category']} ({info['vehicles']} vehicles/hour)")
    print(f"    Recommended timing: {info['timing']} seconds")

print("✅ Exercise 4 Complete: Fully structured program created!\n")


# =============================================================================
# EXERCISE 5: Refactoring Poorly Structured Code
# =============================================================================
print("\n📝 EXERCISE 5: Refactor Poorly Structured Code")
print("-" * 70)
print("Task: Take messy code and restructure it completely")
print()

# MESSY CODE TO REFACTOR:
# speeds = [45, 60, 55, 70, 65]
# total = 0
# for s in speeds:
#     total += s
# avg = total/len(speeds)
# if avg > 60:
#     status = "Fast"
# else:
#     status = "Normal"
# for s in speeds:
#     if s > avg:
#         print(f"{s} is above average")

# YOUR REFACTORED VERSION:

# Constants
FAST_SPEED_THRESHOLD = 60

# Functions


def calculate_speed_average(speeds):
    """Calculate average speed.

    Args:
        speeds (list): List of speed values

    Returns:
        float: Average speed
    """
    return sum(speeds) / len(speeds)


def classify_speed(average_speed, threshold=FAST_SPEED_THRESHOLD):
    """Classify speed as Fast or Normal.

    Args:
        average_speed (float): Average speed value
        threshold (float): Threshold for fast classification

    Returns:
        str: "Fast" or "Normal"
    """
    return "Fast" if average_speed > threshold else "Normal"


def find_above_average_speeds(speeds, average):
    """Find speeds that are above average.

    Args:
        speeds (list): List of speed values
        average (float): Average speed

    Returns:
        list: Speeds above average
    """
    return [speed for speed in speeds if speed > average]


# Main execution
speeds = [45, 60, 55, 70, 65]
average_speed = calculate_speed_average(speeds)
speed_status = classify_speed(average_speed)
above_average = find_above_average_speeds(speeds, average_speed)

print(f"Average speed: {average_speed:.1f} mph ({speed_status})")
print("Speeds above average:")
for speed in above_average:
    print(f"  {speed} mph is above average")

print("✅ Exercise 5 Complete: Code successfully refactored!\n")


# =============================================================================
# CONGRATULATIONS!
# =============================================================================
print("=" * 70)
print("🎉 ALL EXERCISES COMPLETED!")
print("=" * 70)
print("\nYou have practiced:")
print("  ✅ Organizing code into logical sections")
print("  ✅ Using functions to eliminate duplication")
print("  ✅ Separating logic from execution")
print("  ✅ Building structured programs from scratch")
print("  ✅ Refactoring messy code into clean structure")
print()
print("🌟 Key Principles You've Learned:")
print("  1. Imports → Constants → Functions → Main Execution")
print("  2. Write functions once, use them many times")
print("  3. Keep logic and execution separate")
print("  4. Use clear names and documentation")
print("  5. Structure makes code maintainable")
print()
print("Next Step: Apply these principles to all your Python projects!")
print("=" * 70)
