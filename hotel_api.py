import json
import requests


def search_hotel(destination, departure_date, return_date, adults):
    print('\n', destination, '\n', departure_date, '\n', return_date, '\n', adults,
          '\n')
    url = "https://engine.hotellook.com/api/v2/cache.json?"
    params = {
        "location": destination,
        "currency": "rub",
        "checkIn": departure_date,
        "checkOut": return_date,
        "currency": "rub",
        "adults": adults,
        "limit": 100
    }
    response = requests.get(url, params=params)

    data = json.loads(response.text)
    with open("hotel_api.json", "w+") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    with open('hotel_api.json', 'r+') as f:
        data = json.load(f)
        print(json.dumps(data))





