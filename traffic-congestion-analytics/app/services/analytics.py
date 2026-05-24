"""
Analytics and insights module
"""
import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)


class TrafficAnalytics:
    """Perform traffic analytics and generate insights"""

    def __init__(self, data):
        """
        Initialize TrafficAnalytics

        Args:
            data (pd.DataFrame): Processed traffic data
        """
        self.data = data

    def find_peak_hours(self):
        """
        Identify peak traffic hours

        Returns:
            pd.Series: Average traffic by hour
        """
        peak_hours = self.data.groupby(
            'hour')['traffic_volume'].mean().sort_values(ascending=False)
        logger.info(
            f"Peak hour: {peak_hours.idxmax()} with avg volume {peak_hours.max():.0f}")
        return peak_hours

    def find_busiest_day(self):
        """
        Identify busiest day of the week

        Returns:
            tuple: (day_name, average_volume)
        """
        daily_traffic = self.data.groupby('weekday_name')[
            'traffic_volume'].mean().sort_values(ascending=False)
        busiest_day = daily_traffic.idxmax()
        avg_volume = daily_traffic.max()

        logger.info(
            f"Busiest day: {busiest_day} with avg volume {avg_volume:.0f}")
        return busiest_day, avg_volume

    def monthly_trends(self):
        """
        Analyze monthly traffic trends

        Returns:
            pd.Series: Average traffic by month
        """
        month_names = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April',
            5: 'May', 6: 'June', 7: 'July', 8: 'August',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'
        }

        monthly = self.data.groupby('month')['traffic_volume'].mean()
        monthly.index = monthly.index.map(month_names)

        return monthly

    def weather_impact(self):
        """
        Analyze weather impact on traffic

        Returns:
            pd.DataFrame: Traffic statistics by weather condition
        """
        if 'weather_main' not in self.data.columns:
            logger.warning("weather_main column not found")
            return pd.DataFrame()

        weather_stats = self.data.groupby('weather_main').agg({
            'traffic_volume': ['mean', 'median', 'std', 'count']
        }).round(2)

        weather_stats.columns = ['_'.join(col).strip()
                                 for col in weather_stats.columns.values]
        weather_stats = weather_stats.sort_values(
            'traffic_volume_mean', ascending=False)

        return weather_stats

    def weekend_vs_weekday(self):
        """
        Compare weekend vs weekday traffic

        Returns:
            pd.Series: Average traffic for weekend vs weekday
        """
        comparison = self.data.groupby('weekend_flag')['traffic_volume'].mean()
        comparison.index = ['Weekday', 'Weekend']

        return comparison

    def congestion_analysis(self):
        """
        Analyze congestion patterns

        Returns:
            dict: Congestion insights
        """
        if 'is_congested' not in self.data.columns:
            logger.warning("is_congested column not found")
            return {}

        total_records = len(self.data)
        congested_records = self.data['is_congested'].sum()
        congestion_rate = (congested_records / total_records) * 100

        # Congestion by hour
        hourly_congestion = self.data.groupby(
            'hour')['is_congested'].mean() * 100
        peak_congestion_hour = hourly_congestion.idxmax()

        # Congestion by day
        daily_congestion = self.data.groupby(
            'weekday_name')['is_congested'].mean() * 100
        peak_congestion_day = daily_congestion.idxmax()

        insights = {
            'total_records': total_records,
            'congested_records': int(congested_records),
            'congestion_rate': round(congestion_rate, 2),
            'peak_congestion_hour': int(peak_congestion_hour),
            'peak_congestion_day': peak_congestion_day,
            'hourly_congestion': hourly_congestion.to_dict(),
            'daily_congestion': daily_congestion.to_dict()
        }

        return insights

    def identify_bottlenecks(self):
        """
        Identify traffic bottlenecks

        Returns:
            list: List of bottleneck insights
        """
        bottlenecks = []

        # High congestion hours
        hourly_congestion = self.data.groupby(
            'hour')['is_congested'].mean() * 100
        high_congestion_hours = hourly_congestion[hourly_congestion > 50].sort_values(
            ascending=False)

        if len(high_congestion_hours) > 0:
            for hour, rate in high_congestion_hours.head(3).items():
                bottlenecks.append({
                    'type': 'Peak Hour Congestion',
                    'description': f'Hour {hour}:00 experiences {rate:.1f}% congestion rate',
                    'severity': 'High' if rate > 70 else 'Medium'
                })

        # High traffic days
        daily_avg = self.data.groupby('weekday_name')['traffic_volume'].mean()
        busiest_days = daily_avg.nlargest(2)

        for day, volume in busiest_days.items():
            bottlenecks.append({
                'type': 'High Volume Day',
                'description': f'{day} has average volume of {volume:.0f} vehicles',
                'severity': 'Medium'
            })

        # Weather-related bottlenecks
        if 'weather_main' in self.data.columns:
            weather_impact = self.data.groupby('weather_main')[
                'traffic_volume'].mean().sort_values(ascending=False)
            if len(weather_impact) > 0:
                top_weather = weather_impact.idxmax()
                top_volume = weather_impact.max()
                bottlenecks.append({
                    'type': 'Weather Impact',
                    'description': f'{top_weather} conditions show highest traffic: {top_volume:.0f} avg vehicles',
                    'severity': 'Low'
                })

        return bottlenecks

    def get_correlation_data(self):
        """
        Get correlation matrix for numeric features

        Returns:
            pd.DataFrame: Correlation matrix
        """
        numeric_cols = ['traffic_volume', 'temp', 'rain_1h', 'snow_1h', 'clouds_all',
                        'hour', 'weekday', 'month', 'weekend_flag']

        # Filter to existing columns
        existing_cols = [
            col for col in numeric_cols if col in self.data.columns]

        correlation_matrix = self.data[existing_cols].corr()

        return correlation_matrix

    def get_summary_stats(self):
        """
        Get comprehensive summary statistics

        Returns:
            dict: Summary statistics
        """
        peak_hours = self.find_peak_hours()
        busiest_day, busiest_volume = self.find_busiest_day()
        congestion = self.congestion_analysis()

        summary = {
            'total_records': len(self.data),
            'avg_traffic_volume': round(self.data['traffic_volume'].mean(), 2),
            'peak_hour': int(peak_hours.idxmax()),
            'peak_hour_volume': round(peak_hours.max(), 2),
            'busiest_day': busiest_day,
            'busiest_day_volume': round(busiest_volume, 2),
            'congestion_rate': congestion.get('congestion_rate', 0),
            'date_range': {
                'start': str(self.data['date_time'].min()),
                'end': str(self.data['date_time'].max())
            }
        }

        return summary
