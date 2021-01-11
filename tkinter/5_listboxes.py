from tkinter import *

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 

listbox = Listbox(root, selectmode = "extended", height = 0)
listbox.insert(0, "apples") # inserting index and its item.
listbox.insert(1, "strawberries")
listbox.insert(2, "bananas")
listbox.insert(END, "watermelons") # appending in the end.
listbox.insert(END, "grapes")
listbox.pack()

def btncmd():
	# listbox.delete(END) # deleting the last item
	# listbox.delete(0) # deleting the first item

	# counts
	print("The number of remaining items: ", listbox.size())

	# item lists
	print("What's remaining: ", listbox.get(0, END))

	# selected items in terms of index.
	print("Selected item: ", listbox.curselection())

btn = Button(root, text = "Clickable", command = btncmd)
btn.pack()

# keeping the GUI window open. 
root.mainloop()