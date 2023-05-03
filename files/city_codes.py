import json
import requests


# функция, которая будет получать код города по его названию
def get_city_code(city_name):
    url = f"https://api.travelpayouts.com/data/ru/cities.json"
    response = requests.get(url)
    cities = json.loads(response.text)
    for city in cities:
        if city["name"] == city_name:
            return city["code"]

def change_city_code(city_name):
    url = f"https://api.travelpayouts.com/data/ru/cities.json"
    response = requests.get(url)
    cities = json.loads(response.text)
    for city in cities:
        if city["name"] == city_name:
            return city["name_translations"]["en"]