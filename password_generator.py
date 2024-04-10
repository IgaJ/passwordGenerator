import tkinter as tk
import random
import string


def generate(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


def generate_print():
    password = generate(12)
    field.delete(0, tk.END)
    field.insert(0, password)


def copy():
    password = field.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()


root = tk.Tk()
root.title("Password generator")

frame = tk.Frame(root)
frame.pack(pady=10)

field = tk.Entry(frame, font=("Arial", 8), width=30, bd=1, relief=tk.SOLID)
field.pack(side=tk.LEFT, padx=5)

button_generate = tk.Button(root, text="  generuj  ", font=("Tahoma", 8), command=generate_print, bg="white", fg="black")
button_generate.pack(side=tk.LEFT, padx=5)

button_copy = tk.Button(root, text="  kopiuj  ", font=("Tahoma", 8), command=copy, bg="white", fg="black")
button_copy.pack(pady=5)

root.mainloop()
