from tkinter import *

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 

def create_new_file():
	print("Creating a new file.")

menu = Menu(root)

# File tab
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "New File", command = create_new_file)
menu_file.add_command(label = "New Window")
menu_file.add_separator()
menu_file.add_command(label = "Open...")
menu_file.add_separator()
menu_file.add_command(label = "Save All", state = "disable")
menu_file.add_separator()
menu_file.add_command(label = "Exit", command = root.quit)
menu.add_cascade(label = "File", menu = menu_file)

# Edit tab
edit_file = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Edit", menu = edit_file)

# Language tab
menu_lang = Menu(menu, tearoff = 0)
menu_lang.add_radiobutton(label = "Python")
menu_lang.add_radiobutton(label = "Java")
menu_lang.add_radiobutton(label = "C++")
menu.add_cascade(label = "Language", menu = menu_lang)

# Viewmeanu tab
menu_view = Menu(menu, tearoff =0)
menu_view.add_checkbutton(label = "Show Minimap")
menu.add_cascade(label = "View", menu = menu_view)

# keeping the GUI window open. 
root.config(menu=menu)
root.mainloop()