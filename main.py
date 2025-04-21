import os
import pandas as pd
import turtle
import math
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from countries.China import plot_country_data as china_plot
from countries.France import plot_country_data as france_plot
from countries.Germany import plot_country_data as germany_plot
from countries.Russia import plot_country_data as russia_plot
from countries.UnitedStates import plot_country_data as us_plot
import matplotlib.pyplot as plt

# Function for handling clicks
def click(x, y):
    for country, (cx, cy, radius) in countries.items():
        if is_click_in_circle(x, y, cx, cy, radius):
            print(f"Clicked on {country}")
            open_popup(country)

# Check if click is inside a circle
def is_click_in_circle(x, y, circle_x, circle_y, radius):
    distance = math.sqrt((x - circle_x) ** 2 + (y - circle_y) ** 2)
    return distance <= radius

# Create the map with countries
def create_circle(circle_x, circle_y, radius):
    circle = turtle.Turtle()
    circle.hideturtle()
    circle.speed(0)
    circle.penup()
    circle.goto(circle_x, circle_y - radius)
    circle.pendown()
    circle.fillcolor("#FF0000")  # Red color for circles
    circle.begin_fill()
    circle.circle(radius)
    circle.end_fill()

# Get tkinter root window used by turtle
root = turtle.Screen()._root

# Function to show graphs in popup
def show_graph(popup, country):
    # Define the directory where the graph CSVs are stored
    country_dir = f"./datasets/{country}"
    
    # Check if the directory exists
    if not os.path.exists(country_dir):
        print(f"Directory for {country} not found!")
        return
    
    # Fetch CSV files for the country
    graph_files = [f for f in os.listdir(country_dir) if f.endswith('.csv')]
    
    if not graph_files:
        print(f"No CSV files found for {country}.")
        return
    
    # Loop through each CSV file and create a plot for it
    for graph_file in graph_files:
        # Read the data from CSV
        file_path = os.path.join(country_dir, graph_file)
        data = pd.read_csv(file_path)

        # Use the imported function to handle plotting
        plot_country_data(data, graph_file, popup)

# Function to show popup box with country info
def open_popup(country):
    popup = tk.Toplevel(root)
    popup.title(f"About {country}")
    popup.geometry("500x400")
    popup.configure(bg="white")
    popup.COUNTRY = country

    label = tk.Label(popup, text=f"Statistics for {country}", bg="white", font=("Arial", 14))
    label.pack(pady=20)

    show_graph(popup=popup, country=country)

# Setup for the country circles (coordinates and radius)
countries = {
    "India": (109, 32, 2),
    "China": (141, 69, 2),
    "Russia": (99, 133, 2),
    "United Kingdom": (-68, 114, 2),
    "France": (-61, 95, 2),
    "Germany": (-47, 108, 2),
    "United States": (-276, 88, 2),
    "Canada": (-269, 122, 2),
    "Mexico": (-292, 39, 2),
    "Brazil": (-185, -50, 2),
    "Nigeria": (-45, 22, 2),
    "Turkey": (2, 78, 2),
    "Australia": (226, -87, 2),
    "New Zealand": (289, -129, 2),
    "Papua New Guinea": (256, -39, 2),
    "South Africa": (-15, -99, 2),
    "Kenya": (17, -21, 2),
    "Indonesia": (161, -26, 2),
}

# Create the map using the custom gif
screen = turtle.Screen()
screen.setup(width=735, height=365)
screen.title("Climate Analysis")
screen.addshape("2DWM.gif")

# Create a new turtle for the map, and make sure it's on the bottom layer
image_turtle = turtle.Turtle()
image_turtle.shape("2DWM.gif")
image_turtle.penup()
image_turtle.goto(0, 0)  # Position the map at the center

# Draw the circles on top of the map after it's created
for country, (cx, cy, radius) in countries.items():
    create_circle(cx, cy, radius)

# Function to handle user clicks
screen.onscreenclick(click)

# Keep the window open and waiting for interactions
screen.mainloop()