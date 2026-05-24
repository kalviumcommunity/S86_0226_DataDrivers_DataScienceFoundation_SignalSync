"""
Machine learning model module
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import logging
import pickle
from pathlib import Path

logger = logging.getLogger(__name__)


class TrafficModel:
    """Machine learning models for traffic prediction and clustering"""

    def __init__(self, random_state=42, test_size=0.2, n_clusters=4):
        """
        Initialize TrafficModel

        Args:
            random_state (int): Random seed
            test_size (float): Test set proportion
            n_clusters (int): Number of clusters for KMeans
        """
        self.random_state = random_state
        self.test_size = test_size
        self.n_clusters = n_clusters
        self.regression_model = None
        self.clustering_model = None
        self.feature_names = None

    def train_regression(self, X, y):
        """
        Train linear regression model to predict traffic volume

        Args:
            X (pd.DataFrame): Features
            y (pd.Series): Target (traffic_volume)

        Returns:
            dict: Training results and metrics
        """
        logger.info("Training linear regression model...")

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state
        )

        # Store feature names
        self.feature_names = X.columns.tolist()

        # Train model
        self.regression_model = LinearRegression()
        self.regression_model.fit(X_train, y_train)

        # Predictions
        y_train_pred = self.regression_model.predict(X_train)
        y_test_pred = self.regression_model.predict(X_test)

        # Evaluate
        train_mae = mean_absolute_error(y_train, y_train_pred)
        test_mae = mean_absolute_error(y_test, y_test_pred)
        train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
        test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

        results = {
            'train_samples': len(X_train),
            'test_samples': len(X_test),
            'train_mae': round(train_mae, 2),
            'test_mae': round(test_mae, 2),
            'train_rmse': round(train_rmse, 2),
            'test_rmse': round(test_rmse, 2),
            'r2_score': round(self.regression_model.score(X_test, y_test), 4),
            'feature_importance': dict(zip(
                self.feature_names,
                [round(coef, 4) for coef in self.regression_model.coef_]
            ))
        }

        logger.info(
            f"Model trained: MAE={test_mae:.2f}, RMSE={test_rmse:.2f}, R²={results['r2_score']}")

        return results

    def train_clustering(self, X):
        """
        Train KMeans clustering model

        Args:
            X (pd.DataFrame): Features for clustering

        Returns:
            dict: Clustering results
        """
        logger.info(
            f"Training KMeans clustering with {self.n_clusters} clusters...")

        self.clustering_model = KMeans(
            n_clusters=self.n_clusters,
            random_state=self.random_state,
            n_init=10
        )

        cluster_labels = self.clustering_model.fit_predict(X)

        results = {
            'n_clusters': self.n_clusters,
            'inertia': round(self.clustering_model.inertia_, 2),
            'cluster_labels': cluster_labels,
            'cluster_centers': self.clustering_model.cluster_centers_,
            'cluster_counts': {
                f'Cluster_{i}': int(np.sum(cluster_labels == i))
                for i in range(self.n_clusters)
            }
        }

        logger.info(f"Clustering complete: Inertia={results['inertia']}")

        return results

    def predict_traffic(self, features):
        """
        Predict traffic volume for given features

        Args:
            features (dict): Feature values

        Returns:
            float: Predicted traffic volume
        """
        if self.regression_model is None:
            raise ValueError("Model not trained. Call train_regression first.")

        # Create feature array in correct order
        feature_array = []
        for feature_name in self.feature_names:
            if feature_name in features:
                feature_array.append(features[feature_name])
            else:
                feature_array.append(0)  # Default value

        feature_array = np.array([feature_array])
        prediction = self.regression_model.predict(feature_array)[0]

        return max(0, prediction)  # Ensure non-negative prediction

    def save_model(self, model_path, model_type='regression'):
        """
        Save trained model to disk

        Args:
            model_path (str): Path to save model
            model_type (str): 'regression' or 'clustering'
        """
        model_path = Path(model_path)
        model_path.parent.mkdir(parents=True, exist_ok=True)

        if model_type == 'regression' and self.regression_model is not None:
            with open(model_path, 'wb') as f:
                pickle.dump({
                    'model': self.regression_model,
                    'feature_names': self.feature_names
                }, f)
            logger.info(f"Regression model saved to {model_path}")

        elif model_type == 'clustering' and self.clustering_model is not None:
            with open(model_path, 'wb') as f:
                pickle.dump(self.clustering_model, f)
            logger.info(f"Clustering model saved to {model_path}")

    def load_model(self, model_path, model_type='regression'):
        """
        Load trained model from disk

        Args:
            model_path (str): Path to model file
            model_type (str): 'regression' or 'clustering'
        """
        model_path = Path(model_path)

        if not model_path.exists():
            raise FileNotFoundError(f"Model file not found: {model_path}")

        with open(model_path, 'rb') as f:
            if model_type == 'regression':
                data = pickle.load(f)
                self.regression_model = data['model']
                self.feature_names = data['feature_names']
                logger.info(f"Regression model loaded from {model_path}")
            elif model_type == 'clustering':
                self.clustering_model = pickle.load(f)
                logger.info(f"Clustering model loaded from {model_path}")
