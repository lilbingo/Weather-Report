import requests

"""Get the user's latitude and longitude based on their zipcode using the zipcodeapi"""
""" NOTE: You must enter your own API key in api_key. Please see README"""
def get_location(zip: str) -> str:
    api_key = ""
    url = f"https://www.zipcodeapi.com/rest/{api_key}/info.json/{zip}/degrees"
    loc_json = requests.get(url).json()
    loc_data = [loc_json["lat"], loc_json["lng"], loc_json["city"], loc_json["state"]]
    return loc_data
