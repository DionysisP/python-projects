from tkinter import *

window = Tk()
window.geometry()
window.title("Chords")


notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def generate_major_chords():
    root_note = 0
    third_note = 4
    fifth_note = 7

    class MajorChords:
        def __init__(self, root, third, fifth):
            self.root = root
            self.third = third
            self.fifth = fifth

    for i in range(12):

        # in case list run out of values
        if len(notes) <= 12:
            # extend the list with itself
            notes.extend(notes)
        else:
            # create objects
            notes[0] = MajorChords(notes[root_note], notes[third_note], notes[fifth_note])
            #res = notes[0].root + " Major : " + notes[0].root, notes[0].third, notes[0].fifth
            print(notes[0].root + " Major : " + notes[0].root, notes[0].third, notes[0].fifth)

            """t = Text(window, width=22, height=2)
            t.insert(INSERT, res)
            t.pack()"""

            root_note += 1
            third_note += 1
            fifth_note += 1

"""def generate_minor_chords():
    root_note = 0
    third_note = 3
    fifth_note = 7

    class MinorChords:
        def __init__(self, root, third, fifth):
            self.root = root
            self.third = third
            self.fifth = fifth

    for i in range(12):

        # in case list run out of values
        if len(notes) <= 12:
            # extend the list with itself
            notes.extend(notes)
        else:
            # create objects
            notes[0] = MinorChords(notes[root_note], notes[third_note], notes[fifth_note])
            res2 = notes[0].root + " Minor : " + notes[0].root, notes[0].third, notes[0].fifth
            print(notes[0].root + " Minor : " + notes[0].root, notes[0].third, notes[0].fifth)

            t2 = Text(window, width=22, height=2)
            t2.insert(INSERT, res2)
            t2.pack()

            root_note += 1
            third_note += 1
            fifth_note += 1

"""
gen_maj = Button(text="Generate Major Chords", command=generate_major_chords)
gen_maj.pack()

"""
gen_min = Button(text="Generate Minor Chords", command=generate_minor_chords)
gen_min.pack()
"""


window.mainloop()