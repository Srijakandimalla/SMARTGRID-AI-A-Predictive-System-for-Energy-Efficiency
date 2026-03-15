# ⚡ SMARTGRID-AI: A Predictive System for Energy Efficiency

## Overview

SMARTGRID-AI is a machine learning system designed to analyze electricity consumption patterns and predict future energy demand in smart grids.

The system uses a **Random Forest Regression model** to forecast hourly electricity usage and detect abnormal energy consumption patterns. By comparing predicted demand with actual consumption, the system identifies potential inefficiencies and estimates the environmental impact in terms of **CO₂ emission reductions**.

An interactive **Streamlit dashboard** allows users to visualize predictions, explore model insights, and monitor energy efficiency.

---

## Key Features

* ⚡ Energy demand prediction using **Machine Learning**
* 📊 Random Forest Regression model
* 🚨 Energy waste anomaly detection
* 📈 Visualization of **Actual vs Predicted electricity demand**
* 🌍 Sustainability analysis with CO₂ emission estimation
* 🖥 Interactive **Streamlit dashboard**

---

## Project Architecture

The SMARTGRID-AI system follows a structured machine learning pipeline.

### Workflow

1. **Data Collection**

   * Historical smart grid electricity dataset

2. **Data Preprocessing**

   * Handle missing values
   * Convert time data to datetime format

3. **Feature Engineering**

   * Extract temporal features such as:

     * Hour of day
     * Day of week
     * Month
     * Weekend indicator
     * Night usage indicator

4. **Machine Learning Model**

   * Random Forest Regression

5. **Energy Demand Prediction**

   * Forecast hourly electricity consumption

6. **Anomaly Detection**

   * Detect inefficient energy usage when actual demand exceeds predicted demand by more than **15%**

7. **Visualization**

   * Energy demand prediction graphs
   * Feature importance analysis

8. **Interactive Dashboard**

   * Real-time energy insights using Streamlit

---

## Dataset

The dataset contains **35,000+ hourly electricity records** including:

* Energy generation sources
* Forecast electricity demand
* Actual electricity load
* Energy market prices

This data allows the model to learn patterns in energy consumption across different times of the day and year.

---

## Machine Learning Model

The system uses **Random Forest Regression**, an ensemble learning method that combines multiple decision trees to improve prediction accuracy.

### Input Features

* Hour
* Day of week
* Month
* Weekend indicator
* Night usage indicator

### Target Variable

* Total electricity load

---

## Model Performance

Average prediction error:

2043.47 MW

### Energy Demand Prediction

![Model Performance](model_performance.png)

This graph compares the **actual electricity demand** with the **AI predicted demand**.
The close alignment between the two lines shows that the model successfully learns energy consumption patterns.

---

## Energy Waste Detection

The system identifies abnormal energy consumption using the rule:

Actual Demand > Predicted Demand + 15%

Example output:

Anomaly Hours Detected: 352

Total Potential Energy Waste: 2,114,900 MWh

Estimated CO₂ Reduction: 401,831 tonnes

Equivalent Trees Planted: 18,082,395

These results demonstrate how machine learning can support **energy efficiency and environmental sustainability**.

---

## Interactive Dashboard

SMARTGRID-AI includes a **Streamlit dashboard** that allows users to:

* View dataset insights
* Monitor model performance
* Visualize energy demand predictions
* Detect energy waste anomalies
* Analyze sustainability impact

Run the dashboard locally to interact with the system.

---

## Project Structure

SMARTGRID-AI
│
├── dashboard.py
├── smartgrid_ai.py
├── energy_dataset.csv
├── model_performance.png
├── requirements.txt
└── README.md

---

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

---

## Run the Machine Learning Model

```
python smartgrid_ai.py
```

---

## Run the Dashboard

```
streamlit run dashboard.py
```

Open the browser at:

```
http://localhost:8501
```

---

## Technologies Used

Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Streamlit

---

## Future Improvements

* Deep learning models for energy forecasting
* Real-time smart grid monitoring
* Integration with IoT energy sensors
* Advanced anomaly detection algorithms

---

## Author

**Srija Kandimalla**

