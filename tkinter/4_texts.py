from tkinter import *

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 

# blank text.
txt = Text(root, width = 30, height = 30)
txt.pack()

txt.insert(END, "input text here.")

# blank entry.
e = Entry(root, width =30)
e.pack()
e.insert(0, "first line input: ")

def btncmd():
	# printing input
	print(txt.get("1.0", END)) # 1 is first row, 0 is 0th column.
	print(e.get())

	# deleting input
	txt.delete("1.0", END)
	e.delete(0, END)

btn = Button(root, text = "Clickable", command = btncmd)
btn.pack()

# keeping the GUI window open. 
root.mainloop()