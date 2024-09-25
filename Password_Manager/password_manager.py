import tkinter
from tkinter import messagebox, Entry, simpledialog
import tkinter.messagebox
import pyperclip
import random
import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker



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
website_input = tkinter.Entry(width= 33)
website_input.focus()
website_input.grid(column=1, row=1)

username_input = tkinter.Entry(width= 53)
username_input.insert(tkinter.END, "debojyotichattoraj1996@gmail.com")
username_input.grid(column=1, row=2, columnspan=2)

password_input = tkinter.Entry(width= 33)
password_input.grid(column=1, row=3)



# ---------------------------- DataBase SETUP ------------------------------- #

# Create an engine
engine = create_engine('sqlite:///password_manager.db', echo=True)


# Create a base class for declarative class definitions
Base = declarative_base()


class PasswordManager(Base):
    __tablename__ = 'password'
    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    email: Mapped[str] = mapped_column(String(250), nullable= False)
    platform: Mapped[str] = mapped_column(String(250), unique= True, nullable= False)
    user_password: Mapped[str] = mapped_column(String(250), nullable= False)


# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pw():

    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    result = session.execute(session.query(PasswordManager).order_by(PasswordManager.id))
    all_result = result.scalars().all()
    all_platform = []
    for item in all_result:
        all_platform.append(item.platform)
    


    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title = "Warning", message = "Field should not be Empty!")
    elif website_input.get() in all_platform:
        messagebox.showinfo(title= "Warning", message= "Credential already exists!")
    else:
        is_ok = messagebox.askokcancel(title= "Save", message= f"You have entered below details: \nWebsite: {website} \nEmail: {username}, \nPassword: {password} \nDo you want to save?")

        if is_ok:
            new_data = PasswordManager(email = f"{username}", platform = f"{website}", user_password = f"{password}")
            session.add(new_data)
            session.commit()
            messagebox.showinfo(title= "Saved", message= "Credential saved Successfully!")
            website_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)


# ---------------------------- AUTHORIZATION ------------------------------- #

def auth():
    user_input = simpledialog.askstring("Input", "Please enter admin password:")
    admin_account = session.query(PasswordManager).filter_by(platform='administrator').first()
    if user_input == admin_account.user_password:
        return True
    else:
        messagebox.showinfo(title= "Update Failed!", message= "Incorrect Password!")
        return False


# ---------------------------- UPDATE PASSWORD ------------------------------- #

def update_pw():
     
    if auth():
        result = session.execute(session.query(PasswordManager).order_by(PasswordManager.id))
        all_result = result.scalars().all()
        all_platform = [item.platform for item in all_result]

        if website_input.get() in all_platform:
            new_password = password_input.get()
            pw_to_update = session.query(PasswordManager).filter_by(platform=website_input.get()).first()
            
            if pw_to_update:
                pw_to_update.user_password = new_password
                try:
                    session.commit()
                    messagebox.showinfo(title= "Success!", message= "Password updated Successfully!")
                except Exception as e:
                    session.rollback()
                    print(f"Error updating user: {e}")
            else:
                print("Password not found.")
        else:
            messagebox.showinfo(title= "Failed!", message= "Password update Failed! Please Add the Platform Credential first.")


# ---------------------------- SEARCH CREDENTIAL ------------------------------- #
           
def find_password():

    if auth():

        result = session.execute(session.query(PasswordManager).order_by(PasswordManager.id))
        all_result = result.scalars().all()
        all_platform = []
        for item in all_result:
            all_platform.append(item.platform)


        if website_input.get() in all_platform:
            platform_to_find = session.query(PasswordManager).filter_by(platform=website_input.get()).first()
            messagebox.showinfo(title= "Credentials", message= f"Your Credentials: \nEmail: {platform_to_find.email}\nPassword: {platform_to_find.user_password}")
        else:
            messagebox.showinfo(title= "Error", message= f"No Credential found for {website_input.get()}!")

    
        
        

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



# ---------------------------- UI SETUP ------------------------------- #

# Add Button:
add_btn = tkinter.Button(text= "Add", width= 28, command= save_pw)
add_btn.grid(column=1, row=4)

# update Button:
update_btn = tkinter.Button(text= "Update Password", width= 15, command= update_pw)
update_btn.grid(column=2, row=4)

#Generate Password Buttons:
generate_pw_btn = tkinter.Button(text= "Generate Password", width= 15, command=pw_generator)
generate_pw_btn.grid(column=2, row=3)

# Search button:
search_btn = tkinter.Button(text= "Search", width= 15, command= find_password)
search_btn.grid(column= 2, row= 1)



window.mainloop()