from tkinter import * #Imports the GUI module
from tkinter import messagebox
import os
import time
import easter_egg
import view_menu
import help_menu
import edit_menu



root = Tk() #sets the root to Tk
root.title("Calculator 0.0.1")
frame = LabelFrame(root, borderwidth = 5)

menubar = Menu(root)
root.config(menu = menubar)

#Code for display screen
display = Entry(frame, width = 35, borderwidth = 5)
display.grid(row = 0 , column = 0, columnspan = 4, ipady = 15) #Screen configuration



#FUNCTIONS

#Function to activate the easter egg
def easter_egg():
    request = messagebox.askquestion(title = "Easter egg", message = "Congratulations! You have activated the easter egg\nDo you want to continue?") #Asks the user if he wants to activate the easter egg
    if request == "no":
        os.system("exit")
    else:
        question = messagebox.askquestion(title = "Easter egg", message = "In order to unlock the easter egg, you will have to answer three simple questions\nWill you?")
        if question == "no":
            os.system("exit")
        else:
            global display
            display.delete(0,END)
            display.configure(state = "normal" )
            display.insert(0, "Your questions will appear soon")


#Fucntion for click
def click(object):
    current = display.get() #Takes in the first number the user enters to prevent it from being read from right to left
    display.delete(0, END) #CLears the input from the display screen
    current = str(current)
    display.insert(0,str(current) + str(object))

#Function for DEL
def backspace(): #Delete only one character from the input display
    number = display.get()
    then = number[:-1]
    display.delete(0,END)
    display.insert(0,then)


#Function for AC
def AC():
    display.delete(0, END)
    button_del.configure(state = "normal")
    display.configure(state = "normal")
    display.delete(0,END)
#Function for equal sign
def equal():
    try:
        equation = display.get() #Takes all the data from the screen and assigns it to "equation"
        if "//" in equation:
            display.delete(0, END)
            display.insert(0, "Syntax Error")
            button_del.configure(state = "disabled")
            display.configure(state = "disabled")

        elif "**" in equation:
            display.delete(0 ,END)
            display.insert(0, "Syntax Error")
            button_del.configure(state = "disabled")
            display.configure(state = "disabled")

        elif "(0249005710)" in equation:
            easter_egg()
        else:
            display.delete(0, END)
            equation = str(equation) #Converts the equation into string format
            display.delete(0, END) #Deletes all the data from the screen
            display.insert(3, eval(equation)) #Displays the right answer
    except SyntaxError:
        display.delete(0 ,END)
        display.insert(0, "Syntax Error")
        button_del.configure(state = "disabled")
        display.configure(state = "disabled")
    except NameError:
        display.delete(0, END)
        display.insert(0, "Syntax Error")
        button_del.configure(state="disabled")
        display.configure(state="disabled")


#Codes for number buttons
button_1 = Button(frame, text = "1", command = lambda : click(1), padx = 20, pady = 20)
button_2 = Button(frame, text = "2", command = lambda : click(2), padx = 20, pady = 20)
button_3 = Button(frame, text = "3", command = lambda : click(3), padx = 20, pady = 20)
button_4 = Button(frame, text = "4", command = lambda : click(4), padx = 20, pady = 20)
button_5 = Button(frame, text = "5", command = lambda : click(5), padx = 20, pady = 20)
button_6 = Button(frame, text = "6", command = lambda : click(6), padx = 20, pady = 20)
button_7 = Button(frame, text = "7", command = lambda : click(7), padx = 20, pady = 20)
button_8 = Button(frame, text = "8", command = lambda : click(8), padx = 20, pady = 20)
button_9 = Button(frame, text = "9", command = lambda : click(9), padx = 20, pady = 20)
button_0 = Button(frame, text = "0", command = lambda : click(0), padx = 20, pady = 20)

#Gridding system for number buttons

button_1.grid(row = 1 , column = 0)
button_2.grid(row = 1 , column = 1)
button_3.grid(row = 1 , column = 2)
button_4.grid(row = 2 , column = 0)
button_5.grid(row = 2 , column = 1)
button_6.grid(row = 2 , column = 2)
button_7.grid(row = 3 , column = 0)
button_8.grid(row = 3 , column = 1)
button_9.grid(row = 3 , column = 2)
button_0.grid(row = 4 , column = 0)

#Codes for symbols
button_point = Button(frame, text = ".",padx =22, pady = 20, command = lambda : click("."))
button_bracket1 = Button(frame, text = "(",padx =22, pady = 20, command = lambda : click("("))
button_bracket2 = Button(frame, text = ")",padx =22, pady = 20, command = lambda : click(")"))
button_ac= Button(frame, text = "AC", fg = "red",padx =15, pady = 20 , command = AC)
button_del = Button(frame, text = "DEL", fg = "red",padx =14, pady = 20 ,command = backspace)
button_plus = Button(frame, text = "+", padx =19, pady = 20, command = lambda : click('+'))
button_minus = Button(frame, text = "-", padx = 20.500, pady = 20, command = lambda : click("-"))
button_divide = Button(frame, text = "÷", padx = 19.400, pady = 20, command = lambda : click("/"))
button_add = Button(frame, text = "+", padx = 22, pady = 20, command = lambda : click("+"))
button_multiply = Button(frame, text = "×", padx = 19, pady = 20 , command = lambda :click("*"))
button_equal = Button(frame, text = "=", fg = "green", pady = 20, padx = 19, command = equal)
#Gridding system for symbols
button_bracket1.grid(row = 4, column = 1)
button_bracket2.grid(row = 4, column = 2)
button_point.grid(row = 5, column = 0)
button_del.grid(row =5, column = 1)
button_ac.grid(row = 5, column = 2)
button_plus.grid(row = 1, column =3)
button_divide.grid(row = 2, column =3)
button_minus.grid(row = 2, column = 3)
button_divide.grid(row = 3, column = 3)
button_multiply.grid(row = 4, column = 3)
button_equal.grid(row = 5, column = 3)



view_menu.main(root, menubar)
edit_menu.main(root, menubar)
help_menu.main(root, menubar)

frame.grid(row =0, column = 0)
root.resizable(width= False, height= False)
root.mainloop() #End of the program
