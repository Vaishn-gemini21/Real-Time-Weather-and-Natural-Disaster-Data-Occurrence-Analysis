# **Real-Time-Weather-and-Natural-Disaster-Data-Occurrence-Analysis**

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


## **OUTPUT SCREENSHOTS**

**Real-Time**
1. Line Chart :

   <img width="1536" height="754" alt="Figure_1" src="https://github.com/user-attachments/assets/260430a9-1efd-42fa-9316-ebcca04cef47" />

2. Bar Chart :

   <img width="1536" height="754" alt="Figure_2" src="https://github.com/user-attachments/assets/fb9b0cf8-df4f-4d6e-be69-01b5e73ce20b" />

3. Pie Chart :
   
   <img width="1536" height="754" alt="Figure_3" src="https://github.com/user-attachments/assets/999c4db8-fae0-4503-adf8-a26d91879e63" />

**Historical Weather Data (CSV) Models**

1. Temperature Data :

   <img width="1536" height="754" alt="Figure_4" src="https://github.com/user-attachments/assets/3bdcf5b9-0f89-4015-b2ac-89daac851d63" />

2. Precipitation Data :

   <img width="1536" height="754" alt="Figure_5" src="https://github.com/user-attachments/assets/4d53b635-0fd7-4312-b0d8-daa6d02bba52" />

3. Humidity Data(2006 & 2023) :

   2006 - <img width="1536" height="754" alt="Figure_6" src="https://github.com/user-attachments/assets/f1ccba77-b429-4472-a3f7-ece7d7867a3c" />
   2023 - <img width="1536" height="754" alt="Figure_7" src="https://github.com/user-attachments/assets/7e125cbb-84c2-4531-8d4b-96477cfcde78" />

4. Natural Disaster Data (2006 & 2023) :

   2006 - <img width="1536" height="754" alt="Figure_8" src="https://github.com/user-attachments/assets/d88dce00-0a6d-407e-b02f-2147fbf7d837" />
   2023 - <img width="1536" height="754" alt="Figure_9" src="https://github.com/user-attachments/assets/8f62a108-f2f2-4482-b329-8eb25eeec351" />










