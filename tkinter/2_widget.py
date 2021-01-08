from tkinter import *

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 

# widget
btn1 = Button(root, text = "button1")
btn1.pack()

btn2 = Button(root, padx = 5, pady = 10, text = "button2")
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5, text = "button3")
btn3.pack()

btn4 = Button(root, width = 10, height = 3, text = "button4")
btn4.pack()

btn5 = Button(root, fg = "red", bg = "yellow", padx = 5, pady = 10, text = "button5")
btn5.pack()

photo = PhotoImage(file = "/Users/phil/Documents/Python/nado/tkinter/images/btn_black.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
	print("The botton is clicked.")

# printable button.
btn7 = Button(root, text = "Clickable 7", command = btncmd)
btn7.pack()

# keeping the GUI window open. 
root.mainloop()