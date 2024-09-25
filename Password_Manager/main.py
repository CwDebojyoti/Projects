import tkinter
from tkinter import messagebox
import tkinter.messagebox
import pyperclip
import random
import json


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx= 20, pady= 20)


canvas = tkinter.Canvas(width= 200, height= 189)
logo_img = tkinter.PhotoImage(file = "logo.png")
canvas.create_image(100, 95, image = logo_img)
canvas.grid(column=1, row=0)

#Labels:
website_label = tkinter.Label(text = "Website:", font= ("Arial", 12, "normal"))
website_label.grid(column=0, row=1, columnspan=1)

username_label = tkinter.Label(text = "Email/Username:", font= ("Arial", 12, "normal"))
username_label.grid(column=0, row=2, columnspan=1)

password_label = tkinter.Label(text = "Password:", font= ("Arial", 12, "normal"))
password_label.grid(column=0, row=3)


#Inputs:
website_input = tkinter.Entry(width= 53)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

username_input = tkinter.Entry(width= 53)
username_input.insert(tkinter.END, "debojyotichattoraj1996@gmail.com")
username_input.grid(column=1, row=2, columnspan=2)

password_input = tkinter.Entry(width= 33)
password_input.grid(column=1, row=3)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pw():

    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        "website": {
            "Email": username,
            "Password": password
        }
    }

    # messagebox.showinfo(title= "Title", message= "message")

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title = "Warning", message = "Field should not be Empty!")
    else:
        is_ok = messagebox.askokcancel(title= "Save", message= f"You have entered below details: \nWebsite: {website} \nEmail: {username}, \nPassword: {password} \nDo you want to save?")

        if is_ok:

            with open("my_data.json", mode="w") as file:     # mode = "a" will append the data to the file while mode = "w" will write (override) the data.
                # file.write(f"\n{website} | {username} | {password}")
                json.dump(new_data, file)
                website_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)
                messagebox.showinfo(title= "Saved", message= "Credential saved Successfully!")

       

# Add Button:
add_btn = tkinter.Button(text= "Add", width= 45, command= save_pw)
add_btn.grid(column=1, row=4, columnspan=2)



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pw_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for letter in range(0, nr_letters)]
    symbol_list = [random.choice(symbols) for symbol in range(0, nr_symbols)]
    number_list = [random.choice(numbers) for number in range(0, nr_numbers)]

    char_list = letter_list + symbol_list + number_list

    random.shuffle(char_list)
   
    final_password = "".join(char_list)     # join() method joins each elements a list or dictionary or tuple to make a string.

    password_input.delete(0, tkinter.END)
    password_input.insert(0, final_password)
    pyperclip.copy(final_password)


#Generate Password Buttons:
generate_pw_btn = tkinter.Button(text= "Generate Password", width= 15, command=pw_generator)
generate_pw_btn.grid(column=2, row=3)



window.mainloop()