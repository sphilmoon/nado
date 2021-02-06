from tkinter import *
import tkinter.messagebox as msgbox

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 

# Booking train tickets.
def info():
	msgbox.showinfo("Notification", "Thank you for booking with us :)")

def warn():
	msgbox.showwarning("Warning", "No vacancy :(")

def error():
	msgbox.showerror("Error", "Payment issues!")

def cancel():
	msgbox.askokcancel("Cancellation", "Would you like to cancel your current booking?")

def retrycancel():
	msgbox.askretrycancel("Retry cancel", "Temporary issue. Would you like to continue?")

def yesno():
	msgbox.askyesno("Yes / No", "You've booked a windown seat. Would you like to continue?")

# False or "No" == 0 
# True or "Yes" == 1
def yesnocancel():
	response = msgbox.askyesnocancel(title="Save current bookings", message="Your booking is incomplete. \nWould you like to save and continue later?")
	print("Response: ", response)
	if response == 0:
		print("No")
	elif response == 1: 
		print("Yes")
	else:
		print("Cancel")

Button(root, text = "Notification", command = info).pack()
Button(root, text = "Warning", command = warn).pack()
Button(root, text = "Error", command = error).pack()

Button(root, text = "Cancellation", command = cancel).pack()
Button(root, text = "Retry cancel", command = retrycancel).pack()
Button(root, text = "Yes / No", command = yesno).pack()
Button(root, text = "Yes / No / Cancel", command = yesnocancel).pack()

# keeping the GUI window open. 
root.mainloop()