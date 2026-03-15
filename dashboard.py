
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

st.title("⚡ SMARTGRID-AI Energy Prediction Dashboard")

# Load dataset
df = pd.read_csv("energy_dataset.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Convert time column
df['Datetime'] = pd.to_datetime(df['time'], errors='coerce', utc=True)

# Feature Engineering
df['hour'] = df['Datetime'].dt.hour
df['day_of_week'] = df['Datetime'].dt.dayofweek
df['month'] = df['Datetime'].dt.month
df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)

# Target column
target_col = "total load actual"
df[target_col] = df[target_col].fillna(df[target_col].median())

features = ['hour','day_of_week','month','is_weekend']

X = df[features]
y = df[target_col]

# Train model
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = RandomForestRegressor(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test,predictions)

st.subheader("Model Performance")
st.write("Average Prediction Error (MAE):", round(mae,2))

# Visualization
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
}).reset_index(drop=True)

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(results['Actual'][:100], label="Actual Demand")
ax.plot(results['Predicted'][:100], linestyle="--", label="Predicted Demand")

ax.set_title("Energy Demand: Actual vs Predicted")
ax.set_xlabel("Hours")
ax.set_ylabel("Energy Units (MW)")
ax.legend()

st.pyplot(fig)

# Anomaly Detection
results['Error'] = results['Actual'] - results['Predicted']

threshold = results['Predicted'] * 0.15
anomalies = results[results['Error'] > threshold]

st.subheader("Energy Waste Detection")

st.write("Number of anomaly hours detected:", len(anomalies))

# Sustainability report
total_wasted_mw = anomalies['Error'].sum()

co2_saved_kg = total_wasted_mw * 1000 * 0.19
co2_saved_tonnes = co2_saved_kg / 1000

st.subheader("Sustainability Report")

st.write("Total potential energy waste detected:", round(total_wasted_mw,2),"MWh")
st.write("Estimated CO2 reduction:", round(co2_saved_tonnes,2),"tonnes")
st.write("Equivalent trees planted:", int(co2_saved_tonnes*45))

