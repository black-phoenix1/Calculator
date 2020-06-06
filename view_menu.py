from tkinter import *

"""This is the part of the program which describes the view meunu"""


class View:

    def date(a):
        print(a)

    def view(menubar):
        view_menu = Menu(menubar, tearoff=0)
        view_menu.add_command(label="Basic mode")
        view_menu.add_separator()
        view_menu.add_command(label="Algebraic Expressions")
        view_menu.add_command(label="Shapes and Figures")
        view_menu.add_separator()
        view_menu.add_command(label="Unit Conversions")
        view_menu.add_command(label="Date Calculations", command=View.date)
        menubar.add_cascade(label="View", menu=view_menu)


def main(root, menubar):
    View.view(menubar)


if __name__ == "__main__":
    print("Please run main")
