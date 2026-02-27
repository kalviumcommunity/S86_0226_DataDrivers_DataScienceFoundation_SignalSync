"""
Simple Traffic Data Calculator
Demonstrates script vs notebook execution concepts
"""

# Sample data - no persistent state between runs
daily_traffic_count = 0
peak_hours = []

print("🚛 Daily Traffic Counter Script")
print("-" * 30)

# Simulate processing traffic data
traffic_observations = [250, 480, 890, 1200, 950, 1350, 980, 640, 320]

for hour, vehicles in enumerate(traffic_observations, 1):
    daily_traffic_count += vehicles
    if vehicles > 1000:
        peak_hours.append(f"Hour {hour}")
    print(f"Hour {hour:2d}: {vehicles:4d} vehicles")

print(f"\nTotal daily traffic: {daily_traffic_count:,} vehicles")
print(f"Peak hours detected: {len(peak_hours)}")
print(f"Peak hours: {', '.join(peak_hours) if peak_hours else 'None'}")

# This variable resets every script run (unlike notebooks)
print(f"\nScript completed. Variables reset on next execution.")