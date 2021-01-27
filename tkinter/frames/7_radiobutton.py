from tkinter import *

# Radiobuton can let you select one item at a time from the list.

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 

# creating labels.
label1 = Label(root, text = "Select your burger")
label1.pack()

# burgers
burger_var = IntVar() # sharing the Var in the menu list
btn_burger1 = Radiobutton(root, text = "Cheeseburger", value = 1, variable = burger_var)
btn_burger1.select() # default select.
btn_burger2 = Radiobutton(root, text = "Double cheeseburger", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = "Bacon burger", value = 3, variable = burger_var)
btn_burger4 = Radiobutton(root, text = "Mushroom burger", value = 4, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
btn_burger4.pack()

# drinks
label2 = Label(root, text = "Select your drink")
label2.pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = "Coke", value = "Coke", variable = drink_var)
btn_drink2 = Radiobutton(root, text = "Dr. Pepper", value = "Dr. Pepper", variable = drink_var)
btn_drink3 = Radiobutton(root, text = "Sprite", value = "Sprite", variable = drink_var)
btn_drink4 = Radiobutton(root, text = "Mountain Dew", value = "Mountain Dew", variable = drink_var)

btn_drink1.pack()
btn_drink1.select() # default select.
btn_drink2.pack()
btn_drink3.pack()
btn_drink4.pack()

def btncmd():
	print(burger_var.get()) # printing their assigned value. 
	print(drink_var.get() )

btn = Button(root, text = "Make an order", command = btncmd)
btn.pack()

# keeping the GUI window open. 
root.mainloop()