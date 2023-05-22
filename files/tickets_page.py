from tkinter import *
from tkinter import ttk
from tkcalendar import *
from datetime import datetime

import tickets_api
from city_codes import get_city_code


class TicketsPage(Frame):
    """
    Страница выбора билетов для перелета. Наследуется от класса Frame.
    """

    def __init__(self, parent, controller):
        """
        Инициализация страницы билетов.
        """
        Frame.__init__(self, parent)
        self.controller = controller

        # Создание и размещение элементов на странице
        label = Label(self, text="Enter ticket details", font=("Verdana", "22", "bold"))
        label.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)

        # Метка и поле ввода для города вылета
        departure_city_label = ttk.Label(self, text='Departure city', font=("Verdana", "14"))
        departure_city_label.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)

        cities = ["Уфа", "Москва", "Санкт-Петербург", "Казань"]
        self.departure_city_combobox = ttk.Combobox(self, width=12, values=cities, font=("Verdana", "12"))
        self.departure_city_combobox.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Метка и поле ввода для города назначения
        destination_city_label = ttk.Label(self, text='Destination city', font=("Verdana", "14"))
        destination_city_label.grid(row=2, column=0, ipadx=6, ipady=6, padx=10, pady=20)

        self.destination_city_combobox = ttk.Combobox(self, width=12, values=cities, font=("Verdana", "12"))
        self.destination_city_combobox.grid(row=2, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Метка и поле ввода для даты вылета
        when_date_label = ttk.Label(self, text='Date of departure', font=("Verdana", "14"))
        when_date_label.grid(row=3, column=0, ipadx=6, ipady=6, padx=10, pady=20)

        self.when_date_entry = DateEntry(self, width=12, foreground='white', font=("Verdana", "12"), state="readonly")
        self.when_date_entry.grid(row=3, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Метка и поле ввода для даты возврата
        back_date_label = ttk.Label(self, text='Return date', font=("Verdana", "14"))
        back_date_label.grid(row=4, column=0, ipadx=6, ipady=6, padx=10, pady=20)

        self.back_date_entry = DateEntry(self, width=12, foreground='white', font=("Verdana", "12"), state="readonly")
        self.back_date_entry.grid(row=4, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Метка и поле ввода для количества пассажиров
        passenger_number_label = ttk.Label(self, text='Number of passengers', font=("Verdana", "14"))
        passenger_number_label.grid(row=5, column=0, ipadx=6, ipady=6, padx=10, pady=20)

        numbers = ["1", "2", "3"]
        self.passenger_number_combobox = ttk.Combobox(self, width=12, values=numbers, font=("Verdana", "12"))
        self.passenger_number_combobox.grid(row=5, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Метка и поле ввода для максимальной цены
        max_tickets_price_label = ttk.Label(self, text='Maximum price', font=("Verdana", "14"))
        max_tickets_price_label.grid(row=6, column=0, ipadx=6, ipady=6, padx=10, pady=20)

        self.max_tickets_price_combobox = ttk.Spinbox(self, width=12, from_=1000.0, to=10000.0, increment=500,  font=("Verdana", "12"))
        self.max_tickets_price_combobox.grid(row=6, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Переход на следующую страницу
        first_button = Button(self, foreground='White', font=("Verdana", "10"), bg='#FF9640', text='Next step',
                              padx=20, pady=10,
                              command=lambda: [
                                  self.on_click_button(),
                                  self.controller.set_dates(self.get_when_date(), self.get_back_date()),
                                  self.controller.frames["HotelsPage"].update_dates(self.get_when_date(),
                                                                                    self.get_back_date()),
                                  self.controller.frames["HotelsPage"].set_guests(self.get_passenger_number()),
                                  self.controller.show_frame("HotelsPage", self.destination_city_combobox.get())
                              ])
        first_button.grid(row=7, column=1, ipadx=6, ipady=6, pady=10)

    def get_departure_city(self):
        """
        Получение кода города вылета.
        """
        departure_city = get_city_code(self.departure_city_combobox.get())
        return departure_city

    def get_destination_city(self):
        """
        Получение кода города назначения.
        """
        destination_city = get_city_code(self.destination_city_combobox.get())
        return destination_city

    def get_when_date(self):
        """
        Получение даты вылета.
        """
        when_date = self.when_date_entry.get()
        when_date_obj = datetime.strptime(when_date, "%m/%d/%y")
        formatted_date_str = when_date_obj.strftime("%Y-%m-%d")
        return formatted_date_str

    def get_back_date(self):
        """
        Получение даты возврата.
        """
        back_date = self.back_date_entry.get()
        back_date_obj = datetime.strptime(back_date, "%m/%d/%y")
        formatted_date_str = back_date_obj.strftime("%Y-%m-%d")
        return formatted_date_str

    def get_passenger_number(self):
        """
        Получение количества пассажиров.
        """
        return self.passenger_number_combobox.get()

    def get_max_tickets_price(self):
        """
        Получение максимальной цены билета.
        """
        return self.max_tickets_price_combobox.get()

    def on_click_button(self):
        """
        Функция, выполняемая при нажатии кнопки.
        """
        origin = self.get_departure_city()
        destination = self.get_destination_city()
        departure_date = self.get_when_date()
        return_date = self.get_back_date()
        adults = self.get_passenger_number()
        tickets = tickets_api.send_data(origin, destination, departure_date, return_date, adults)
        max_tickets_price = self.get_max_tickets_price()
        self.controller.set_max_tickets_price(max_tickets_price)
        self.controller.frames["FullInfoPage"].update_flights_info(tickets)
        self.controller.show_frame("FullInfoPage")
