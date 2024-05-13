from customtkinter import *
from PIL import Image,ImageTk
import mcq_quiz

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

        #charecters



        #Buttons 

        self.mcq_button = CTkButton(self.home_window, text = 'Multiple Choice', font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.start_mcq, width=150,height=50 )
        self.mcq_button.place(x=170,y=120)

        self.tf_button = CTkButton(self.home_window, text = 'True/False', font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.start_tf, width=168,height=50 )
        self.tf_button.place(x=170,y=190)

        self.scoreboard_button = CTkButton(self.home_window, text = 'Scoreboard', font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.start_scoreboard, width=168,height=50 )
        self.scoreboard_button.place(x=170,y=260)

        self.button =CTkButton(self.home_window, text='close', command= self.close)
        self.button.place(x=40,y=90)




        self.home_window.mainloop()

    def start_mcq(self):
        print('mcq started')
        self.home_window.destroy()
        start = mcq_quiz.MC_Quiz()
        
        


    def start_tf(self):
        print('tf started')
        self.home_window.destroy()

    def start_scoreboard(self):
        print('scoreboard started')
        self.home_window.destroy()


    def close(self):
        self.home_window.destroy()



HomePage()





