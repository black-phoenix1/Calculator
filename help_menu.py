from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Help:
	def about_message():
		showinfo(title = "About calculator", message = "All-Purpose Calculator\nVersion 0.0.1\nFor more info: lucretiusbiah15@gmail.com ")

	def source_code():
		showinfo(title ="Source code", message = "This program is open source\nAnyone is free to edit and re-distribute the source code.")

	def help_message():
		showinfo(title = "Calculator ", message = """This calculator is used to perform simple arithmetic operations and even complex ones.\nIt is still under development and you are sure to experience a few bugs, if that happens, kindly email me the bug and I will fix it in the next update\nCOMMON ERRORS AND SOLUTIONS
	*Pressing in the '=' sign without any equation produces a Syntax Error and disabled the screen. Just press the 'AC' to revert to normal
	*In any case where you recieve a Syntax Error, the AC key reverts everything back to normal.
		""")



	def help(menubar):
		help_menu = Menu(menubar, tearoff = 0)
		help_menu.add_command(label = "View help", command = Help.help_message)
		help_menu.add_command(label = "About", command = Help.about_message)
		help_menu.add_separator()
		help_menu.add_command(label = "Source code", command = Help.source_code)
		menubar.add_cascade(label = "Help", menu = help_menu)






def main(root, menubar):
	Help.help(menubar)

	


if __name__ == "__main__":
	print("Please run main")