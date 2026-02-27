#!/usr/bin/env python3
"""
SignalSync Traffic Analysis Script
A simple Python script demonstrating basic traffic data analysis
"""

def main():
    print("=" * 50)
    print("🚦 SignalSync Traffic Analysis Script")
    print("=" * 50)
    
    # Sample traffic data for demonstration
    print("\n📊 Processing sample traffic data...")
    
    # Traffic volume data for different hours (vehicles per hour)
    traffic_data = {
        "6_AM": 420,
        "7_AM": 850,
        "8_AM": 1200,
        "9_AM": 680,
        "12_PM": 950,
        "5_PM": 1350,
        "6_PM": 1180,
        "7_PM": 890
    }
    
    print(f"Sample data points: {len(traffic_data)} hours")
    
    # Calculate basic statistics
    volumes = list(traffic_data.values())
    total_vehicles = sum(volumes)
    average_volume = total_vehicles / len(volumes)
    max_volume = max(volumes)
    min_volume = min(volumes)
    
    print("\n📈 Traffic Analysis Results:")
    print(f"Total vehicles observed: {total_vehicles:,}")
    print(f"Average hourly volume: {average_volume:.1f}")
    print(f"Peak traffic volume: {max_volume:,}")
    print(f"Minimum traffic volume: {min_volume:,}")
    
    # Identify rush hours (traffic > 1000 vehicles/hour)
    rush_hour_threshold = 1000
    rush_hours = []
    
    for hour, volume in traffic_data.items():
        if volume > rush_hour_threshold:
            rush_hours.append(hour)
    
    print(f"\n🚨 Rush Hours Identified (>{rush_hour_threshold:,} vehicles/hour):")
    for hour in rush_hours:
        volume = traffic_data[hour]
        print(f"  - {hour.replace('_', ' ')}: {volume:,} vehicles")
    
    # Calculate congestion percentage
    congested_hours = len(rush_hours)
    total_hours = len(traffic_data)
    congestion_percentage = (congested_hours / total_hours) * 100
    
    print(f"\n📊 Congestion Summary:")
    print(f"Congested periods: {congested_hours}/{total_hours} hours")
    print(f"Congestion rate: {congestion_percentage:.1f}%")
    
    # Traffic optimization recommendations
    print(f"\n💡 Recommendations:")
    if congestion_percentage > 30:
        print("  - High congestion detected - consider signal optimization")
        print("  - Deploy traffic personnel during peak hours")
    elif congestion_percentage > 15:
        print("  - Moderate congestion - monitor closely")
    else:
        print("  - Traffic flow appears normal")
    
    print("\n" + "=" * 50)
    print("✅ Analysis complete! Script executed successfully.")
    print("=" * 50)

if __name__ == "__main__":
    main()