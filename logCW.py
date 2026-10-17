from tkinter import *

root = Tk()
root.title("Login App")
root.geometry("400x400")

frame = Frame(master=root, height=200, width=360, bg="#01fef6")

lbl1 = Label(frame, text = "Full Name", bg="#f0f4eb", fg="#1A0E0E", width=12)
lbl2 = Label(frame, text = "Email id", bg="#000100", fg="#FFFFFF", width=12)
lbl3 = Label(frame, text = "enterPassword", bg="#0e0f0c", fg="#FFFFFF", width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="?")
def display():
    name = name_entry.get()
    greet = "Hello " + name
    message = "\nthank you for logging in"
    textbox.insert(END, greet + message)   


textbox = Text(bg="#0d100a", fg="#FFFFFF")
btn = Button(frame, text="create your Account", bg="#F0F1EF", command=display)
frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=60)
email_entry.place(x=150, y=60)
lbl3.place(x=20, y=100)
pass_entry.place(x=150, y=100)
btn.place(x=150, y=140)
textbox.place(x=20, y=180)

root.mainloop()
