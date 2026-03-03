#!/usr/bin/env python3
"""
SignalSync Function Parameters and Return Values Milestone
A comprehensive demonstration of Python function inputs and outputs for traffic data analysis
"""

def demonstrate_parameters_and_arguments():
    """1. Understanding Parameters and Arguments"""
    print("=" * 60)
    print("📋 1. FUNCTION PARAMETERS AND ARGUMENTS")
    print("=" * 60)
    
    # Function with single parameter
    def calculate_congestion_percentage(congested_hours, total_hours):
        """Calculate what percentage of time traffic is congested"""
        percentage = (congested_hours / total_hours) * 100
        return percentage
    
    # Function with meaningful parameter names
    def classify_traffic_volume(vehicle_count, hour_of_day):
        """Classify traffic volume based on count and time context"""
        if hour_of_day in [7, 8, 17, 18]:  # Rush hours
            if vehicle_count > 800:
                return "Heavy Rush Hour Traffic"
            else:
                return "Light Rush Hour Traffic"
        else:  # Non-rush hours
            if vehicle_count > 500:
                return "High Off-Peak Traffic"
            else:
                return "Normal Off-Peak Traffic"
    
    # Function with multiple parameters of different types
    def generate_traffic_alert(location, volume, weather_condition, is_emergency=False):
        """Generate traffic alert message with multiple input parameters"""
        base_message = f"Traffic Alert for {location}: {volume} vehicles/hour"
        
        if weather_condition != "clear":
            base_message += f" - Weather: {weather_condition}"
        
        if is_emergency:
            base_message = "🚨 EMERGENCY " + base_message
        
        return base_message
    
    print("📋 Demonstrating function calls with different arguments:")
    print()
    
    # Calling functions with various arguments
    congestion_result = calculate_congestion_percentage(6, 24)
    print(f"Daily congestion: {congestion_result:.1f}%")
    
    # Different arguments produce different results
    traffic_class_morning = classify_traffic_volume(950, 8)
    traffic_class_noon = classify_traffic_volume(450, 13)
    print(f"8 AM traffic (950 vehicles): {traffic_class_morning}")
    print(f"1 PM traffic (450 vehicles): {traffic_class_noon}")
    
    # Multiple parameter types
    alert1 = generate_traffic_alert("Highway 101", 1200, "clear")
    alert2 = generate_traffic_alert("Downtown Bridge", 800, "heavy_rain", True)
    print(f"Alert 1: {alert1}")
    print(f"Alert 2: {alert2}")
    
    print("✓ Parameters and arguments demonstration completed")


def demonstrate_returning_values():
    """2. Returning Values from Functions"""
    print("=" * 60)
    print("🔄 2. RETURNING VALUES FROM FUNCTIONS")
    print("=" * 60)
    
    # Function that returns a single calculated value
    def calculate_average_speed(distance_miles, travel_time_minutes):
        """Calculate average speed and return the result"""
        travel_time_hours = travel_time_minutes / 60
        average_speed = distance_miles / travel_time_hours
        return average_speed  # Return the calculated value
    
    # Function that returns based on conditions
    def determine_signal_timing(traffic_volume):
        """Determine optimal signal timing based on traffic volume"""
        if traffic_volume > 1500:
            return 90  # Extended timing for heavy traffic
        elif traffic_volume > 800:
            return 60  # Standard timing
        else:
            return 45  # Short timing for light traffic
    
    # Function that returns different data types
    def analyze_traffic_data(hourly_volumes):
        """Analyze traffic data and return summary statistics"""
        if not hourly_volumes:
            return "No data available"
        
        total_vehicles = sum(hourly_volumes)
        average_volume = total_vehicles / len(hourly_volumes)
        peak_volume = max(hourly_volumes)
        
        # Return a formatted string with analysis
        return f"Total: {total_vehicles}, Average: {average_volume:.1f}, Peak: {peak_volume}"
    
    # Function with multiple return points
    def get_traffic_recommendation(volume, weather):
        """Get traffic management recommendation"""
        if volume > 2000:
            return "Deploy emergency traffic control"
        
        if weather in ["heavy_rain", "snow", "fog"]:
            if volume > 1000:
                return "Activate weather protocols with additional personnel"
            else:
                return "Standard weather advisory"
        
        if volume > 1200:
            return "Monitor closely, consider additional signals"
        
        return "Continue standard operations"
    
    print("🔄 Demonstrating functions that return values:")
    print()
    
    # Functions return values that can be captured and used
    speed = calculate_average_speed(25, 45)  # 25 miles in 45 minutes
    print(f"Average speed: {speed:.1f} mph")
    
    # Return values can be used immediately
    timing_heavy = determine_signal_timing(1600)
    timing_light = determine_signal_timing(400)
    print(f"Heavy traffic signal timing: {timing_heavy} seconds")
    print(f"Light traffic signal timing: {timing_light} seconds")
    
    # Return different types of data
    sample_data = [850, 1200, 950, 1400, 780]
    analysis_result = analyze_traffic_data(sample_data)
    print(f"Traffic analysis: {analysis_result}")
    
    # Multiple return points based on conditions
    recommendation1 = get_traffic_recommendation(2500, "clear")
    recommendation2 = get_traffic_recommendation(900, "heavy_rain")
    print(f"High volume recommendation: {recommendation1}")
    print(f"Weather condition recommendation: {recommendation2}")
    
    print("✓ Return values demonstration completed")


def demonstrate_using_returned_results():
    """3. Using Returned Results"""
    print("=" * 60)
    print("🔗 3. USING RETURNED RESULTS")
    print("=" * 60)
    
    # Functions that build on each other's results
    def calculate_hourly_capacity(lanes, speed_limit):
        """Calculate theoretical hourly capacity of a road segment"""
        vehicles_per_lane_per_hour = speed_limit * 20  # Simplified formula
        total_capacity = lanes * vehicles_per_lane_per_hour
        return total_capacity
    
    def calculate_congestion_ratio(actual_volume, theoretical_capacity):
        """Calculate how congested a road is as a ratio"""
        ratio = actual_volume / theoretical_capacity
        return ratio
    
    def get_congestion_status(congestion_ratio):
        """Convert congestion ratio to human-readable status"""
        if congestion_ratio >= 0.9:
            return "Severely Congested"
        elif congestion_ratio >= 0.7:
            return "Heavy Traffic"
        elif congestion_ratio >= 0.4:
            return "Moderate Traffic"
        else:
            return "Free Flow"
    
    def calculate_delay_minutes(distance_miles, free_flow_speed, congested_speed):
        """Calculate delay caused by congestion"""
        free_flow_time = distance_miles / free_flow_speed * 60  # minutes
        congested_time = distance_miles / congested_speed * 60  # minutes
        delay = congested_time - free_flow_time
        return max(0, delay)  # Don't return negative delays
    
    print("🔗 Demonstrating chained function calls and result usage:")
    print()
    
    # Chain function results together
    road_capacity = calculate_hourly_capacity(4, 65)  # 4 lanes, 65 mph limit
    print(f"Road theoretical capacity: {road_capacity:,} vehicles/hour")
    
    # Use returned result in next calculation
    current_volume = 4200
    congestion_ratio = calculate_congestion_ratio(current_volume, road_capacity)
    print(f"Current volume: {current_volume:,} vehicles/hour")
    print(f"Congestion ratio: {congestion_ratio:.2f}")
    
    # Use returned result to determine status
    traffic_status = get_congestion_status(congestion_ratio)
    print(f"Traffic status: {traffic_status}")
    
    # Store results in variables for later use
    delay = calculate_delay_minutes(15, 65, 25)  # 15 miles, free flow 65mph, congested 25mph
    print(f"Estimated delay: {delay:.1f} minutes")
    
    # Use returned results in mathematical operations
    total_daily_vehicles = 0
    hourly_readings = [850, 1200, 950, 1800, 2200, 1900, 1400, 1100]
    
    for i, volume in enumerate(hourly_readings):
        capacity = calculate_hourly_capacity(3, 55)  # 3 lanes, 55 mph
        ratio = calculate_congestion_ratio(volume, capacity)
        status = get_congestion_status(ratio)
        total_daily_vehicles += volume
        
        print(f"Hour {i+1:2d}: {volume:4d} vehicles - {status}")
    
    # Use accumulated results
    average_hourly = total_daily_vehicles / len(hourly_readings)
    print(f"\nDaily total: {total_daily_vehicles:,} vehicles")
    print(f"Average hourly: {average_hourly:.0f} vehicles")
    
    print("✓ Using returned results demonstration completed")


def demonstrate_common_mistakes():
    """4. Avoiding Common Function Mistakes"""
    print("=" * 60)
    print("⚠️  4. COMMON FUNCTION MISTAKES TO AVOID")
    print("=" * 60)
    
    print("❌ MISTAKE 1: Printing instead of returning")
    print("Bad example:")
    
    def bad_calculate_efficiency_print(volume, capacity):
        """BAD: This function only prints, doesn't return"""
        efficiency = (volume / capacity) * 100
        print(f"Efficiency: {efficiency}%")  # Can't reuse this value!
    
    print("Good example:")
    
    def good_calculate_efficiency_return(volume, capacity):
        """GOOD: This function returns a value for reuse"""
        efficiency = (volume / capacity) * 100
        return efficiency  # Value can be stored and reused
    
    # Demonstrate the difference
    print("Calling bad function (prints but returns None):")
    result_bad = bad_calculate_efficiency_print(800, 1200)
    print(f"Returned value: {result_bad}")  # Will be None
    
    print("\nCalling good function (returns usable value):")
    result_good = good_calculate_efficiency_return(800, 1200)
    print(f"Returned value: {result_good}%")  # Will be the calculated percentage
    print()
    
    print("❌ MISTAKE 2: Hardcoding values inside functions")
    print("Bad example:")
    
    def bad_hardcoded_threshold():
        """BAD: Hardcoded values make function inflexible"""
        traffic_volume = 1000  # Hardcoded!
        if traffic_volume > 800:
            return "Heavy traffic"
        return "Light traffic"
    
    print("Good example:")
    
    def good_flexible_threshold(traffic_volume, threshold=800):
        """GOOD: Accepts parameters, flexible for different scenarios"""
        if traffic_volume > threshold:
            return "Heavy traffic"
        return "Light traffic"
    
    # Show flexibility
    print("Hardcoded function always uses same internal value:")
    print(f"Result: {bad_hardcoded_threshold()}")
    
    print("\nFlexible function can handle different inputs:")
    print(f"Volume 600 vs threshold 800: {good_flexible_threshold(600)}")
    print(f"Volume 1200 vs threshold 800: {good_flexible_threshold(1200)}")
    print(f"Volume 1200 vs threshold 1500: {good_flexible_threshold(1200, 1500)}")
    print()
    
    print("❌ MISTAKE 3: Functions with no clear return path")
    print("Bad example:")
    
    def bad_inconsistent_return(traffic_data):
        """BAD: Sometimes returns value, sometimes doesn't"""
        if len(traffic_data) > 0:
            return sum(traffic_data) / len(traffic_data)
        # Missing return for empty data case!
    
    print("Good example:")
    
    def good_consistent_return(traffic_data):
        """GOOD: Always returns a value or handles edge cases clearly"""
        if len(traffic_data) > 0:
            return sum(traffic_data) / len(traffic_data)
        else:
            return 0  # Clear default for empty data
    
    # Test both functions
    empty_data = []
    sample_data = [100, 200, 300]
    
    print("Testing with empty data:")
    bad_result = bad_inconsistent_return(empty_data)
    good_result = good_consistent_return(empty_data)
    print(f"Bad function result: {bad_result}")  # Will be None
    print(f"Good function result: {good_result}")  # Will be 0
    
    print("✓ Common mistakes demonstration completed")


def demonstrate_real_world_function_design():
    """5. Real-World Function Design Patterns"""
    print("=" * 60)
    print("🏗️  5. REAL-WORLD FUNCTION DESIGN")
    print("=" * 60)
    
    # Well-designed functions for a traffic management system
    def parse_sensor_reading(raw_data_string):
        """Parse raw sensor data into structured format"""
        try:
            parts = raw_data_string.split(',')
            timestamp = parts[0]
            vehicle_count = int(parts[1])
            average_speed = float(parts[2])
            
            return {
                'timestamp': timestamp,
                'vehicles': vehicle_count,
                'speed': average_speed
            }
        except (IndexError, ValueError):
            return None
    
    def calculate_traffic_metrics(sensor_data_list):
        """Calculate comprehensive traffic metrics from sensor data"""
        if not sensor_data_list:
            return {'error': 'No data provided'}
        
        valid_readings = [data for data in sensor_data_list if data is not None]
        
        if not valid_readings:
            return {'error': 'No valid readings found'}
        
        total_vehicles = sum(reading['vehicles'] for reading in valid_readings)
        average_vehicles = total_vehicles / len(valid_readings)
        average_speed = sum(reading['speed'] for reading in valid_readings) / len(valid_readings)
        
        return {
            'total_vehicles': total_vehicles,
            'average_vehicles_per_reading': average_vehicles,
            'average_speed': average_speed,
            'readings_processed': len(valid_readings)
        }
    
    def generate_traffic_report(metrics_dict, location_name):
        """Generate formatted traffic report from metrics"""
        if 'error' in metrics_dict:
            return f"Traffic Report for {location_name}: {metrics_dict['error']}"
        
        report = f"""
Traffic Report for {location_name}
{'='*40}
Total vehicles detected: {metrics_dict['total_vehicles']:,}
Average per reading: {metrics_dict['average_vehicles_per_reading']:.1f}
Average speed: {metrics_dict['average_speed']:.1f} mph
Readings processed: {metrics_dict['readings_processed']}
"""
        return report.strip()
    
    def recommend_signal_adjustment(current_metrics, target_efficiency=0.75):
        """Recommend signal timing adjustments based on traffic metrics"""
        if 'error' in current_metrics:
            return "Cannot make recommendations: " + current_metrics['error']
        
        avg_vehicles = current_metrics['average_vehicles_per_reading']
        avg_speed = current_metrics['average_speed']
        
        # Simple efficiency calculation
        efficiency = min(avg_speed / 45, 1.0)  # 45 mph as ideal speed
        
        if efficiency >= target_efficiency:
            return f"Optimal performance (efficiency: {efficiency:.2f})"
        elif efficiency >= 0.6:
            return f"Minor adjustment needed (efficiency: {efficiency:.2f}) - Extend green by 5 seconds"
        elif efficiency >= 0.4:
            return f"Moderate adjustment needed (efficiency: {efficiency:.2f}) - Extend green by 10 seconds"
        else:
            return f"Major adjustment needed (efficiency: {efficiency:.2f}) - Consider traffic personnel"
    
    print("🏗️ Demonstrating complete workflow with function composition:")
    print()
    
    # Simulate raw sensor data
    raw_sensor_readings = [
        "2026-03-03 08:00,85,42.5",
        "2026-03-03 08:15,120,38.2",
        "2026-03-03 08:30,95,41.8",
        "invalid,data,here",  # Bad data to test error handling
        "2026-03-03 08:45,110,35.6",
        "2026-03-03 09:00,78,44.1"
    ]
    
    # Process data through function chain
    print("Step 1: Parsing raw sensor readings...")
    parsed_readings = []
    for raw_reading in raw_sensor_readings:
        parsed = parse_sensor_reading(raw_reading)
        parsed_readings.append(parsed)
        status = "✓ Valid" if parsed else "✗ Invalid"
        print(f"  {raw_reading[:20]:20} -> {status}")
    
    print("\nStep 2: Calculating traffic metrics...")
    traffic_metrics = calculate_traffic_metrics(parsed_readings)
    for key, value in traffic_metrics.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.1f}")
        else:
            print(f"  {key}: {value}")
    
    print("\nStep 3: Generating traffic report...")
    report = generate_traffic_report(traffic_metrics, "Highway 101 North")
    print(report)
    
    print("\nStep 4: Getting signal recommendations...")
    recommendation = recommend_signal_adjustment(traffic_metrics)
    print(f"Recommendation: {recommendation}")
    
    print("\n✓ Real-world function design demonstration completed")


def main():
    """Main function demonstrating all function parameter and return value concepts"""
    print("🔧" * 20)
    print("SIGNALSYNC FUNCTION PARAMETERS & RETURN VALUES MILESTONE")
    print("Python Function Input-Output Mastery for Traffic Management")
    print("🔧" * 20)
    print()
    
    # Execute all demonstrations in sequence
    demonstrate_parameters_and_arguments()
    print("\n")
    
    demonstrate_returning_values()
    print("\n")
    
    demonstrate_using_returned_results()
    print("\n")
    
    demonstrate_common_mistakes()
    print("\n")
    
    demonstrate_real_world_function_design()
    print("\n")
    
    # Final summary
    print("=" * 60)
    print("✅ FUNCTION PARAMETERS & RETURN VALUES MILESTONE COMPLETE")
    print("=" * 60)
    print()
    print("📚 Skills Demonstrated:")
    print("   ✓ Function parameters and argument passing")
    print("   ✓ Return statements for sending data back")
    print("   ✓ Using returned values in further computations")
    print("   ✓ Avoiding common function design mistakes")
    print("   ✓ Real-world function composition patterns")
    print()
    print("🎯 Key Learning Outcomes:")
    print("   • Functions accept inputs through parameters")
    print("   • Return values enable data flow between functions")
    print("   • Returned results can be stored and reused")
    print("   • Good function design improves code modularity")
    print("   • Avoid printing inside functions - return instead")
    print()
    print("🚀 Ready for advanced function concepts and modular programming!")
    print("🔧" * 20)


if __name__ == "__main__":
    main()