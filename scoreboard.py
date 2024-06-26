from customtkinter import *
from PIL import Image, ImageTk

import json

# Predefined constants : These are values which are going to be used across the application 
ORANGE = '#FFb900'
YELLOW  = '#FFF370'
fontlabel = ("Segoe UI Black", 40, "bold")
buttonfonts = ("Segoe UI Black", 20, "bold")

class Scoreboard():
    def __init__(self):

        # Window setup
        self.scoreboard_window = CTk()
        self.scoreboard_window.minsize(width=600,height=400)# Sets the window dimensions
        self.scoreboard_window.maxsize(width=600,height=400)# Sets the window dimensions
        self.scoreboard_window.resizable(False,False)
        self.scoreboard_window.config(bg=YELLOW)# Sets the window color

        # Displays the App name at the top of the window
        self.app_name = CTkLabel(self.scoreboard_window,text = 'Math Geniuses', text_color=ORANGE,bg_color=YELLOW, font=fontlabel )
        self.app_name.place(x=155,y=0)

        # Lists which contain the top 10 performers of each quiz
        self.tf_scores = self.get_top_10_tf_results()
        print(self.tf_scores)
        self.mcq_scores = self.get_top_10_mcq_results()
        print(self.mcq_scores)

        # Initialises and displays the back home button (allows the user to return back home )
        self.back_home = CTkButton(self.scoreboard_window, text='home', bg_color=YELLOW, font=("Segoe UI Black", 10, "bold"), command=self.back_home, width=70, height=10, fg_color=ORANGE, hover_color='#ff7b00')
        self.back_home.place(x=0,y=0)

        # these are coordinates which are going to be used to display the results in a list format
        self.tf_y_cords = 100
        self.mcq_y_cords = 100

        # Labels which shows which category of results are begin displayed
        self.mcq_name = CTkLabel(self.scoreboard_window, text = 'Multiple Choice', font = ("Segoe UI Black", 25, "bold"), bg_color=YELLOW, width=40, text_color=ORANGE)
        self.mcq_name.place(x=320, y=80)

        self.tf_name = CTkLabel(self.scoreboard_window, text = 'True / False', font = ("Segoe UI Black", 25, "bold"), bg_color=YELLOW, width=40, text_color=ORANGE)
        self.tf_name.place(x=50, y=80)

        for names in self.tf_scores: # Loops through the list and displays the results on the window for True/False quiz
            self.tf_y_cords +=25
            self.name = names[0]
            self.score = names[1]
            self.time = names[2]
            self.details = (f'{self.name} , {self.score}, {self.time}')
            self.name_display = CTkLabel(self.scoreboard_window, text = self.details, font = buttonfonts, bg_color=YELLOW, width=40, text_color='#dc2f02')
            self.name_display.place(x=50, y=self.tf_y_cords)

        for names in self.mcq_scores:# Loops through the list and displays the results on the window for Multiple choice quiz
            self.mcq_y_cords +=25
            self.name = names[0]
            self.score = names[1]
            self.time = names[2]
            self.details = (f'{self.name} , {self.score}, {self.time}')
            self.name_display = CTkLabel(self.scoreboard_window, text = self.details, font = buttonfonts, bg_color=YELLOW, width=40, text_color='#dc2f02')
            self.name_display.place(x=320, y=self.mcq_y_cords)



        
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
    

    def back_home(self):# Destroys the Scoreboard page and starts the Homepage
        
        self.scoreboard_window.destroy()
        import homepage
        home = homepage.HomePage()
        

