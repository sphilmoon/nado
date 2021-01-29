from tkinter import *
import tkinter.messagebox as msgbox

# Radiobuton can let you select one item at a time from the list.

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 

# creating labels.
# label_burgers = Label(root, text = "Select your burger")
# label_burgers.pack()
	# using frames instead.
frame_burgers = LabelFrame(root, text = "Select your burgers") # outline is solid line.
frame_burgers.pack()

# burgers
burger_var = StringVar() # sharing the Var in the menu list
btn_burger1 = Radiobutton(frame_burgers, text = "Cheeseburger", value = "Cheeseburger", variable = burger_var)
btn_burger1.select() # default select.
btn_burger2 = Radiobutton(frame_burgers, text = "Double cheeseburger", value = "Double cheeseburger", variable = burger_var)
btn_burger3 = Radiobutton(frame_burgers, text = "Bacon burger", value = "Bacon burger", variable = burger_var)
btn_burger4 = Radiobutton(frame_burgers, text = "Mushroom burger", value = "Mushroom burger", variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
btn_burger4.pack()

# drinks
# label_drinks = Label(root, text = "Select your drink")
# label_drinks.pack()
	# using frames instead.
frame_drinks = LabelFrame(root, text="Select your drinks") 
frame_drinks.pack()
# Button(frame_drinks).pack()

drink_var = StringVar()
btn_coke = Radiobutton(frame_drinks, text = "Coke", value = "Coke", variable = drink_var)
btn_coke.pack()
btn_coke.select() # default select.
Radiobutton(frame_drinks, text = "Dr. Pepper", value = "Dr. Pepper", variable = drink_var).pack()
Radiobutton(frame_drinks, text = "Sprite", value = "Sprite", variable = drink_var).pack()
Radiobutton(frame_drinks, text = "Mountain Dew", value = "Mountain Dew", variable = drink_var).pack()



def yesnocancel():
	response = msgbox.askyesnocancel(title=None, message= "Would you like to checkout \nour dessert menu?")
	if response is False: 
		print(burger_var.get()) # printing their assigned value. 
		print(drink_var.get() )
	elif response is True:
		print("Go to the dessert menu.")
	else:
		print("Cancel")

Button(root, text = "Proceed to checkout", command = yesnocancel).pack(side="top")

# keeping the GUI window open. 
root.mainloop()