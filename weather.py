from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def getWeather(city = "Kansas City"):
  request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial"
  weatherData = requests.get(request_url).json()
  return weatherData

if __name__ == "__main__":
  print("\n*** Get Weather Conditions ***\n")

  city = input("\nPlease enter a city name:\n")

  # Check for empty strings
  if not bool(city.strip()):
    city = "Kansas City"

  weatherData = getWeather(city)

  print("\n")
  pprint(weatherData)


