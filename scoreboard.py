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
        self.scoreboard_img = CTkImage(light_image = Image.open('images/scoreboard4.png'), dark_image=Image.open('images/scoreboard4.png'),size=(500,380))
        self.scorebaord_display = CTkLabel(self.scoreboard_window,text='',image=self.scoreboard_img,bg_color= YELLOW)
        self.scorebaord_display.place(x=0,y= 40)
        self.app_name = CTkLabel(self.scoreboard_window,text = 'Math Geniuses', text_color=ORANGE,bg_color=YELLOW, font=fontlabel )
        self.app_name.place(x=105,y=0)

        self.tf_scores = self.get_top_10_tf_results()
        print(self.tf_scores)
        self.mcq_scores = self.get_top_10_mcq_results()
        print(self.mcq_scores)

        self.home_button = CTkButton(self.scoreboard_window, text = 'Home', bg_color=YELLOW, command=self.home)
        self.home_button.place(x=0,y=0)



        
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
    

    # def home(self):
    #     self.scoreboard_window.destroy()
    #     home = homepage.HomePage()
        

