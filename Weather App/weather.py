import requests

api_key = '56a1b3d2cce54f496b845c803279658e'

city_name = input("Enter city: ")

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&APPID={api_key}")

if response.json()['cod'] == '404':
    print("No City Found")
else:
    weather_condition = response.json()['weather'][0]['main']
    temperature = round(response.json()['main']['temp'])

    print(f"The weather in {city_name} is: {weather_condition}")
    print(f"The temperature in {city_name} is: {temperature}ºF")
