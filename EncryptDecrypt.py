import base64
from tkinter import messagebox
from tkinter import Tk, mainloop, Label, Text, Entry, Button, StringVar, Toplevel, END, WORD

import password

# import password as password
import tkinter as tk

screen = tk.Tk()

# screenone = Tk()
screen.geometry("420x420")
# 420(width)x420(height)")screen.title() title change
"""for other things tkinter module for buttons
label for heading  ,
place function for packing
 text widget
 """
# get func used for information fetch,variabl name password,textvariabl name is code
# Indentation level of code within the if statement
# Rest of your code
# toplevel widget so when we click on encrypt new window wil open
screen.title("Encryption and Decryption")
screen.configure(bg="grey")  # configure used for background


def encrypt():
    code_value = code.get()


    if code_value == "1234":
        screen1 = tk.Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="pink")

        message = text1.get(1.0, END)  # 1st line 0 character se end tk ko fetch krdo
        # Encode message using ASCII encoding
        encode_message = message.encode("ascii")

        # Encode the ASCII-encoded message using base64 encoding
        menc = base64.b64encode(encode_message)

        # Decode the base64-encoded message back to ASCII
        encrypt = menc.decode("ascii")

        Label(screen1,text="Code is Encrypted", font="impack 10 bold").place(x=5,y=6)
        text2 = Text(screen1,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(END,encrypt)


    elif code_value == "":

        messagebox.showerror("Error", "Please enter the secret key")
    elif code_value != "1234":
         messagebox.showerror("Oops", "Invalid secret key")


def decrypt():
    code_value = code.get()


    if code_value == "1234":
        screen2 = tk.Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x250")
        screen2.configure(bg="green")

        message = text1.get(1.0, END)  # 1st line 0 character se end tk ko fetch krdo
        # Encode message using ASCII encoding
        encode_message = message.encode("ascii")

        # Encode the ASCII-encoded message using base64 encoding
        menc = base64.b64decode(encode_message)

        # Decode the base64-encoded message back to ASCII
        encrypt = menc.decode("ascii")

        Label(screen2, text="Code is decrypted", font="impack 10 bold").place(x=5, y=6)
        text2 = Text(screen2, font="30", bd=4, wrap=WORD)
        text2.place(x=2, y=30, width=390, height=180)
        text2.insert(END, encrypt)


    elif code_value == "":

        messagebox.showerror("Error", "Please enter the secret key")
    elif code_value != "1234":
        messagebox.showerror("Oops", "Invalid secret key")


def reset():
    text1.delete(1.0,END)
    code.set("")


Label(screen, text="Enter the text for encryption and decryption", font="impack 14 bold", bg="yellow").place(x=5, y=6)
text1 = Text(screen, font="20")
text1.place(x=5, y=45, width=410, height=120)
Label(screen, text="Enter Secret key", font="impack 13 bold").place(x=138, y=185)
# entry widget  isme text var se hme pata chl jayega ki user ne koi secret key enter ki hai
code: StringVar = StringVar()
Entry(textvariable=code, bd=4, font="20", show="*").place(x=110, y=220)
# button widget
Button(screen, text="ENCRYPT", font="aerial 15 bold", bg="red", fg="black", command=encrypt).place(x=15, y=280,
                                                                                                   width=180)
Button(screen, text="DECRYPT", font="aerial 15 bold", bg="green", fg="black",command=decrypt).place(x=220, y=280, width=180)
Button(screen, text="RESET", font="aerial 15 bold", bg="blue", fg="black",command=reset).place(x=60, y=350, width=280)
mainloop()
