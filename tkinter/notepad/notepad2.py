import os
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile 

# opening the GUI window
root = Tk()

root.title("MY NOTE")
root.geometry("640x580")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(True, True) # x, y resizable is disabled. 

# Defining the actions of each tab. 
def create_new_file():
	print("Creating a New File...")

def create_new_window():
	print("Creating a New Window...")

def open_file():
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
    if file is not None: 
        content = file.read() 
        print(content)
	# if os.path.isfile(filename):
	# 	with open(filename, "r", encoding="utf8") as file:
	# 		txt.delete("1.0", END)
	# 		txt.insert(END, file.read())

def save_file(): 
	format = [("All Format", "*.*"),  
        		("Python Format", "*.py"), 
          		("Text Format", "*.txt")] 
	file = asksaveasfile(filetypes = format, defaultextension = format)

# Defining a Menu function. 
menu = Menu(root)

# Creating File tab.
file_tab = Menu(menu, tearoff=0)
file_tab.add_command(label = "New File", command = create_new_file)
file_tab.add_command(label = "New Window", command = create_new_window)
file_tab.add_separator()
file_tab.add_command(label = "Open...", command = open_file)
file_tab.add_separator()
file_tab.add_command(label = "Save", command = lambda : save_file())
file_tab.add_separator()
file_tab.add_command(label = "Exit", command=root.quit)
menu.add_cascade(label = "File", menu = file_tab)  # showing up on the menu bar.

# Creating Edit tab.
edit_tab = Menu(menu, tearoff=0)
menu.add_cascade(label = "Edit", menu = edit_tab)

# Creating Selection tab.
selection_tab = Menu(menu, tearoff=0)
menu.add_cascade(label = "Selection", menu = selection_tab)

# Creating Help tab.
help_tab = Menu(menu, tearoff=0)
menu.add_cascade(label = "Help", menu = help_tab)

# Adding a scrollbar.
scroll = Scrollbar(root)
scroll.pack(side="right", fill="y")

# Creating Text input in a scrollbar.
txt = Text(root, yscrollcommand = scroll.set) 
txt.pack(side="left", fill="both", expand=True)
scroll.config(command=txt.yview)

txt.insert(END, "input text here.")

# keeping the GUI window open. 
root.config(menu=menu)
root.mainloop()


# def save_file():
# 	msgbox.askyesnocancel(message = "Save current note?")