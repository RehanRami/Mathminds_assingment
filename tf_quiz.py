from customtkinter import *
import random
from PIL import Image,ImageTk
from stopwatch import Stopwatch
import json


ORANGE = '#FFb900'
YELLOW  = '#FFF370'
fontlabel = ("Segoe UI Black", 50, "bold")
buttonfonts = ("Segoe UI Black", 20, "bold")
THEME_COLOR = "#375362"

class TF_Quiz():
    def __init__(self):
        self.tf_window = CTk()
        self.tf_window.title('True/False')
        
        self.tf_window.minsize(width=500, height=400)
        self.tf_window.maxsize(width=500,height=400)
        self.tf_window.resizable(False,False)
        self.tf_window.config(bg=YELLOW)
        self.app_name = CTkLabel(self.tf_window, text='Math Minds', text_color=ORANGE,bg_color=YELLOW, font=fontlabel )
        self.app_name.place(x=105,y=10)

        self.back_home = CTkButton(self.tf_window, text='home', bg_color=YELLOW, font=("Segoe UI Black", 10, "bold"), command=self.back_home, width=70, height=10)
        self.back_home.place(x=0,y=0)

        self.amount_of_questions = 10
        self.username = None
        self.answers_correct = 0
        self.stopwatch = Stopwatch(2)


        if self.amount_of_questions == 10:
            self.get_name()
            self.stopwatch.start()
        else:   
            self.generate_questions()

        self.tf_window.mainloop()

    def generate_questions(self):


        if self.amount_of_questions > 0:
            #question maker 
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
            #
            self.user_response = None
            self.question_baser = random.choice([True,False])
            self.display_answer = None
            if self.question_baser == True:
                self.display_answer = self.correct_answer
            else:
                x = random.choice([4,-4,1,-3,3,-1,2,-2,-5,5])
                self.display_answer = self.correct_answer + x
            # Canvas 
            self.canvas = CTkCanvas(self.tf_window,width=300, height=100, bg="white")
       
            self.canvas.place(x=100,y=100)
            self.canvas.create_text(
            150,
            50,
            text=f'{self.num1} {self.operation} {self.num2} = {self.display_answer}',
            fill="black",
            font=("Arial", 20, "bold")
            )

            self.true_button_img = CTkImage(light_image=Image.open('images/True button.png'), dark_image=Image.open('images/True button.png'),size=(160,130))
            self.true_button = CTkButton(self.tf_window,text='', image=self.true_button_img,command=self.true_button_cmd,bg_color=YELLOW,border_color=YELLOW,)
            self.true_button.place(x=30,y=230)

            self.false_button_img = CTkImage(light_image=Image.open('images/False button.png'), dark_image=Image.open('images/False button.png'),size=(160,130))
            self.false_button = CTkButton(self.tf_window,text='', image=self.false_button_img,command=self.false_button_cmd,bg_color=YELLOW,border_color=YELLOW,border_width=0)
            self.false_button.place(x=290,y=230) 

            self.amount_of_questions -=1 
            self.tf_window.mainloop()
        else:
            self.true_button.destroy()
            self.false_button.destroy()
            self.canvas.destroy()
            self.stopwatch.stop()


            self.time_display = CTkLabel(self.tf_window,text=round(self.stopwatch.duration,2), font=fontlabel, bg_color=YELLOW)
            self.time_display.place(x=315,y=295)
            self.time_taken_label = CTkLabel(self.tf_window,text="Time Take", font=("Segoe UI Black", 15, "bold"), bg_color=YELLOW)
            self.time_taken_label.place(x=315,y=270)

            self.answerlabel = CTkLabel(self.tf_window,text = f'{self.answers_correct}/10', font=fontlabel, bg_color=YELLOW)
            self.answerlabel.place(x=90,y=295)
            self.question_answered_label = CTkLabel(self.tf_window, text = 'Answers Correct', font =  ("Segoe UI Black", 15, "bold"), bg_color=YELLOW )
            if len(self.username) > 6:
                x = 60
            else:
                x=80
            self.question_answered_label.place(x=x,y=270)
            
            self.name_display = CTkLabel(self.tf_window,text=self.username, font=fontlabel,bg_color=YELLOW)
            self.name_display.place(x=175,y=200)
            self.crown_img = CTkImage(light_image=Image.open('images/crown.png'), dark_image=Image.open('images/crown.png'),size=(160,130))
            self.crown_display = CTkLabel(self.tf_window,text='',image=self.crown_img,bg_color=YELLOW)
            self.crown_display.place(x=175,y=75)

            #uploading data
            with open("database.json", "r") as file:
                data = json.load(file)
    
            score_key = f"{self.answers_correct}/10"
    
            data["tf"][score_key].append([self.username, score_key, str(round(self.stopwatch.duration,2))])

            with open("database.json", "w") as file:
                json.dump(data, file, indent=4)
                
                
            


    def true_button_cmd(self):
        self.user_response = True
        self.check_answer()
        
    def false_button_cmd(self):
        self.user_response = False
        self.check_answer()


    def check_answer(self):
        self.true_button.destroy()
        self.false_button.destroy()
        self.canvas.destroy()
        if self.user_response == self.question_baser:
            self.answers_correct += 1
        else:
            self.answers_correct = self.answers_correct
        
        
        self.generate_questions()


    def get_name(self):
            self.name_entry_box = CTkEntry(self.tf_window, placeholder_text='     NAME', font=fontlabel,height=105,width=305)
            self.name_entry_box.place(x=100,y=100)
            self.play_button = CTkButton(self.tf_window, text = 'LETS PLAY', font=buttonfonts,text_color='white', fg_color='#FFC773', command=self.name_input, width=150,height=50 )
            self.play_button.place(x=180,y=290)
            self.proceed = False
            self.tf_window.mainloop() 

    def name_input(self):
        self.name = self.name_entry_box.get()
        self.username = self.name
        print(self.name)
        if self.name == '':
            pass
        else:
            self.proceed = True
            self.name_entry_box.destroy()
            self.play_button.destroy()
            self.generate_questions()

    def add_tf_result(score, user_name, time_taken):
        with open("data.json", "r") as file:
            data = json.load(file)
    
        score_key = f"{score}/10"
    
        data["tf"][score_key].append([user_name, score_key, str(time_taken)])

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)


    def back_home(self):
        
        self.tf_window.destroy()
        import homepage
        home = homepage.HomePage()