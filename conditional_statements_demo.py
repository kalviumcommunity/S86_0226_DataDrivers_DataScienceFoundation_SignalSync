#!/usr/bin/env python3
"""
SignalSync Conditional Statements Milestone
A comprehensive demonstration of Python conditional logic for traffic data analysis
"""

def demonstrate_basic_if_statements():
    """1. Writing Basic if Statements"""
    print("=" * 60)
    print("🔍 1. BASIC IF STATEMENTS")
    print("=" * 60)
    
    # Simple traffic volume check
    current_volume = 850
    rush_hour_threshold = 1000
    
    print(f"Current traffic volume: {current_volume} vehicles/hour")
    print(f"Rush hour threshold: {rush_hour_threshold} vehicles/hour")
    print()
    
    # Basic if statement - only executes when condition is true
    if current_volume > rush_hour_threshold:
        print("🚨 ALERT: Rush hour traffic detected!")
        print("   Recommend signal optimization")
    
    print("✓ Basic if statement check completed")
    print()
    
    # Another example with string comparison
    traffic_light_status = "red"
    
    print(f"Traffic light status: {traffic_light_status}")
    
    if traffic_light_status == "red":
        print("🔴 Vehicles must stop")
    
    if traffic_light_status == "green":
        print("🟢 Vehicles may proceed")
    
    print("✓ String condition check completed")


def demonstrate_if_else_branching():
    """2. Using if–else for Decision Branching"""
    print("=" * 60)
    print("🔀 2. IF-ELSE DECISION BRANCHING")
    print("=" * 60)
    
    # Traffic volume classification with clear true/false paths
    volumes_to_test = [450, 1200, 800, 1500]
    
    for volume in volumes_to_test:
        print(f"Testing volume: {volume} vehicles/hour")
        
        if volume >= 1000:
            print("   📈 High traffic - Deploy additional resources")
            recommendation = "Increase signal timing"
        else:
            print("   📊 Normal traffic - Standard operations")
            recommendation = "Maintain current settings"
        
        print(f"   Action: {recommendation}")
        print()
    
    # Weather-based traffic management
    weather_condition = "heavy_rain"
    
    print(f"Current weather: {weather_condition}")
    
    if weather_condition == "clear":
        print("   ☀️ Normal traffic patterns expected")
    else:
        print("   🌧️ Adverse weather - Expect slower traffic")
        print("   Recommend increased safety messaging")
    
    print("✓ If-else branching demonstration completed")


def demonstrate_elif_multiple_conditions():
    """3. Handling Multiple Conditions with elif"""
    print("=" * 60)
    print("🎯 3. MULTIPLE CONDITIONS WITH ELIF")
    print("=" * 60)
    
    # Traffic congestion level classification
    test_volumes = [300, 750, 1100, 1800, 2500]
    
    for volume in test_volumes:
        print(f"Analyzing volume: {volume} vehicles/hour")
        
        # Multiple condition checks with elif - only one branch executes
        if volume < 500:
            level = "Light"
            color = "🟢"
            action = "Normal operations"
        elif volume < 1000:
            level = "Moderate" 
            color = "🟡"
            action = "Monitor closely"
        elif volume < 1500:
            level = "Heavy"
            color = "🟠"
            action = "Optimize signals"
        elif volume < 2000:
            level = "Severe"
            color = "🔴"
            action = "Deploy traffic personnel"
        else:
            level = "Critical"
            color = "⚫"
            action = "Emergency traffic management"
        
        print(f"   {color} Traffic Level: {level}")
        print(f"   Recommended Action: {action}")
        print()
    
    # Time-based traffic management
    current_hour = 17  # 5 PM
    
    print(f"Current time: {current_hour}:00")
    
    if current_hour < 6:
        period = "Late Night"
        signal_mode = "Flashing yellow"
    elif current_hour < 9:
        period = "Morning Rush"
        signal_mode = "Extended green for main routes"
    elif current_hour < 16:
        period = "Midday"
        signal_mode = "Standard timing"
    elif current_hour < 19:
        period = "Evening Rush"
        signal_mode = "Extended green for exit routes"
    else:
        period = "Evening"
        signal_mode = "Reduced timing"
    
    print(f"   Period: {period}")
    print(f"   Signal Mode: {signal_mode}")
    print("✓ Elif multiple conditions demonstration completed")


def demonstrate_logical_operators():
    """4. Using Logical Operators"""
    print("=" * 60)
    print("🔗 4. LOGICAL OPERATORS (AND, OR, NOT)")
    print("=" * 60)
    
    # Sample traffic data for logical operator demonstrations
    volume = 1200
    weather = "rain"
    time_hour = 8
    accident_reported = False
    
    print("Current Traffic Conditions:")
    print(f"   Volume: {volume} vehicles/hour")
    print(f"   Weather: {weather}")
    print(f"   Time: {time_hour}:00")
    print(f"   Accident reported: {accident_reported}")
    print()
    
    # AND operator - all conditions must be true
    print("🔗 Using AND operator:")
    if volume > 1000 and time_hour >= 7 and time_hour <= 9:
        print("   ✅ Morning rush hour with high volume detected")
        print("   Action: Activate full rush hour protocols")
    else:
        print("   ❌ Not peak morning rush conditions")
    print()
    
    # OR operator - any condition can be true
    print("🔗 Using OR operator:")
    if weather == "rain" or weather == "snow" or weather == "fog":
        print("   ⚠️ Adverse weather conditions detected")
        print("   Action: Reduce speed limits and increase messaging")
    else:
        print("   ☀️ Clear weather conditions")
    print()
    
    # NOT operator - inverting conditions
    print("🔗 Using NOT operator:")
    if not accident_reported:
        print("   ✅ No accidents reported - normal operations")
    else:
        print("   🚨 Accident reported - emergency protocols active")
    print()
    
    # Complex combined conditions
    print("🔗 Combining multiple logical operators:")
    
    # Rush hour AND (bad weather OR high volume) AND no accidents
    rush_hour = (time_hour >= 7 and time_hour <= 9) or (time_hour >= 17 and time_hour <= 19)
    problematic_conditions = weather in ["rain", "snow", "fog"] or volume > 1500
    safe_operations = not accident_reported
    
    if rush_hour and problematic_conditions and safe_operations:
        print("   🚨 COMPLEX ALERT: Rush hour with challenging conditions")
        print("   Action: Full traffic management deployment")
        priority_level = "HIGH"
    elif rush_hour and safe_operations:
        print("   📊 Standard rush hour management")
        priority_level = "MEDIUM"
    elif problematic_conditions and safe_operations:
        print("   ⚠️ Weather-related traffic management")
        priority_level = "MEDIUM"
    elif not safe_operations:
        print("   🚨 EMERGENCY: Accident management protocols")
        priority_level = "CRITICAL"
    else:
        print("   ✅ Normal traffic operations")
        priority_level = "LOW"
    
    print(f"   Priority Level: {priority_level}")
    print("✓ Logical operators demonstration completed")


def demonstrate_decision_outcomes():
    """5. Demonstrating Decision Outcomes"""
    print("=" * 60)
    print("📊 5. DECISION OUTCOME EXAMPLES")
    print("=" * 60)
    
    # Real-world traffic scenarios with clear decision paths
    scenarios = [
        {"name": "School Zone Morning", "volume": 600, "time": 8, "zone": "school", "weather": "clear"},
        {"name": "Highway Rush Hour", "volume": 1800, "time": 17, "zone": "highway", "weather": "rain"},
        {"name": "Downtown Midday", "volume": 900, "time": 13, "zone": "downtown", "weather": "clear"},
        {"name": "Residential Evening", "volume": 300, "time": 20, "zone": "residential", "weather": "fog"},
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"{i}. {scenario['name']}:")
        print(f"   Volume: {scenario['volume']}, Time: {scenario['time']}:00")
        print(f"   Zone: {scenario['zone']}, Weather: {scenario['weather']}")
        
        # Complex decision logic combining multiple factors
        volume = scenario['volume']
        time = scenario['time']
        zone = scenario['zone']
        weather = scenario['weather']
        
        # Determine base alert level
        if volume > 1500:
            alert_level = "HIGH"
        elif volume > 1000:
            alert_level = "MEDIUM"
        else:
            alert_level = "LOW"
        
        # Adjust for time-based factors
        rush_hour = (7 <= time <= 9) or (16 <= time <= 19)
        if rush_hour and volume > 500:
            alert_level = "HIGH" if alert_level != "HIGH" else "CRITICAL"
        
        # Adjust for zone-specific factors
        if zone == "school" and 7 <= time <= 9:
            if volume > 400:
                alert_level = "HIGH"
            safety_message = "School zone active - reduce speed"
        elif zone == "highway":
            safety_message = "Monitor merge points closely"
        else:
            safety_message = "Standard traffic monitoring"
        
        # Adjust for weather
        if weather != "clear":
            if alert_level == "LOW":
                alert_level = "MEDIUM"
            elif alert_level == "MEDIUM":
                alert_level = "HIGH"
            safety_message += " + Weather advisory active"
        
        # Output decision results
        print(f"   🚨 Alert Level: {alert_level}")
        print(f"   📢 Message: {safety_message}")
        
        # Final recommendations based on all factors
        if alert_level == "CRITICAL":
            print("   🚑 Action: Emergency traffic control deployment")
        elif alert_level == "HIGH":
            print("   👮 Action: Additional traffic personnel required")
        elif alert_level == "MEDIUM":
            print("   📊 Action: Enhanced monitoring and messaging")
        else:
            print("   ✅ Action: Standard operations sufficient")
        
        print()
    
    print("✓ Decision outcomes demonstration completed")


def main():
    """Main function demonstrating all conditional statement concepts"""
    print("🚦" * 20)
    print("SIGNALSYNC CONDITIONAL STATEMENTS MILESTONE")
    print("Python Conditional Logic for Traffic Management")
    print("🚦" * 20)
    print()
    
    # Execute all demonstrations in sequence
    demonstrate_basic_if_statements()
    print("\n")
    
    demonstrate_if_else_branching()
    print("\n")
    
    demonstrate_elif_multiple_conditions() 
    print("\n")
    
    demonstrate_logical_operators()
    print("\n")
    
    demonstrate_decision_outcomes()
    print("\n")
    
    # Final summary
    print("=" * 60)
    print("✅ CONDITIONAL STATEMENTS MILESTONE COMPLETE")
    print("=" * 60)
    print()
    print("📚 Skills Demonstrated:")
    print("   ✓ Basic if statements for simple conditions")
    print("   ✓ If-else branching for binary decisions")
    print("   ✓ Elif chains for multiple condition handling")  
    print("   ✓ Logical operators (and, or, not)")
    print("   ✓ Complex decision trees with real-world scenarios")
    print()
    print("🎯 Key Learning Outcomes:")
    print("   • Conditional statements control program flow")
    print("   • Proper indentation is critical for logic")
    print("   • Logical operators enable complex decisions")
    print("   • Real-world scenarios require multiple conditions")
    print("   • Clear condition structure improves readability")
    print()
    print("🚀 Ready for advanced Python programming concepts!")
    print("🚦" * 20)


if __name__ == "__main__":
    main()