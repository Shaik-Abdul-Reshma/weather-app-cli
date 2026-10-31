# Weather App CLI - Codtech Internship Task 2
# Intern ID: CITS9867 | Author: Shaik Abdul Reshma

import json
import urllib.request
import urllib.parse

def get_weather(city):
    try:
        # Encode city name
        city_encoded = urllib.parse.quote(city)
        url = f"https://wttr.in/{city_encoded}?format=j1"
        
        # Fetch data using built-in urllib (no pip needed)
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        current = data['current_condition'][0]
        nearest = data['nearest_area'][0]
        
        print("\n" + "="*40)
        print(f" Weather Report for {city.upper()} ")
        print("="*40)
        print(f"Location      : {nearest['areaName'][0]['value']}, {nearest['country'][0]['value']}")
        print(f"Temperature   : {current['temp_C']}°C / {current['temp_F']}°F")
        print(f"Condition     : {current['weatherDesc'][0]['value']}")
        print(f"Humidity      : {current['humidity']}%")
        print(f"Wind Speed    : {current['windspeedKmph']} km/h")
        print(f"Feels Like    : {current['FeelsLikeC']}°C")
        print("="*40 + "\n")
        
    except Exception as e:
        print(f"\nError: Could not fetch weather for '{city}'. Check city name or internet.")
        print(f"Details: {e}\n")

def main():
    print("=== CLI Weather App | CITS9867 ===")
    print("Type city name (e.g., Hyderabad, London)")
    print("Type 'exit' to quit\n")
    
    while True:
        city = input("Enter City Name: ").strip()
        if city.lower() == 'exit':
            print("Goodbye! Stay weather-aware!")
            break
        if city == "":
            print("Please enter a city name!")
            continue
        get_weather(city)

if __name__ == "__main__":
    main()
