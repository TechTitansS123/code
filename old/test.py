import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('ds/Monthly_MinT_Temperature_1744686188582.csv')

# Convert 'Temperature (in °C)' to numeric, invalid parsing will be set to NaN
data['Temperature (in °C)'] = pd.to_numeric(data['Temperature (in °C)'], errors='coerce')

# Ensure 'Station Name' is a string type
data['Station Name'] = data['Station Name'].astype(str)

# Sort the data by temperature
sorted_data = data.sort_values(by='Temperature (in °C)')

# Create the plot
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot the horizontal bar chart
axs[0].barh(sorted_data['Station Name'], sorted_data['Temperature (in °C)'], color='skyblue')
axs[0].set_title('Temperature by Station')
axs[0].set_xlabel('Temperature (°C)')
axs[0].set_ylabel('Station Name')

# Remove all x-axis labels and ticks for the bar plot
axs[0].set_xticks([])  # Remove x-axis ticks
axs[0].set_xticklabels([])  # Remove x-axis labels

# Plot the scatter chart
axs[1].scatter(sorted_data['Station Name'], sorted_data['Temperature (in °C)'], color='orange')
axs[1].set_title('Temperature Distribution by Station')
axs[1].set_xlabel('Station Name')
axs[1].set_ylabel('Temperature (°C)')

# Remove all x-axis labels and ticks for the scatter plot
axs[1].set_xticks([])  # Remove x-axis ticks
axs[1].set_xticklabels([])  # Remove x-axis labels

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
