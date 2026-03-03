#!/usr/bin/env python3
"""
SignalSync Code Readability and PEP 8 Naming Milestone
A comprehensive demonstration of readable variable names and meaningful comments
for professional Python code in traffic analysis
"""

def demonstrate_variable_naming_problems():
    """1. Writing Readable Variable Names - Problems to Avoid"""
    print("=" * 60)
    print("❌ 1. POOR VARIABLE NAMING EXAMPLES")
    print("=" * 60)
    
    print("Bad Example 1: Cryptic single-letter variables")
    print("```python")
    print("def bad_example_1():")
    print("    # BAD: What do these variables represent?")
    print("    x = 850")
    print("    y = 1200") 
    print("    z = x / y")
    print("    if z > 0.8:")
    print("        return 'high'")
    print("    return 'low'")
    print("```")
    print()
    
    print("Bad Example 2: Vague and meaningless names")
    print("```python")
    print("def bad_example_2():")
    print("    # BAD: Names don't explain purpose")
    print("    data = [100, 200, 300, 400]")
    print("    result = sum(data)")
    print("    temp = result / len(data)")
    print("    val = temp * 1.5")
    print("    return val")
    print("```")
    print()
    
    print("Bad Example 3: Inconsistent naming styles")
    print("```python")
    print("def bad_example_3():")
    print("    # BAD: Mixed naming conventions")
    print("    TrafficVolume = 1200  # PascalCase")
    print("    average_speed = 45    # snake_case")
    print("    totalVehicles = 500   # camelCase")
    print("    MAX_CAPACITY = 2000   # UPPER_CASE")
    print("    return TrafficVolume + totalVehicles")
    print("```")
    print()
    
    print("❌ These examples show common naming problems:")
    print("  • Cryptic single-letter variables")
    print("  • Vague names that don't explain purpose")
    print("  • Inconsistent naming conventions")
    print("  • Names that require mental translation")
    print()
    print("✓ Poor variable naming examples demonstrated")


def demonstrate_good_variable_naming():
    """1. Writing Readable Variable Names - Good Examples"""
    print("=" * 60)
    print("✅ 1. GOOD VARIABLE NAMING EXAMPLES")
    print("=" * 60)
    
    print("Good Example 1: Descriptive, clear variable names")
    
    def calculate_traffic_congestion_ratio():
        """Calculate congestion ratio with clear variable names"""
        # GOOD: Names clearly explain what each variable represents
        current_vehicle_count = 850
        maximum_road_capacity = 1200
        congestion_ratio = current_vehicle_count / maximum_road_capacity
        
        if congestion_ratio > 0.8:
            return "high_congestion"
        return "normal_flow"
    
    result = calculate_traffic_congestion_ratio()
    print(f"Traffic status: {result}")
    print()
    
    print("Good Example 2: Meaningful names that explain purpose")
    
    def calculate_average_daily_traffic():
        """Calculate average with descriptive variable names"""
        # GOOD: Names explain the data and its purpose
        hourly_vehicle_counts = [100, 200, 300, 400]
        total_daily_vehicles = sum(hourly_vehicle_counts)
        average_hourly_traffic = total_daily_vehicles / len(hourly_vehicle_counts)
        peak_hour_multiplier = 1.5
        estimated_peak_volume = average_hourly_traffic * peak_hour_multiplier
        
        return estimated_peak_volume
    
    peak_estimate = calculate_average_daily_traffic()
    print(f"Estimated peak traffic: {peak_estimate:.0f} vehicles/hour")
    print()
    
    print("Good Example 3: Consistent snake_case naming")
    
    def analyze_traffic_conditions():
        """Analyze traffic with consistent PEP 8 naming"""
        # GOOD: All variables follow snake_case convention
        current_traffic_volume = 1200
        average_speed_mph = 45
        total_vehicles_processed = 500
        road_capacity_limit = 2000
        
        utilization_percentage = (current_traffic_volume / road_capacity_limit) * 100
        
        return {
            'volume': current_traffic_volume,
            'speed': average_speed_mph,
            'utilization': utilization_percentage,
            'status': 'optimal' if utilization_percentage < 80 else 'congested'
        }
    
    conditions = analyze_traffic_conditions()
    print(f"Traffic conditions: {conditions}")
    print()
    
    print("✅ These examples show good naming practices:")
    print("  • Variable names explain their purpose clearly")
    print("  • Consistent snake_case convention throughout")
    print("  • Names reduce need for additional comments")
    print("  • Code is self-documenting and readable")
    print()
    print("✓ Good variable naming examples demonstrated")


def demonstrate_pep8_naming_conventions():
    """2. Following PEP 8 Naming Conventions"""
    print("=" * 60)
    print("📏 2. PEP 8 NAMING CONVENTIONS")
    print("=" * 60)
    
    # PEP 8 Convention Examples
    
    # Variables and functions: snake_case
    traffic_sensor_id = "SENSOR_001"
    maximum_speed_limit = 65
    current_weather_condition = "clear"
    
    def calculate_travel_time_estimate(distance_miles, average_speed_mph):
        """Function names and parameters use snake_case"""
        estimated_travel_minutes = (distance_miles / average_speed_mph) * 60
        return estimated_travel_minutes
    
    # Constants: UPPER_CASE_WITH_UNDERSCORES
    MAX_VEHICLES_PER_HOUR = 2000
    DEFAULT_SPEED_LIMIT_MPH = 55
    EMERGENCY_THRESHOLD_VOLUME = 1800
    RUSH_HOUR_START_TIME = 7
    RUSH_HOUR_END_TIME = 9
    
    # Class names: PascalCase (for reference, not used in this simple example)
    class TrafficSignalController:
        """Class names use PascalCase"""
        
        def __init__(self, intersection_name):
            # Instance variables: snake_case
            self.intersection_name = intersection_name
            self.current_signal_state = "red"
            self.last_cycle_duration = 0
        
        def update_signal_timing(self, new_duration_seconds):
            """Method names use snake_case"""
            self.last_cycle_duration = new_duration_seconds
    
    print("📏 PEP 8 naming convention examples:")
    print()
    
    print("Variables and function names (snake_case):")
    print(f"  traffic_sensor_id = '{traffic_sensor_id}'")
    print(f"  maximum_speed_limit = {maximum_speed_limit}")
    print(f"  current_weather_condition = '{current_weather_condition}'")
    print()
    
    travel_time = calculate_travel_time_estimate(25, 60)
    print(f"Function call: calculate_travel_time_estimate(25, 60) = {travel_time:.1f} minutes")
    print()
    
    print("Constants (UPPER_CASE_WITH_UNDERSCORES):")
    print(f"  MAX_VEHICLES_PER_HOUR = {MAX_VEHICLES_PER_HOUR}")
    print(f"  DEFAULT_SPEED_LIMIT_MPH = {DEFAULT_SPEED_LIMIT_MPH}")
    print(f"  EMERGENCY_THRESHOLD_VOLUME = {EMERGENCY_THRESHOLD_VOLUME}")
    print()
    
    print("Class and method names:")
    signal_controller = TrafficSignalController("Main St & 1st Ave")
    signal_controller.update_signal_timing(90)
    print(f"  Class: TrafficSignalController")
    print(f"  Method: update_signal_timing()")
    print(f"  Instance: {signal_controller.intersection_name}")
    print()
    
    print("✅ PEP 8 naming guidelines:")
    print("  • Variables/functions: snake_case")
    print("  • Constants: UPPER_CASE_WITH_UNDERSCORES")
    print("  • Classes: PascalCase")
    print("  • Be descriptive but concise")
    print("  • Use full words, avoid abbreviations")
    print()
    print("✓ PEP 8 naming conventions demonstrated")


def demonstrate_meaningful_comments():
    """3. Writing Useful Comments"""
    print("=" * 60)
    print("💬 3. MEANINGFUL COMMENTS")
    print("=" * 60)
    
    print("❌ Poor commenting examples:")
    print()
    
    print("Bad Example 1: Obvious comments")
    print("```python")
    print("# BAD: Comments that just restate what the code does")
    print("traffic_volume = 1200  # Set traffic_volume to 1200")
    print("total = volume1 + volume2  # Add volume1 and volume2")
    print("if total > 1000:  # If total is greater than 1000")
    print("    print('High traffic')  # Print 'High traffic'")
    print("```")
    print()
    
    print("Bad Example 2: Misleading or outdated comments")
    print("```python")
    print("# BAD: Comment doesn't match the code")
    print("# Calculate average speed")
    print("traffic_density = vehicles_count / road_length  # Actually calculating density!")
    print("```")
    print()
    
    print("✅ Good commenting examples:")
    print()
    
    def analyze_rush_hour_patterns():
        """Analyze traffic patterns to determine rush hour efficiency"""
        
        # Traffic volume data from sensors over the past week
        daily_traffic_readings = [
            [800, 1200, 900, 1400, 1800, 1600, 1100],  # Monday
            [750, 1100, 850, 1300, 1750, 1550, 1050],  # Tuesday  
            [820, 1250, 920, 1450, 1820, 1620, 1120],  # Wednesday
        ]
        
        rush_hour_efficiency_scores = []
        
        for day_index, daily_readings in enumerate(daily_traffic_readings):
            # Rush hours are typically 7-9 AM (indices 1-2) and 5-7 PM (indices 4-5)
            morning_rush_avg = (daily_readings[1] + daily_readings[2]) / 2
            evening_rush_avg = (daily_readings[4] + daily_readings[5]) / 2
            
            # Efficiency decreases as traffic increases beyond optimal flow (1000 vehicles/hour)
            # Using inverse relationship: higher traffic = lower efficiency
            optimal_flow_rate = 1000
            morning_efficiency = min(100, (optimal_flow_rate / morning_rush_avg) * 100)
            evening_efficiency = min(100, (optimal_flow_rate / evening_rush_avg) * 100)
            
            daily_avg_efficiency = (morning_efficiency + evening_efficiency) / 2
            rush_hour_efficiency_scores.append(daily_avg_efficiency)
            
            print(f"Day {day_index + 1}: {daily_avg_efficiency:.1f}% rush hour efficiency")
        
        # Flag days with efficiency below 70% for signal optimization review
        optimization_needed_days = [
            day + 1 for day, efficiency in enumerate(rush_hour_efficiency_scores)
            if efficiency < 70.0
        ]
        
        return optimization_needed_days
    
    print("Function demonstrating good comment practices:")
    days_needing_optimization = analyze_rush_hour_patterns()
    
    if days_needing_optimization:
        print(f"\n⚠️  Signal optimization recommended for days: {days_needing_optimization}")
    else:
        print(f"\n✅ All days showing acceptable rush hour efficiency")
    
    print()
    print("✅ Good commenting practices shown:")
    print("  • Comments explain WHY, not WHAT")
    print("  • Business logic and assumptions are documented")
    print("  • Complex calculations include reasoning")
    print("  • Comments add value beyond obvious code")
    print("  • Magic numbers are explained (optimal_flow_rate)")
    print()
    print("✓ Meaningful comments demonstrated")


def demonstrate_readability_mistakes():
    """4. Avoiding Common Readability Mistakes"""
    print("=" * 60)
    print("⚠️  4. COMMON READABILITY MISTAKES TO AVOID")
    print("=" * 60)
    
    print("❌ Mistake 1: Commented-out code")
    print("```python")
    print("def calculate_metrics():")
    print("    current_volume = 1200") 
    print("    # old_calculation = volume * 0.8  # Don't leave dead code!")
    print("    # return old_calculation")
    print("    return current_volume * 0.9  # New calculation")
    print("```")
    print("FIX: Remove commented-out code. Use version control instead.")
    print()
    
    print("❌ Mistake 2: Inconsistent naming within same function")
    print("```python")
    print("def bad_consistency():")
    print("    trafficVolume = 1200    # camelCase")
    print("    average_speed = 45      # snake_case") 
    print("    TotalVehicles = 800     # PascalCase")
    print("    # Mixing styles makes code hard to follow")
    print("```")
    print("FIX: Use snake_case consistently for variables.")
    print()
    
    print("❌ Mistake 3: Over-commenting simple operations")
    print("```python")
    print("# BAD: Every line doesn't need a comment")
    print("def over_commented():")
    print("    x = 10        # Initialize x to 10")
    print("    y = 20        # Initialize y to 20") 
    print("    total = x + y # Add x and y to get total")
    print("    return total  # Return the total")
    print("```")
    print("FIX: Only comment when explanation adds value.")
    print()
    
    print("✅ Good practices demonstration:")
    
    def analyze_traffic_efficiency():
        """Calculate traffic efficiency metrics for signal optimization"""
        
        # Input data from traffic monitoring system
        peak_hour_volumes = [1200, 1450, 1300, 1180, 1520]
        road_design_capacity = 1600
        
        # Calculate utilization rates for each peak period
        utilization_rates = []
        for volume in peak_hour_volumes:
            utilization_percentage = (volume / road_design_capacity) * 100
            utilization_rates.append(utilization_percentage)
        
        average_utilization = sum(utilization_rates) / len(utilization_rates)
        
        # Determine if signal timing adjustments are needed
        # Research shows efficiency drops significantly above 85% utilization
        efficiency_threshold = 85.0
        needs_optimization = average_utilization > efficiency_threshold
        
        return {
            'average_utilization_percent': average_utilization,
            'requires_signal_optimization': needs_optimization,
            'utilization_readings': utilization_rates
        }
    
    results = analyze_traffic_efficiency()
    
    print("Clean, readable function example:")
    print(f"Average utilization: {results['average_utilization_percent']:.1f}%")
    print(f"Needs optimization: {results['requires_signal_optimization']}")
    print()
    
    print("✅ Best practices demonstrated:")
    print("  • Consistent snake_case naming throughout")
    print("  • Comments explain business logic and thresholds")
    print("  • No commented-out code")
    print("  • Self-explanatory variable names")
    print("  • Comments add contextual value")
    print()
    print("✓ Readability best practices demonstrated")


def demonstrate_before_after_refactoring():
    """5. Before and After Code Refactoring Example"""
    print("=" * 60)
    print("🔄 5. BEFORE AND AFTER REFACTORING")
    print("=" * 60)
    
    print("❌ BEFORE: Poor readability")
    print("```python")
    print("def bad_code():")
    print("    # bad variable names, poor comments")
    print("    x = [100, 200, 300, 400, 500]  # numbers")
    print("    y = 0")
    print("    for i in x:")
    print("        y += i  # add i to y") 
    print("    z = y / len(x)  # divide")
    print("    if z > 250:")
    print("        return True  # return true")
    print("    else:")
    print("        return False  # return false")
    print("```")
    print()
    
    print("✅ AFTER: Improved readability")
    
    def calculate_traffic_alert_status(hourly_vehicle_counts):
        """
        Determine if traffic levels warrant an alert based on average volume.
        
        Args:
            hourly_vehicle_counts: List of vehicle counts for each hour
            
        Returns:
            bool: True if average exceeds alert threshold, False otherwise
        """
        # Calculate average hourly traffic volume
        total_vehicles_observed = sum(hourly_vehicle_counts)
        average_hourly_volume = total_vehicles_observed / len(hourly_vehicle_counts)
        
        # Alert threshold based on road capacity studies
        # Values above 250 vehicles/hour indicate potential congestion
        congestion_alert_threshold = 250
        
        alert_required = average_hourly_volume > congestion_alert_threshold
        return alert_required
    
    # Test the refactored function
    sample_traffic_data = [100, 200, 300, 400, 500]
    alert_status = calculate_traffic_alert_status(sample_traffic_data)
    
    print("Refactored function in action:")
    print(f"Traffic data: {sample_traffic_data}")
    print(f"Alert required: {alert_status}")
    print()
    
    print("🔄 Improvements made:")
    print("  • Descriptive function and variable names")
    print("  • Clear docstring explaining purpose")
    print("  • Comments explain business logic, not syntax")
    print("  • Consistent naming convention (snake_case)")
    print("  • Self-documenting code structure")
    print("  • Meaningful return value context")
    print()
    print("✓ Before/after refactoring demonstrated")


def main():
    """Main function demonstrating all code readability and PEP 8 concepts"""
    print("📝" * 20)
    print("SIGNALSYNC CODE READABILITY & PEP 8 NAMING MILESTONE")
    print("Professional Python Code Standards for Traffic Analysis")
    print("📝" * 20)
    print()
    
    # Execute all demonstrations in sequence
    demonstrate_variable_naming_problems()
    print("\n")
    
    demonstrate_good_variable_naming()
    print("\n")
    
    demonstrate_pep8_naming_conventions()
    print("\n")
    
    demonstrate_meaningful_comments()
    print("\n")
    
    demonstrate_readability_mistakes()
    print("\n")
    
    demonstrate_before_after_refactoring()
    print("\n")
    
    # Final summary
    print("=" * 60)
    print("✅ CODE READABILITY & PEP 8 MILESTONE COMPLETE")
    print("=" * 60)
    print()
    print("📚 Skills Demonstrated:")
    print("   ✓ Readable variable naming with clear intent")
    print("   ✓ PEP 8 naming conventions (snake_case, CONSTANTS)")
    print("   ✓ Meaningful comments that explain why, not what")
    print("   ✓ Avoiding common readability mistakes")
    print("   ✓ Before/after code refactoring examples")
    print()
    print("🎯 Key Learning Outcomes:")
    print("   • Variable names should be self-explanatory")
    print("   • Consistent naming conventions improve readability")
    print("   • Comments should explain intent and business logic")
    print("   • Clean code is easier to maintain and review")
    print("   • Professional coding standards build team trust")
    print()
    print("💡 Remember:")
    print("   • Code is read more often than it's written")
    print("   • Write for humans first, computers second")
    print("   • Consistency is more important than personal preference")
    print("   • Good naming reduces the need for comments")
    print()
    print("🚀 Ready for professional-quality Python development!")
    print("📝" * 20)


if __name__ == "__main__":
    main()