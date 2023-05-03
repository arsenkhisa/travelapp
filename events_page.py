from tkinter import *
from tkinter import ttk
from tkcalendar import *

import event_api
from city_codes import change_city_code
from event_num import change_event_type


class EventsPage(Frame):
    def __init__(self, parent, controller, destination_city=None):
        self.destination_city = StringVar()
        Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()
    def update_destination_city(self, destination_city):
        self.destination_city.set(destination_city)
    def create_widgets(self):
        label = Label(self, text="Enter event details", font=("Verdana", "22", "bold"))
        label.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)
        event_date_label = ttk.Label(self, text='Date of the event', font=("Verdana", "14"))
        event_date_label.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)
        cities = ["Ufa", "Moscow", "St.Petersburg", "Kazan"]
        city_combobox = ttk.Combobox(self, width=12, values=cities, font=("Verdana", "12"),
                                     textvariable=self.destination_city)
        city_combobox.set(self.destination_city)
        city_combobox.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        type_of_event_label = ttk.Label(self, text='Choose type of the event', font=("Verdana", "14"))
        type_of_event_label.grid(row=2, column=0, ipadx=6, ipady=6, padx=5, pady=5)
        self.date_event_entry = DateEntry(self, width=12, foreground='white', font=("Verdana", "12"))
        self.date_event_entry.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        events = ["Экскурсия", "Активный отдых", "Трансфер","Мастер-класс", "Билет в музей или на мероприятие"]
        self.type_of_event_combobox = ttk.Combobox(self, width=12, font=("Verdana", "12"), values=events)
        self.type_of_event_combobox.grid(row=2, column=1, ipadx=6, ipady=6, padx=5, pady=5)
        first_button = Button(self, foreground='White', font=("Verdana", "10"), bg='#FF9640', text='See results',
                              padx=20, pady=10,
                              command=lambda: [self.on_click_button(),
                                               self.controller.show_frame("Results")])
        first_button.grid(row=3, column=1, ipadx=6, ipady=6, pady=10)
        second_button = Button(self, foreground='White', font=("Verdana", "10"), bg='#FF9640', text='Back',
                               padx=20, pady=10, command=lambda: self.controller.show_frame("HotelsPage"))
        second_button.grid(row=3, column=0, ipadx=6, ipady=6, pady=10)

    def on_click_button(self):
        destination = change_city_code(self.destination_city.get())
        event_type = change_event_type(self.type_of_event_combobox.get())
        event_api.search_events(destination, event_type)



