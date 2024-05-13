from customtkinter import *
from PIL import Image, ImageTk


ORANGE = '#FFb900'
YELLOW  = '#FFF370'
fontlabel = ("Segoe UI Black", 50, "bold")
buttonfonts = ("Segoe UI Black", 20, "bold")
class MC_Quiz():
    def __init__(self):
        self.mcq_window = CTk()
        self.mcq_window.title('Multiple Choice Questions')

        self.mcq_window.minsize(width=500,height=370)
        self.mcq_window.maxsize(width=500,height=370)
        self.mcq_window.resizable(False,False)
        self.mcq_window.config(bg=YELLOW)
        self.app_name = CTkLabel(self.mcq_window,text = 'Math Minds', text_color=ORANGE,bg_color=YELLOW, font=fontlabel )
        self.app_name.place(x=105,y=10)

        # self.question_box = CTkLabel()


        self.mcq_window.mainloop()

    def generate_questions(self):
        pass