"""
Visualization module for traffic analytics
"""
from pathlib import Path
import logging
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

logger = logging.getLogger(__name__)


class TrafficVisualizer:
    """Generate visualizations for traffic data"""

    def __init__(self, data, output_dir):
        """
        Initialize TrafficVisualizer

        Args:
            data (pd.DataFrame): Processed traffic data
            output_dir (Path): Directory to save visualizations
        """
        self.data = data
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Set style
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 6)
        plt.rcParams['font.size'] = 10

    def plot_hourly_trend(self):
        """Generate hourly traffic trend visualization"""
        try:
            plt.figure(figsize=(14, 6))
            hourly_avg = self.data.groupby('hour')['traffic_volume'].mean()

            plt.plot(hourly_avg.index, hourly_avg.values, marker='o',
                     linewidth=2, markersize=8, color='#FF6B00')
            plt.fill_between(hourly_avg.index, hourly_avg.values,
                             alpha=0.3, color='#FF6B00')

            plt.title('Average Traffic Volume by Hour',
                      fontsize=16, fontweight='bold', pad=20)
            plt.xlabel('Hour of Day', fontsize=12, fontweight='bold')
            plt.ylabel('Average Traffic Volume',
                       fontsize=12, fontweight='bold')
            plt.xticks(range(24))
            plt.grid(True, alpha=0.3)
            plt.tight_layout()

            output_path = self.output_dir / 'hourly_trend.png'
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()

            logger.info(f"Saved hourly trend chart to {output_path}")
            return str(output_path)

        except Exception as e:
            logger.error(f"Error generating hourly trend: {e}")
            plt.close()
            return None

    def plot_weekly_trend(self):
        """Generate weekly traffic trend visualization"""
        try:
            plt.figure(figsize=(12, 6))

            days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                          'Friday', 'Saturday', 'Sunday']
            daily_avg = self.data.groupby('weekday_name')[
                'traffic_volume'].mean()
            daily_avg = daily_avg.reindex(days_order)

            colors = ['#FF6B00' if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                      else '#2ECC71' for day in days_order]

            plt.bar(range(len(daily_avg)), daily_avg.values,
                    color=colors, edgecolor='black', linewidth=1.2)
            plt.title('Average Traffic Volume by Day of Week',
                      fontsize=16, fontweight='bold', pad=20)
            plt.xlabel('Day of Week', fontsize=12, fontweight='bold')
            plt.ylabel('Average Traffic Volume',
                       fontsize=12, fontweight='bold')
            plt.xticks(range(len(days_order)), days_order, rotation=45)
            plt.grid(True, alpha=0.3, axis='y')
            plt.tight_layout()

            output_path = self.output_dir / 'weekly_trend.png'
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()

            logger.info(f"Saved weekly trend chart to {output_path}")
            return str(output_path)

        except Exception as e:
            logger.error(f"Error generating weekly trend: {e}")
            plt.close()
            return None

    def plot_monthly_trend(self):
        """Generate monthly traffic trend visualization"""
        try:
            plt.figure(figsize=(14, 6))

            month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            monthly_avg = self.data.groupby('month')['traffic_volume'].mean()

            plt.plot(monthly_avg.index, monthly_avg.values, marker='s',
                     linewidth=2.5, markersize=10, color='#FF6B00')
            plt.fill_between(monthly_avg.index,
                             monthly_avg.values, alpha=0.2, color='#FF6B00')

            plt.title('Average Traffic Volume by Month',
                      fontsize=16, fontweight='bold', pad=20)
            plt.xlabel('Month', fontsize=12, fontweight='bold')
            plt.ylabel('Average Traffic Volume',
                       fontsize=12, fontweight='bold')
            plt.xticks(range(1, 13), month_names)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()

            output_path = self.output_dir / 'monthly_trend.png'
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()

            logger.info(f"Saved monthly trend chart to {output_path}")
            return str(output_path)

        except Exception as e:
            logger.error(f"Error generating monthly trend: {e}")
            plt.close()
            return None

    def plot_weather_impact(self):
        """Generate weather impact visualization"""
        try:
            if 'weather_main' not in self.data.columns:
                logger.warning("weather_main column not found")
                return None

            plt.figure(figsize=(12, 6))

            weather_avg = self.data.groupby('weather_main')[
                'traffic_volume'].mean().sort_values(ascending=False)

            colors = plt.cm.RdYlGn_r(np.linspace(0.3, 0.7, len(weather_avg)))

            plt.barh(range(len(weather_avg)), weather_avg.values,
                     color=colors, edgecolor='black', linewidth=1.2)
            plt.title('Traffic Volume by Weather Condition',
                      fontsize=16, fontweight='bold', pad=20)
            plt.xlabel('Average Traffic Volume',
                       fontsize=12, fontweight='bold')
            plt.ylabel('Weather Condition', fontsize=12, fontweight='bold')
            plt.yticks(range(len(weather_avg)), weather_avg.index)
            plt.grid(True, alpha=0.3, axis='x')
            plt.tight_layout()

            output_path = self.output_dir / 'weather_impact.png'
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()

            logger.info(f"Saved weather impact chart to {output_path}")
            return str(output_path)

        except Exception as e:
            logger.error(f"Error generating weather impact: {e}")
            plt.close()
            return None

    def plot_correlation_heatmap(self, correlation_matrix):
        """Generate correlation heatmap"""
        try:
            plt.figure(figsize=(12, 10))

            mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

            sns.heatmap(correlation_matrix, mask=mask, annot=True, fmt='.2f',
                        cmap='RdYlGn', center=0, square=True, linewidths=1,
                        cbar_kws={"shrink": 0.8})

            plt.title('Feature Correlation Heatmap',
                      fontsize=16, fontweight='bold', pad=20)
            plt.tight_layout()

            output_path = self.output_dir / 'correlation_heatmap.png'
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()

            logger.info(f"Saved correlation heatmap to {output_path}")
            return str(output_path)

        except Exception as e:
            logger.error(f"Error generating correlation heatmap: {e}")
            plt.close()
            return None

    def plot_congestion_distribution(self):
        """Generate congestion distribution visualization"""
        try:
            if 'is_congested' not in self.data.columns:
                logger.warning("is_congested column not found")
                return None

            plt.figure(figsize=(10, 6))

            congestion_counts = self.data['is_congested'].value_counts()
            labels = ['Normal Traffic', 'Congested']
            colors = ['#2ECC71', '#FF6B00']

            plt.pie(congestion_counts.values, labels=labels, autopct='%1.1f%%',
                    startangle=90, colors=colors, textprops={'fontsize': 12, 'fontweight': 'bold'},
                    explode=(0, 0.05))

            plt.title('Traffic Congestion Distribution',
                      fontsize=16, fontweight='bold', pad=20)
            plt.axis('equal')
            plt.tight_layout()

            output_path = self.output_dir / 'congestion_distribution.png'
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()

            logger.info(
                f"Saved congestion distribution chart to {output_path}")
            return str(output_path)

        except Exception as e:
            logger.error(f"Error generating congestion distribution: {e}")
            plt.close()
            return None

    def plot_clustering(self, cluster_labels):
        """Generate clustering visualization"""
        try:
            plt.figure(figsize=(14, 8))

            # Use hour and traffic_volume for 2D visualization
            scatter_data = self.data[['hour', 'traffic_volume']].copy()
            scatter_data['cluster'] = cluster_labels

            colors = ['#FF6B00', '#2ECC71', '#3498DB', '#9B59B6']

            for cluster in sorted(scatter_data['cluster'].unique()):
                cluster_data = scatter_data[scatter_data['cluster'] == cluster]
                plt.scatter(cluster_data['hour'], cluster_data['traffic_volume'],
                            c=colors[cluster %
                                     len(colors)], label=f'Cluster {cluster}',
                            alpha=0.6, s=30, edgecolors='black', linewidth=0.5)

            plt.title('Traffic Clustering (K-Means)',
                      fontsize=16, fontweight='bold', pad=20)
            plt.xlabel('Hour of Day', fontsize=12, fontweight='bold')
            plt.ylabel('Traffic Volume', fontsize=12, fontweight='bold')
            plt.legend(loc='best', fontsize=10)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()

            output_path = self.output_dir / 'clustering.png'
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()

            logger.info(f"Saved clustering chart to {output_path}")
            return str(output_path)

        except Exception as e:
            logger.error(f"Error generating clustering visualization: {e}")
            plt.close()
            return None

    def generate_all_visualizations(self, correlation_matrix=None, cluster_labels=None):
        """
        Generate all visualizations

        Args:
            correlation_matrix (pd.DataFrame): Correlation matrix
            cluster_labels (np.array): Cluster labels

        Returns:
            dict: Paths to generated visualizations
        """
        logger.info("Generating all visualizations...")

        visualizations = {
            'hourly_trend': self.plot_hourly_trend(),
            'weekly_trend': self.plot_weekly_trend(),
            'monthly_trend': self.plot_monthly_trend(),
            'weather_impact': self.plot_weather_impact(),
            'congestion_distribution': self.plot_congestion_distribution()
        }

        if correlation_matrix is not None:
            visualizations['correlation_heatmap'] = self.plot_correlation_heatmap(
                correlation_matrix)

        if cluster_labels is not None:
            visualizations['clustering'] = self.plot_clustering(cluster_labels)

        logger.info("All visualizations generated successfully")
        return visualizations
