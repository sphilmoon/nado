from tkinter import *
import os

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")

# current_path = os.path.dirname(__file__)
# image_path = os.path.join(current_path, "images")

label1 = Label(root, text = "Please select the followings")
label1.pack()

# inserting image to the label.
photo = images.load(image_path, "btn_black.png")
photo = PhotoImage(file = "/Users/phil/Documents/Python/nado/tkinter/images/btn_black.png")
label2 = Label(root, image = photo)
label2.pack()

# changing the label with a click with a new photo. 
def change():
	label1.config(text = "see you later.")

	global photo2
	photo2 = PhotoImage(file = "/Users/phil/Documents/Python/nado/tkinter/images/btn2.png")
	label2.config(image = photo2)

btn = Button(root, text = "Click", command = change)
btn.pack()

# keeping the GUI window open. 
root.mainloop()