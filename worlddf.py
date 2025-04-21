import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('worlddf.csv')
years = [str(year) for year in range(1990, 2022)]
top_countries = ['World', 'China', 'United States', 'India', 'European Union (27)']
filtered_data = data[data['Country'].isin(top_countries)]

plt.figure(figsize=(12, 6))
for country in top_countries:
    country_data = filtered_data[filtered_data['Country'] == country]
    plt.plot(years, country_data[years].values.flatten(), label=country)

plt.xlabel('Year')
plt.ylabel('Emissions (MtCO₂e)')
plt.title('Greenhouse Gas Emissions (1990-2021)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
