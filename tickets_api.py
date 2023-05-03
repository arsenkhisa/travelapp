import requests
import json


def send_data(origin, destination, departure_date, return_date, adults):
    print('\n', origin, '\n', destination, '\n', departure_date, '\n', return_date, '\n', adults,
          '\n')
    url = "https://api.travelpayouts.com/v1/prices/calendar"
    params = {
        "origin": origin,
        "destination": destination,
        "departure_at": departure_date,
        "return_at": return_date,
        "currency": "rub",
        "token": "9570cd803e10001a719af1e9aba6835a",
        "adults": adults,
    }
    response = requests.get(url, params=params)

    data = json.loads(response.text)
    with open("data.json", "w+") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    with open('data.json', 'r+') as f:
        data = json.load(f)
        print(json.dumps(data))
