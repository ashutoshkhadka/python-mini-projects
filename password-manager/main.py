import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))] + \
                    [random.choice(symbols) for _ in range(random.randint(2, 4))] + \
                    [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Missing information", message="Please fill out the mandatory values")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            write_data = new_data
        else:
            write_data = data
        finally:
            with open("data.json", "w") as f:
                json.dump(write_data, f, indent=4)
    website_input.delete(0, END)
    password_input.delete(0, END)


def search_password():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            website = website_input.get()
            credentials = data[website]
            messagebox.showinfo(title="Credentials",
                                message=f"username: {credentials['email']}\n password: {credentials['password']}")
    except FileNotFoundError:
        messagebox.showerror(title="No data found", message="File does not exist")
    except KeyError:
        messagebox.showerror(title="No data found", message=f"No credentials found for the website: {website}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("My Password Manager")
# window.minsize(width=200, height=450)
window.config(pady=50, padx=50)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

username_label = Label(text="Username/Email")
username_label.grid(row=2, column=0)

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky=W)
username_input.insert(0, "khadkashutosh@outlook.com")

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky=W)

generate_button = Button(text="Generate", width=9, command=generate_password)
generate_button.grid(row=3, column=2, sticky=N)

search_button = Button(text="Search", command=search_password, width=9)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=32, command=save_password)
add_button.grid(row=4, columnspan=2, column=1, sticky=W)

window.mainloop()
