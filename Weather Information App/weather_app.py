import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

API_KEY = os.getenv("Weather_API_KEY")

#Function to get weather information
def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q" : city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        #Send request to weather API
        response = requests.get(url,params=params)

        #Check for API errors
        response.raise_for_status()

        #Convert response to json
        data = response.json()

        #Get required weather information
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        print("\n==========WEATHER INFORMATION==========")
        print("City:" , city)
        print("Temperature:" , temperature, "°C")
        print("Condition:" , condition.title())
    except requests.exceptions.RequestException:
        print("\nUnable to get weather information.")
        print("Please check the city name or your internet connection.")

# Main program
print("============================================================================================================")
print("                         WEATHER INFORMATION APP")
print("============================================================================================================")
while True:
    city = input("\nEnter city name:  ")

    if not city:
        print("Please enter a city name.")
        continue

    get_weather(city)

    choice = input("\nSearch another city? (y/n): ").lower()


    if choice != "y":
        print("\nThank you for using Weather Information App!")
        break


