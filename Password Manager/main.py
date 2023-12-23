from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
"""NOTE import * imports everything from the main file of tkinter, but tkinter has another module of just messagebox"""
import prettytable

TEXT_FONT = ("Courier", 14, "bold")
INPUT_FONT = ("Arial", 14, "normal")
SMALL_FONT = ("Courier", 10, "normal")
ENTRY_IPAD = 3

SAVED_EMAIL = "hoshimachisuisei@hololive.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    password = password_generator()

    password_input.delete(0, END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    entries = {"website": website_input.get(), 
               "username": username_input.get(), 
               "password": password_input.get()
                }
    # User input validation
    input_valid = True

    if len(entries["website"]) == 0 or len(entries["username"]) == 0 or len(entries["password"]) == 0:
        messagebox.showinfo(title="Notice", message="Don't leave any fields blank!")
        input_valid = False
    
    # TODO Escape Troublesome Input

    # Ask user for confirmation
    if input_valid:
        confirm = messagebox.askokcancel(title=f"{entries["website"]}", message=f"Save entry?\n\n"
                                                                                f"Username/Email: {entries["username"]}\n"
                                                                                f"            Password: {entries["password"]}")
        if confirm:
            with open("passwords.csv", "a") as csv_file:
                csv_file.write(f'"{entries["website"]}",')
                csv_file.write(f'"{entries["username"]}",')
                csv_file.write(f'"{entries["password"]}"\n')
            
            with open("passwords.csv", "r") as csv_file:
                pretty_table = prettytable.from_csv(csv_file)
            
            with open("passwords.txt", "w") as txt_file:
                string = pretty_table.get_string()
                txt_file.write(string)
            
            # Reset all input fields if confirm save password
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Row 1: Canvas with logo image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

# Row 2: Website Label and Entry
website_label = Label(text="Website/App:", font=TEXT_FONT, pady=8)
website_label.grid(column=1, row=2)
website_input = Entry(width=35, font=INPUT_FONT)
website_input.grid(column=2, row=2, ipady=ENTRY_IPAD)

# Row 3: Username/Email Label and Entry
username_label = Label(text="Username/Email:", font=TEXT_FONT, pady=8)
username_label.grid(column=1, row=3)
username_input = Entry(width=35, font=INPUT_FONT)
username_input.insert(0, SAVED_EMAIL)
username_input.grid(column=2, row=3, ipady=ENTRY_IPAD)

# Row 4: Passwword Label, Entry and Generate Button
password_label = Label(text="Password:", font=TEXT_FONT, pady=8)
password_label.grid(column=1, row=4)
password_input = Entry(width=35, font=INPUT_FONT)
password_input.grid(column=2, row=4, ipady=ENTRY_IPAD)
space = Label(width=1)
space.grid(column=3, row=4)
pw_gen_button = Button(text="Generate", font=TEXT_FONT, width=10, command=gen_password)
pw_gen_button.grid(column=4, row=4)

# Row 5: A space before the Save Button
space2 = Label()
space2.grid(column=1, row=5, columnspan=4)

# Row 6: Save Button
save_button = Button(text="Save", font=TEXT_FONT, width=15, command=save_password)
save_button.grid(column=2, row=6)

window.mainloop()

