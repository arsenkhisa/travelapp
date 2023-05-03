import json
import requests


# функция, которая будет получать код города по его названию
def change_event_type(event_type):
    if event_type == "Экскурсия":
        return 1
    if event_type == "Активный отдых":
        return 2
    if event_type == "Трансфер":
        return 5
    if event_type == "Мастер-класс":
        return 7
    if event_type == "Билет в музей или на мероприятие":
        return 8