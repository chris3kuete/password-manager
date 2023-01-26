from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # for char in range(nr_letters):
    # password_list.append(random.choice(letters))
    p_letters = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    # password_list += random.choice(symbols)
    p_symbols = [random.choice(symbols) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    # password_list += random.choice(numbers)
    p_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = p_numbers + p_symbols + p_letters
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    # password += char
    password = "".join(password_list)
    passwordEntry.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def addInfos():
    website = website_input.get()
    email = EmailInput.get()
    password = passwordEntry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="ooh", message="Please fill in all your information")
    else:

        # Is_ok = messagebox.askokcancel(title=website_input,
        # message=f"These are the details entered: \nWebsite:{website_input.get()}" f"\nEmail:{EmailInput.get()}" f"\nPassword:{passwordEntry.get()}  \nIs it Ok to save?")
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            passwordEntry.delete(0, END)

        # f.writelines('\n' + '\n' + website_input.get())
        # f.writelines('\n' + EmailInput.get())
        # f.writelines('\n' + passwordEntry.get())


def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="This doesn't exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"the email is:\n {email} and the password is:\n {password}")
        else:
            messagebox.showinfo(title="Entry not found", message="No Entry Found with this name")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
PadLock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=PadLock)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)

website_input = Entry(width=45)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
website_input.get()

label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)

EmailInput = Entry(width=45)
EmailInput.grid(column=1, row=2, columnspan=2)
EmailInput.insert(0, "chriskuete@yahoo.fr")
EmailInput.get()

label3 = Label(text="Password:")
label3.grid(column=0, row=3)

passwordEntry = Entry(width=25)
passwordEntry.grid(column=1, row=3)
passwordEntry.get()

buttonPassword = Button(text="Generate Password", width=14, command=generate_password)
buttonPassword.grid(column=2, row=3)

addButton = Button(text="Add", width=40, command=addInfos)
addButton.grid(column=1, row=4, columnspan=2)

searchButton = Button(text="Search", width=8, command=find_password)
searchButton.grid(column=2, row=1)

window.mainloop()
