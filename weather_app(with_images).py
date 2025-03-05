#Weather app  
# 
# Last update: 12/5

import requests
import json
import urllib.request
import io
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

###FORMATTING APP###
root = tk.Tk()
root.geometry("350x250")
root.title("Weather App")

weather_label = tk.Label(root)
weather_label.pack()

weather_image = tk.Label(root)
weather_image.pack()
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



#Define the function to determine the weather 
def fetch_weather():
    city = city_entry.get()
    #Add the api key here 
    api_key = "116a735e60672ae7ffe35bfc0da60014" #from martian manhunter email
    #old key from yahoo email "a5d559f997066b872b3f1482b7130a6d"
    url = "http://api.weatherstack.com/current?access_key=" + api_key + "&query=" + city 
    #may have to use open wethermap instead of weatherstack, currently have api for weatherstack
    response = requests.get(url)
    data = response.json()
    
    try:
        formatted_data = json.dumps(data, indent = 4) #command for formatting json information to be more readable
        print(formatted_data)
        temperature = data["current"]["temperature"]
        Farenheit = (temperature * 9/5) + 32 
        weather = data["current"]["weather_descriptions"][0]
        weathimage = data["current"]["weather_icons"][0]
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")
        return
        
    try:   
        with urllib.request.urlopen(weathimage) as u:
            raw_data = u.read()
    except Exception as ugh:
        messagebox.showerror("Error",f"Can't read the url:\n{ugh}")
        return

    try:    
        pic = Image.open(io.BytesIO(raw_data))
        photo = ImageTk.PhotoImage(pic)
        weather_label.config(text=f"\n\n\nTemperature: {Farenheit}°F / {temperature}°C\nWeather: {weather}")
        weather_image.config(image=photo)
        weather_image.image=photo
        weatherimage = weather_image.place(x=150,y = 85)
        weatherlabel= weather_label.place(x=100,y=120) 
    except Exception as wack:
        messagebox.showerror("Error","Can't open the image")
        return
    return city
    

#Create a button to fetch the weather data
fetch_button = tk.Button(root, text= "Fetch Weather",font=("Arial", 10,"bold"),bd=3)
fetch_button.config(command=fetch_weather)
fetchbutton = fetch_button.place(x=50,y=45)

root.mainloop()

