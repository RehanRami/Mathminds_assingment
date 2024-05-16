from customtkinter import *
from PIL import Image,ImageTk
from mcq_quiz import MC_Quiz
from tf_quiz import TF_Quiz

ORANGE = '#FFb900'
YELLOW  = '#FFF370'
fontlabel = ("Segoe UI Black", 50, "bold")
buttonfonts = ("Segoe UI Black", 20, "bold")


class HomePage():
    def __init__(self):

        #window setup
        self.home_window = CTk()
        self.home_window.title('HOMEPAGE')
        self.home_window.minsize(width=500,height=370)
        self.home_window.maxsize(width=500,height=370)
        self.home_window.resizable(False,False)
        self.home_window.config(bg=YELLOW)
        self.app_name = CTkLabel(self.home_window,text = 'Math Minds', text_color=ORANGE,bg_color=YELLOW, font=fontlabel )
        self.app_name.place(x=105,y=10)

        #Characters
        
        self.times_symbol_img = CTkImage(light_image = Image.open('images/times charecter.png'), dark_image=Image.open('images/times charecter.png'),size=(120,120))
        self.times_symbol_display = CTkLabel(self.home_window,text='',image=self.times_symbol_img,bg_color=YELLOW)
        self.times_symbol_display.place(x=365,y=220)

        self.minus_symbol_img = CTkImage(light_image = Image.open('images/minus charecter.png'), dark_image=Image.open('images/minus charecter.png'),size=(130,80))
        self.minus_symbol_display = CTkLabel(self.home_window,text='',image=self.minus_symbol_img,bg_color=YELLOW)
        self.minus_symbol_display.place(x=25,y=90)

        self.divide_symbol_img = CTkImage(light_image = Image.open('images/divide charecter.png'), dark_image=Image.open('images/divide charecter.png'),size=(130,130))
        self.divide_symbol_display = CTkLabel(self.home_window,text='',image=self.divide_symbol_img,bg_color=YELLOW)
        self.divide_symbol_display.place(x=25,y=215)

        self.plus_symbol_img = CTkImage(light_image = Image.open('images/plus charecter.png'), dark_image=Image.open('images/plus charecter.png'),size=(125,125))
        self.plus_symbol_display = CTkLabel(self.home_window,text='',image=self.plus_symbol_img,bg_color=YELLOW)
        self.plus_symbol_display.place(x=365,y=85)


        #Buttons 

        self.mcq_button = CTkButton(self.home_window, text = 'Multiple Choice', font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.start_mcq, width=150,height=50 )
        self.mcq_button.place(x=170,y=120)

        self.tf_button = CTkButton(self.home_window, text = 'True/False', font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.start_tf, width=168,height=50 )
        self.tf_button.place(x=170,y=190)

        self.scoreboard_button = CTkButton(self.home_window, text = 'Scoreboard', font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.start_scoreboard, width=168,height=50 )
        self.scoreboard_button.place(x=170,y=260)

        # self.button =CTkButton(self.home_window, text='close', command= self.close)
        # self.button.place(x=40,y=90)

        self.home_window.mainloop()

    def start_mcq(self):
        print('mcq started')
        self.home_window.destroy()
        start = MC_Quiz()

    def start_tf(self):
        print('tf started')
        self.home_window.destroy()
        start = TF_Quiz()

    def start_scoreboard(self):
        print('scoreboard started')
        self.home_window.destroy()

    def close(self):
        self.home_window.destroy()

HomePage()





