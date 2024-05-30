from customtkinter import *
import random
from PIL import Image,ImageTk
from stopwatch import Stopwatch
import json

# Predefined constants : These are values which are going to be used across the application 
ORANGE = '#FFb900'
YELLOW  = '#FFF370'
fontlabel = ("Segoe UI Black", 50, "bold")
buttonfonts = ("Segoe UI Black", 20, "bold")
THEME_COLOR = "#375362"

class TF_Quiz():
    def __init__(self):
        # Window setup
        self.tf_window = CTk()
        self.tf_window.title('True/False')
        self.tf_window.minsize(width=500, height=400)# Sets the window dimensions
        self.tf_window.maxsize(width=500,height=400)# Sets the window dimensions
        self.tf_window.resizable(False,False)
        self.tf_window.config(bg=YELLOW)# Sets the window color

        # Displays the App name at the top of the window 
        self.app_name = CTkLabel(self.tf_window, text='Math Minds', text_color=ORANGE,bg_color=YELLOW, font=fontlabel )
        self.app_name.place(x=105,y=10)

        # Initialises and displays the back home button (allows the user to return back home )
        self.back_home = CTkButton(self.tf_window, text='home', bg_color=YELLOW, font=("Segoe UI Black", 10, "bold"), command=self.back_home, width=70, height=10, hover_color='#ff7b00', fg_color=ORANGE )
        self.back_home.place(x=0,y=0)

        #genenral information about the game  (these are values which are going to be used to update the database )
        self.amount_of_questions = 10
        self.username = None
        self.answers_correct = 0
        self.stopwatch = Stopwatch(2)

        # Checks if its the Pregame and if so then it asks for the user's name if not it continues with the game
        if self.amount_of_questions == 10:
            self.get_name()# Gets the user's name 
            self.stopwatch.start()#starts the stopwatch
        else:   
            self.generate_questions() #starts the quiz

        self.tf_window.mainloop()

    def generate_questions(self):# makes the question and the buttons 


        if self.amount_of_questions > 0:# check if the user has completed the quiz
            
            self.current_score_display = CTkLabel(self.tf_window, text = f'{self.answers_correct}/10', text_color=ORANGE, font=buttonfonts, bg_color=YELLOW)
            self.current_score_display.place(x=225, y=270)

            #chooses a random operation for the question
            self.operation_list = ['*','+','-','/']
            self.operation = random.choice(self.operation_list)
        
            if self.operation == '/':# checks if the operation is division and if so chooses a set of numbers which the answer can only be a whole number 
                self.num1 = random.choice([2,4,6,8,10,3,9])
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
            
            # This is going to hold the button value of which the user has choosen
            self.user_response = None
            # Chooses a random boolean in which the correct answer button will be set to
            self.question_baser = random.choice([True,False])
            self.display_answer = None

            # Depending on the question baser this decides if they are going to show the correct answer to the user
            if self.question_baser == True:
                self.display_answer = self.correct_answer
            else:
                x = random.choice([4,-4,1,-3,3,-1,2,-2,-5,5])
                self.display_answer = self.correct_answer + x

            
            # This is a canvas where the question will be showed to the user
            self.canvas = CTkCanvas(self.tf_window,width=300, height=100, bg="white")
       
            self.canvas.place(x=100,y=100)
            self.canvas.create_text(
            150,
            50,
            text=f'{self.num1} {self.operation} {self.num2} = {self.display_answer}',
            fill="black",
            font=("Arial", 20, "bold")
            )

            #Displays the True button with an Image 
            self.true_button_img = CTkImage(light_image=Image.open('images/True button.png'), dark_image=Image.open('images/True button.png'),size=(160,130))
            self.true_button = CTkButton(self.tf_window,text='', image=self.true_button_img,command=self.true_button_cmd,bg_color=YELLOW,border_color=YELLOW,)
            self.true_button.place(x=30,y=230)

            #Displays the Flase button with an Image
            self.false_button_img = CTkImage(light_image=Image.open('images/False button.png'), dark_image=Image.open('images/False button.png'),size=(160,130))
            self.false_button = CTkButton(self.tf_window,text='', image=self.false_button_img,command=self.false_button_cmd,bg_color=YELLOW,border_color=YELLOW,border_width=0)
            self.false_button.place(x=290,y=230) 

            # Takes 1 away from the amount of questions the user has to answer
            self.amount_of_questions -=1 
            self.tf_window.mainloop()

        else:# if the user has answered 10 questions, loads up achivement screen and saves the user's progress

            # Destroys everything on window except app name
            self.true_button.destroy()
            self.false_button.destroy()
            self.canvas.destroy()
            self.current_score_display.destroy()
            self.stopwatch.stop()# stops the stopwatch

            # Displays a label and the ammount of time the user took to complete the quiz 
            self.time_display = CTkLabel(self.tf_window,text=round(self.stopwatch.duration,2), font=fontlabel, bg_color=YELLOW)
            self.time_display.place(x=315,y=295)
            self.time_taken_label = CTkLabel(self.tf_window,text="Time Take", font=("Segoe UI Black", 15, "bold"), bg_color=YELLOW)
            self.time_taken_label.place(x=315,y=270)

            #Shows a label and the amount of questions the ues got correct
            self.answerlabel = CTkLabel(self.tf_window,text = f'{self.answers_correct}/10', font=fontlabel, bg_color=YELLOW)
            self.answerlabel.place(x=90,y=295)
            self.question_answered_label = CTkLabel(self.tf_window, text = 'Answers Correct', font =  ("Segoe UI Black", 15, "bold"), bg_color=YELLOW )
            
            # Makes a rough estimate on where the user's name will be displayed depending on its length
            if len(self.username) > 6:
                x = 60
            else:
                x=80
            self.question_answered_label.place(x=x,y=270)
            
            #Displays a crown image and the User's name
            self.name_display = CTkLabel(self.tf_window,text=self.username, font=fontlabel,bg_color=YELLOW)
            self.name_display.place(x=175,y=200)
            self.crown_img = CTkImage(light_image=Image.open('images/crown.png'), dark_image=Image.open('images/crown.png'),size=(160,130))
            self.crown_display = CTkLabel(self.tf_window,text='',image=self.crown_img,bg_color=YELLOW)
            self.crown_display.place(x=175,y=75)

            #Uploads the user's score , name and amount of time they took to finsh the quiz
            with open("database.json", "r") as file:
                data = json.load(file)
    
            score_key = f"{self.answers_correct}/10"
    
            data["tf"][score_key].append([self.username, score_key, str(round(self.stopwatch.duration,2))])

            with open("database.json", "w") as file:
                json.dump(data, file, indent=4)
                
                
            


    def true_button_cmd(self):# sets the value of user response to True and checks answer
        self.user_response = True
        self.check_answer()
        
    def false_button_cmd(self):# sets the value of user response to False and checks answer
        self.user_response = False
        self.check_answer()


    def check_answer(self):
        #Destroys all components of the window except the App name
        self.true_button.destroy()
        self.false_button.destroy()
        self.canvas.destroy()
        self.current_score_display.destroy()
        #Checks if user's response matches with the question baser 
        if self.user_response == self.question_baser:
            self.answers_correct += 1 #adds 1 to the amount of questions the user correctly answered
        else:
            self.answers_correct = self.answers_correct
        
        
        self.generate_questions()#goes to next question


    def get_name(self):# Displays all the components which are used to get the users name 
            self.name_entry_box = CTkEntry(self.tf_window, placeholder_text='     NAME', font=fontlabel,height=105,width=305)
            self.name_entry_box.place(x=100,y=100)
            self.play_button = CTkButton(self.tf_window, text = 'LETS PLAY', font=buttonfonts,text_color='white', fg_color='#FFC773', command=self.name_input, width=150,height=50 )
            self.play_button.place(x=180,y=290)
            self.error_input = CTkLabel(self.tf_window, text='The name must be less than 10 letters and must not include any spaces or symbols', text_color='red', bg_color=YELLOW, font=('Arial',9,'bold'))
            self.error_input.place(x=70, y=210)
            self.proceed = False
            self.tf_window.mainloop() 

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



    def back_home(self):# Destroys the True/False quiz and starts the Homepage
        
        self.tf_window.destroy()
        import homepage
        home = homepage.HomePage()