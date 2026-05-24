"""
Data processing and feature engineering module
"""
import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)


class DataProcessor:
    """Process and engineer features from traffic data"""

    def __init__(self, congestion_threshold=4500):
        """
        Initialize DataProcessor

        Args:
            congestion_threshold (int): Traffic volume threshold for congestion
        """
        self.congestion_threshold = congestion_threshold

    def clean_data(self, df):
        """
        Clean the dataset

        Args:
            df (pd.DataFrame): Raw traffic data

        Returns:
            pd.DataFrame: Cleaned data
        """
        logger.info("Cleaning data...")
        df_clean = df.copy()

        # Drop null values
        initial_shape = df_clean.shape
        df_clean = df_clean.dropna()
        logger.info(
            f"Removed {initial_shape[0] - df_clean.shape[0]} rows with null values")

        # Remove duplicates
        df_clean = df_clean.drop_duplicates()

        # Convert date_time to datetime
        if 'date_time' in df_clean.columns:
            df_clean['date_time'] = pd.to_datetime(df_clean['date_time'])
            logger.info("Converted date_time to datetime format")

        return df_clean

    def engineer_features(self, df):
        """
        Create time-based features

        Args:
            df (pd.DataFrame): Cleaned traffic data

        Returns:
            pd.DataFrame: Data with engineered features
        """
        logger.info("Engineering features...")
        df_feat = df.copy()

        # Time-based features
        df_feat['hour'] = df_feat['date_time'].dt.hour
        df_feat['day'] = df_feat['date_time'].dt.day
        df_feat['month'] = df_feat['date_time'].dt.month
        df_feat['year'] = df_feat['date_time'].dt.year
        df_feat['weekday'] = df_feat['date_time'].dt.weekday
        df_feat['weekday_name'] = df_feat['date_time'].dt.day_name()

        # Weekend flag (0 = Weekday, 1 = Weekend)
        df_feat['weekend_flag'] = (df_feat['weekday'] >= 5).astype(int)

        # Congestion flag
        df_feat['is_congested'] = (
            df_feat['traffic_volume'] > self.congestion_threshold).astype(int)

        # Time of day category
        df_feat['time_of_day'] = pd.cut(
            df_feat['hour'],
            bins=[0, 6, 12, 18, 24],
            labels=['Night', 'Morning', 'Afternoon', 'Evening'],
            right=False
        )

        logger.info(
            f"Engineered {len(['hour', 'day', 'month', 'year', 'weekday', 'weekend_flag', 'is_congested', 'time_of_day'])} new features")

        return df_feat

    def encode_categorical(self, df):
        """
        Encode categorical variables

        Args:
            df (pd.DataFrame): Data with categorical variables

        Returns:
            pd.DataFrame: Data with encoded categoricals
        """
        df_encoded = df.copy()

        # One-hot encode weather_main
        if 'weather_main' in df_encoded.columns:
            weather_dummies = pd.get_dummies(
                df_encoded['weather_main'], prefix='weather')
            df_encoded = pd.concat([df_encoded, weather_dummies], axis=1)

        # One-hot encode weather_description
        if 'weather_description' in df_encoded.columns:
            desc_dummies = pd.get_dummies(
                df_encoded['weather_description'], prefix='weather_desc')
            df_encoded = pd.concat([df_encoded, desc_dummies], axis=1)

        return df_encoded

    def prepare_model_data(self, df):
        """
        Prepare data for machine learning

        Args:
            df (pd.DataFrame): Processed data

        Returns:
            tuple: (X, y) features and target
        """
        # Select numeric features for modeling
        feature_cols = ['hour', 'day', 'month', 'year', 'weekday', 'weekend_flag',
                        'temp', 'rain_1h', 'snow_1h', 'clouds_all']

        # Add weather dummies if they exist (exclude original categorical columns)
        weather_cols = [
            col for col in df.columns
            if col.startswith('weather_') and col not in ['weather_main', 'weather_description']
        ]
        feature_cols.extend(weather_cols)

        # Filter to existing columns
        feature_cols = [col for col in feature_cols if col in df.columns]

        X = df[feature_cols].copy()
        y = df['traffic_volume'].copy()

        # Ensure all columns are numeric
        X = X.select_dtypes(include=[np.number])

        # Fill any remaining NaN values
        X = X.fillna(0)

        logger.info(
            f"Prepared model data: {X.shape[0]} samples, {X.shape[1]} features")

        return X, y

    def get_statistical_summary(self, df):
        """
        Get statistical summary of processed data

        Args:
            df (pd.DataFrame): Processed data

        Returns:
            dict: Statistical summary
        """
        numeric_cols = df.select_dtypes(include=[np.number]).columns

        summary = {
            'total_records': len(df),
            'date_range': {
                'start': str(df['date_time'].min()),
                'end': str(df['date_time'].max())
            },
            'traffic_volume': {
                'mean': float(df['traffic_volume'].mean()),
                'median': float(df['traffic_volume'].median()),
                'std': float(df['traffic_volume'].std()),
                'min': int(df['traffic_volume'].min()),
                'max': int(df['traffic_volume'].max())
            },
            'congestion_rate': float((df['is_congested'].sum() / len(df)) * 100) if 'is_congested' in df.columns else 0
        }

        return summary
