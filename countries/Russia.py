import os
import pandas as pd

def plot_country_data():
    print(f"Plotting data for Russia...")
    def get_country_data():
        file_path = os.path.join(os.getcwd(), f"{country_name}.csv")
        return pd.read_csv(file_path)
    get_country_data(country_name)