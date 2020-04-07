
from tkinter import *
from tkinter import messagebox  
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    db = "mydatabase"
)

cursor = mydb.cursor()

window = Tk()
window.geometry("350x200")
window.title("This is the best GUI program!")

def insert():
    print("\nfunction works perfectly!")
    name_taken = name.get()
    age_taken = age.get()

    print(len(name_taken))
    
    if name_taken == "" or  age_taken == "":
        messagebox.showinfo("Error","Insert all data")
    else:
        sql = "INSERT INTO users (user_name, user_age) VALUES (%s, %s)"
        val = name_taken, age_taken
        cursor.execute(sql,val)
        mydb.commit()



name_label = Label(text="Name : ")
name_label.grid(row=0, column=0)
name = Entry()
name.grid(row=0, column=1)


age_label = Label(text="Age : ")
age_label.grid(row=1, column=0)
age = Entry()
age.grid(row=1, column=1)

confirm = Button(text="Add person", command=insert)
confirm.grid(row=3)


window.mainloop()