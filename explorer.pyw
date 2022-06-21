from tkinter import *
from tkinter import filedialog
import os

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/",
                                          title="Open file:",
                                          filetypes= (("All files","*.*"),
                                          ("Text files","*.txt")))
    os.startfile(filepath)

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()