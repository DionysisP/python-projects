from tkinter import *

window = Tk()
window.geometry("200x200")


def create_file():

    f_title = file_title.get()
    f_h1 = h1.get()
    f_h1 = "<h1>" + f_h1 + "</h1>"
    print(f_h1)

    f = open("index.html", "w+")
    f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>" + f_title + "</title>\n<link rel='stylesheet' href='styles.css'>\n</head>\n<body>\n" + f_h1 + "\n</body>\n</html>")
    print("File created!")


create_f = Button(text="add html file", command=create_file)
create_f.pack()

file_title = Entry(window)
file_title.pack()

h1 = Entry(window)
h1.pack()

window.mainloop()
