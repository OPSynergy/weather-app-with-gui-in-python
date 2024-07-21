import tkinter as tk
import requests
from tkinter import messagebox

root = tk.Tk()
root.title("Weather App")
root.geometry("500x600")
root.config(bg="black")

def fetch_weather():
    city = entry.get().capitalize()
    api_key = '2491a218721fcc91d4c9b5857e182cc9'
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"
    
    try:
        geo_response = requests.get(geo_url)

        if geo_response.status_code == 200:

            geo_data = geo_response.json()

            for i in geo_data:
                
                latitude = i['lat']
                longitude = i['lon']
                location_name = i['name']

            weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"

            weather_response = requests.get(weather_url)

            if weather_response.status_code == 200:

                weather_data = weather_response.json()

                temperature = str(int(weather_data['main']['temp']) - 270)
                weather_info = f"Temperature : {temperature}\nLocation : {location_name}\nLatitude : {latitude}\nLongitude : {longitude}\nWeather : {weather_data['weather'][0]['description'].capitalize()}"
                
                tk.messagebox.showinfo("Weather Info", weather_info)
                
            else:
                
                tk.messagebox.showerror("Error", f"City not found: {city}")

    except requests.exceptions.RequestException as e:
        tk.messagebox.showerror("Error", f"Failed to fetch weather data: {str(e)}")


label = tk.Label(root, text="Weather App", font=('Times New Roman', 40, "bold"), fg='#00ff00', bg='black')
label.pack()

l1 = tk.Label(root, text="\n Enter City For Weather Info : ", font=('calibri', 20, "italic"), fg='#00ff00', bg='black')
l1.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Show Info", background="cyan", fg="black", relief="raised", command=fetch_weather)
button.pack(pady=10)

def exit_app():
    root.destroy()

b2 = tk.Button(root, text="Exit App", background="red", fg="black", relief="raised", command=exit_app)
b2.pack(pady=10)

root.mainloop()