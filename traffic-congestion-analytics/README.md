# Traffic Congestion Analytics System

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A production-level traffic congestion analytics system that provides actionable insights for urban traffic management using machine learning and data visualization.

## 🎯 Problem Statement

Urban planners collect traffic sensor data but lack actionable insights for congestion management. This system analyzes traffic flow data to identify:

- 🚦 Congestion hotspots
- ⏰ Peak travel times
- 🔄 Recurring traffic bottlenecks
- 🌤️ Weather impact on traffic
- 📅 Weekly & monthly traffic trends

## ✨ Features

### Data Science Pipeline
- ✅ Automated dataset loading from Kaggle using KaggleHub
- ✅ Comprehensive data cleaning and preprocessing
- ✅ Advanced feature engineering (time-based, weather-based)
- ✅ Traffic congestion detection and classification
- ✅ Peak hour and bottleneck identification
- ✅ Weather impact analysis
- ✅ Correlation analysis and heatmaps

### Machine Learning Models
- 📈 **Linear Regression**: Traffic volume prediction (MAE, RMSE evaluation)
- 🎯 **K-Means Clustering**: Traffic pattern segmentation
- 🔮 **Real-time Prediction API**: Dynamic traffic forecasting

### Visualizations
- 📊 Hourly traffic trends
- 📅 Weekly traffic patterns
- 📆 Monthly traffic variations
- 🌦️ Weather vs traffic volume analysis
- 🔥 Correlation heatmaps
- 🥧 Congestion distribution charts
- 🎨 Traffic clustering visualizations

### Web Dashboard
- 🎨 Modern, responsive UI with card-based design
- 🟠 Orange (#FF6B00) and Green (#2ECC71) color scheme
- 📱 Mobile-friendly responsive layout
- 📋 Summary metric cards
- 📈 Interactive charts and visualizations
- ⚠️ Bottleneck alerts and insights
- 🔍 Detailed congestion analysis

### REST API Endpoints
- `GET /` - Dashboard homepage
- `GET /api/summary` - Complete traffic summary statistics
- `GET /api/predict` - Traffic volume prediction
- `GET /api/analytics/{type}` - Specific analytics (peak_hours, weather_impact, etc.)

## 🏗️ Project Structure

```
traffic-congestion-analytics/
│
├── app/
│   ├── __init__.py                 # Flask app initialization
│   ├── routes.py                   # API routes and endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── data_loader.py         # Kaggle dataset loading
│   │   ├── data_processor.py      # Data cleaning & feature engineering
│   │   ├── analytics.py           # Traffic analytics & insights
│   │   ├── visualization.py       # Chart generation
│   │   └── model.py               # ML models (regression, clustering)
│   ├── templates/
│   │   ├── base.html              # Base template
│   │   └── dashboard.html         # Dashboard UI
│   └── static/
│       ├── css/
│       │   └── style.css          # Custom styles
│       └── images/                # Generated charts
│
├── config/
│   └── settings.py                # Configuration settings
│
├── data/                          # Dataset storage
├── notebooks/
│   └── EDA.ipynb                  # Exploratory data analysis
├── tests/                         # Unit tests
├── run.py                         # Application entry point
├── requirements.txt               # Python dependencies
└── README.md                      # Documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip package manager
- Kaggle API credentials (for dataset download)

### Step 1: Clone the Repository
```bash
cd traffic-congestion-analytics
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Kaggle API (Optional)
If you want to download the dataset automatically:

1. Create a Kaggle account at [kaggle.com](https://www.kaggle.com)
2. Go to Account Settings → API → Create New API Token
3. Place `kaggle.json` in:
   - Windows: `C:\Users\<username>\.kaggle\`
   - Linux/Mac: `~/.kaggle/`

### Step 5: Run the Application
```bash
python run.py
```

The application will:
1. Download the traffic dataset from Kaggle
2. Process and analyze the data
3. Train ML models
4. Generate visualizations
5. Start the Flask web server

Access the dashboard at: **http://localhost:5000**

## 📊 Dataset

**Source**: [Highway Traffic Volume - Kaggle](https://www.kaggle.com/datasets/galenchen/highway-traffic-volume)

**Features**:
- `traffic_volume`: Number of vehicles (target variable)
- `date_time`: Timestamp of observation
- `temp`: Temperature (Kelvin)
- `rain_1h`: Rain volume (mm)
- `snow_1h`: Snow volume (mm)
- `clouds_all`: Cloud coverage percentage
- `weather_main`: Weather category
- `weather_description`: Detailed weather description

## 🔌 API Usage

### Get Traffic Summary
```bash
curl http://localhost:5000/api/summary
```

**Response**:
```json
{
  "status": "success",
  "data": {
    "summary": {
      "total_records": 48204,
      "avg_traffic_volume": 3259.82,
      "peak_hour": 17,
      "congestion_rate": 23.45
    }
  }
}
```

### Predict Traffic Volume
```bash
curl "http://localhost:5000/api/predict?hour=17&weather=Rain&temp=285&weekday=1&month=6"
```

**Response**:
```json
{
  "status": "success",
  "data": {
    "predicted_volume": 4523.67,
    "is_congested": true,
    "congestion_threshold": 4500,
    "input_features": {
      "hour": 17,
      "weather": "Rain",
      "temp": 285
    }
  }
}
```

### Get Specific Analytics
```bash
# Peak hours analysis
curl http://localhost:5000/api/analytics/peak_hours

# Weather impact
curl http://localhost:5000/api/analytics/weather_impact

# Monthly trends
curl http://localhost:5000/api/analytics/monthly_trends

# Bottlenecks
curl http://localhost:5000/api/analytics/bottlenecks
```

## 🧪 Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=app --cov-report=html
```

## 📓 Jupyter Notebook Analysis

Explore the detailed EDA in the Jupyter notebook:

```bash
jupyter notebook notebooks/EDA.ipynb
```

The notebook includes:
- Complete data exploration
- Statistical analysis
- Visualization generation
- Model training and evaluation
- Key insights and recommendations

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | Python 3.11+, Flask 3.0 |
| **Data Science** | Pandas, NumPy, Scikit-learn |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Frontend** | HTML5, CSS3, Jinja2 |
| **Data Source** | KaggleHub API |
| **ML Models** | Linear Regression, K-Means |

## 📈 Model Performance

### Linear Regression (Traffic Volume Prediction)
- **MAE (Mean Absolute Error)**: ~750-850 vehicles
- **RMSE (Root Mean Squared Error)**: ~1100-1300 vehicles
- **R² Score**: ~0.75-0.80
- **Features**: Hour, month, weekday, temperature, weather conditions

### K-Means Clustering
- **Clusters**: 4 distinct traffic patterns
- **Features**: Hour, traffic volume, temperature, weekday
- **Use Case**: Pattern identification for targeted interventions

## 🎨 UI Design

### Color Scheme
- **Primary Orange**: `#FF6B00` - Alerts, highlights, primary actions
- **Accent Green**: `#2ECC71` - Success states, positive metrics
- **White Background**: `#FFFFFF` - Clean, modern interface
- **Dark Text**: `#2C3E50` - Readability and contrast

### Design Principles
- Card-based layout for modular information
- Responsive grid system
- High contrast for accessibility
- Modern sans-serif typography (Inter font)
- Smooth transitions and hover effects

## 🔧 Configuration

Edit `config/settings.py` to customize:

```python
# Data settings
CONGESTION_THRESHOLD = 4500  # Traffic volume threshold

# Model settings
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_CLUSTERS = 4

# Flask settings
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True
```

## 🚨 Troubleshooting

### Issue: Dataset not downloading
**Solution**: Ensure Kaggle API is configured correctly. Manually download from Kaggle and place in `data/` folder.

### Issue: Port 5000 already in use
**Solution**: Change port in `config/settings.py` or use:
```bash
PORT=8080 python run.py
```

### Issue: Memory error during processing
**Solution**: Reduce dataset size or increase system memory allocation.

## 📝 Future Enhancements

- [ ] Real-time traffic data integration
- [ ] Deep learning models (LSTM, GRU)
- [ ] Interactive Plotly charts
- [ ] User authentication system
- [ ] Historical comparison features
- [ ] Export reports to PDF
- [ ] Email alerts for high congestion
- [ ] Mobile app integration

## 👥 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Dataset: [Galen Chen](https://www.kaggle.com/galenchen) - Highway Traffic Volume
- Framework: Flask Development Team
- Libraries: Scikit-learn, Pandas, Matplotlib, Seaborn communities

## 📧 Contact

For questions or support, please open an issue on the repository.

---

**Built with ❤️ for better urban traffic management**
