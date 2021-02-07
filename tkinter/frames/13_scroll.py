from tkinter import *
import tkinter.ttk as ttk
import time

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 

# putting a scrollbar in a Frame.
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# listbox in a Frame as well.
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand= scrollbar.set)
for i in range(1, 32):
	listbox.insert(END, str(i) + "date")
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)

# keeping the GUI window open. 
root.mainloop()