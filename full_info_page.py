from tkinter import *
from tkinter import ttk

class FullInfoPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        label = Label(self, text="Full Info", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.info_text = Text(self, wrap=WORD)
        self.info_text.pack(expand=True, fill=BOTH)

        back_button = ttk.Button(self, text="Back",
                                 command=lambda: controller.show_frame("Results"))
        back_button.pack(side="bottom")

    def update_info(self, info):
        self.info_text.delete(1.0, END)
        self.info_text.insert(INSERT, info)
