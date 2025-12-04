import tkinter as tk
from tkinter import RIGHT, END, DISABLED, NORMAL 

#1st DEAL WITH LAYOUT OF CALCULATOR 
#define the window 
root = tk.Tk() 
root.title("CS112 Calculator") 
root.geometry("340x400") #specifies the shape of window 
root.resizable(0,0) #tow 0's (booleans) means don't resize on the x or y axis 

#define colors and fonts 
darkOrange = "#e07b39" 
lightOrange = "#80931e" 
whiteOrange = "#edb879" 
fontButtons = ("Arial", 18) 
fontDisplay = ("Arial", 30)
btnMultiply = tk.Button(root, text="multiply")
btnDivide = tk.Button(root, text="divide")
btnDecimal = tk.Button(text='decimal')



#function definitions 
def submitNumber(number): 
    """add a number or decimal to the display (Docstring)""" 
    display.insert(END, number)
    if "." == display.get(): 
        btnDecimal.config(state=DISABLED)

def operation(operator): 
    """store the first number of the expression and the operator to be used""" 
    global firstNumber 
    global operation 

    #get the operator and the value of the display (the first number in the calculation) 
    operation = operator
    firstNumber = display.get() 

    #delete the value from the display
    display.delete(0,END) 
    
    #disable all operator buttons until equal or clear is pressed 
    btnAddition.config(state=DISABLED)
    btnSubtract.config(state=DISABLED)
    btnMultiply.config(state=DISABLED)
    btnDivide.config(state=DISABLED)
    btnExponent.config(state=DISABLED)
    btnInverse.config(state=DISABLED)
    btnSquare.config(state=DISABLED)
#enable decimal button for the next number Entry
btnDecimal.config(state=NORMAL)

def equal(): 
    """run the stored operation for two number""" 
    if operation == "add": 
        value = float(firstNumber) + float(display.get()) 
    elif operation == "subtract": 
        value = float(firstNumber) - float(display.get()) 
    elif operation == "multiply": 
        value = float(firstNumber) * float(display.get()) 
    elif operation == "divide": 
        if display.get() == "0": 
            value = "ERROR" 
        else: 
            value = float(firstNumber) / float(display.get()) 
    elif operation == "expononet": 
        value = float(firstNumber) ** float(display.get())

    #clear the display and update it withthe operation result
    display.delete(0, END)
    display.insert(0, value) 

    #return button to normal state
    enableOperationButtons
btnMultiply = tk.Button(root, text="multiply")
btnDivide = tk.Button(root, text="divide")
def enableOperationButtons(): 
    btnAddition.config(state=NORMAL)
    btnSubtract.config(state=NORMAL)
    btnMultiply.config(state=NORMAL)
    btnDivide.config(state=NORMAL)
    btnExponent.config(state=NORMAL)
    btnInverse.config(state=NORMAL)
    btnSquare.config(state=NORMAL)
    btnDecimal.config(state=NORMAL) 

def clear(): 
    """clear the display button""" 
    display.delete(0, END) 
    #return buttons to normal state
    enableOperationButtons

def inverse(): 
    """calculate the inverse of a given number""" 
    if display.get() == "0":
        value = "ERROR" 
    else: 
        value = 1.0 / float(display.get()) 

    #clear display and update it with the result 
    display.delete(0, END) 
    display.insert(0, value)

#graphical user interface layout 
frameDisplay = tk.LabelFrame(root) 
frameButton = tk.LabelFrame(root) 

frameDisplay.pack(padx=2, pady=(5,30)) 
#controls layout of GUI's items 
frameButton.pack(padx=2, pady=5) 

display = tk.Entry(frameDisplay, width = 50, font=fontDisplay, bg=whiteOrange, borderwidth= 5, justify=RIGHT)
display.pack(padx=5, pady=5) 

#second work with the frameButton 
frameButton.place(x=50, y=50)

btnClear = tk.Button(frameButton, text="Clear", font=fontButtons, bg=darkOrange, command=clear)
btnQuiz = tk.Button(frameButton, text="Quit", font=fontButtons, bg=darkOrange, command=clear)

btnInverse = tk.Button(frameButton, text="1/x", font=fontButtons, bg=lightOrange)
btnSquare = tk.Button(frameButton, text="x^2", font=fontButtons, bg=lightOrange)
btnExponent = tk.Button(frameButton, text="x^y", font=fontButtons, bg=lightOrange)
btnDivided = tk.Button(frameButton, text="/", font=fontButtons, bg=lightOrange)
btnMultiple = tk.Button(frameButton, text="*", font=fontButtons, bg=lightOrange)
btnSubtract = tk.Button(frameButton, text="-", font=fontButtons, bg=lightOrange)
btnAddition = tk.Button(frameButton, text="+", font=fontButtons, bg=lightOrange)

btnEquals = tk.Button(frameButton, text="=", font=fontButtons, bg=darkOrange)
btnDecimal = tk.Button(frameButton, text=".", font=fontButtons, bg="white", fg="black")
btnNegate = tk.Button(frameButton, text="+/-", font=fontButtons, bg="white", fg="black")

btn9 = tk.Button(frameButton, text="9", font=fontButtons, bg="white", fg="black")
btn8 = tk.Button(frameButton, text="8", font=fontButtons, bg="white", fg="black")
btn7 = tk.Button(frameButton, text="7", font=fontButtons, bg="white", fg="black")
btn6 = tk.Button(frameButton, text="6", font=fontButtons, bg="white", fg="black")
btn5 = tk.Button(frameButton, text="5", font=fontButtons, bg="white", fg="black")
btn4 = tk.Button(frameButton, text="4", font=fontButtons, bg="white", fg="black")
btn3 = tk.Button(frameButton, text="3", font=fontButtons, bg="white", fg="black")
btn2 = tk.Button(frameButton, text="2", font=fontButtons, bg="white", fg="black")
btn1 = tk.Button(frameButton, text="1", font=fontButtons, bg="white", fg="black")
btn0 = tk.Button(frameButton, text="0", font=fontButtons, bg="white", fg="black")
tk.mainloop()