"""
Configuration settings for Traffic Congestion Analytics System
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data settings
DATA_DIR = BASE_DIR / 'data'
KAGGLE_DATASET = "galenchen/highway-traffic-volume"
DATASET_FILENAME = "Metro_Interstate_Traffic_Volume.csv"

# Static files
STATIC_DIR = BASE_DIR / 'app' / 'static'
IMAGES_DIR = STATIC_DIR / 'images'

# Model settings
CONGESTION_THRESHOLD = 4500  # Traffic volume threshold for congestion
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_CLUSTERS = 4

# Flask settings
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'dev-secret-key-change-in-production')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', 5000))

# Caching
CACHE_TIMEOUT = 300  # 5 minutes

# Logging
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
