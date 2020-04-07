from tkinter import *


root = Tk()
root.title("Character Selection")
root.geometry("200x200")

welcome = Label(text="Choose a class\n")
welcome.grid(column=0)


class Character:
    def __init__(self, c_class, c_atk, c_def, c_hp):
        self.c_class = c_class
        self.c_atk = c_atk
        self.c_def = c_def
        self.c_hp = c_hp

        def selection():
            print(self.c_class)
            myselection = Label(text="You selected: " + self.c_class)
            myselection.grid(column=0)

        c_class = Button(text=self.c_class, command=selection)
        c_class.grid(column=0)


assasin = Character("Assasin", 40, 25, 250)
mage = Character("Mage", 30, 15, 350)
tank = Character("Tank", 15, 55, 500)
healer = Character("Healer", 10, 20, 300)



root.mainloop()