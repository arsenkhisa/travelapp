import webbrowser


def browse_results(departure_city, departure_date, destination_city, destination_date, passengers_num):
    """
    Функция для открытия браузера с результатами поиска билетов.

    :param departure_city: Город отправления.
    :param departure_date: Дата отправления.
    :param destination_city: Город назначения.
    :param destination_date: Дата прибытия.
    :param passengers_num: Количество пассажиров.
    """
    tickets = departure_city + departure_date + destination_city + destination_date + passengers_num
    webbrowser.open_new('https://www.aviasales.ru/search/' + tickets)
