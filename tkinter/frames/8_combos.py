from tkinter import *
import tkinter.ttk as ttk

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 


values = [str(i) + " date" for i in range(1, 32)] # 1 - 31 dates
combobox = ttk.Combobox(root, height =5, values = values)
combobox.pack()
combobox.set("Select payment date") # default text of the combobox. 

readonly_combobox = ttk.Combobox(root, height =10, values = values, state = "readonly")
readonly_combobox.current(0) # 0th index default
readonly_combobox.pack()
# readonly_combobox.set("Select payment date") # default text of the combobox. 

def btncmd():
	print(combobox.get()) # when 'Done' is clicked, printing i values.
	print(readonly_combobox.get()) 

btn = Button(root, text = "Done", command = btncmd)
btn.pack()


# keeping the GUI window open. 
root.mainloop()