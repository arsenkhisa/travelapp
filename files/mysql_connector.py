import requests
import mysql.connector

# Коды городов
codes = ['MOW', 'LED', 'UFA', 'KZN', 'VVO']

# Даты для обновления данных
dates = ['2023-05-16', '2023-05-17', '2023-05-18', '2023-05-19', '2023-05-20', '2023-05-21',
         '2023-05-22', '2023-05-22', '2023-05-23', '2023-05-24', '2023-05-25', '2023-05-26',
         '2023-05-27', '2023-05-28', '2023-05-29', '2023-05-30', '2023-05-31', '2023-06-01',
         '2023-06-02', '2023-06-03', '2023-06-04', '2023-06-05', '2023-06-06', '2023-06-07',
         '2023-06-08', '2023-06-09', '2023-06-10', '2023-06-11', '2023-06-12', '2023-06-13']

# Типы мероприятий для обновления данных
types = [1, 2, 5, 7, 8]

# Установка соединения с базой данных MySQL
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="TheCloudKA2004",
    database="app"
)

# Создание курсора для выполнения запросов SQL
mycursor = mydb.cursor()

def events_update():
    """
    Обновление мероприятий в базе данных.

    Функция обходит каждый город и каждый тип мероприятия,
    делает запрос к API и обновляет данные о мероприятиях в базе данных.
    """
    # Проход по каждому городу
    for city in range(len(codes)):
        # Проход по каждому типу мероприятия
        for event in range(len(types)):
            # URL API для запроса данных
            url = "https://experience.tripster.ru/api/partners/%3Cpartner_name%3E/experiences/?"
            params = {
                "city__iata": codes[city],
                "exp_format": types[event],
            }
            # Выполнение GET запроса к API
            response = requests.get(url, params=params)
            data = response.json()
            # Если есть результаты, обновляем данные в базе данных
            if len(data['results']) != 0 and len(data) != 0:
                # Проход по каждому результату
                for i in range(len(data['results'])):
                    # SQL запрос для вставки данных в таблицу "events"
                    sql = "INSERT INTO events (city, title, tagline, event_type, " \
                          "duration, price, url)" \
                          " VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (data['results'][i]['city']['name_ru'], data['results'][i]['title'],
                           data['results'][i]['tagline'], data['results'][i]['type'],
                           data['results'][i]['duration'], data['results'][i]['price']['value'],
                           data['results'][i]['url'])
                    # Выполнение SQL запроса
                    mycursor.execute(sql, val)
                    # Подтверждение изменений в базе данных
                    mydb.commit()

# Вызов функции для обновления данных о мероприятиях
events_update()

# Закрытие соединения с базой данных
mydb.close()
