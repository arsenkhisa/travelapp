from tkinter import *
from tkinter import ttk

class FullInfoPage(Frame):
    """
    Класс страницы полной информации.
    """
    def __init__(self, parent, controller):
        """
        Инициализация страницы полной информации.
        :param parent: родительский виджет.
        :param controller: контроллер, управляющий страницами.
        """
        super().__init__(parent)

        self.controller = controller

        # Инициализация списков полетов, отелей и событий и их индексов
        self.flights = []
        self.flight_index = 0
        self.hotels = []
        self.hotels_index = 0

        # Создание и размещение виджетов на странице
        label = Label(self, text="Full Info", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.info_text = Text(self, wrap=WORD)
        self.info_text.pack(expand=True, fill=BOTH)

        prevFlight_button = ttk.Button(self, text="Previous Flight", command=self.show_previous_flight)
        prevFlight_button.pack(side="left")

        nextFlight_button = ttk.Button(self, text="Next Flight", command=self.show_next_flight)
        nextFlight_button.pack(side="right")

        prevHotel_button = ttk.Button(self, text="Previous Hotel", command=self.show_previous_hotel)
        prevHotel_button.pack(side="left")

        nextHotel_button = ttk.Button(self, text="Next Hotel", command=self.show_next_hotel)
        nextHotel_button.pack(side="right")

        prevEvent_button = ttk.Button(self, text="Previous event", command=self.show_previous_event)
        prevEvent_button.pack(side="left")

        nextEvent_button = ttk.Button(self, text="Next event", command=self.show_next_event)
        nextEvent_button.pack(side="right")

        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_frame("TicketsPage"))
        back_button.pack(side="bottom")

    def update_flights_info(self, flights):
        """
        Обновление информации о полетах.
        :param flights: список полетов.
        """
        self.flights = [flight for flight in flights if flight['price'] <= float(self.controller.max_tickets_price)]
        self.flight_index = 0
        self.show_flight_info()

    def update_hotels_info(self, hotels):
        """
        Обновление информации об отелях.
        :param hotels: список отелей.
        """
        self.hotels = [hotel for hotel in hotels if hotel['avgPrice'] <= int(self.controller.max_hotels_price)]
        self.hotels_index = 0
        self.show_hotels_info()

    def update_events_info(self, events):
        """
        Обновление информации о событиях.
        :param events: список событий.
        """
        self.events = events
        self.events_index = 0
        self.show_events_info()

    def show_flight_info(self):
        """
        Отображение информации о билетах.
        :param flights: список билетов.
        """
        self.info_text.delete(1.0, END)
        if self.flights:
            flight = self.flights[self.flight_index]
            info = f"""
Flight tickets:
---------------
Airline: {flight['airline']}
Departure: {flight['departure']}
From: {flight['from']}
To: {flight['to']}
Price: {flight['price']}
"""
            self.info_text.insert(INSERT, info)

    def show_hotels_info(self):
        """
        Отображение информации об отелях.
        :param hotels: список отелей.
        """
        self.info_text.delete(1.0, END)
        if self.flights:
            hotel = self.hotels[self.hotels_index]
            info = f"""
Hotel rooms:
---------------
Hotel name: {hotel['hotelName']}
Stars: {hotel['stars']}
Check In: {hotel['checkIn']}
Check Out: {hotel['checkOut']}
Average price: {hotel['avgPrice']}
"""
            self.info_text.insert(INSERT, info)

    def show_events_info(self):
        """
        Отображение информации о мероприятиях.
        :param events: список мероприятий.
        """
        self.info_text.delete(1.0, END)
        if self.events:
            event = self.events[self.events_index]
            info = f"""
Events:
--------------
Event name: {event['eventName']}
Description: {event['description']}
Price: {event['price']}
Movement type: {event['movementType']}
Duration: {event['duration']}
"""
            self.info_text.insert(INSERT, info)

    def show_previous_flight(self):
        """
        Отображение прошлой информации о билетах.
        """
        if self.flight_index > 0:
            self.flight_index -= 1
            self.show_flight_info()

    def show_next_flight(self):
        """
        Отображение новой информации о билетах.
        """
        if self.flight_index < len(self.flights) - 1:
            self.flight_index += 1
            self.show_flight_info()

    def show_previous_hotel(self):
        """
        Отображение прошлой информации об отелях.
        """
        if self.hotels_index > 0:
            self.hotels_index -= 1
            self.show_hotels_info()

    def show_next_hotel(self):
        """
        Отображение новой информации об отелях.
        """
        if self.hotels_index < len(self.hotels) - 1:
            self.hotels_index += 1
            self.show_hotels_info()

    def show_previous_event(self):
        """
        Отображение прошлой информации о мероприятиях.
        """
        if self.events_index > 0:
            self.events_index -= 1
            self.show_events_info()

    def show_next_event(self):
        """
        Отображение новой информации о мероприятиях.
        """
        if self.events_index < len(self.events) - 1:
            self.events_index += 1
            self.show_events_info()