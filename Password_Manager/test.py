import tkinter as tk
from tkinter import simpledialog

def open_popup():
    # Create a new Toplevel window
    popup = tk.Toplevel(root)
    popup.title("Input Entry")
    popup.geometry("300x150")

    # Create an Entry widget in the popup window
    entry = tk.Entry(popup)
    entry.pack(pady=20)

    # Function to handle the submission
    def submit():
        user_input = entry.get()
        entry_text.set(user_input)
        popup.destroy()  # Close the popup window

    # Create a Submit button in the popup window
    submit_button = tk.Button(popup, text="Submit", command=submit)
    submit_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

# Variable to store the input text
entry_text = tk.StringVar()

# Label to display the entry from the popup window
label = tk.Label(root, textvariable=entry_text)
label.pack(pady=20)

# Button in the main window to open the popup window
open_popup_button = tk.Button(root, text="Open Popup", command=open_popup)
open_popup_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
