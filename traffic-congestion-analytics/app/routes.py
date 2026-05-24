"""
Flask routes for Traffic Congestion Analytics System
"""
from flask import render_template, jsonify, request
import logging
import os
from pathlib import Path
from functools import lru_cache

from config.settings import DATA_DIR, KAGGLE_DATASET, IMAGES_DIR, CONGESTION_THRESHOLD, RANDOM_STATE, N_CLUSTERS
from app.services.data_loader import DataLoader
from app.services.data_processor import DataProcessor
from app.services.analytics import TrafficAnalytics
from app.services.visualization import TrafficVisualizer
from app.services.model import TrafficModel

logger = logging.getLogger(__name__)

# Global cache for data and models
_cached_data = None
_cached_model = None
_cached_analytics = None


def load_and_process_data():
    """Load and process data with caching"""
    global _cached_data, _cached_analytics, _cached_model

    if _cached_data is not None:
        logger.info("Using cached data")
        return _cached_data, _cached_analytics, _cached_model

    try:
        # Load data
        logger.info("Loading traffic data...")
        loader = DataLoader(KAGGLE_DATASET, DATA_DIR)
        df = loader.load_data()

        # Process data
        logger.info("Processing data...")
        processor = DataProcessor(congestion_threshold=CONGESTION_THRESHOLD)
        df_clean = processor.clean_data(df)
        df_processed = processor.engineer_features(df_clean)
        df_encoded = processor.encode_categorical(df_processed)

        # Analytics
        logger.info("Performing analytics...")
        analytics = TrafficAnalytics(df_processed)

        # Visualizations
        logger.info("Generating visualizations...")
        visualizer = TrafficVisualizer(df_processed, IMAGES_DIR)
        correlation_matrix = analytics.get_correlation_data()

        # Model training
        logger.info("Training models...")
        model = TrafficModel(random_state=RANDOM_STATE, n_clusters=N_CLUSTERS)
        X, y = processor.prepare_model_data(df_encoded)

        # Train regression
        regression_results = model.train_regression(X, y)
        logger.info(
            f"Regression model trained: MAE={regression_results['test_mae']}")

        # Train clustering
        clustering_features = df_processed[[
            'hour', 'traffic_volume', 'temp', 'weekday']].fillna(0)
        clustering_results = model.train_clustering(clustering_features)

        # Generate all visualizations
        visualizer.generate_all_visualizations(
            correlation_matrix=correlation_matrix,
            cluster_labels=clustering_results['cluster_labels']
        )

        # Cache results
        _cached_data = df_processed
        _cached_analytics = analytics
        _cached_model = model

        logger.info("Data loaded and processed successfully")
        return df_processed, analytics, model

    except Exception as e:
        logger.error(f"Error in load_and_process_data: {e}")
        raise


def register_routes(app):
    """
    Register Flask routes

    Args:
        app (Flask): Flask application
    """

    @app.route('/')
    def index():
        """Dashboard homepage"""
        try:
            data, analytics, model = load_and_process_data()

            # Get summary statistics
            summary = analytics.get_summary_stats()

            # Get bottlenecks
            bottlenecks = analytics.identify_bottlenecks()

            # Get congestion analysis
            congestion = analytics.congestion_analysis()

            # Check which images exist
            images = {}
            image_files = ['hourly_trend.png', 'weekly_trend.png', 'monthly_trend.png',
                           'weather_impact.png', 'correlation_heatmap.png',
                           'congestion_distribution.png', 'clustering.png']

            for img_file in image_files:
                img_path = IMAGES_DIR / img_file
                if img_path.exists():
                    images[img_file.replace('.png', '')
                           ] = f'/static/images/{img_file}'

            return render_template('dashboard.html',
                                   summary=summary,
                                   bottlenecks=bottlenecks,
                                   congestion=congestion,
                                   images=images)

        except Exception as e:
            logger.error(f"Error in index route: {e}")
            return f"Error loading dashboard: {str(e)}", 500

    @app.route('/about')
    def about():
        """About page"""
        return render_template('about.html')

    @app.route('/analytics')
    def analytics():
        """Analytics page"""
        try:
            data, analytics_obj, model = load_and_process_data()

            # Check which images exist
            images = {}
            image_files = ['hourly_trend.png', 'weekly_trend.png', 'monthly_trend.png',
                           'weather_impact.png', 'correlation_heatmap.png',
                           'congestion_distribution.png', 'clustering.png']

            for img_file in image_files:
                img_path = IMAGES_DIR / img_file
                if img_path.exists():
                    images[img_file.replace('.png', '')
                           ] = f'/static/images/{img_file}'

            return render_template('analytics.html', images=images)

        except Exception as e:
            logger.error(f"Error in analytics route: {e}")
            return f"Error loading analytics: {str(e)}", 500

    @app.route('/documentation')
    def documentation():
        """Documentation page"""
        return render_template('documentation.html')

    @app.route('/api/summary')
    def api_summary():
        """API endpoint for summary statistics"""
        try:
            data, analytics, model = load_and_process_data()
            summary = analytics.get_summary_stats()
            congestion = analytics.congestion_analysis()

            response = {
                'status': 'success',
                'data': {
                    'summary': summary,
                    'congestion': congestion
                }
            }

            return jsonify(response)

        except Exception as e:
            logger.error(f"Error in api_summary: {e}")
            return jsonify({'status': 'error', 'message': str(e)}), 500

    @app.route('/api/predict')
    def api_predict():
        """API endpoint for traffic prediction"""
        try:
            # Get query parameters
            hour = request.args.get('hour', type=int)
            weather = request.args.get('weather', 'Clear')
            temp = request.args.get('temp', 280, type=float)
            weekday = request.args.get('weekday', 0, type=int)
            month = request.args.get('month', 1, type=int)

            if hour is None:
                return jsonify({
                    'status': 'error',
                    'message': 'Missing required parameter: hour'
                }), 400

            if not (0 <= hour <= 23):
                return jsonify({
                    'status': 'error',
                    'message': 'Hour must be between 0 and 23'
                }), 400

            data, analytics, model = load_and_process_data()

            # Prepare features
            features = {
                'hour': hour,
                'month': month,
                'weekday': weekday,
                'weekend_flag': 1 if weekday >= 5 else 0,
                'temp': temp,
                'rain_1h': 0,
                'snow_1h': 0,
                'clouds_all': 50,
                f'weather_{weather}': 1
            }

            # Make prediction
            prediction = model.predict_traffic(features)
            is_congested = prediction > CONGESTION_THRESHOLD

            response = {
                'status': 'success',
                'data': {
                    'predicted_volume': round(prediction, 2),
                    'is_congested': bool(is_congested),
                    'congestion_threshold': CONGESTION_THRESHOLD,
                    'input_features': {
                        'hour': hour,
                        'weather': weather,
                        'temp': temp,
                        'weekday': weekday,
                        'month': month
                    }
                }
            }

            return jsonify(response)

        except Exception as e:
            logger.error(f"Error in api_predict: {e}")
            return jsonify({'status': 'error', 'message': str(e)}), 500

    @app.route('/api/analytics/<analysis_type>')
    def api_analytics(analysis_type):
        """API endpoint for specific analytics"""
        try:
            data, analytics, model = load_and_process_data()

            if analysis_type == 'peak_hours':
                peak_hours = analytics.find_peak_hours()
                result = peak_hours.to_dict()

            elif analysis_type == 'weather_impact':
                weather_stats = analytics.weather_impact()
                result = weather_stats.to_dict() if not weather_stats.empty else {}

            elif analysis_type == 'monthly_trends':
                monthly = analytics.monthly_trends()
                result = monthly.to_dict()

            elif analysis_type == 'bottlenecks':
                result = analytics.identify_bottlenecks()

            else:
                return jsonify({
                    'status': 'error',
                    'message': 'Invalid analysis type'
                }), 400

            response = {
                'status': 'success',
                'analysis_type': analysis_type,
                'data': result
            }

            return jsonify(response)

        except Exception as e:
            logger.error(f"Error in api_analytics: {e}")
            return jsonify({'status': 'error', 'message': str(e)}), 500

    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return jsonify({'status': 'error', 'message': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors"""
        logger.error(f"Internal server error: {error}")
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500
