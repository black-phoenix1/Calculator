from tkinter import *

"""This is the part of the program which describes the view meunu"""


class View:
    def date(root):
        date_frame = LabelFrame(root, background = "light green")
        label = Label(date_frame, text = "Select the type of date calculation").grid(row = 0, column = 0)
        clicked = StringVar()

        drop_down = OptionMenu(date_frame, clicked, "Calculate difference between dates","Add or subtract to a specified date         ").grid(row = 1, column = 0)
        date_frame.grid(row =0, column = 1)













    def view(menubar, root):
        view_menu = Menu(menubar, tearoff=0)
        view_menu.add_command(label="Basic mode")
        view_menu.add_separator()
        view_menu.add_command(label="Algebraic Expressions")
        view_menu.add_command(label="Shapes and Figures")
        view_menu.add_separator()
        view_menu.add_command(label="Unit Conversions")
        view_menu.add_command(label="Date Calculations", command = lambda : View.date(root))
        menubar.add_cascade(label="View", menu=view_menu)


def main(root, menubar):
    View.view(menubar, root)


if __name__ == "__main__":
    print("Please run main")
