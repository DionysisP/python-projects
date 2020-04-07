from tkinter import *
from random import randint
import random

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("200x200")


your_selection = ""
ai_selection = ""

p1_wins = 0
ai_wins = 0

rounds = 1

options = ["Rock", "Paper", "Scissor"]


def check_winner():
    global ai_wins
    global p1_wins

    #Generate random choice for computer
    ai_selection = random.choice(options)
    global rounds
    print("ROUND ", end="")
    print(rounds)
    print("Your selection : " + your_selection)
    print("Computer selection : " + ai_selection)

    #Check you wins this round
    if your_selection == ai_selection:
        print("DRAW")
    #Bad code here
    elif your_selection == "Rock" and ai_selection == "Paper" or your_selection == "Paper" and ai_selection == "Scissor" or your_selection == "Scissor" and ai_selection == "Rock":
        print("You lose")

        ai_wins = ai_wins + 1

    elif your_selection == "Rock" and ai_selection == "Scissor" or your_selection == "Scissor" and ai_selection == "Paper" or your_selection == "Paper" and ai_selection == "Rock":
        print("You win")

        p1_wins = p1_wins + 1

    rounds = rounds + 1
    #print("Total rounds : ", end="")
    #print(rounds)
    print("____________________________________")
    print("Score")
    print("You : ", end=""), print(p1_wins)
    print("Computer : ", end="")
    print(ai_wins)
    print("____________________________________")

#Also bad code, still learning
def selection1():
    global your_selection
    global ai_selection
    your_selection = options[0]
    return check_winner()


def selection2():
    global your_selection
    global ai_selection
    your_selection = options[1]
    return check_winner()


def selection3():
    global your_selection
    global ai_selection
    your_selection = options[2]
    return check_winner()


button1 = Button(text=options[0], command=selection1)
button1.pack()

button2 = Button(text=options[1], command=selection2)
button2.pack()

button3 = Button(text=options[2], command=selection3)
button3.pack()


window.mainloop()