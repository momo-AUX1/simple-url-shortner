import pyshorteners
import tkinter as tk 
from tkinter import ttk
import pyperclip as pc

app = tk.Tk()
app.title("url shortner")
app.config(height=365,width=546)

T = tk.Label(
    app,
    text= "py Url Shortener",
    bg="green",
    font="roboto"
)


Te = ttk.Entry(
    app,
    width=65
)







Tee = ttk.Label(
    app,
    text= ""
)


def C():
    link = Te.get()
    P1 = pyshorteners.Shortener().tinyurl.short(link)
    Tee.config(text=P1 + "\n" + "(already copied to clipboard)")
    pc.copy(P1)
    






def C1():
    app.destroy()

B = tk.Button(
    app,
    text= "shorten!",
    command= C
)



B1 = tk.Button(
    app,
    text="close",
    command= C1
)


Tee.place(x=210,y=190)
B1.place(x=390,y=170)
B.place(x=90,y=170)
Te.place(x=70,y=120)
T.place(x=210,y=70)
app.mainloop()