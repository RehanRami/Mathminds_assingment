from customtkinter import *
from PIL import Image, ImageTk
import random
from stopwatch import Stopwatch
import json


# Predefined constants : These are values which are going to be used across the application 
ORANGE = '#FFb900'
YELLOW  = '#FFF370'
fontlabel = ("Segoe UI Black", 50, "bold")
buttonfonts = ("Segoe UI Black", 20, "bold")



class MC_Quiz():
    def __init__(self):
        # Window setup
        self.mcq_window = CTk()
        self.mcq_window.title('Multiple Choice Questions')
        self.mcq_window.minsize(width=500,height=400) # Sets the window dimensions
        self.mcq_window.maxsize(width=500,height=400)# Sets the window dimensions
        self.mcq_window.resizable(False,False)
        self.mcq_window.config(bg=YELLOW)# Sets the window color

        # Displays the App name at the top of the window 
        self.app_name = CTkLabel(self.mcq_window,text = 'Math Minds', text_color=ORANGE,bg_color=YELLOW, font=fontlabel )
        self.app_name.place(x=105,y=10)

        # Initialises and displays the back home button (allows the user to return back home )
        self.back_home = CTkButton(self.mcq_window, text='home', bg_color=YELLOW, font=("Segoe UI Black", 10, "bold"), command=self.back_home, width=70, height=10, fg_color=ORANGE, hover_color='#ff7b00')
        self.back_home.place(x=0,y=0)

        #genenral information about the game  (these are values which are going to be used to update the database )
        self.amount_of_questions = 10
        self.username = None
        self.answers_correct = 0
        self.stopwatch = Stopwatch(2)

        # Checks if its the Pregame and if so then it asks for the user's name if not it continues with the game 
        if self.amount_of_questions== 10:
            self.get_name() # Gets the user's name 
            self.stopwatch.start() #starts the stopwatch
            
        else:
            self.generate_questions() #starts the quiz

        self.mcq_window.mainloop()

    def generate_questions(self): # makes the question and the buttons 

        self.current_score_display = CTkLabel(self.mcq_window, text = f'{self.answers_correct}/10', text_color=ORANGE, font=buttonfonts, bg_color=YELLOW)
        self.current_score_display.place(x=225, y=290)

        if self.amount_of_questions > 0: # check if the user has completed the quiz

            #chooses a random operation for the question
            self.operation_list = ['*','+','-','/']
            self.operation = random.choice(self.operation_list)

            if self.operation == '/':# checks if the operation is division and if so chooses a set of numbers which the answer can only be a whole number 
                self.num1 = random.choice([2,4,6,8,10,3,6,9])
                if self.num1 % 2 ==0 and self.num1 % 3 ==0:
                    self.num2 = 3
                elif self.num1 % 2 ==0:
                    self.num2 = 2
                elif self.num1 % 3 == 0:
                    self.num2 = 3
            else:# if the opertion chosen was not division it picks 2 random numbers 
                self.numbers = [1,2,3,4,5,6,7,8,9]
                self.num1 = random.choice(self.numbers)
                self.num2 = random.choice(self.numbers)

            # Evaluates the the question which is made by the 2 numbers chosen and the operation
            self.correct_answer = int(eval(f'{self.num1}{self.operation}{self.num2}'))
             
            # This is going to hold the button number of which the user has choosen 
            self.user_response = None
            #chooses a random button to put the correct option in
            self.button_chooser = random.choice([1,2,3,4]) 
            # Defines the buttons values which are going to set later
            self.button1_value = None
            self.button2_value = None
            self.button3_value = None
            self.button4_value = None 

            # Depending on what button the program chose to put the correct ans in, this will SET that button with the correct value and the rest with other numbers 
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

            # This is a canvas where the question will be showed to the user
            self.canvas = CTkCanvas(self.mcq_window,width=300, height=100, bg="white")
       
            self.canvas.place(x=100,y=100)
            self.canvas.create_text(
            150,
            50,
            text=f'{self.num1} {self.operation} {self.num2} ',
            fill="black",
            font=("Arial", 20, "bold")
            )


            # Displays the 4 buttons 
            self.button1 =CTkButton(self.mcq_window, text = self.button1_value, font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.button1_cmd, width=150,height=50 )
            self.button1.place(x=50,y=250)
            self.button2 =CTkButton(self.mcq_window, text = self.button2_value, font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.button2_cmd, width=150,height=50 )
            self.button2.place(x=50,y=320)
            self.button3 =CTkButton(self.mcq_window, text = self.button3_value, font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.button3_cmd, width=150,height=50 )
            self.button3.place(x=295,y=250)
            self.button4 =CTkButton(self.mcq_window, text = self.button4_value, font=buttonfonts,text_color='white', fg_color=ORANGE, command=self.button4_cmd, width=150,height=50 )
            self.button4.place(x=295,y=320)

            # Takes 1 away from the amount of questions the user has to answer
            self.amount_of_questions -= 1
            self.mcq_window.mainloop()

        else:# if the user has answered 10 questions, loads up achivement screen and saves the user's progress

            # Destroys everything on window except app name
            self.button1.destroy()
            self.button2.destroy()
            self.button3.destroy()
            self.button4.destroy()
            self.canvas.destroy()
            self.current_score_display.destroy()
            self.stopwatch.stop()# stops the stopwatch 

            # Displays a label and the ammount of time the user took to complete the quiz 
            self.time_display = CTkLabel(self.mcq_window,text=round(self.stopwatch.duration,2), font=fontlabel, bg_color=YELLOW)
            self.time_display.place(x=315,y=295)
            self.time_taken_label = CTkLabel(self.mcq_window,text="Time Take", font=("Segoe UI Black", 15, "bold"), bg_color=YELLOW)
            self.time_taken_label.place(x=315,y=270)


            #Shows a label and the amount of questions the ues got correct 
            self.answerlabel = CTkLabel(self.mcq_window,text = f'{self.answers_correct}/10', font=fontlabel, bg_color=YELLOW)
            self.answerlabel.place(x=90,y=295)
            self.question_answered_label = CTkLabel(self.mcq_window, text = 'Answers Correct', font =  ("Segoe UI Black", 15, "bold"), bg_color=YELLOW )

            # Makes a rough estimate on where the user's name will be displayed depending on its length
            if len(self.username) > 6:
                x = 60
            else:
                x=80
            self.question_answered_label.place(x=x,y=270)

            #Displays a crown image and the User's name 
            self.name_display = CTkLabel(self.mcq_window,text=self.username, font=fontlabel,bg_color=YELLOW)
            self.name_display.place(x=175,y=200)
            self.crown_img = CTkImage(light_image=Image.open('images/crown.png'), dark_image=Image.open('images/crown.png'),size=(160,130))
            self.crown_display = CTkLabel(self.mcq_window,text='',image=self.crown_img,bg_color=YELLOW)
            self.crown_display.place(x=175,y=75)

            #Uploads the user's score , name and amount of time they took to finsh the quiz
            with open("database.json", "r") as file:
                data = json.load(file)
    
            score_key = f"{self.answers_correct}/10"
    
            data["mcq"][score_key].append([self.username, score_key, str(round(self.stopwatch.duration,2))])

            with open("database.json", "w") as file:
                json.dump(data, file, indent=4)


    def button1_cmd(self):# sets the value of user response to 1 and checks answer
        self.user_response = 1
        self.check_answer()

    def button2_cmd(self):# sets the value of user response to 2 and checks answer
        self.user_response = 2
        self.check_answer()

    def button3_cmd(self):# sets the value of user response to 3 and checks answer
        self.user_response = 3
        self.check_answer()

    def button4_cmd(self):# sets the value of user response to 4 and checks answer 
        self.user_response = 4
        self.check_answer()

    def check_answer(self):
        #Destroys all components of the window except the App name
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.canvas.destroy()
        self.current_score_display.destroy()

        #Checks if user's response matches with the button which the correct value was set to 
        if self.user_response == self.button_chooser:
            self.answers_correct += 1 #adds 1 to the amount of questions the user correctly answered
        else:
            self.answers_correct = self.answers_correct
        
        self.generate_questions() # goes to the next question 


    def get_name(self):# Displays all the components which are used to get the users name 
        self.name_entry_box = CTkEntry(self.mcq_window, placeholder_text='     NAME', font=fontlabel,height=105,width=305)
        self.name_entry_box.place(x=100,y=100)
        self.play_button = CTkButton(self.mcq_window, text = 'LETS PLAY', font=buttonfonts,text_color='white', fg_color='#FFC773', command=self.name_input, width=150,height=50 )
        self.play_button.place(x=180,y=290)
        self.error_input = CTkLabel(self.mcq_window, text='The name must be less than 10 letters and must not include any spaces or symbols', text_color='red', bg_color=YELLOW, font=('Arial',9,'bold'))
        self.error_input.place(x=70, y=210)
        self.proceed = False
        self.mcq_window.mainloop()
        

    def name_input(self):# Gets the user's name and stores it 
        self.name = self.name_entry_box.get()
        self.username = self.name
        print(self.name)
        self.symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=',',','.','<','>','/','?',':',';','"',"'",'`','~',']','[','{','}',"|"]
        self.split_username = list(self.name)
    
        for letter in self.split_username:
            if letter in self.symbols:
                self.symbol_exists = True
                break
            else:
                self.symbol_exists = False
        if self.name == '':
            pass
        elif len(self.name) > 10:
            pass
        elif self.name.count(' ')>0:
            pass
        elif self.symbol_exists == True:
            pass
        else:
            self.proceed = True
            self.name_entry_box.destroy()
            self.play_button.destroy()
            self.error_input.destroy()
            self.generate_questions()

    def back_home(self): # Destroys the Multiple choice quiz and starts the Homepage 
        self.mcq_window.destroy()
        import homepage
        start = homepage.HomePage()
      
        