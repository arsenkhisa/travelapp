from tkinter import *
from tkinter import ttk
from tkcalendar import *
from datetime import datetime

import hotel_api
from city_codes import get_city_code

class HotelsPage(Frame):
    """
    Окно с информацией о бронировании отеля.
    """
    def __init__(self, parent, controller):
        """
        Инициализация класса HotelsPage.

        Args:
            parent: родительский виджет.
            controller: контроллер приложения.
        """
        Frame.__init__(self, parent)
        self.controller = controller
        self.destination_city = StringVar()
        self.create_widgets()

    def update_destination_city(self, destination_city):
        """
        Обновить город назначения.

        Args:
            destination_city (str): новый город назначения.
        """
        self.destination_city.set(destination_city)

    def set_guests(self, guests):
        """
        Установить количество гостей.

        Args:
            guests (int): новое количество гостей.
        """
        self.guest_number_combobox.set(guests)

    def create_widgets(self):
        """
        Создание виджетов для страницы бронирования отеля.
        """
        # Пометка с вводом деталей отеля
        label = Label(self, text="Enter hotel details", font=("Verdana", "22", "bold"))
        label.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)

        # Метка и поле ввода для города
        city_name_label = ttk.Label(self, text='Сity', font=("Verdana", "14"))
        city_name_label.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)
        cities = ["Ufa", "Moscow", "St.Petersburg", "Kazan"]
        city_combobox = ttk.Combobox(self, width=12, values=cities, font=("Verdana", "12"),
                                     textvariable=self.destination_city)
        city_combobox.set(self.destination_city)
        city_combobox.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Метки и поля ввода для дат прибытия и отъезда
        arrival_date_label = ttk.Label(self, text='Date of arrival', font=("Verdana", "14"))
        arrival_date_label.grid(row=2, column=0, ipadx=6, ipady=6, padx=10, pady=20)
        self.arrival_date_entry = DateEntry(self, width=12, foreground='white', font=("Verdana", "12"))
        self.arrival_date_entry.grid(row=2, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        departure_date_label = ttk.Label(self, text='Date of departure', font=("Verdana", "14"))
        departure_date_label.grid(row=3, column=0, ipadx=6, ipady=6, padx=10, pady=20)
        self.departure_date_entry = DateEntry(self, width=12, foreground='white', font=("Verdana", "12"))
        self.departure_date_entry.grid(row=3, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Метка и поле ввода для количества гостей
        guest_number_label = ttk.Label(self, text='Number of guests', font=("Verdana", "14"))
        guest_number_label.grid(row=4, column=0, ipadx=6, ipady=6, padx=10, pady=20)
        guests = ["1", "2", "3", "4", "5"]
        self.guest_number_combobox = ttk.Combobox(self, width=12, values=guests, font=("Verdana", "12"))
        self.guest_number_combobox.grid(row=4, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Метка и поле ввода для максимальной цены
        max_hotels_price_label = ttk.Label(self, text='Maximum price', font=("Verdana", "14"))
        max_hotels_price_label.grid(row=5, column=0, ipadx=6, ipady=6, padx=10, pady=20)

        self.max_hotels_price_combobox = ttk.Spinbox(self, width=12, from_=1000.0, to=10000.0, increment=500,
                                         font=("Verdana", "12"))
        self.max_hotels_price_combobox.grid(row=5, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Кнопки для перехода к следующему шагу и возврата назад
        first_button = Button(self, foreground='White', font=("Verdana", "10"), bg='#FF9640', text='Next step',
                              padx=20, pady=10,
                              command=lambda: [self.on_click_button(),
                                               self.controller.show_frame("EventsPage", self.destination_city.get())])
        first_button.grid(row=6, column=1, ipadx=6, ipady=6, pady=10)
        second_button = Button(self, foreground='White', font=("Verdana", "10"), bg='#FF9640', text='Back',
                               padx=20, pady=10, command=lambda: self.controller.show_frame("TicketsPage"))
        second_button.grid(row=6, column=0, ipadx=6, ipady=6, pady=10)

    def get_max_hotels_price(self):
        return self.max_hotels_price_combobox.get()


    def update_dates(self, when_date_str, back_date_str):
        """
        Обновить даты прибытия и отъезда.

        Args:
            when_date_str (str): дата прибытия.
            back_date_str (str): дата отъезда.
        """
        when_date_obj = datetime.strptime(when_date_str, "%Y-%m-%d")
        back_date_obj = datetime.strptime(back_date_str, "%Y-%m-%d")
        self.arrival_date_entry.set_date(when_date_obj)
        self.departure_date_entry.set_date(back_date_obj)

    def on_click_button(self):
        """
        Выполнить при нажатии кнопки.
        """
        destination = get_city_code(self.destination_city.get())
        departure_date = self.arrival_date_entry.get_date().strftime("%Y-%m-%d")
        return_date = self.departure_date_entry.get_date().strftime("%Y-%m-%d")
        adults = int(self.guest_number_combobox.get())
        hotels = hotel_api.search_hotels(destination, departure_date, return_date, adults)
        max_hotels_price = self.get_max_hotels_price()
        self.controller.set_max_hotels_price(max_hotels_price)
        self.controller.frames["FullInfoPage"].update_hotels_info(hotels)
        self.controller.show_frame("FullInfoPage")
