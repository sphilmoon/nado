from tkinter import *
import tkinter.ttk as ttk
import time

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 

frame_burger = Frame(root, relief="solid", bd=2)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="burger").pack()

# keeping the GUI window open. 
root.mainloop()