from tkinter import *
from tkinter import messagebox
from password_generator import make
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_maker():
    password_entry.delete(0, END)
    new_password = make()
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_dictionary = {
        website: {
            'email': email,
            'password': password
        }}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='OOPs', message='Hey dont leave any field empty')
    else:
        # is_ok=messagebox.askokcancel(title=website,message=f'There are the details entered:\nEmail:{email}\nPassword:{password}\nIs it OK to save')
        # if is_ok==True:
        #    mystring = f'{website} | {email} | {password}\n'
        #    print(mystring)
        try:
            with open('data.json', 'r') as datafile:
                # reading old data
                current_data = json.load(datafile)

        except FileNotFoundError:
            with open('data.json', 'w') as datafile:
                json.dump(new_dictionary, datafile, indent=4)
        else:
            with open('data.json', 'w') as datafile:
                # updating old data
                current_data.update(new_dictionary)
                # again putting updated old data
                json.dump(current_data, datafile, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ----------------------------search------------------------------------#

def search():
    tosearch = website_entry.get()
    if len(tosearch) == 0:
        messagebox.showerror(title='OOPs', message='Hey dont leave website field empty')
    else:
        try:
            with open('data.json', 'r') as dataset:
                whole_list = json.load(dataset)

                if tosearch in whole_list:
                    messagebox.showinfo(title=tosearch,
                                        message=f"Email: {whole_list[tosearch]['email']}\nPassword: {whole_list[tosearch]['password']} ")
                else:
                    messagebox.showinfo(title=tosearch, message=f"not present")
        except:
            messagebox.showinfo(title=tosearch, message=f"No Data File is found")


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title('Password Manager')
windows.config(padx=20, pady=20)
canvas = Canvas(width=200, height=190)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1, sticky=W, columnspan=2)

label1 = Label(text='Website: ')
label1.grid(row=1, column=0)
label2 = Label(text='Email/Username: ')
label2.grid(row=2, column=0)
label3 = Label(text='Password: ')
label3.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky=W)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(END, 'aquilhassan420@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=W)

button1 = Button(text='Generate Password', command=password_maker)
button1.grid(row=3, column=2, sticky=W, padx=15)
button2 = Button(text='Add', width=35, command=save_password)
button2.grid(row=4, column=1, columnspan=2, sticky=W)
button3 = Button(text="search", width=15, command=search, bg='blue')
button3.grid(row=1, column=2)

windows.mainloop()
