import turtle
import math
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def click(x, y):
    print(f"You clicked at ({x}, {y})")
    check_click1(x, y)
    check_click2(x, y)
    check_click3(x, y)
    check_click4(x, y)
    check_click5(x, y)
    check_click6(x, y)
    check_click7(x, y)
    check_click8(x, y)
    check_click9(x, y)
    check_click10(x, y)
    check_click11(x, y)
    check_click12(x, y)

screen = turtle.Screen()
screen.setup(width=735, height=365)
screen.title("Climate Analysis")
screen.onscreenclick(click)

screen.addshape("2DWM.gif")

image_turtle = turtle.Turtle()
image_turtle.shape("2DWM.gif")

def create_circle(circle_x, circle_y, radius):
    circle = turtle.Turtle()
    circle.hideturtle()
    circle.speed(0)
    circle.penup()
    circle.goto(circle_x, circle_y - radius)
    circle.pendown()
    circle.fillcolor("#FF0000")
    circle.begin_fill()
    circle.circle(radius)
    circle.end_fill()
  

# Get tkinter root window used by turtle
root = screen._root

# Function to show graph in popup
def show_graph(popup):
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot([1, 2, 3, 4], [10, 20, 5, 30])
    ax.set_title("Sample Graph")

    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Function to show popup box
def open_popup(country):
    popup = tk.Toplevel(root)
    popup.title(f"About {country}")
    popup.geometry("500x400")
    popup.configure(bg="white")
    popup.COUNTRY = country

    label = tk.Label(popup, text=f"Statistics for {country}", bg="white", font=("Arial", 14))
    label.pack(pady=20)

    show_graph(popup)

# Check if the circle was clicked

# India
def check_click1(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("India")

# China
def check_click2(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("China")

# Russia
def check_click3(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("Russia")

# United Kingdom
def check_click4(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("United Kingdom")

# France
def check_click5(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("France")

# Germany
def check_click6(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("Germany")

# United States
def check_click7(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("United States")

# Canada
def check_click8(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("Canada")

# Mexico
def check_click9(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("Mexico")

# Brazil
def check_click10(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("Brazil")

# Argentina
def check_click11(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("Argentina")

# Peru
def check_click12(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("Peru")

# Australia
def check_click13(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("Australia")

# New Zealand
def check_click14(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("New Zealand")

# Papua New Guinea
def check_click15(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("Papua New Guinea")

# South Africa
def check_click16(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("South Africa")

# Kenya
def check_click17(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("Kenya")

# Egypt
def check_click18(x, y):
    circle_x = 109
    circle_y = 32
    radius = 2
    distance = math.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= radius:
        print("Circle clicked!")
        open_popup("Egypt")

create_circle(109, 32, 2) # India
create_circle(141, 69, 2) # China
create_circle(99, 133, 2) # Russia
create_circle(-68, 114, 2) # United Kingdom
create_circle(-61, 95, 2) # France
create_circle(-47, 108, 2) # Germany
create_circle(-276, 88, 2) # United States
create_circle(-269, 122, 2) # Canada
create_circle(-292, 39, 2) # Mexico
create_circle(-185, -50, 2) # Brazil
create_circle(-45, 22, 2) # Nigeria
create_circle(2, 78, 2) # Turkey
create_circle(226, -87, 2) # Australia
create_circle(289, -129, 2) # New Zealand
create_circle(256, -39, 2) # Papua New Guinea
create_circle(-15, -99, 2) # South Africa
create_circle(17, -21, 2) # Kenya
create_circle(161, -26, 2) # Indonesia
turtle.done()