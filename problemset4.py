#It used the APIXU API for Weather (seoyeon, Park)
#For API Call
import requests
import matplotlib.pyplot as plt

# API key and base URL configuration
API_KEY = '724b9d38864a9a7537f1a8ce0726bb77'
BASE_URL = 'http://api.weatherstack.com/current'

# City to query
city = 'Seoul'

# Construct API request URL
params = {
    'access_key': API_KEY,
    'query': city
}

# Make API call and process the response
response = requests.get(BASE_URL, params=params)
data = response.json()

# Check if the response is valid
if 'current' in data:
    current_weather = data['current']

    # Extract useful information
    temperature = current_weather['temperature']
    feels_like = current_weather['feelslike']
    humidity = current_weather['humidity']
    wind_speed = current_weather['wind_speed']

    # Print the results
    print(f"city: {city}")
    print(f"current temperature: {temperature}°C")
    print(f"apparent temperature: {feels_like}°C")
    print(f"humidity: {humidity}%")
    print(f"wind speed: {wind_speed} km/h")

   # Visualization: Compare actual temperature vs. feels like temperature
    labels = ['Actual Temperature', 'Feels Like']
    values = [temperature, feels_like]

    plt.bar(labels, values, color=['skyblue', 'lightcoral'])
    plt.title(f'Temperature Comparison in {city}')
    plt.ylabel('Temperature (°C)')
    plt.show()

else:
    print(f"Failed to retrieve data: {data.get('error', {}).get('info', 'Unknown error')}")
