from tkinter import *
from tkinter import ttk
from tkcalendar import *
from datetime import datetime

import tickets_api
from city_codes import get_city_code

class TicketsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Enter ticket details", font=("Verdana", "22", "bold"))
        label.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)
        departure_city_label = ttk.Label(self, text='Departure city', font=("Verdana", "14"))
        departure_city_label.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)
        destination_city_label = ttk.Label(self, text='Destination city', font=("Verdana", "14"))
        destination_city_label.grid(row=2, column=0, ipadx=6, ipady=6, padx=10, pady=20)
        when_date_label = ttk.Label(self, text='Date of departure', font=("Verdana", "14"))
        when_date_label.grid(row=3, column=0, ipadx=6, ipady=6, padx=10, pady=20)
        back_date_label = ttk.Label(self, text='Return date', font=("Verdana", "14"))
        back_date_label.grid(row=4, column=0, ipadx=6, ipady=6, padx=10, pady=20)
        passenger_number_label = ttk.Label(self, text='Number of passengers', font=("Verdana", "14"))
        passenger_number_label.grid(row=5, column=0, ipadx=6, ipady=6, padx=10, pady=20)
        cities = ["Уфа", "Москва", "Санкт-Петербург", "Казань"]
        departure_city_combobox = ttk.Combobox(self, width=12, values=cities, font=("Verdana", "12"))
        departure_city_combobox.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        def get_departure_city():
            departure_city = get_city_code(departure_city_combobox.get())
            return departure_city
        destination_city_combobox = ttk.Combobox(self, width=12, values=cities, font=("Verdana", "12"))
        destination_city_combobox.grid(row=2, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        def get_destination_city():
            destination_city = get_city_code(destination_city_combobox.get())
            return destination_city
        when_date_entry = DateEntry(self, width=12, foreground='white', font=("Verdana", "12"), state="readonly")
        when_date_entry.grid(row=3, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        def get_when_date():
            when_date = when_date_entry.get()
            when_date_obj = datetime.strptime(when_date, "%m/%d/%y")
            formatted_date_str = when_date_obj.strftime("%Y-%m-%d")
            return formatted_date_str
        back_date_entry = DateEntry(self, width=12, foreground='white', font=("Verdana", "12"), state="readonly")
        back_date_entry.grid(row=4, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        def get_back_date():
            back_date = back_date_entry.get()
            back_date_obj = datetime.strptime(back_date, "%m/%d/%y")
            formatted_date_str = back_date_obj.strftime("%Y-%m-%d")
            return formatted_date_str
        numbers = ["1", "2", "3"]
        passenger_number_combobox = ttk.Combobox(self, width=12, values=numbers, font=("Verdana", "12"))
        passenger_number_combobox.grid(row=5, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        def get_passenger_number():
            return passenger_number_combobox.get()
        def on_click_button():
            origin = get_departure_city()
            destination = get_destination_city()
            departure_date = get_when_date()
            return_date = get_back_date()
            adults = get_passenger_number()
            tickets_api.send_data(origin, destination, departure_date, return_date, adults)
            controller.show_frame("HotelsPage", get_destination_city())
            controller.frames["HotelsPage"].update_dates(get_when_date(), get_back_date())
        first_button = Button(self, foreground='White', font=("Verdana", "10"), bg='#FF9640', text='Next step',
                              padx=20, pady=10,
                              command=lambda: [on_click_button(),
                                               controller.set_dates(get_when_date(), get_back_date()),
                                               controller.show_frame("HotelsPage", destination_city_combobox.get())])
        first_button.grid(row=6, column=1, ipadx=6, ipady=6, pady=10)
