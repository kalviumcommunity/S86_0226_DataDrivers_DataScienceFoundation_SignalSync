"""
Traffic Congestion Analytics System - Main Entry Point
"""
import logging
from config.settings import HOST, PORT, DEBUG
from app import create_app
import sys
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent))


logger = logging.getLogger(__name__)


def main():
    """
    Main function to run the Flask application
    """
    try:
        # Create Flask app
        app = create_app()

        logger.info("="*60)
        logger.info("Traffic Congestion Analytics System")
        logger.info("="*60)
        logger.info(f"Starting server on http://{HOST}:{PORT}")
        logger.info(f"Debug mode: {DEBUG}")
        logger.info("Press CTRL+C to quit")
        logger.info("="*60)

        # Run the application
        app.run(host=HOST, port=PORT, debug=DEBUG)

    except Exception as e:
        logger.error(f"Error starting application: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
