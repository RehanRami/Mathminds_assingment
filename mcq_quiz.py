from customtkinter import *
from PIL import Image, ImageTk
import random
from stopwatch import Stopwatch
import json


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

        #genenral information about the game 
        self.amount_of_questions = 10
        self.username = None
        self.answers_correct = 0
        self.stopwatch = Stopwatch(2)

        if self.amount_of_questions== 10:
            self.get_name()
            self.stopwatch.start()
            
        else:
            self.generate_questions()

        self.mcq_window.mainloop()

    def generate_questions(self):
        if self.amount_of_questions > 0:
            self.operation_list = ['*','+','-','/']
            self.operation = random.choice(self.operation_list)

            if self.operation == '/':
                self.num1 = random.choice([2,4,6,8,10,3,6,9])
                if self.num1 % 2 ==0 and self.num1 % 3 ==0:
                    self.num2 = 3
                elif self.num1 % 2 ==0:
                    self.num2 = 2
                elif self.num1 % 3 == 0:
                    self.num2 = 3
            else:
                self.numbers = [1,2,3,4,5,6,7,8,9]
                self.num1 = random.choice(self.numbers)
                self.num2 = random.choice(self.numbers)

            self.correct_answer = int(eval(f'{self.num1}{self.operation}{self.num2}'))
            
            self.user_response = None
            self.button_chooser = random.choice([1,2,3,4]) 
            self.button1_value = None
            self.button2_value = None
            self.button3_value = None
            self.button4_value = None 

            if self.button_chooser == 1:
                self.button1_value = self.correct_answer
                self.button2_value = self.correct_answer + random.choice([1,-1,5,-5])
                self.button3_value = self.correct_answer + random.choice([2,-2,4,-4])
                self.button4_value = self.correct_answer + random.choice([3,-3,6,-6])
            elif self.button_chooser == 2:
                self.button2_value = self.correct_answer
                self.button1_value = self.correct_answer + random.choice([1,-1,5,-5])
                self.button3_value = self.correct_answer + random.choice([2,-2,4,-4])
                self.button4_value = self.correct_answer + random.choice([3,-3,6,-6])
            elif self.button_chooser == 3:
                self.button3_value = self.correct_answer
                self.button1_value = self.correct_answer + random.choice([1,-1,5,-5])
                self.button2_value = self.correct_answer + random.choice([2,-2,4,-4])
                self.button4_value = self.correct_answer + random.choice([3,-3,6,-6])
            else:
                self.button4_value = self.correct_answer
                self.button1_value = self.correct_answer + random.choice([1,-1,5,-5])
                self.button2_value = self.correct_answer + random.choice([2,-2,4,-4])
                self.button3_value = self.correct_answer + random.choice([3,-3,6,-6])

            # Canvas 
            self.canvas = CTkCanvas(self.mcq_window,width=300, height=100, bg="white")
       
            self.canvas.place(x=100,y=100)
            self.canvas.create_text(
            150,
            50,
            text=f'{self.num1} {self.operation} {self.num2} ',
            fill="black",
            font=("Arial", 20, "bold")
            )

            self.button1 =CTkButton(self.mcq_window, text = self.button1_value, font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.button1_cmd, width=150,height=50 )
            self.button1.place(x=50,y=250)
            self.button2 =CTkButton(self.mcq_window, text = self.button2_value, font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.button2_cmd, width=150,height=50 )
            self.button2.place(x=50,y=320)
            self.button3 =CTkButton(self.mcq_window, text = self.button3_value, font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.button3_cmd, width=150,height=50 )
            self.button3.place(x=295,y=250)
            self.button4 =CTkButton(self.mcq_window, text = self.button4_value, font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.button4_cmd, width=150,height=50 )
            self.button4.place(x=295,y=320)

            self.amount_of_questions -= 1
            self.mcq_window.mainloop()

        else:
            self.button1.destroy()
            self.button2.destroy()
            self.button3.destroy()
            self.button4.destroy()
            self.canvas.destroy()
            self.stopwatch.stop()

            self.time_display = CTkLabel(self.mcq_window,text=round(self.stopwatch.duration,2), font=fontlabel, bg_color=YELLOW)
            self.time_display.place(x=315,y=295)
            self.time_taken_label = CTkLabel(self.mcq_window,text="Time Take", font=("Segoe UI Black", 15, "bold"), bg_color=YELLOW)
            self.time_taken_label.place(x=315,y=270)

            self.answerlabel = CTkLabel(self.mcq_window,text = f'{self.answers_correct}/10', font=fontlabel, bg_color=YELLOW)
            self.answerlabel.place(x=90,y=295)
            self.question_answered_label = CTkLabel(self.mcq_window, text = 'Answers Correct', font =  ("Segoe UI Black", 15, "bold"), bg_color=YELLOW )
            if len(self.username) > 6:
                x = 60
            else:
                x=80
            self.question_answered_label.place(x=x,y=270)

            self.name_display = CTkLabel(self.mcq_window,text=self.username, font=fontlabel,bg_color=YELLOW)
            self.name_display.place(x=175,y=200)
            self.crown_img = CTkImage(light_image=Image.open('images/crown.png'), dark_image=Image.open('images/crown.png'),size=(160,130))
            self.crown_display = CTkLabel(self.mcq_window,text='',image=self.crown_img,bg_color=YELLOW)
            self.crown_display.place(x=175,y=75)

            #uploading data
            with open("database.json", "r") as file:
                data = json.load(file)
    
            score_key = f"{self.answers_correct}/10"
    
            data["mcq"][score_key].append([self.username, score_key, str(round(self.stopwatch.duration,2))])

            with open("database.json", "w") as file:
                json.dump(data, file, indent=4)

    def button1_cmd(self):
        self.user_response = 1
        self.check_answer()

    def button2_cmd(self):
        self.user_response = 2
        self.check_answer()

    def button3_cmd(self):
        self.user_response = 3
        self.check_answer()

    def button4_cmd(self):
        self.user_response = 4
        self.check_answer()

    def check_answer(self):
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.canvas.destroy()
        if self.user_response == self.button_chooser:
            self.answers_correct += 1
        else:
            self.answers_correct = self.answers_correct
        
        self.generate_questions()


    def get_name(self):
        self.name_entry_box = CTkEntry(self.mcq_window, placeholder_text='     NAME', font=fontlabel,height=105,width=305)
        self.name_entry_box.place(x=100,y=100)
        self.play_button = CTkButton(self.mcq_window, text = 'LETS PLAY', font=buttonfonts,text_color='white', fg_color='#FFC773', command=self.name_input, width=150,height=50 )
        self.play_button.place(x=180,y=290)
        self.proceed = False
        self.mcq_window.mainloop()
        

    def name_input(self):# stores the user's name 
        self.name = self.name_entry_box.get()
        self.username = self.name
        print(self.name)
        if self.name == '' :
            pass
        else:
            self.proceed = True
            self.name_entry_box.destroy()
            self.play_button.destroy()
            self.generate_questions()

            
