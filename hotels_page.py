from tkinter import *
from tkinter import ttk
from tkcalendar import *
from datetime import datetime

import hotel_api
from city_codes import get_city_code

class HotelsPage(Frame):
    def __init__(self, parent, controller, destination_city=None):
        self.destination_city = StringVar()
        Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()
    def update_destination_city(self, destination_city):
        self.destination_city.set(destination_city)
    def create_widgets(self):
        label = Label(self, text="Enter hotel details", font=("Verdana", "22", "bold"))
        label.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)
        city_name_label = ttk.Label(self, text='Сity', font=("Verdana", "14"))
        city_name_label.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)
        arrival_date_label = ttk.Label(self, text='Date of arrival', font=("Verdana", "14"))
        arrival_date_label.grid(row=2, column=0, ipadx=6, ipady=6, padx=10, pady=20)
        departure_date_label = ttk.Label(self, text='Date of departure', font=("Verdana", "14"))
        departure_date_label.grid(row=3, column=0, ipadx=6, ipady=6, padx=10, pady=20)
        guest_number_label = ttk.Label(self, text='Number of guests', font=("Verdana", "14"))
        guest_number_label.grid(row=4, column=0, ipadx=6, ipady=6, padx=10, pady=20)
        cities = ["Ufa", "Moscow", "St.Petersburg", "Kazan"]
        city_combobox = ttk.Combobox(self, width=12, values=cities, font=("Verdana", "12"), textvariable=self.destination_city)
        city_combobox.set(self.destination_city)
        city_combobox.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        self.arrival_date_entry = DateEntry(self, width=12, foreground='white', font=("Verdana", "12"))
        self.arrival_date_entry.grid(row=2, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        self.departure_date_entry = DateEntry(self, width=12, foreground='white', font=("Verdana", "12"))
        self.departure_date_entry.grid(row=3, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        guests = ["1", "2", "3", "4", "5"]
        self.guest_number_combobox = ttk.Combobox(self, width=12, values=guests, font=("Verdana", "12"))
        self.guest_number_combobox.grid(row=4, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        first_button = Button(self, foreground='White', font=("Verdana", "10"), bg='#FF9640', text='Next step',
                              padx=20, pady=10,
                              command=lambda: [self.on_click_button(),
                                               self.controller.show_frame("EventsPage", self.destination_city.get())])
        first_button.grid(row=5, column=1, ipadx=6, ipady=6, pady=10)
        second_button = Button(self, foreground='White', font=("Verdana", "10"), bg='#FF9640', text='Back',
                               padx=20, pady=10, command=lambda: self.controller.show_frame("TicketsPage"))
        second_button.grid(row=5, column=0, ipadx=6, ipady=6, pady=10)

    def update_dates(self, when_date_str, back_date_str):
        when_date_obj = datetime.strptime(when_date_str, "%Y-%m-%d")
        back_date_obj = datetime.strptime(back_date_str, "%Y-%m-%d")
        self.arrival_date_entry.set_date(when_date_obj)
        self.departure_date_entry.set_date(back_date_obj)

    def on_click_button(self):
        destination = get_city_code(self.destination_city.get())
        departure_date = self.arrival_date_entry.get_date().strftime("%Y-%m-%d")
        return_date = self.departure_date_entry.get_date().strftime("%Y-%m-%d")
        adults = int(self.guest_number_combobox.get())
        hotel_api.search_hotel(destination, departure_date, return_date, adults)

