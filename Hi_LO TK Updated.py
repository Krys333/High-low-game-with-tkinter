from random import randint
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import time                         #this bit is for time delay "time.sleep(seconds)"         


window = tk.Tk()
window.geometry("447x483")
window.title("Hi_Lo Game")
photo = tk.PhotoImage(file = "favicon.png")
window.iconphoto(True, photo)

canvas = Canvas(window, width = 447, height = 483)          
canvas.place(x=0, y=0, relwidth=1, relheight=1)
img = PhotoImage(file="BgDice.png")      
canvas.create_image(0,0, anchor=NW, image=img)

secret = randint(0,100)

#maingame logic
def mygame(event=None):

    g = (int)(guess.get())
    if g < secret:
        lbl_result["text"] = "your guess is too low"
    if g > secret:
        lbl_result["text"] = "your guess is too high"
    if g == secret:
        lbl_result["text"] = "Bingo! You are correct."
        

window.bind('<Return>', mygame)

Welcome = tk.Frame(master=window)
frm_entry = tk.Frame(master=window)

Message = tk.Label(text="Welcome to Hi-Lo!", fg="white", bg="black")
Message.config(font=("Courier", 12))



# this is the number entry field
guess = tk.Entry(master=frm_entry, width=10, fg="white", bg="black")

#this is just a basic text after the entry box
txt_aft_usrEnt = tk.Label(master=frm_entry, text="guess", fg="white", bg="black")

guess.grid(row=0, column=0, sticky="e")
txt_aft_usrEnt.grid(row=0, column=1, sticky="w")


#this section is where the button is given its function
btn_convert = tk.Button(master=window, text="press to guess", command=mygame, fg="white", bg="black")
lbl_result = tk.Label(master=window, text="You are correct", fg="white", bg="black")


Welcome.grid(row=0, column=0, padx=10, pady=10)
Message.grid(row=0, column=0, padx=10, pady=10)

frm_entry.grid(row=1, column=0, padx=10, pady=150)
btn_convert.grid(row=1, column=1, pady=10)
lbl_result.grid(row=1, column=2, padx=10)


#bg_img.image = bg_img
window.mainloop()


