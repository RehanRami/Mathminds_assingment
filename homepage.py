from customtkinter import *
from PIL import Image,ImageTk
from mcq_quiz import MC_Quiz
from tf_quiz import TF_Quiz
from scoreboard import Scoreboard

ORANGE = '#FFb900'
YELLOW  = '#FFF370'
fontlabel = ("Segoe UI Black", 50, "bold")
buttonfonts = ("Segoe UI Black", 20, "bold")


class HomePage():
    def __init__(self):

        #window setup
        self.home_window = CTk()
        self.home_window.title('HOMEPAGE')
        self.home_window.minsize(width=500,height=370) # Sets the window dimensions
        self.home_window.maxsize(width=500,height=370)# Sets the window dimensions
        self.home_window.resizable(False,False)
        self.home_window.config(bg=YELLOW)#changes the window color 

        # Displays the application name at the top of the window 
        self.app_name = CTkLabel(self.home_window,text = 'Math Minds', text_color=ORANGE,bg_color=YELLOW, font=fontlabel )
        self.app_name.place(x=105,y=10)

        # Displaying cartoon math figures 
        
        # Displays the Multiplication character 
        self.times_symbol_img = CTkImage(light_image = Image.open('images/times charecter.png'), dark_image=Image.open('images/times charecter.png'),size=(120,120))
        self.times_symbol_display = CTkLabel(self.home_window,text='',image=self.times_symbol_img,bg_color=YELLOW)
        self.times_symbol_display.place(x=365,y=220)

        # Displays the Minus character 
        self.minus_symbol_img = CTkImage(light_image = Image.open('images/minus charecter.png'), dark_image=Image.open('images/minus charecter.png'),size=(130,80))
        self.minus_symbol_display = CTkLabel(self.home_window,text='',image=self.minus_symbol_img,bg_color=YELLOW)
        self.minus_symbol_display.place(x=25,y=90)

        # Displays the Divide character 
        self.divide_symbol_img = CTkImage(light_image = Image.open('images/divide charecter.png'), dark_image=Image.open('images/divide charecter.png'),size=(130,130))
        self.divide_symbol_display = CTkLabel(self.home_window,text='',image=self.divide_symbol_img,bg_color=YELLOW)
        self.divide_symbol_display.place(x=25,y=215)

        # Displays the Addition character 
        self.plus_symbol_img = CTkImage(light_image = Image.open('images/plus charecter.png'), dark_image=Image.open('images/plus charecter.png'),size=(125,125))
        self.plus_symbol_display = CTkLabel(self.home_window,text='',image=self.plus_symbol_img,bg_color=YELLOW)
        self.plus_symbol_display.place(x=365,y=85)


        # Buttons for the 4 main functions 

        # Initialises and displays the Multiple chioce button
        self.mcq_button = CTkButton(self.home_window, text = 'Multiple Choice', font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.start_mcq, width=150,height=50, hover_color='#ff7b00' )
        self.mcq_button.place(x=170,y=110)

        # Initialises and displays the True/False button
        self.tf_button = CTkButton(self.home_window, text = 'True/False', font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.start_tf, width=168,height=50, hover_color='#ff7b00' )
        self.tf_button.place(x=170,y=180)

        # Initialises and displays the Scoreboard button
        self.scoreboard_button = CTkButton(self.home_window, text = 'Scoreboard', font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.start_scoreboard, width=168,height=50, hover_color='#ff7b00' )
        self.scoreboard_button.place(x=170,y=250)

        # Initialises and displays the close button
        self.close_button =CTkButton(self.home_window, text='close', command= self.close, width=70, height = 20, bg_color=YELLOW, fg_color=ORANGE, hover_color='#ff7b00')
        self.close_button.place(x=210,y=320)
        self.home_window.mainloop()



    def start_mcq(self):# Destroys the Home window and starts the Multiple chioce quiz 
        print('mcq started')
        self.home_window.destroy()
        start = MC_Quiz()

    def start_tf(self): # Destroys the Home window and starts the True/False quiz
        print('tf started')
        self.home_window.destroy()
        start = TF_Quiz()

    def start_scoreboard(self): # Destroys the Home window and starts the Scoreboard page 
        print('scoreboard started')
        self.home_window.destroy()
        start = Scoreboard()

    def close(self): # Destroys the Home window/ exits the program
        self.home_window.destroy()

