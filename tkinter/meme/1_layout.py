from tkinter import *
import tkinter.ttk as ttk

root=Tk()
root.title("MEME")

# Creating the "File" frame.
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, text = "Add Files")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, text="Delete Files")
btn_del_file.pack(side="right")

# Creating List frame.
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

	# putting scrollbar in the List frame.
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y", padx=5, pady=5)

	# putting listbox int the List frame.
	# also, sync Scrollbar and Listbox together. 
list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", padx=5, pady=5, expand=True, ipady=4)
scrollbar.config(command=list_file.yview)

# Creating Save Path frame.
save_frame =LabelFrame(root, text = "Save Path")
save_frame.pack(fill="x", padx=5, pady=5, ipady=4)

txt_desktop_save = Entry(save_frame)
txt_desktop_save.pack(side="left", fill="x", padx=5, pady=5, expand=True)

btn_desktop_save = Button(save_frame, text = "Search", width=10)
btn_desktop_save.pack(side="right")

# Creating Option frame.

option_frame = LabelFrame(root, text = "Option")
option_frame.pack(padx=5, pady=5, ipady=4)

	# Width
lbl_width = Label(option_frame, text = "Width", width=7)
lbl_width.pack(side="left", padx=5, pady=5)
	# With Combo aka selections.
option_width_values = ["Original", "1024", "800", "640"]
combo_width = ttk.Combobox(option_frame, state="readonly", values = option_width_values, width=10)
combo_width.current(0)  # Setting default
combo_width.pack(side="left")

	# Space between photos
lbl_space = Label(option_frame, text = "Space", width=7)
lbl_space.pack(side="left", padx=5, pady=5)
	# Space Combo
space_values = ["None", "Small", "Medium", "Large"]
combo_space = ttk.Combobox(option_frame, state="readonly", values = space_values)
combo_space.current(0)
combo_space.pack(side="left")

	# Format
lbl_format = Label(option_frame, text = "Format", width=7)
lbl_format.pack(side="left", padx=5, pady=5)
	# Format Combo
format_values= ["PNG", "JPEG", "BMP"]
combo_format = ttk.Combobox(option_frame, state="readonly", values = format_values)
combo_format.current(0)
combo_format.pack(side="left")

# Creating Status Frame
progress_frame = LabelFrame(root, text = "Progress")
progress_frame.pack(fill="x", padx=5, pady=5, ipady=4)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, maximum=100, variable= p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Creating Run Frame
run_frame = Label(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_finish = Button(run_frame, padx=5, pady=5, text = "Finish", width=10, command=root.quit)
btn_finish.pack(side="right", padx=5, pady=5)

btn_start = Button(run_frame, padx=5, pady=5, text = "Start", width=10)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()