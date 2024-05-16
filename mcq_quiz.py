from customtkinter import *
from PIL import Image, ImageTk
import random


ORANGE = '#FFb900'
YELLOW  = '#FFF370'
fontlabel = ("Segoe UI Black", 50, "bold")
buttonfonts = ("Segoe UI Black", 20, "bold")



class MC_Quiz():
    def __init__(self):
        self.mcq_window = CTk()
        self.mcq_window.title('Multiple Choice Questions')

        self.mcq_window.minsize(width=500,height=400)
        self.mcq_window.maxsize(width=500,height=400)
        self.mcq_window.resizable(False,False)
        self.mcq_window.config(bg=YELLOW)
        self.app_name = CTkLabel(self.mcq_window,text = 'Math Minds', text_color=ORANGE,bg_color=YELLOW, font=fontlabel )
        self.app_name.place(x=105,y=10)

        #Canvas
        self.canvas = CTkCanvas(self.mcq_window,width=300, height=100, bg="white")
       
        self.canvas.place(x=100,y=100)
        self.canvas.create_text(
            150,
            50,
            text="Some Questions",
            fill="black",
            font=("Arial", 20, "bold")
        )


        #genenral information about the game 
        self.amount_of_questions = 10
        self.username = None
        self.correct_answers = 0

        self.generate_questions()

        self.mcq_window.mainloop()

    def generate_questions(self):
        while self.amount_of_questions > 0:
            
            if self.amount_of_questions == 10:
                self.name_entry_box = CTkEntry(self.mcq_window, placeholder_text='     NAME', font=fontlabel,height=105,width=305)
                self.name_entry_box.place(x=100,y=100)
                self.play_button = CTkButton(self.mcq_window, text = 'LETS PLAY', font=buttonfonts,text_color='white', fg_color='#FFC773', command=self.name_input, width=150,height=50 )
                self.play_button.place(x=180,y=290)



            self.operation_list = ['*','+','-','/']
            self.operation = random.choice(self.operation_list)
            print(self.operation)

            self.amount_of_questions -=1 
            if self.operation == '/':
                pass
                

            
    def name_input(self):# stores the user's name 
        self.name = self.name_entry_box.get()
        self.username = self.name
        print(self.name)
        if self.name == '' :
            pass
        else:
            self.name_entry_box.destroy()
            self.play_button.destroy()

            
