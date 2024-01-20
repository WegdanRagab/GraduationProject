# Write your code here :-)
from tkinter import *
from tkinter import ttk
import tkinter as tk
import customtkinter
#import self
import top as top
import home as h
from PIL import ImageTk, Image


def add_patient_page():
    add_patient_frame = tk.Frame(h.main_frame)
    # add_patient_frame.configure(width=1440,height=1024)
    width = add_patient_frame.winfo_screenwidth()
    height = add_patient_frame.winfo_screenheight()

    imgTemp = Image.open("images/bg.jpg")
    img2 = imgTemp.resize((height, 1800))
    img2 = imgTemp.resize((width, height))
    img = ImageTk.PhotoImage(img2)

    label = Label(add_patient_frame,image=img)
    label.place(x=0, y=0,rely=1,relx=1)


    add_patient_frame.place()
# Write your code here :-)
