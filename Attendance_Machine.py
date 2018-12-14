import datetime
import base64
import tkinter


class AttendanceManager:
	"""GUI Class that manage the attendance."""
	def __init__(self, dictionary):
		"""
		Initialize the label, button, entry, and the command.
		Passing the username and password from main.
		"""
		self.root = tkinter.Tk() # Create the GUI

		# Get the username and password from main
		self.dictionary = dictionary

		# Create the heading label, entry label, and the message label
		self.heading = tkinter.Label(self.root, text="Attendance Machine",
			height=2)
		self.username_label = tkinter.Label(self.root, text="Username")
		self.password_label = tkinter.Label(self.root, text="Password")
		self.message = tkinter.Label(self.root, text="")

		# Create the entry and show the password as "*"
		self.username_field = tkinter.Entry(self.root)
		self.password_field = tkinter.Entry(self.root, show="*")

		# Create the event command in the entry
		self.username_field.bind("<Return>", self.present)
		self.password_field.bind("<Return>", self.present)

		# Create the button
		self.present_button = tkinter.Button(self.root, text="Present",
			command=self.button_press)
		self.create_button = tkinter.Button(self.root, text="Create Account",
			command=self.create_account)

		self.create_gui() # Place the widget in the Tk GUI field
		self.mainloop() # Start the app

	def create_gui(self):
		"""Initialize the layout."""
		self.root.title("Attendance Machine") # Set the title
		self.root.geometry("450x250")  # Set window size

		# Place the label labels in the Tk GUI field
		self.heading.grid(row=0, column=1)
		self.username_label.grid(row=1, column=0)
		self.password_label.grid(row=2, column=0)
		self.message.grid(row=5, column=1)

		# Place the entry in the Tk GUI field
		self.username_field.grid(row=1, column=1, ipadx="100")
		self.password_field.grid(row=2, column=1, ipadx="100")

		# Place the button in the Tk GUI field
		self.present_button.grid(row=7, column=1)
		self.create_button.grid(row=8, column=1)

	def reset(self):
		"""Clears all the fields and move focus back to username."""
		self.username_field.focus_set()

		self.username_field.delete(0, tkinter.END)
		self.password_field.delete(0, tkinter.END)

	def mainloop(self):
		"""Starts the app"""
		self.root.mainloop()

	def present(self, event):
		"""Save the attendance time when the button is clicked."""
		# Get the username and password from the entry
		username = self.username_field.get()
		password = self.password_field.get()

		# Show error message when there is empty entry
		if len(username) == 0 or len(password) == 0:
			self.message.config(text="Please fill all the fields.")
		else:
			# Encode the password to base 64 value
			password = str(base64.b64encode(password.encode()))

			# Show error message if the username is not registered
			if username not in self.dictionary:
				self.message.config(text="Username not found.")
			# Show error message if the password is wrong
			elif password != self.dictionary[username]:
				self.message.config(text="Wrong password.")
			# Save the date and time when the user is present
			else:
				# Get the current date and time and save it in the file
				# Show the message of the data entered to the file
				present_time = datetime.datetime.now()
				self.message.config(text=f"User {username} "
					f"present at {present_time}.")
				# Open the file and append the data to the file
				with open("Attendance_Log.txt","a") as attendance_file:
					attendance_file.write(f"{username} : {present_time}\n")

				# Reset the entry and move the focus to username field
				self.reset()

	def button_press(self):
		"""
		Save the attendance time when the return key is pressed in the entry.
		"""
		# Get the username and password from the entry
		username = self.username_field.get()
		password = self.password_field.get()

		# Show error message when there is empty entry
		if len(username) == 0 or len(password) == 0:
			self.message.config(text="Please fill all the fields.")
		else:
			# Encode the password to base 64 value
			password = str(base64.b64encode(password.encode()))

			# Show error message if the username is not registered
			if username not in self.dictionary:
				self.message.config(text="Username not found.")
			# Show error message if the password is wrong
			elif password != self.dictionary[username]:
				self.message.config(text="Wrong password.")
			# Save the date and time when the user is present
			else:
				# Get the current date and time and save it in the file
				# Show the message of the data entered to the file
				present_time = datetime.datetime.now()
				self.message.config(text=f"User {username} "
					f"present at {present_time}.")
				# Open the file and append the data to the file
				with open("Attendance_Log.txt","a") as attendance_file:
					attendance_file.write(f"{username} : {present_time}\n")

				# Reset the entry and move the focus to username field
				self.reset()

	def create_account(self):
		"""
		Create an account and save it to the dictionary and add the
		username and password to the Data file.
		"""
		# Get the username and password from the entry
		username = self.username_field.get()
		password = self.password_field.get()

		# Show error message when there is empty entry
		if len(username) == 0 or len(password) == 0:
			self.message.config(text="Please fill all the fields.")
		else:
			# Encode the password to base 64 value
			password = str(base64.b64encode(password.encode()))

			# Show error message if the username is registered
			if username in self.dictionary:
				self.message.config(text="Username has already taken.")
			# Save the username and password to the Data file
			else:
				self.dictionary[username] = password
				self.message.config(text=f"User {username} "
					"has been created.")
				with open("Data.txt","a") as data:
					data.write(f"{username} {password}\n")
				# Reset the entry and move the focus to username field
				self.reset()
		

def main():
	# Open the data file contain the username and password
	try:
		with open("Data.txt","r") as data_list:
			all_data = data_list.readlines()
			dictionary = {}

			# Split the data to get the username and password
			# and save it in dictionary
			for data in all_data:
				data = data.split()
				dictionary[data[0]] = str(data[1])

			# Pass the dictionary from main to the AttendanceManager class
			app = AttendanceManager(dictionary)
	# If the file not found, create the file and print the message.
	except FileNotFoundError:
		with open("Data.txt","w") as data:
			data.write("")
			print("File Data.txt has been created.\n"
				"Please restart the program.")
		

if __name__ == "__main__":
    main()