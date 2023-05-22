from tkinter import *
from tkinter import ttk
from tkcalendar import *

import event_api
from city_codes import change_city_code
from event_num import change_event_type


class EventsPage(Frame):
    """
    Класс страницы событий.
    """
    def __init__(self, parent, controller, destination_city=None):
        """
        Инициализация страницы событий.
        :param parent: родительский виджет.
        :param controller: контроллер, управляющий страницами.
        :param destination_city: город назначения.
        """
        super().__init__(parent)
        self.controller = controller
        self.destination_city = StringVar(value=destination_city)
        self.create_widgets()

    def update_destination_city(self, destination_city):
        """
        Обновление города назначения.
        :param destination_city: город назначения.
        """
        self.destination_city.set(destination_city)

    def update_event_date(self, arrival_date):
        """
        Обновление даты события.
        :param arrival_date: дата события.
        """
        self.date_event_entry.set_date(arrival_date)

    def create_widgets(self):
        """
        Создание виджетов на странице.
        """
        # Пометка с вводом деталей мероприятий
        label = Label(self, text="Enter event details", font=("Verdana", "22", "bold"))
        label.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)

        # Метки и поля ввода для даты мероприятия
        event_date_label = ttk.Label(self, text='City of the event', font=("Verdana", "14"))
        event_date_label.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)

        self.date_event_entry = DateEntry(self, width=12, foreground='white', font=("Verdana", "12"))
        self.date_event_entry.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Метка и поле ввода для города
        cities = ["Ufa", "Moscow", "St.Petersburg", "Kazan"]
        city_combobox = ttk.Combobox(self, width=12, values=cities, font=("Verdana", "12"),
                                     textvariable=self.destination_city)
        city_combobox.set(self.destination_city)
        city_combobox.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Метки и поля ввода для типа мероприятия
        events = ["Экскурсия", "Активный отдых", "Трансфер", "Мастер-класс", "Билет в музей или на мероприятие"]
        type_of_event_label = ttk.Label(self, text='Choose type of the event', font=("Verdana", "14"))
        type_of_event_label.grid(row=2, column=0, ipadx=6, ipady=6, padx=5, pady=5)
        self.type_of_event_combobox = ttk.Combobox(self, width=12, font=("Verdana", "12"), values=events)
        self.type_of_event_combobox.grid(row=2, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        # Кнопки для перехода к следующему шагу и возврата назад
        first_button = Button(self, foreground='White', font=("Verdana", "10"), bg='#FF9640', text='See results',
                              padx=20, pady=10,
                              command=lambda: [self.on_click_button(),
                                               self.controller.show_frame("FullInfoPage")])
        first_button.grid(row=3, column=1, ipadx=6, ipady=6, pady=10)
        second_button = Button(self, foreground='White', font=("Verdana", "10"), bg='#FF9640', text='Back',
                               padx=20, pady=10, command=lambda: self.controller.show_frame("HotelsPage"))
        second_button.grid(row=3, column=0, ipadx=6, ipady=6, pady=10)

    def on_click_button(self):
        """
        Обработка нажатия на кнопку.
        Вызывает поиск событий и обновление информации на странице полной информации.
        """
        destination = change_city_code(self.destination_city.get())
        event_type = change_event_type(self.type_of_event_combobox.get())
        event_api.search_events(destination, event_type)
        events = event_api.search_events(destination, event_type)
        self.controller.frames["FullInfoPage"].update_events_info(events)
        self.controller.show_frame("FullInfoPage")