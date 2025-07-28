import requests

API_KEY = "YOUR_OPENWEATHER_KEY"
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

data = requests.get(url).json()
print(data)
