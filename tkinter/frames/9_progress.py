from tkinter import *
import tkinter.ttk as ttk
import time

# opening the GUI window
root = Tk()

root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100") # w x h + x + y coordinants. 
root.resizable(False, False) # x, y resizable is disabled. 

'''
# creating progress bar
# progressbar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate")
progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate")
progressbar.start(20) # moving per 20 ms
progressbar.pack()


def btncmd():
	progressbar.stop()

btn = Button(root, text = "Done", command = btncmd)
btn.pack()
'''

variable2 = DoubleVar() # doubling up the speed.
progressbar2 = ttk.Progressbar(root, maximum =100, length = 150, variable = variable2) # GUI
progressbar2.pack() # GUI print.

def btncmd2():
	for i in range(1, 101): # 1 - 100
		time.sleep(0.01) # 0.01 s delay

		variable2.set(i) # setting the parameter
		progressbar2.update() # UI update.
		print(variable2.get()) # the current %

btn2 = Button(root, text = "Start", command = btncmd2)
btn2.pack()

# keeping the GUI window open. 
root.mainloop()