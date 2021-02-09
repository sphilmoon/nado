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
	# exapmles:
btn1 = Button(root, text = "Button1")
btn2 = Button(root, text = "Button2")

btn1.grid(row=0, column=1)
btn2.grid(row=2, column=4)
'''

# making a calculator with grid. 
# the 1st row
btn_f16 = Button(root, text = "F16", width=5, height=2)
btn_f17 = Button(root, text = "F17", width=5, height=2)
btn_f18 = Button(root, text = "F18", width=5, height=2)
btn_f19 = Button(root, text = "F19", width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# the 2nd row

btn_clear = Button(root, text = "Clear", width=5, height=2)
btn_equal = Button(root, text = "=", width=5, height=2)
btn_division = Button(root, text = "/", width=5, height=2)
btn_produce = Button(root, text = "*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_division.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_produce.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# the 3rd row

btn_7 = Button(root, text = "7", width=5, height=2)
btn_8= Button(root, text = "8", width=5, height=2)
btn_9 = Button(root, text = "9", width=5, height=2)
btn_sub = Button(root, text = "-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# the 4th row

btn_4 = Button(root, text = "4", width=5, height=2)
btn_5= Button(root, text = "5", width=5, height=2)
btn_6 = Button(root, text = "6", width=5, height=2)
btn_sum = Button(root, text = "+", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sum.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# the 5th row

btn_1 = Button(root, text = "1", width=5, height=2)
btn_2= Button(root, text = "2", width=5, height=2)
btn_3 = Button(root, text = "3", width=5, height=2)
btn_enter = Button(root, text = "Enter", width=5, height=2)

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)  # row span two more from top to bottom.

# the 6th row

btn_0 = Button(root, text = "0", width=5, height=2)
btn_point = Button(root, text = ".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)  # column span two more from left to right.
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

# keeping the GUI window open. 
root.mainloop()