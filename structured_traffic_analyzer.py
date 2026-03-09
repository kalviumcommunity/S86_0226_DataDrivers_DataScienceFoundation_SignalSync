#!/usr/bin/env python3
"""
SignalSync Traffic Analyzer - Well-Structured Example
======================================================
A comprehensive example of well-structured Python code for traffic analysis.

Purpose:
    Demonstrates professional code organization with clear sections,
    reusable functions, and separation of concerns.

Author: DataDrivers Team
Date: March 2026
"""

# ============================================================================
# SECTION 1: IMPORTS
# ============================================================================
# Import statements go at the top
from datetime import datetime

# ============================================================================
# SECTION 2: CONSTANTS AND CONFIGURATION
# ============================================================================
# Define configuration values that might change

# Traffic thresholds
LIGHT_TRAFFIC_MAX = 500
MODERATE_TRAFFIC_MAX = 1000
HEAVY_TRAFFIC_MAX = 1500
# Values above HEAVY_TRAFFIC_MAX are considered "Critical"

# Peak hours (24-hour format)
MORNING_PEAK_START = 7
MORNING_PEAK_END = 9
EVENING_PEAK_START = 17
EVENING_PEAK_END = 19

# Alert settings
ALERT_THRESHOLD = 1200
CONGESTION_PERCENTAGE_WARNING = 30.0


# ============================================================================
# SECTION 3: HELPER FUNCTIONS (Reusable Utilities)
# ============================================================================

def calculate_average(values):
    """Calculate the average of a list of numbers.

    Args:
        values (list): List of numeric values

    Returns:
        float: Average value, or 0 if list is empty
    """
    if not values:
        return 0
    return sum(values) / len(values)


def calculate_percentage(part, total):
    """Calculate percentage of part relative to total.

    Args:
        part (int/float): The part value
        total (int/float): The total value

    Returns:
        float: Percentage value (0-100)
    """
    if total == 0:
        return 0
    return (part / total) * 100


def format_time(hour):
    """Format hour (0-23) into readable time string.

    Args:
        hour (int): Hour in 24-hour format (0-23)

    Returns:
        str: Formatted time string (e.g., "7:00 AM")
    """
    period = "AM" if hour < 12 else "PM"
    display_hour = hour if hour <= 12 else hour - 12
    display_hour = 12 if display_hour == 0 else display_hour
    return f"{display_hour}:00 {period}"


# ============================================================================
# SECTION 4: CLASSIFICATION FUNCTIONS
# ============================================================================

def classify_traffic_level(volume):
    """Classify traffic volume into descriptive levels.

    Args:
        volume (int): Number of vehicles per hour

    Returns:
        str: Traffic level classification
    """
    if volume < LIGHT_TRAFFIC_MAX:
        return "Light"
    elif volume < MODERATE_TRAFFIC_MAX:
        return "Moderate"
    elif volume < HEAVY_TRAFFIC_MAX:
        return "Heavy"
    else:
        return "Critical"


def is_peak_hour(hour):
    """Determine if given hour is during peak traffic times.

    Args:
        hour (int): Hour in 24-hour format (0-23)

    Returns:
        bool: True if peak hour, False otherwise
    """
    is_morning_peak = MORNING_PEAK_START <= hour < MORNING_PEAK_END
    is_evening_peak = EVENING_PEAK_START <= hour < EVENING_PEAK_END
    return is_morning_peak or is_evening_peak


def should_alert(volume):
    """Determine if traffic volume requires an alert.

    Args:
        volume (int): Number of vehicles per hour

    Returns:
        bool: True if alert needed, False otherwise
    """
    return volume >= ALERT_THRESHOLD


# ============================================================================
# SECTION 5: DATA ANALYSIS FUNCTIONS
# ============================================================================

def analyze_hourly_data(hourly_volumes):
    """Analyze hourly traffic data and return statistics.

    Args:
        hourly_volumes (dict): Dict mapping hour to vehicle count

    Returns:
        dict: Dictionary containing analysis results
    """
    volumes = list(hourly_volumes.values())

    analysis = {
        'total_vehicles': sum(volumes),
        'average_volume': calculate_average(volumes),
        'peak_volume': max(volumes) if volumes else 0,
        'min_volume': min(volumes) if volumes else 0,
        'hours_analyzed': len(volumes)
    }

    return analysis


def identify_congested_hours(hourly_volumes):
    """Identify hours with high congestion.

    Args:
        hourly_volumes (dict): Dict mapping hour to vehicle count

    Returns:
        list: List of tuples (hour, volume) for congested periods
    """
    congested = []
    for hour, volume in hourly_volumes.items():
        if should_alert(volume):
            congested.append((hour, volume))
    return congested


def calculate_congestion_rate(hourly_volumes):
    """Calculate what percentage of time traffic is congested.

    Args:
        hourly_volumes (dict): Dict mapping hour to vehicle count

    Returns:
        float: Congestion percentage (0-100)
    """
    congested_hours = identify_congested_hours(hourly_volumes)
    total_hours = len(hourly_volumes)
    return calculate_percentage(len(congested_hours), total_hours)


# ============================================================================
# SECTION 6: REPORTING FUNCTIONS
# ============================================================================

def print_header(title):
    """Print a formatted section header.

    Args:
        title (str): Header title text
    """
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_statistics(stats):
    """Print traffic statistics in formatted style.

    Args:
        stats (dict): Dictionary containing statistics
    """
    print(f"\nTotal vehicles observed: {stats['total_vehicles']:,}")
    print(f"Average hourly volume: {stats['average_volume']:.1f}")
    print(f"Peak traffic volume: {stats['peak_volume']:,}")
    print(f"Minimum traffic volume: {stats['min_volume']:,}")
    print(f"Hours analyzed: {stats['hours_analyzed']}")


def print_congestion_report(hourly_volumes):
    """Print report of congested hours.

    Args:
        hourly_volumes (dict): Dict mapping hour to vehicle count
    """
    congested = identify_congested_hours(hourly_volumes)

    print(f"\n🚨 Congested Hours (>{ALERT_THRESHOLD:,} vehicles/hour):")
    if congested:
        for hour, volume in congested:
            time_str = format_time(hour)
            level = classify_traffic_level(volume)
            peak_marker = " [PEAK]" if is_peak_hour(hour) else ""
            print(f"  • {time_str}: {volume:,} vehicles - {level}{peak_marker}")
    else:
        print("  None detected")


def print_recommendations(congestion_rate):
    """Print traffic management recommendations.

    Args:
        congestion_rate (float): Percentage of time with congestion
    """
    print("\n💡 Recommendations:")
    if congestion_rate > CONGESTION_PERCENTAGE_WARNING:
        print("  • HIGH congestion detected - Signal optimization needed")
        print("  • Deploy traffic personnel during peak hours")
        print("  • Consider alternative route notifications")
    elif congestion_rate > 15:
        print("  • MODERATE congestion - Continue monitoring")
        print("  • Prepare contingency plans")
    else:
        print("  • Traffic flow is NORMAL - Maintain current operations")


# ============================================================================
# SECTION 7: MAIN EXECUTION LOGIC
# ============================================================================

def run_traffic_analysis(traffic_data):
    """Execute complete traffic analysis workflow.

    Args:
        traffic_data (dict): Hourly traffic volume data

    Returns:
        dict: Complete analysis results
    """
    # Analyze data
    stats = analyze_hourly_data(traffic_data)
    congestion_rate = calculate_congestion_rate(traffic_data)

    # Generate reports
    print_header("📊 TRAFFIC ANALYSIS RESULTS")
    print_statistics(stats)
    print_congestion_report(traffic_data)

    print(f"\n📈 Congestion Rate: {congestion_rate:.1f}%")
    print_recommendations(congestion_rate)

    # Return results for potential further use
    return {
        'statistics': stats,
        'congestion_rate': congestion_rate
    }


def main():
    """Main program entry point."""
    # Display program header
    print_header("🚦 SignalSync Traffic Analyzer")
    print("Well-Structured Code Example")
    print("Analyzing traffic patterns for optimization")

    # Sample data: Hour -> Vehicle Count
    traffic_data = {
        6: 420,
        7: 850,
        8: 1200,
        9: 680,
        10: 550,
        11: 720,
        12: 950,
        13: 880,
        14: 790,
        15: 920,
        16: 1100,
        17: 1350,
        18: 1280,
        19: 890,
        20: 640
    }

    print(f"\nProcessing {len(traffic_data)} hours of traffic data...")

    # Run analysis
    results = run_traffic_analysis(traffic_data)

    # Completion message
    print("\n" + "=" * 70)
    print("✅ Analysis Complete!")
    print("=" * 70)

    return results


# ============================================================================
# SECTION 8: SCRIPT ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    # Execute main function only when script is run directly
    main()


# ============================================================================
# KEY STRUCTURE PRINCIPLES DEMONSTRATED:
# ============================================================================
# 1. CLEAR SECTIONS: Imports, constants, functions, main execution
# 2. REUSABLE FUNCTIONS: Each function has one clear purpose
# 3. NO DUPLICATION: Logic written once, used many times
# 4. SEPARATION OF CONCERNS: Data, logic, and display are separate
# 5. TOP-TO-BOTTOM FLOW: Code reads naturally like a story
# 6. DOCUMENTATION: Docstrings explain purpose and usage
# 7. MAINTAINABILITY: Easy to modify, test, and extend
# ============================================================================
