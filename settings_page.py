import configparser
from tkinter import Toplevel, Button, Frame

class SettingsPage(Toplevel):
    def __init__(self, app):
        Toplevel.__init__(self)
        self.title("Settings")
        self.app = app

        self.geometry("300x200")
        self.resizable(width=False, height=False)

        frame = Frame(self)
        frame.pack()

        theme_button = Button(frame, text="Dark/Light theme", command=self.change_theme)
        theme_button.pack()

    def change_theme(self):
        self.app.change_theme()
