import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Aerospace Engineering Analysis Tool")

# User Input for Aircraft Parameters
st.sidebar.header("Input Parameters")
altitude = st.sidebar.slider("Altitude (m)", 0, 20000, 10000)
speed = st.sidebar.slider("Speed (m/s)", 100, 1000, 250)
air_density = 1.225 * np.exp(-altitude / 8000)  # Simple atmospheric model

# Lift Calculation
st.header("Aerodynamic Forces")
lift_coefficient = st.slider("Lift Coefficient (Cl)", 0.1, 2.0, 1.0)
wing_area = st.slider("Wing Area (m²)", 10, 500, 50)
lift_force = 0.5 * air_density * speed**2 * wing_area * lift_coefficient
st.write(f"### Lift Force: {lift_force:.2f} N")

# Drag Calculation
drag_coefficient = st.slider("Drag Coefficient (Cd)", 0.01, 0.5, 0.1)
drag_force = 0.5 * air_density * speed**2 * wing_area * drag_coefficient
st.write(f"### Drag Force: {drag_force:.2f} N")

# Thrust and Fuel Efficiency
st.header("Propulsion Analysis")
thrust = st.slider("Thrust (N)", 1000, 50000, 20000)
specific_fuel_consumption = st.slider("Specific Fuel Consumption (kg/N/s)", 0.0001, 0.01, 0.002)
fuel_burn_rate = thrust * specific_fuel_consumption
st.write(f"### Fuel Burn Rate: {fuel_burn_rate:.4f} kg/s")

# Plot Lift vs Drag Curve
st.header("Lift vs Drag Curve")
Cl_values = np.linspace(0.1, 2.0, 50)
Cd_values = np.linspace(0.01, 0.5, 50)
plt.figure(figsize=(6, 4))
plt.plot(Cd_values, Cl_values, label="Lift vs Drag Curve")
plt.xlabel("Drag Coefficient (Cd)")
plt.ylabel("Lift Coefficient (Cl)")
plt.legend()
st.pyplot(plt)

# Conclusion
st.write("This tool provides a simplified aerodynamic and propulsion analysis for aerospace engineering applications.")
