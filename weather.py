import requests
from location import get_location

def get_zipcode():
    zipcode = input("Enter your zipcode: ")
    location = get_location(zipcode)
    get_weather(location)


"""NOTE: You must get your own api key. See README"""
def get_weather(location: str):
    api_key = ""
    # location[0] = latitude 
    # location[1] = longitude
    # location[2] = city 
    # location[3] = state
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={location[0]}&lon={location[1]}' \
          f'&units=imperial&exclude=minutely&appid={api_key}'
    data = requests.get(url).json()
    print_weather(data, location[2], location[3])  


def print_weather(data: dict, city: str, state: str):
    print(f"\nYour location: {city.title()}, {state.upper()}")
    print(f'It is currently {data["current"]["temp"]} degrees '
          f'and feels like {data["current"]["feels_like"]} degrees.')
    print(f'Current conditions: {data["current"]["weather"][0]["description"]}')


if __name__ == '__main__':
    get_zipcode()
