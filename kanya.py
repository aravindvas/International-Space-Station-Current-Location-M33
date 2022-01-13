from tkinter import *
import requests

def Qts():
    rsp2 = requests.get(url="https://api.kanye.rest/")
    rsp2.raise_for_status()
    d2 = rsp2.json()["quote"]
    c.itemconfig(ct2, text=d2)

w = Tk()
w.title("Aravindvas's Kayne's Quotes")
w.config(padx=50, pady=50)

c = Canvas(width=300, height=414)
im = PhotoImage(file="background.png")
im2 = PhotoImage(file="kanye.png")
c.create_image(150, 206, image=im)
ct2 = c.create_text(150, 206, text="Click on my face", width=250, font=("Arial", 30, "bold"), fill="white")
c.grid(row=0, column=0)

b = Button(image=im2, highlightthickness=0, command=Qts)
b.grid(row=1, column=0)

w.mainloop()