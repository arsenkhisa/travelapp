from tkinter import Toplevel, Button, Frame, Scale, HORIZONTAL
from tkinter.colorchooser import askcolor

class SettingsPage(Toplevel):
    """
    Класс страницы настроек.
    """

    def __init__(self, app):
        """
        Инициализация страницы настроек.
        :param app: приложение, к которому привязана страница настроек.
        """
        super().__init__()
        self.title("Settings")
        self.app = app

        # Задание геометрии и параметров изменения размера окна
        self.geometry("300x200")
        self.resizable(width=False, height=False)

        # Создание и упаковка фрейма
        frame = Frame(self)
        frame.pack()

        # Создание слайдеров для изменения ширины и высоты
        width_scale = Scale(frame, from_=400, to=800, orient=HORIZONTAL, command=self.update_width)
        width_scale.pack()
        height_scale = Scale(frame, from_=500, to=600, orient=HORIZONTAL, command=self.update_height)
        height_scale.pack()

        # Создание кнопки для смены темы
        theme_button = Button(frame, text="Dark/Light theme", command=self.change_theme)
        theme_button.pack()

        # Создание кнопки для выбора цвета фона
        bg_color_button = Button(frame, text="Choose BG color", command=self.change_bg_color)
        bg_color_button.pack()

    def update_width(self, new_width):
        """
        Обновление ширины приложения.
        :param new_width: новая ширина приложения.
        """
        self.app.geometry(f"{new_width}x{self.app.winfo_height()}")

    def update_height(self, new_height):
        """
        Обновление высоты приложения.
        :param new_height: новая высота приложения.
        """
        self.app.geometry(f"{self.app.winfo_width()}x{new_height}")

    def change_theme(self):
        """
        Изменение темы приложения.
        """
        self.app.change_theme()

    def change_bg_color(self):
        """
        Изменение цвета фона приложения.
        """
        # Вызов диалога выбора цвета
        color = askcolor()[1]
        # Если выбран цвет, применяем его ко всем фреймам
        if color:
            self.app.configure(background=color)
            for frame in self.app.frames.values():
                frame.configure(background=color)
