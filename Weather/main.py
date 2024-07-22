import requests

API_Key = "87cb20bee0648fcb5fa65fca154cebb2"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name (e.g., Chicago, IL, US): ")
request_url = f"{BASE_URL}?q={city}&appid={API_Key}&units=imperial"
response = requests.get(request_url)

# If response was successful
if response.status_code == 200:
    data = response.json()
    #get the weather key
    weather = data['weather'][0]['description']
    print(weather)
    #Accessed the main and temp key
    temperature = round(data["main"]["temp"])

    print("Weather:", weather)
    print("Temperature:", temperature)
else:
    print("An error occurred.")
