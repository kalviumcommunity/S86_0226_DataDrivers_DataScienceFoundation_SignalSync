#!/usr/bin/env python3
"""
Code Structure Comparison: Poor vs. Well-Structured
====================================================
This file demonstrates the difference between poorly structured and 
well-structured Python code.

Learning Objectives:
- Understand why code structure matters
- See the impact of organization on readability
- Learn to separate concerns effectively
"""

print("=" * 70)
print("DEMONSTRATION: POOR CODE STRUCTURE vs. WELL-STRUCTURED CODE")
print("=" * 70)

# =============================================================================
# PART 1: POORLY STRUCTURED CODE
# =============================================================================
print("\n❌ PART 1: POORLY STRUCTURED CODE")
print("-" * 70)
print("Problems in this code:")
print("  • No clear organization or sections")
print("  • Repeated logic scattered throughout")
print("  • Mixed concerns (data, logic, execution)")
print("  • Hard to read and maintain")
print("-" * 70)

print("\n```python")
print("# BAD: Everything mixed together, no structure")
print("vehicles = [850, 1200, 450, 980, 1500, 670]")
print("total = 0")
print("for v in vehicles:")
print("    total = total + v")
print("avg = total / len(vehicles)")
print("print(avg)")
print("")
print("# BAD: Duplicated logic")
print("if vehicles[0] > 1000:")
print("    print('High')")
print("else:")
print("    print('Normal')")
print("")
print("if vehicles[1] > 1000:")
print("    print('High')")
print("else:")
print("    print('Normal')")
print("")
print("# More duplicated checks...")
print("if vehicles[2] > 1000:")
print("    print('High')")
print("else:")
print("    print('Normal')")
print("```\n")

# Actual execution of poor code for demonstration
vehicles = [850, 1200, 450, 980, 1500, 670]
total = 0
for v in vehicles:
    total = total + v
avg = total / len(vehicles)
print(f"Output: Average = {avg:.1f}")

if vehicles[0] > 1000:
    result1 = 'High'
else:
    result1 = 'Normal'
print(f"Output: Vehicle 1 = {result1}")

if vehicles[1] > 1000:
    result2 = 'High'
else:
    result2 = 'Normal'
print(f"Output: Vehicle 2 = {result2}")


# =============================================================================
# PART 2: WELL-STRUCTURED CODE
# =============================================================================
print("\n\n✅ PART 2: WELL-STRUCTURED CODE")
print("-" * 70)
print("Improvements in this code:")
print("  • Clear sections: imports, constants, functions, main")
print("  • Reusable functions eliminate duplication")
print("  • Separated logic from execution")
print("  • Easy to read, test, and maintain")
print("-" * 70)

print("\n```python")
print("# ============================================================================")
print("# SECTION 1: IMPORTS")
print("# ============================================================================")
print("# (imports would go here if needed)")
print("")
print("# ============================================================================")
print("# SECTION 2: CONSTANTS AND CONFIGURATION")
print("# ============================================================================")
print("HIGH_TRAFFIC_THRESHOLD = 1000")
print("")
print("# ============================================================================")
print("# SECTION 3: REUSABLE FUNCTIONS")
print("# ============================================================================")
print("def calculate_average(numbers):")
print("    '''Calculate average of a list of numbers'''")
print("    return sum(numbers) / len(numbers)")
print("")
print("def classify_traffic_volume(volume, threshold=1000):")
print("    '''Classify traffic volume as High or Normal'''")
print("    return 'High' if volume > threshold else 'Normal'")
print("")
print("def analyze_traffic_data(volumes):")
print("    '''Analyze traffic data and return classifications'''")
print("    results = []")
print("    for volume in volumes:")
print("        classification = classify_traffic_volume(volume)")
print("        results.append(classification)")
print("    return results")
print("")
print("# ============================================================================")
print("# SECTION 4: MAIN EXECUTION")
print("# ============================================================================")
print("def main():")
print("    vehicle_data = [850, 1200, 450, 980, 1500, 670]")
print("    average = calculate_average(vehicle_data)")
print("    classifications = analyze_traffic_data(vehicle_data)")
print("    print(f'Average: {average:.1f}')")
print("    for i, classification in enumerate(classifications, 1):")
print("        print(f'Vehicle {i} = {classification}')")
print("")
print("if __name__ == '__main__':")
print("    main()")
print("```\n")

# Actual execution of well-structured code

# ============================================================================
# SECTION 1: IMPORTS
# ============================================================================
# (no external imports needed for this simple example)

# ============================================================================
# SECTION 2: CONSTANTS AND CONFIGURATION
# ============================================================================
HIGH_TRAFFIC_THRESHOLD = 1000

# ============================================================================
# SECTION 3: REUSABLE FUNCTIONS
# ============================================================================


def calculate_average(numbers):
    """Calculate average of a list of numbers.

    Args:
        numbers (list): List of numeric values

    Returns:
        float: Average value
    """
    return sum(numbers) / len(numbers)


def classify_traffic_volume(volume, threshold=HIGH_TRAFFIC_THRESHOLD):
    """Classify traffic volume as High or Normal.

    Args:
        volume (int): Vehicle count
        threshold (int): Threshold for high traffic

    Returns:
        str: Classification ('High' or 'Normal')
    """
    return 'High' if volume > threshold else 'Normal'


def analyze_traffic_data(volumes):
    """Analyze traffic data and return classifications.

    Args:
        volumes (list): List of vehicle counts

    Returns:
        list: List of traffic classifications
    """
    results = []
    for volume in volumes:
        classification = classify_traffic_volume(volume)
        results.append(classification)
    return results


# ============================================================================
# SECTION 4: MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    # Data
    vehicle_data = [850, 1200, 450, 980, 1500, 670]

    # Process
    average = calculate_average(vehicle_data)
    classifications = analyze_traffic_data(vehicle_data)

    # Display results
    print(f"Output: Average = {average:.1f}")
    for i, classification in enumerate(classifications, 1):
        print(f"Output: Vehicle {i} = {classification}")


# Execute only if run as a script
if __name__ == "__main__":
    main()


# =============================================================================
# SUMMARY OF BENEFITS
# =============================================================================
print("\n\n📊 COMPARISON SUMMARY")
print("=" * 70)
print("POORLY STRUCTURED CODE:")
print("  ❌ Hard to understand flow")
print("  ❌ Duplicated logic (3+ times)")
print("  ❌ Difficult to modify or test")
print("  ❌ No reusability")
print()
print("WELL-STRUCTURED CODE:")
print("  ✅ Clear, logical organization")
print("  ✅ Reusable functions (no duplication)")
print("  ✅ Easy to test and maintain")
print("  ✅ Scalable and professional")
print("=" * 70)

print("\n🎯 KEY TAKEAWAY:")
print("Structure transforms working code into maintainable, professional code.")
print("Good structure makes code easier to read, debug, and extend over time.")
print("=" * 70)
