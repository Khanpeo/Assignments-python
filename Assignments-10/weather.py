import requests

city = input("Enter city: ")
api_key = "3adaeab6dff6a941088bff8c9f2eb152" 

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

# get info
temp_kelvin = data["main"]["temp"]
temp_celsius = temp_kelvin - 273.15
description = data["weather"][0]["description"]

print("Weather:", description)
print("Temperature:", round(temp_celsius, 2), "°C")