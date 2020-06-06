from tkinter import *


class Edit:
	def edit(menubar):
		edit_menu = Menu(menubar, tearoff = 0)
		edit_menu.add_command(label = "Copy     Ctrl+C")
		edit_menu.add_command(label = "Paste    Ctrl+V")
		menubar.add_cascade(label = "Edit", menu = edit_menu)







def main(root, menubar):
	Edit.edit(menubar)