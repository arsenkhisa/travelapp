# импорт библиотеки
from tkinter import *


# класс results
class Results(Frame):
    def __init__(self, parent, controller):
        """
        конструктор класса
        """
        # вызываем конструктор родительского класса
        Frame.__init__(self, parent)

        # сохраняем обьект контроллера
        self.controller = controller

        # создаем метку 'results'
        label = Label(self, text="Results", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        # создаем метку 'see results'
        button = Button(self, text="See results",
                        command=self.show_full_info)
        button.pack()

    def show_full_info(self):
        # Здесь вы должны получить информацию о билетах, отелях и мероприятиях, в зависимости от выбора пользователя.
        # Затем объедините всю информацию в одну строку и передайте ее в update_info.
        full_info = "Тут должна быть информация о билетах, отелях и мероприятиях"
        full_info_page = self.controller.frames["FullInfoPage"]
        full_info_page.update_info(full_info)
        self.controller.show_frame("FullInfoPage")
