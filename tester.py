#for testing the api implementation
#api Key site https://weatherstack.com/login
#Documenation https://weatherstack.com/documentation
#Guide https://medium.com/@buddyminds/creating-a-weather-application-in-python-a-step-by-step-guide-b14152cc936a

import requests
import json
import urllib.request
import io
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

###FORMATTING APP###
root = tk.Tk()
root.geometry("1000x650")
root.title("Weather App")

weather_label = tk.Label(root)
weather_label.pack()

#create an entry form
entry = tk.Entry(root,width=20)
enter=entry.place(x=100,y=20)

#Create a panel to show the forecast which populates automatically 
forecast = tk.PanedWindow(root,bd=3)
forecast.pack(expand=2)
dayone = tk.Label(forecast,text="dayOne",bd=5)
forecast.add(dayone)
daytwo = tk.Label(forecast,text="daytwo",bd=5)
forecast.add(daytwo)
daythree = tk.Label(forecast,text="daythree",bd=5)
forecast.add(daythree)


fetch_button = tk.Button(root, text= "Fetch Weather",font=("Arial", 10,"bold"),bd=3)
fetchbutton = fetch_button.place(x=50,y=45)


def display_image_from_url(url):
    entrance = entry.get()
    try:
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
    except Exception as e:
        print(f"Error fetching the image: {e}")
        return

    try:
        image = Image.open(io.BytesIO(raw_data))
        photo = ImageTk.PhotoImage(image)
        weather_label.config(image=photo,text="\nthis shit worked finalfuckingly")
        weather_label.image=photo
    except Exception as d:
        print(f"Error opening the image{d}")
        return
    return entrance

def display_color(color):
    print("what is the color you chose?\n"+color)
    dayone.config(text= "you chose Red didnt you?")


 
#photo = display_image_from_url("https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png")
#photo("https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png")
fetch_button.config(command=lambda: display_color(display_image_from_url("https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png")))   
#run the function

root.mainloop()
#display_image_from_url("https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png")












#api_key = "a5d559f997066b872b3f1482b7130a6d"
#query = input("City Name\n")
#url = "http://api.weatherstack.com/current?access_key=" + api_key + "&query=" + query 
#response = requests.get(url)
#print(response.json())