
import json
import requests

def search_events(destination, type):
    print('\n', destination, '\n', type, '\n')
    url = "https://experience.tripster.ru/api/partners/%3Cpartner_name%3E/experiences/?"
    params = {
        "city__name_en": destination,
        "exp_format": type,
    }
    response = requests.get(url, params=params)

    data = json.loads(response.text)
    with open("events_api.json", "w+", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    with open('events_api.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        print(json.dumps(data))