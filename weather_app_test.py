#Weather app  
# 
# Last update: 12/5

import requests
import json
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

###FORMATTING APP###

root = tk.Tk()
root.geometry("1000x650")
root.title("Weather App")

#Create and configure labels and entry fields 
city_label = tk.Label(root,
                       text="City:",
                       #anchor=tk.CENTER,
                       #bg="grey",
                       height=1,
                       width=6,
                       bd=3,
                       font=("Times New Roman", 16, "bold"),
                       #cursor="hand2",
                       fg="black",
                       padx=3,
                       pady=3,
                       justify=tk.CENTER,
                       relief=tk.RAISED,
                       #underline=0,
                       wraplength=250
                       ).place(x=5,y=5)
city_entry = tk.Entry(root,width=20)
cityenter=city_entry.place(x=100,y=20)

#Create a button to fetch the weather data
fetch_button = tk.Button(root, text= "Fetch Weather",font=("Arial", 10,"bold"),bd=3)
fetchbutton = fetch_button.place(x=50,y=45)

#Create a label to display weather information
weather_label = tk.Label(root, text="")
weather_label.pack()

#Create a panel to show the forecast which populates automatically 
forecast = tk.PanedWindow(root,bd=3)
forecast.pack(expand=2)
dayone = tk.Label(forecast,text="dayOne",bd=5)
forecast.add(dayone)
daytwo = tk.Label(forecast,text="daytwo",bd=5)
forecast.add(daytwo)
daythree = tk.Label(forecast,text="daythree",bd=5)
forecast.add(daythree)

#Define the function to determine the weather 
def fetch_weather():
    city = city_entry.get()
    #Add the api key here 
    api_key = "a5d559f997066b872b3f1482b7130a6d"
    url = "http://api.weatherstack.com/current?access_key=" + api_key + "&query=" + city 
    #may have to use open wethermap instead of weatherstack, currently have api for weatherstack

    try:
        response = requests.get(url)
        data = response.json()
        formatted_data = json.dumps(data, indent = 4) #command for formatting json information to be more readable
        print(formatted_data)
        temperature = data["current"]["temperature"]
        Farenheit = (temperature * 9/5) + 32 
        weather = data["current"]["weather_descriptions"]
        
        weather_label.config(text=f"Temperature: {Farenheit}°F / {temperature}°C\nWeather: {weather}")
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")

fetch_button.config(command=fetch_weather)
6
#def forecasted():


root.mainloop()

