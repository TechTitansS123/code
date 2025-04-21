import pandas as pd

# Creating a sample dataset for climate data in India
years = list(range(2000, 2025))
average_temperatures = [25.3, 25.6, 25.7, 25.9, 26.1, 26.3, 26.5, 26.6, 26.8, 27.0, 
                        27.1, 27.2, 27.4, 27.5, 27.6, 27.8, 28.0, 28.1, 28.3, 28.4, 
                        28.5, 28.7, 28.9, 29.0, 29.1]  # Adjusted this to 25 values as needed

# Making sure both arrays are the same length
if len(years) == len(average_temperatures):
    # Creating a dataframe
    climate_data = pd.DataFrame({
        'Year': years,
        'Average Temperature': average_temperatures
    })

    # Saving the dataframe to a CSV file
    climate_data.to_csv('climate_data_india.csv', index=False)
else:
    print("Error: The length of the arrays do not match.")
