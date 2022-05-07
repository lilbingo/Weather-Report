import requests

# Uses zipcode to get location information from get_location then sends data to get_weather
def get_zipcode():
    zipcode = input("Enter your zipcode: ")
    location = get_location(zipcode)
    get_weather(location)


# Gets latitude, longitude, city, and state from zipcode api and sends data back to get_zipcode
def get_location(zip: str) -> str:
    api_key = ""
    url = f"https://www.zipcodeapi.com/rest/{api_key}/info.json/{zip}/degrees"
    loc_json = requests.get(url).json()
    loc_data = [loc_json["lat"], loc_json["lng"], loc_json["city"], loc_json["state"]]
    return loc_data


# Gets weather data from openweathermap using location data from get_location
def get_weather(location: str):
    api_key = ""
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={location[0]}&lon={location[1]}' \
          f'&units=imperial&exclude=minutely&appid={api_key}'
    data = requests.get(url).json()
    print_weather(data, location[2], location[3])  


# Displays weather data received in get_weather
def print_weather(data: dict, city: str, state: str):
    print(f"\nYour location: {city.title()}, {state.upper()}")
    print(f'It is currently {data["current"]["temp"]} degrees '
          f'and feels like {data["current"]["feels_like"]} degrees.')
    print(f'Current conditions: {data["current"]["weather"][0]["description"]}')


if __name__ == '__main__':
    get_zipcode()
