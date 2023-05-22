from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont
import configparser

from tickets_page import TicketsPage
from hotels_page import HotelsPage
from events_page import EventsPage
from settings_page import SettingsPage
from full_info_page import FullInfoPage

class App(Tk):
    """
    Основной класс приложения, наследуемый от Tk.
    Он создает главное окно и управляет навигацией между различными страницами.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализация главного окна.
        """
        Tk.__init__(self, *args, **kwargs)

        self.title("Tour app")  # название приложения
        self.title_font = tkfont.Font(family='Verdana', size=20)  # шрифт заголовка
        self.resizable(width=True, height=True)  # опция изменения размера окна
        self.geometry("900x570")  # начальные размеры окна

        # Создание главной рамки
        main_frame = ttk.Frame(self)
        main_frame.pack_propagate(False)
        main_frame.pack(side="top", fill="both", expand=True)

        # Словарь для хранения всех страниц
        self.frames = {}
        self.destination_city = None

        # Создание всех страниц
        self.create_frames(main_frame)

        # Показать начальную страницу
        self.show_frame("TicketsPage")

        # Создание кнопки для открытия окна настроек
        settings_button = ttk.Button(self, text="Settings", command=self.open_settings)
        settings_button.pack(side="bottom")


    def create_frames(self, main_frame):
        """
        Создает все страницы приложения.
        """
        for page in (TicketsPage, HotelsPage, EventsPage, FullInfoPage):
            frame = page(parent=main_frame, controller=self)
            page_name = page.__name__
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def set_dates(self, when_date, back_date):
        """
        Устанавливает даты путешествия.
        """
        self.when_date = when_date
        self.back_date = back_date

    def open_settings(self):
        """
        Открывает окно настроек.
        """
        SettingsPage(self)

    def change_theme(self):
        """
        Меняет тему приложения.
        """
        config = configparser.ConfigParser()
        config.read('settings.ini')
        current_theme = config.get('theme', 'current_theme')

        # Меняет тему на светлую или темную в зависимости от текущей темы
        if current_theme == 'light':
            self.configure(background='#303030')
            for frame in self.frames.values():
                frame.configure(background='#303030')
                for label in frame.grid_slaves():
                    if isinstance(label, Label) or isinstance(label, Button):
                        label.config(fg='#d3d3d3', bg='#303030', bd=0)
            config.set('theme', 'current_theme', 'black')
        else:
            self.configure(background='#d3d3d3')
            for frame in self.frames.values():
                frame.configure(background='#d3d3d3')
                for label in frame.grid_slaves():
                    if isinstance(label, Label) or isinstance(label, Button):
                        label.config(fg='#303030', bg='#d3d3d3', bd=1, relief='solid')
            config.set('theme', 'current_theme', 'light')

        # Сохраняет изменения темы в файле настроек
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)

    def set_destination_city(self, destination_city):
        """
        Устанавливает город назначения.
        """
        self.destination_city = destination_city

    def set_max_tickets_price(self, max_price):
        self.max_tickets_price = max_price

    def set_max_hotels_price(self, max_price):
        self.max_hotels_price = max_price


    def show_frame(self, page_name, destination_city=None):
        """
        Показывает указанную страницу.
        """
        if destination_city:
            self.set_destination_city(destination_city)
            for page in (HotelsPage, EventsPage):
                frame = self.frames[page.__name__]
                frame.update_destination_city(destination_city)
        frame = self.frames[page_name]
        frame.tkraise()

# Запуск главного цикла обработки событий
App().mainloop()
