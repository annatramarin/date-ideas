# From the shell:
# pip install tkinter

# Import lists
general = open("./general.txt", "r", encoding='utf-8').read().split("\n")
winter = open("./winter.txt", "r", encoding="utf-8").read().split("\n")
spring = open("./spring.txt", "r", encoding="utf-8").read().split("\n")
summer = open("./summer.txt", "r", encoding="utf-8").read().split("\n")
autumn = open("./autumn.txt", "r", encoding="utf-8").read().split("\n")


# Pick a random activity from the list
import random

# def date_ideas(nome_lista):
    # ideas = random.choice(nome_lista)
    # return ideas

import tkinter
from tkinter import *
from tkinter import ttk

TITLE_FONT = ("Comic Sans MS", "16")
BUTTON_FONT = ("Comic Sans MS", "12")
OUTCOME_FONT = ("Comic Sans MS", "11")

#Create an instance of Tkinter frame
window = tkinter.Tk()
window.title("Date ideas")

#Set the geometry of the Tkinter frame
window.geometry("500x500")

l = Label(window, text="Welcome! \n Would you like to choose a season?", font=TITLE_FONT)   
l.pack()

def no():
    s = "Okay, then... {}".format(str(random.choice(general)))
    label_no_yes['text'] = s

def haru():
    fruehling = "Then... {}".format(str(random.choice(spring)))
    label_seasons['text'] = fruehling 
    
def natsu():
    sommer = "Then... {}".format(str(random.choice(summer)))
    label_seasons['text'] = sommer 
    
def aki():
    herbst = "Then... {}".format(str(random.choice(autumn)))
    label_seasons['text'] = herbst 

def fuyu():
    Winter = "Then... {}".format(str(random.choice(winter)))
    label_seasons['text'] = Winter
    
def yes():
    scelta = "What season is it?"
    label_no_yes['text'] = scelta
    
    button_spring = Button(window, text= "Spring", font= BUTTON_FONT, command=haru)   
    button_spring.pack()
    button_spring.place(relx = 0.5,
                   rely = 0.43,   
                   anchor = 'center')
    
    button_summer = Button(window, text= "Summer", font= BUTTON_FONT, command=natsu)   
    button_summer.pack()
    button_summer.place(relx = 0.5,
                   rely = 0.51,
                   anchor = 'center')
    
    button_autumn = Button(window, text= "Autumn", font= BUTTON_FONT, command=aki)   
    button_autumn.pack()
    button_autumn.place(relx = 0.5,
                   rely = 0.59,
                   anchor = 'center')
    
    button_winter = Button(window, text= "Winter", font= BUTTON_FONT, command=fuyu)   
    button_winter.pack()
    button_winter.place(relx = 0.5,
                   rely = 0.67,
                   anchor = 'center')
    
    
button1 = Button(window, text='Yes', font= BUTTON_FONT, command=yes)  
button1.place(relx = 0.5,
                   rely = 0.15,
                   anchor = 'center')
button1.pack()

button2 = Button(window, text='No', font= BUTTON_FONT, command=no)   
button2.pack()

label_no_yes = Label(window, font=OUTCOME_FONT)
label_no_yes.pack()
label_no_yes.place(relx = 0.5,
                   rely = 0.35,
                   anchor = 'center')

label_seasons = Label(window, font=OUTCOME_FONT)
label_seasons.pack()
label_seasons.place(relx = 0.5,
                   rely = 0.8,
                   anchor = 'center')
                                  
window.mainloop()
