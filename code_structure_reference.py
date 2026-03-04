#!/usr/bin/env python3
"""
Code Structure Quick Reference Guide
=====================================
A template and reference for structuring Python code properly.

Use this as a starting point for all your Python projects!
"""

# ============================================================================
# TEMPLATE: WELL-STRUCTURED PYTHON SCRIPT
# ============================================================================

"""
YOUR SCRIPT TITLE
=================
Brief description of what this script does.

Author: Your Name
Date: Date Created
Purpose: Main purpose of the script
"""

# ============================================================================
# SECTION 1: IMPORTS
# ============================================================================
# All import statements go at the very top
# Organize: Standard library → Third-party → Local modules

# Standard library imports
# import os
# import sys
# from datetime import datetime

# Third-party imports
# import numpy as np
# import pandas as pd

# Local module imports
# from my_module import my_function


# ============================================================================
# SECTION 2: CONSTANTS AND CONFIGURATION
# ============================================================================
# Define constants using UPPER_CASE_WITH_UNDERSCORES
# These are values that don't change during execution

# Example constants:
# MAX_THRESHOLD = 1000
# MIN_THRESHOLD = 100
# DEFAULT_VALUE = 50
# FILE_PATH = "data/input.csv"


# ============================================================================
# SECTION 3: HELPER FUNCTIONS
# ============================================================================
# Small, reusable utility functions
# Each function should do ONE thing well
# Always include docstrings

def example_helper_function(parameter):
    """Brief description of what this function does.

    Args:
        parameter (type): Description of parameter

    Returns:
        type: Description of return value
    """
    # Function implementation
    result = parameter * 2
    return result


# ============================================================================
# SECTION 4: CORE LOGIC FUNCTIONS
# ============================================================================
# Main business logic functions
# These use the helper functions to accomplish larger tasks

def example_processing_function(data):
    """Process data using helper functions.

    Args:
        data (list): Input data to process

    Returns:
        list: Processed results
    """
    results = []
    for item in data:
        processed = example_helper_function(item)
        results.append(processed)
    return results


# ============================================================================
# SECTION 5: OUTPUT/DISPLAY FUNCTIONS
# ============================================================================
# Functions that handle displaying results or generating output

def display_results(results):
    """Display results in a formatted way.

    Args:
        results (list): Results to display
    """
    print("Results:")
    for i, result in enumerate(results, 1):
        print(f"  {i}. {result}")


# ============================================================================
# SECTION 6: MAIN EXECUTION FUNCTION
# ============================================================================
# The main() function orchestrates the entire program flow

def main():
    """Main execution function - program entry point."""
    # 1. Setup/initialization
    print("Program starting...")

    # 2. Load or prepare data
    sample_data = [10, 20, 30, 40, 50]

    # 3. Process data
    results = example_processing_function(sample_data)

    # 4. Display results
    display_results(results)

    # 5. Cleanup/completion
    print("Program complete!")


# ============================================================================
# SECTION 7: SCRIPT ENTRY POINT
# ============================================================================
# This allows the script to be imported without executing

if __name__ == "__main__":
    main()


# ============================================================================
# QUICK REFERENCE: DO'S AND DON'TS
# ============================================================================

print("\n" + "=" * 70)
print("CODE STRUCTURE QUICK REFERENCE")
print("=" * 70)

print("\n✅ DO:")
print("  • Organize code into clear sections")
print("  • Put imports at the top")
print("  • Define constants before functions")
print("  • Write functions before using them")
print("  • Use descriptive names")
print("  • Add docstrings to functions")
print("  • Keep functions focused and small")
print("  • Separate logic from execution")
print("  • Use main() function")
print("  • Use if __name__ == '__main__'")

print("\n❌ DON'T:")
print("  • Mix imports with code")
print("  • Use unclear variable names (x, y, temp)")
print("  • Duplicate code instead of using functions")
print("  • Write functions after calling them")
print("  • Mix logic and execution randomly")
print("  • Create giant functions that do everything")
print("  • Skip documentation")
print("  • Ignore consistent formatting")

print("\n" + "=" * 70)
print("STRUCTURE PATTERN")
print("=" * 70)
print("""
1. Module docstring
2. Imports (standard → third-party → local)
3. Constants (UPPERCASE)
4. Helper functions (small utilities)
5. Core functions (business logic)
6. Main function (orchestration)
7. Entry point (if __name__ == "__main__")
""")

print("=" * 70)
print("FUNCTION DESIGN PRINCIPLES")
print("=" * 70)
print("""
✓ One function = One responsibility
✓ Function name describes what it does
✓ Parameters make function reusable
✓ Return values make output predictable
✓ Docstrings explain purpose and usage
✓ Keep functions short (< 30 lines ideal)
✓ Avoid side effects when possible
""")

print("=" * 70)
print("NAMING CONVENTIONS")
print("=" * 70)
print("""
Variables:       lowercase_with_underscores
Functions:       lowercase_with_underscores
Constants:       UPPERCASE_WITH_UNDERSCORES
Classes:         PascalCase (later lessons)
Private:         _leading_underscore
""")

print("=" * 70)
print("EXAMPLE: GOOD vs BAD FUNCTION STRUCTURE")
print("=" * 70)

print("\n❌ BAD EXAMPLE:")
print("""
def f(x, y):
    return x / y if y != 0 else 0
""")

print("✅ GOOD EXAMPLE:")
print("""
def calculate_percentage(part, total):
    '''Calculate what percentage part is of total.
    
    Args:
        part (float): The part value
        total (float): The total value
        
    Returns:
        float: Percentage (0-100), or 0 if total is zero
    '''
    if total == 0:
        return 0
    return (part / total) * 100
""")

print("\n" + "=" * 70)
print("REUSABILITY CHECKLIST")
print("=" * 70)
print("""
Before writing code, ask:

□ Have I written this logic before?
  → If yes, extract it into a function

□ Will I need this logic again?
  → If yes, make it a function now

□ Does this code do more than one thing?
  → If yes, split into multiple functions

□ Can someone understand this in 30 seconds?
  → If no, add documentation or simplify

□ Would this be easy to test?
  → If no, refactor for testability
""")

print("=" * 70)
print("COMMON REFACTORING PATTERNS")
print("=" * 70)
print("""
PATTERN 1: Extract Repeated Code
BEFORE:
    if x > 100: print("High")
    if y > 100: print("High")
    if z > 100: print("High")

AFTER:
    def classify(val):
        return "High" if val > 100 else "Normal"
    
    print(classify(x))
    print(classify(y))
    print(classify(z))

---

PATTERN 2: Extract Complex Condition
BEFORE:
    if (temp > 70 and humidity < 50) or (temp > 80):
        activate_cooling()

AFTER:
    def needs_cooling(temperature, humidity):
        return (temp > 70 and humidity < 50) or (temp > 80)
    
    if needs_cooling(temp, humidity):
        activate_cooling()

---

PATTERN 3: Extract Calculation
BEFORE:
    result = (x + y + z) / 3

AFTER:
    def calculate_average(values):
        return sum(values) / len(values)
    
    result = calculate_average([x, y, z])
""")

print("\n" + "=" * 70)
print("DEBUGGING TIP")
print("=" * 70)
print("""
Well-structured code is easier to debug:

✓ Each function can be tested independently
✓ Clear names help identify issues quickly
✓ Separation makes problems easier to isolate
✓ Reusable functions mean fewer places to fix bugs
""")

print("\n" + "=" * 70)
print("COLLABORATION TIP")
print("=" * 70)
print("""
Good structure helps teams work together:

✓ Others can understand your code quickly
✓ Clear sections make it easy to find logic
✓ Documentation helps onboard new members
✓ Consistent patterns enable parallel work
""")

print("\n" + "=" * 70)
print("🎯 REMEMBER")
print("=" * 70)
print("""
"Any fool can write code that a computer can understand.
Good programmers write code that humans can understand."
    - Martin Fowler

Structure is not about following rules blindly.
Structure is about respecting future readers of your code,
including yourself.
""")
print("=" * 70)

print("\n📚 Use this file as a reference when starting new projects!")
print("Happy coding! 🚀\n")
