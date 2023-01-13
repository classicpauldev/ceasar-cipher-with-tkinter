from tkinter import *
import tkinter.messagebox
import clipboard
WHITE = "#fff"
BLACK = "#000"
FONT = ("Arial", 15)
ALPHABET = 'qwertyuiopasdfghjklzxcvbnm'
ALPHABETS = ALPHABET * 100000  # Extended for large shifts

window = Tk()
window.title("Ceasar Cipher X")
window.config(padx=50, pady=50, bg=WHITE)

# Creating the functions


def encrypt():
    word = text_entry.get()
    if len(word) == 0:
        tkinter.messagebox.showerror(title="Error", message="Text field cannot be empty")
        return False
    encrypted_word = ""
    try:
        shift = int(shift_entry.get())
    except ValueError:
        tkinter.messagebox.showerror(title="Error", message="Passcode must be a number\nExample: 123456")
    else:
        for letter in word:
            if letter.isupper():
                if letter.lower() in ALPHABETS:
                    new_letter = ALPHABETS[ALPHABETS.index(letter.lower()) + shift]
                    encrypted_word += new_letter.upper()
            elif letter in ALPHABETS:
                new_letter = ALPHABETS[ALPHABETS.index(letter) + shift]
                encrypted_word += new_letter
            else:
                encrypted_word += letter
        clipboard.copy(encrypted_word)
        text_entry.delete(0, END)
        text_entry.insert(END, string=f"{encrypted_word}")
        tkinter.messagebox.showinfo(title="Success", message="The encrypted word's has been saved to your clipboard")


def decrypt():
    word = text_entry.get()
    if len(word) == 0:
        tkinter.messagebox.showerror(title="Error", message="Text field cannot be empty")
        return False
    decrypted_word = ""
    try:
        shift = int(shift_entry.get())
        shift *= -1
    except ValueError:
        tkinter.messagebox.showerror(title="Error", message="Passcode must be a number\nExample: 123456")
    else:
        for letter in word:
            if letter.isupper():
                if letter.lower() in ALPHABETS:
                    new_letter = ALPHABETS[ALPHABETS.index(letter.lower()) + shift]
                    decrypted_word += new_letter.upper()
            elif letter in ALPHABETS:
                new_letter = ALPHABETS[ALPHABETS.index(letter) + shift]
                decrypted_word += new_letter
            else:
                decrypted_word += letter
        clipboard.copy(decrypted_word)
        text_entry.delete(0, END)
        text_entry.insert(END, string=f"{decrypted_word}")
        tkinter.messagebox.showinfo(title="Success", message="The decrypted word's has been saved to your clipboard")


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


# Creating the image
canvas = Canvas(width=250, height=250, bg=WHITE, highlightthickness=0)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)
window.mainloop()
