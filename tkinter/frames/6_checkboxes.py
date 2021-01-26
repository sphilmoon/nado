from tkinter import *

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 

# creating checkboxes.
checkvar = IntVar() # saving variable (in integer) inside this definition.
checkbox = Checkbutton(root, text = "HIDE UNTIL TOMORROW", variable = checkvar)
checkbox.select() # selected in default.
# checkbox.deselect() 
checkbox.pack()

checkvar2 = IntVar()
checkbox2 = Checkbutton(root, text = "HIDE UNTIL NEXT WEEK", variable = checkvar2)
checkbox2.select()
checkbox2.pack()

def btncmd():
	print(checkvar.get()) # 0 is unchecked, 1 is checked.
	print(checkvar2.get())

btn = Button(root, text = "Clickable", command = btncmd)
btn.pack()

# keeping the GUI window open. 
root.mainloop()