"""
Programmer: Daniel Lyles 
Data : April 1, 2022
Purpose: Creating a automation system that uses a free API to get Weather Reports 
on Different Citys 
"""
import requests 

API_KEY = "e93c1adb8f8d162f9c0ce9c14acf9402"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
#
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = round(data["main"]["temp"] -273.15,2)
    print("Weather:",weather)
    print("Temperature:", temperature, "celsius")
else:
    print("an error.")