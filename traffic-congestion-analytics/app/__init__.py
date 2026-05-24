"""
Flask application initialization
"""
from config.settings import SECRET_KEY, DEBUG, STATIC_DIR, IMAGES_DIR, LOG_LEVEL, LOG_FORMAT
from flask import Flask
import logging
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def create_app():
    """
    Create and configure Flask application

    Returns:
        Flask: Configured Flask app
    """
    app = Flask(__name__,
                static_folder=str(STATIC_DIR),
                template_folder=str(Path(__file__).parent / 'templates'))

    # Configuration
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['DEBUG'] = DEBUG

    # Ensure directories exist
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Setup logging
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL),
        format=LOG_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('traffic_analytics.log')
        ]
    )

    logger = logging.getLogger(__name__)
    logger.info("Flask application initialized")

    # Register routes
    from app.routes import register_routes
    register_routes(app)

    return app
