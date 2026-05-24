"""
Data loading module for Traffic Congestion Analytics
"""
import os
import pandas as pd
import kagglehub
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class DataLoader:
    """Handle dataset downloading and loading"""

    def __init__(self, dataset_name, data_dir):
        """
        Initialize DataLoader

        Args:
            dataset_name (str): Kaggle dataset name
            data_dir (Path): Directory to store data
        """
        self.dataset_name = dataset_name
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def download_dataset(self):
        """
        Download dataset from Kaggle using kagglehub

        Returns:
            str: Path to downloaded dataset
        """
        try:
            logger.info(f"Downloading dataset: {self.dataset_name}")

            # Try different kagglehub API methods based on version
            path = None
            if hasattr(kagglehub, 'dataset_download'):
                path = kagglehub.dataset_download(self.dataset_name)
            elif hasattr(kagglehub, 'download'):
                path = kagglehub.download(self.dataset_name)
            else:
                raise AttributeError(
                    "kagglehub API method not found. Please update kagglehub: pip install --upgrade kagglehub")

            logger.info(f"Path to dataset files: {path}")
            return path
        except Exception as e:
            logger.error(f"Error downloading dataset: {e}")
            raise

    def load_data(self, force_download=False):
        """
        Load traffic data from dataset

        Args:
            force_download (bool): Force re-download of dataset

        Returns:
            pd.DataFrame: Traffic data
        """
        try:
            # Check if data already exists locally
            local_csv_path = self.data_dir / "Metro_Interstate_Traffic_Volume.csv"

            if not local_csv_path.exists() or force_download:
                try:
                    # Download dataset
                    dataset_path = self.download_dataset()

                    # Find CSV file in downloaded path
                    csv_files = list(Path(dataset_path).glob("*.csv"))
                    if not csv_files:
                        raise FileNotFoundError(
                            "No CSV file found in downloaded dataset")

                    source_csv = csv_files[0]

                    # Copy to local data directory
                    import shutil
                    shutil.copy(source_csv, local_csv_path)
                    logger.info(f"Dataset copied to: {local_csv_path}")

                except Exception as download_error:
                    logger.warning(
                        f"Could not download dataset: {download_error}")
                    logger.info("Please manually download the dataset:")
                    logger.info(
                        "1. Go to: https://www.kaggle.com/datasets/galenchen/highway-traffic-volume")
                    logger.info(
                        "2. Download 'Metro_Interstate_Traffic_Volume.csv'")
                    logger.info(f"3. Place it in: {local_csv_path}")

                    if not local_csv_path.exists():
                        raise FileNotFoundError(
                            f"Dataset not found. Please download manually from:\n"
                            f"https://www.kaggle.com/datasets/galenchen/highway-traffic-volume\n"
                            f"and place 'Metro_Interstate_Traffic_Volume.csv' in:\n"
                            f"{local_csv_path}"
                        )

            # Load data
            logger.info(f"Loading data from: {local_csv_path}")
            df = pd.read_csv(local_csv_path)
            logger.info(f"Data loaded successfully. Shape: {df.shape}")

            return df

        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise

    def get_data_info(self, df):
        """
        Get basic information about the dataset

        Args:
            df (pd.DataFrame): Traffic data

        Returns:
            dict: Dataset information
        """
        return {
            'shape': df.shape,
            'columns': df.columns.tolist(),
            'dtypes': df.dtypes.to_dict(),
            'null_counts': df.isnull().sum().to_dict(),
            'memory_usage': df.memory_usage(deep=True).sum() / 1024**2  # MB
        }
