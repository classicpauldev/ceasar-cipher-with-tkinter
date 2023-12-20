from tkinter import *
import tkinter.messagebox
import clipboard

from cipher import encrypt as cipher_encrypt, decrypt as cipher_decrypt

WHITE = "#fff"
BLACK = "#000"
FONT = ("Arial", 15)
window = Tk()
window.title("Caesar Cipher X")
window.config(padx=50, pady=50, bg=WHITE)

# Creating the functions


def _clear_fields():
    """Clear text and passcode fields."""
    text_entry.delete(0, END)
    text_entry.insert(END, string="Write a text")
    shift_entry.delete(0, END)
    shift_entry.insert(END, string="Passcode")


def _get_shift() -> int | None:
    """Parse shift from entry, show error and return None if invalid."""
    try:
        return int(shift_entry.get())
    except ValueError:
        tkinter.messagebox.showerror(title="Error", message="Passcode must be a number (e.g. 123)")
        return None


def encrypt():
    """Encrypt the text in the entry field using the passcode shift."""
    word = text_entry.get().strip()
    if word in ("", "Write a text"):
        tkinter.messagebox.showerror(title="Error", message="Please enter some text to encrypt")
        return False
    shift = _get_shift()
    if shift is None:
        return
    encrypted_word = cipher_encrypt(word, shift)
    clipboard.copy(encrypted_word)
    text_entry.delete(0, END)
    text_entry.insert(END, string=encrypted_word)
    tkinter.messagebox.showinfo(title="Success", message="The encrypted text has been saved to your clipboard")


def decrypt():
    """Decrypt the text in the entry field using the passcode shift."""
    word = text_entry.get().strip()
    if word in ("", "Write a text"):
        tkinter.messagebox.showerror(title="Error", message="Please enter some text to decrypt")
        return False
    shift = _get_shift()
    if shift is None:
        return
    decrypted_word = cipher_decrypt(word, shift)
    clipboard.copy(decrypted_word)
    text_entry.delete(0, END)
    text_entry.insert(END, string=decrypted_word)
    tkinter.messagebox.showinfo(title="Success", message="The decrypted text has been saved to your clipboard")


# Creating the entry textbox
text_entry = Entry(width=65, highlightbackground=WHITE, highlightthickness=0)
text_entry.insert(END, string="Write a text")
text_entry.focus()
text_entry.grid(column=0, row=1, columnspan=3)


shift_entry = Entry(width=13, highlightbackground=WHITE, highlightthickness=0)
shift_entry.insert(END, string="Passcode")
shift_entry.grid(column=0, row=2)

encode_button = Button(text="Encrypt", highlightbackground=WHITE, width=20, command=encrypt)
encode_button.grid(column=1, row=2)

decode_button = Button(text="Decrypt", highlightbackground=WHITE, width=20, command=decrypt)
decode_button.grid(column=2, row=2)

clear_button = Button(text="Clear", highlightbackground=WHITE, width=20, command=_clear_fields)
clear_button.grid(column=0, row=3, columnspan=3)

window.bind("<Control-e>", lambda e: encrypt())
window.bind("<Control-d>", lambda e: decrypt())


# Creating the image
canvas = Canvas(width=250, height=250, bg=WHITE, highlightthickness=0)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)
window.mainloop()
