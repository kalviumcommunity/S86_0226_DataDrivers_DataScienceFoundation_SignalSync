"""
Dataset Download Helper Script
Run this if automatic download fails
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path
import sys

print("="*70)
print("Traffic Congestion Analytics - Dataset Download Helper")
print("="*70)

# Check if data directory exists
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

csv_path = data_dir / "Metro_Interstate_Traffic_Volume.csv"

if csv_path.exists():
    print(f"\n✅ Dataset already exists at: {csv_path}")
    print(f"   File size: {csv_path.stat().st_size / (1024*1024):.2f} MB")

    response = input("\nDo you want to regenerate sample data? (y/n): ")
    if response.lower() != 'y':
        print("\nExiting. Dataset is ready to use!")
        sys.exit(0)

print("\n📊 Generating sample traffic dataset...")
print("   (This is synthetic data for testing purposes)")

# Create realistic sample data
np.random.seed(42)
n_samples = 48000  # Similar to real dataset size

# Generate timestamps (1 year of hourly data)
start_date = datetime(2020, 1, 1)
dates = [start_date + timedelta(hours=i) for i in range(n_samples)]

# Generate realistic traffic patterns
hours = np.array([d.hour for d in dates])
weekdays = np.array([d.weekday() for d in dates])
months = np.array([d.month for d in dates])

# Base traffic with patterns
base_traffic = 3000

# Rush hour effect (morning 7-9, evening 17-19)
rush_hour_boost = np.where(
    ((hours >= 7) & (hours <= 9)) | ((hours >= 17) & (hours <= 19)),
    1500,
    0
)

# Weekday vs weekend
weekday_factor = np.where(weekdays < 5, 1.2, 0.8)

# Night reduction
night_penalty = np.where((hours >= 0) & (hours <= 5), -1000, 0)

# Random variation
random_variation = np.random.normal(0, 500, n_samples)

# Calculate traffic volume
traffic_volume = (base_traffic + rush_hour_boost +
                  night_penalty) * weekday_factor + random_variation
traffic_volume = np.clip(traffic_volume, 0, 7500).astype(int)

# Generate weather data
weather_types = ['Clear', 'Clouds', 'Rain', 'Snow', 'Mist', 'Drizzle', 'Fog']
weather_weights = [0.4, 0.25, 0.15, 0.08, 0.05, 0.04, 0.03]
weather_main = np.random.choice(weather_types, n_samples, p=weather_weights)

# Temperature (Kelvin) - seasonal variation
seasonal_temp = 280 + 15 * np.sin((months - 1) * np.pi / 6)
temp = seasonal_temp + np.random.normal(0, 5, n_samples)

# Rain and snow based on weather
rain_1h = np.where(
    (weather_main == 'Rain') | (weather_main == 'Drizzle'),
    np.random.exponential(1.5, n_samples),
    0
)

snow_1h = np.where(
    weather_main == 'Snow',
    np.random.exponential(0.8, n_samples),
    0
)

# Cloud coverage
clouds_all = np.random.randint(0, 100, n_samples)

# Weather descriptions
weather_desc_map = {
    'Clear': ['clear sky', 'few clouds'],
    'Clouds': ['scattered clouds', 'broken clouds', 'overcast clouds'],
    'Rain': ['light rain', 'moderate rain', 'heavy rain'],
    'Snow': ['light snow', 'snow'],
    'Mist': ['mist'],
    'Drizzle': ['light drizzle', 'drizzle'],
    'Fog': ['fog']
}

weather_description = [
    np.random.choice(weather_desc_map[w]) for w in weather_main
]

# Create DataFrame
df = pd.DataFrame({
    'date_time': dates,
    'traffic_volume': traffic_volume,
    'temp': temp,
    'rain_1h': rain_1h,
    'snow_1h': snow_1h,
    'clouds_all': clouds_all,
    'weather_main': weather_main,
    'weather_description': weather_description
})

# Save to CSV
print(f"\n💾 Saving dataset to: {csv_path}")
df.to_csv(csv_path, index=False)

print("\n✅ Dataset created successfully!")
print(f"\n📊 Dataset Statistics:")
print(f"   Total records: {len(df):,}")
print(f"   Date range: {df['date_time'].min()} to {df['date_time'].max()}")
print(
    f"   Traffic volume range: {df['traffic_volume'].min()} - {df['traffic_volume'].max()}")
print(f"   Average traffic: {df['traffic_volume'].mean():.0f}")
print(f"   File size: {csv_path.stat().st_size / (1024*1024):.2f} MB")

print("\n" + "="*70)
print("✨ You can now run the application:")
print("   python run.py")
print("="*70)
