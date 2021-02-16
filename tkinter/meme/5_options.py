from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import PIL.Image
import os

root=Tk()
root.title("MEME")

# adding files/images in the Listbox.
def add_file():
	files = filedialog.askopenfilenames(title="Select images",
		filetypes = (("PNG images", "*.png"), ("All images", "*.*")),
		initialdir = r"/Users/phil/Documents/Python/nado/tkinter/meme/")

	# inserting file in the Listbox.
	for file in files:
		list_file.insert(END, file)

def del_file():
	# print(list_file.curselection())

	for index in reversed(list_file.curselection()):
		list_file.delete(index)

# Save Path in the save_frame
def browse_save_path():
	selected_folder = filedialog.askdirectory(initialdir = 
						r"/Users/phil/Documents/Python/nado/tkinter/meme/")
	if selected_folder == '':
		print("Cancel selected path")
		return
	save_desktop_path.delete(0, END)
	save_desktop_path.insert(0, selected_folder)

# Merging Images.
def merge_images():

	try:
		img_width = combo_width.get()
		if img_width == "Original":
			img_width = -1 # just picked this random number so we can maniplate inputted widths.
		else:
			img_width = int(img_width)

		img_space = combo_space.get()
		if img_space == "Small":
			img_space = 30
		elif img_space == "Medium":
			img_space = 60
		elif img_space == "Large":
			img_space = 90
		else:
			img_space = 0

		img_format = combo_format.get().lower()

		images = [PIL.Image.open(x) for x in list_file.get(0, END)]

		images_sizes = []
		if img_width > -1:
			images_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
		else:
			images_sizes = [(x.size[0], x.size[1]) for x in images]

			# calculations
			# x : y = x' : y'
			# y' = x'y / x
			# x = width = x.size[0]
			# y = height = x.size[1]
			# x' = img_width
			# y' = img_width * x.size[1] / x.size[0]


		# for both widths and heights. 
		widths, heights = zip(*(images_sizes)) 

		# finding out max width and total heights.
		max_widths, total_heights = max(widths), sum(heights)
		print("Max widths: ", max_widths)
		print("Total height: ", total_heights)

		# sketchbook.
		if img_space > 0:
			total_heights += img_space * (len(images) - 1)

		result_img = PIL.Image.new("RGB", (max_widths, total_heights), (255,255,255))
		y_offset =0

		# adding a Progress bar. 
		# also, resizing based on inputted image width.
		for idx, img in enumerate(images):
			if img_width > -1:
				img = img.resize(images_sizes[idx])

			result_img.paste(img, (0, y_offset))
			y_offset += (img.size[1] + img_space)

			progress = (idx + 1) / len(images) * 100
			p_var.set(progress)
			progress_bar.update()

		filename = "MEME_merged." + img_format
		merge_desktop_path = os.path.join(save_desktop_path.get(), filename)
		result_img.save(merge_desktop_path)
		msgbox.showinfo("Notification", "Merge completed!")
	except Exception as err:
		msgbox.showerror("Error!", err)

# Start Command.
def start():
	# checking Options
	# print("Width: ", combo_width.get())
	# print("Space: ", combo_space.get())
	# print("Format: ", combo_format.get())

	# checking the selected files
	if list_file.size() == 0:
		msgbox.showwarning("Warning!", "Please select images.")
		return

	# checking the selected Save To
	if len(save_desktop_path.get()) == 0:
		msgbox.showwarning("Warning!", "Please select where you want to save the images.")
		return

	merge_images()

# quit Command.
def finish():
	quit_response = msgbox.askyesno("Quit", "Would you like to exit the program?")
	print("Response", quit_response)
	if quit_response == 0:
		print("Stay")
	else:
		print("Quit it")
		root.quit()

# Creating the "File" frame.
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, text = "Add Files", command = add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, text= "Delete Files", command = del_file)
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
save_frame =LabelFrame(root, text = "Save to")
save_frame.pack(fill="x", padx=5, pady=5, ipady=4)

	# outputting the saved path as a text ti the Save Path.
save_desktop_path = Entry(save_frame)
save_desktop_path.pack(side="left", fill="x", padx=5, pady=5, expand=True)

btn_desktop_save = Button(save_frame, text = "Search", width=10, command = browse_save_path)
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

btn_quit = Button(run_frame, padx=5, pady=5, text = "Quit", width=10, command=finish)
btn_quit.pack(side="right", padx=5, pady=5)

btn_start = Button(run_frame, padx=5, pady=5, text = "Start", width=10, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()