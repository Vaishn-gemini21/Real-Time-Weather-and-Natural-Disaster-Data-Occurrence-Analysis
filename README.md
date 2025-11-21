#**Real-Time-Weather-and-Natural-Disaster-Data-Occurrence-Analysis**

## **PROJECT SYNOPSIS**

The Real-Time Weather and Natural Disaster Data Analysis project is a Python-based application that allows users to analyse and visualise both historical and real-time weather and natural disaster data. The system provides a comprehensive range of functionalities, including fetching live weather data, performing analysis on temperature, precipitation, and humidity, tracking natural disaster occurrences, and generating dynamic visualisations. Users can monitor current weather conditions, observe trends over time, and gain insights into natural disaster patterns, enabling both historical comparison and up-to-the-minute analysis.


**FEATURES**

**1. Data Source Layer**
Real-Time Weather Data (API)
Obtained via OpenWeatherMap API.
Provides temperature, humidity, pressure, wind speed, and weather description.

Historical Weather & Disaster Data (CSV Model)
Temperature, rainfall, humidity (Mumbai: 2006 & 2023)
Natural disaster records (Floods, Cyclones, Landslides, Tsunamis, Earthquakes)
Both pipelines ensure flexibility: the system can fetch live updates OR analyse past trends.

**2. Data Processing Layer**
This layer manages retrieval, cleaning, and structuring of data.
Components:
WeatherAPI Class
Handles API requests, JSON parsing, and structured dictionary output.          CSV Data Loader
Reads historical CSV files using Pandas and preprocesses them for visualization.
This layer abstracts all raw data interactions, keeping the core logic clean.

3. Analysis Layer
This layer applies logic to interpret processed data.
Components:
WeatherAnalysis Class

##**Technologies Used**

1. Python 3 — Core programming language
2. Requests — Fetching real-time weather data via API
3. Pandas & NumPy — Data handling and numerical operations
4. Matplotlib — Data visualization (line, bar, pie, histogram)
5. OpenWeather API — Real-time weather data source
6. CSV Datasets — Historical weather & disaster data
7. VS Code — Development environment
8. Virtual Environment (.venv) — Dependency isolation

**Steps to Install & Run the Project**

1. Clone the Repository
2. Create & Activate a Virtual Environment
3. Install Dependencies
4. Add Your API Key
5. Place the CSV Files
6. Running the Project


This layer transforms raw values into meaningful insights for users.

