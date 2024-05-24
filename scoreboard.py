from customtkinter import *
from PIL import Image, ImageTk

import json


ORANGE = '#FFb900'
YELLOW  = '#FFF370'
fontlabel = ("Segoe UI Black", 40, "bold")
buttonfonts = ("Segoe UI Black", 20, "bold")

class Scoreboard():
    def __init__(self):


        self.scoreboard_window = CTk()
        self.scoreboard_window.minsize(width=500,height=400)
        self.scoreboard_window.maxsize(width=500,height=400)
        self.scoreboard_window.resizable(False,False)
        self.scoreboard_window.config(bg=YELLOW)
        # self.scoreboard_img = CTkImage(light_image = Image.open('images/scoreboard4.png'), dark_image=Image.open('images/scoreboard4.png'),size=(500,380))
        # self.scoreboard_display = CTkLabel(self.scoreboard_window,text='',image=self.scoreboard_img,bg_color= YELLOW)
        # self.scoreboard_display.place(x=0,y= 40)
        self.app_name = CTkLabel(self.scoreboard_window,text = 'Math Geniuses', text_color=ORANGE,bg_color=YELLOW, font=fontlabel )
        self.app_name.place(x=105,y=0)

        self.tf_scores = self.get_top_10_tf_results()
        print(self.tf_scores)
        self.mcq_scores = self.get_top_10_mcq_results()
        print(self.mcq_scores)

        self.back_home = CTkButton(self.scoreboard_window, text='home', bg_color=YELLOW, font=("Segoe UI Black", 10, "bold"), command=self.back_home, width=70, height=10)
        self.back_home.place(x=0,y=0)

        self.tf_y_cords = 100
        self.mcq_y_cords = 100

        self.mcq_name = CTkLabel(self.scoreboard_window, text = 'Multiple Choice', font = ("Segoe UI Black", 25, "bold"), bg_color=YELLOW, width=40, text_color=ORANGE)
        self.mcq_name.place(x=270, y=80)

        self.tf_name = CTkLabel(self.scoreboard_window, text = 'True / False', font = ("Segoe UI Black", 25, "bold"), bg_color=YELLOW, width=40, text_color=ORANGE)
        self.tf_name.place(x=50, y=80)

        for names in self.tf_scores:
            self.tf_y_cords +=25
            self.name = names[0]
            self.score = names[1]
            self.time = names[2]
            self.details = (f'{self.name} , {self.score}, {self.time}')
            self.name_display = CTkLabel(self.scoreboard_window, text = self.details, font = buttonfonts, bg_color=YELLOW, width=40, text_color='#dc2f02')
            self.name_display.place(x=50, y=self.tf_y_cords)

        for names in self.mcq_scores:
            self.mcq_y_cords +=25
            self.name = names[0]
            self.score = names[1]
            self.time = names[2]
            self.details = (f'{self.name} , {self.score}, {self.time}')
            self.name_display = CTkLabel(self.scoreboard_window, text = self.details, font = buttonfonts, bg_color=YELLOW, width=40, text_color='#dc2f02')
            self.name_display.place(x=270, y=self.mcq_y_cords)



        
        self.scoreboard_window.mainloop()


    def get_top_10_tf_results(self):
    # Load the JSON data from the file
        with open("database.json", "r") as file:
            data = json.load(file)

    # Initialize a list to collect all results
        self.all_results = []

    # Iterate over each score category for the TF quiz and collect results
        for score_category, results in data["tf"].items():
            self.all_results.extend(results)

    # Sort the collected results first by score (descending) and then by time taken (ascending)
        self.all_results.sort(key=lambda x: (-int(x[1].split('/')[0]), float(x[2])))

    # Return the top 10 results
        return self.all_results[:10]
    
    
    def get_top_10_mcq_results(self):
    # Load the JSON data from the file
        with open("database.json", "r") as file:
            data = json.load(file)

    # Initialize a list to collect all results
        self.all_results = []

    # Iterate over each score category for the MCQ quiz and collect results
        for score_category, results in data["mcq"].items():
            self.all_results.extend(results)

    # Sort the collected results first by score (descending) and then by time taken (ascending)
        self.all_results.sort(key=lambda x: (-int(x[1].split('/')[0]), float(x[2])))

    # Return the top 10 results
        return self.all_results[:10]
    

    def back_home(self):
        
        self.scoreboard_window.destroy()
        import homepage
        home = homepage.HomePage()
        

