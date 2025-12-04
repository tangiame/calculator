# standard import tkinter
from tkinter import *
# declare a window
rootw = Tk()
# naming a window whatever i want
rootw.title("PaisaSoft")
#make an entry widget in order to access terminal
e1 = Entry(rootw, width=20, bg = "hot pink", fg = "green")
l1 = Label(rootw, text='Please enter name', font = "Arial")
# placing on window
e1.grid(column=0 , row=0)
l1.grid(column=0 , row=1)
# do this to open window
rootw.mainloop()

import numpy as np
#make numpy array
print("my numpy array is,")
arr1d = np.array([1, 2, 3, 4, 5])







