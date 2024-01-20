# Write your code here :-)
from tkinter import*
from tkinter import ttk
import tkinter as tk
import customtkinter
#import self
import top as top
import home as h
from PIL import ImageTk, Image


def add_patient_page():
    add_patient_frame = tk.Frame(h.main_frame)


    def on_resize(event):
        # resize the background image to the size of label
        #photo = ImageTk.PhotoImage(Image.open("images/bg.jpg"))
        photo = Image.open('images/bg.jpg') # load the background image
        image = photo.resize((event.width, event.height), Image.ANTIALIAS)
        # update the image of the label
        img.image = ImageTk.PhotoImage(image)
        img.config(image=img.image)

    img= tk.Label(add_patient_frame)
    img.place(x=0, y=0,relwidth=1, relheight=1) # make label l to fit the parent window always
    img.bind('<Configure>', on_resize) # on_resi

    patient_name_label = tk.Label(add_patient_frame, text="Add Patient Data",font=('Bold',20),fg="#02808A",bg="#c7ebed")
    patient_name_label.grid(row=0, column=1,pady=20)


    patient_name_label = tk.Label(add_patient_frame, text="            Patient Name",font=('Bold',15),fg="#02808A",bg="#c7ebed")
    patient_name_label.grid(row=1, column=0,pady=25)
    patient_name_entry = customtkinter.CTkEntry(master=add_patient_frame,
                                width=610,
                               height=50,
                               corner_radius=20,
                               placeholder_text="Enter Patient Name",
                               font=('Inter',16),
                               fg_color="#c7ebed",
                               bg_color="#c7ebed",
                               border_color="#02808A",)
    #patient_name_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,border=0)
    #patient_name_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    patient_name_entry.grid(row=1, column=1)

    patient_id_label = tk.Label(add_patient_frame, text="        Patient ID",font=('Bold',15),fg="#02808A",bg="#c7ebed")
    patient_id_label.grid(row=2, column=0,pady=25,padx=50)
    patient_id_entry=customtkinter.CTkEntry(master=add_patient_frame,
                               width=610,
                               height=50,
                               corner_radius=20,
                               placeholder_text="Enter Patient ID",
                               font=('Inter',16),
                               fg_color="#c7ebed",
                               bg_color="#c7ebed",
                               border_color="#02808A",)
    #patient_id_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,borderwidth=0)
    #patient_id_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    patient_id_entry.grid(row=2, column=1,pady=20)

    hospital_id_label = tk.Label(add_patient_frame, text="        Hospital ID",font=('Bold',15),fg="#02808A",bg="#c7ebed")
    hospital_id_label.grid(row=3, column=0,pady=25)
    hospital_id_entry = customtkinter.CTkEntry(master=add_patient_frame,
                               width=610,
                               height=50,
                               corner_radius=20,
                               placeholder_text="Enter Hospital ID",
                               font=('Inter',16),
                               fg_color="#c7ebed",
                               bg_color="#c7ebed",
                               border_color="#02808A",)
    #hospital_id_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,borderwidth=0)
    #hospital_id_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    hospital_id_entry.grid(row=3, column=1)

    phone_num_label = tk.Label(add_patient_frame, text="               Phone Number",font=('Bold',15),fg="#02808A",bg="#c7ebed")
    phone_num_label.grid(row=4, column=0,pady=25)
    phone_num_entry = customtkinter.CTkEntry(master=add_patient_frame,
                              width=610,
                               height=50,
                               corner_radius=20,
                               placeholder_text="Enter Phone Number",
                               font=('Inter',16),
                               fg_color="#c7ebed",
                               bg_color="#c7ebed",
                               border_color="#02808A",)
    #phone_num_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,borderwidth=0)
    #phone_num_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    phone_num_entry.grid(row=4, column=1,pady=20)

    age_label = tk.Label(add_patient_frame, text="Age",font=('Bold',15),fg="#02808A",bg="#c7ebed")
    age_label.grid(row=5, column=0,pady=25)
    age_entry = customtkinter.CTkEntry(master=add_patient_frame,
                               width=610,
                               height=50,
                               corner_radius=20,
                               placeholder_text="Enter Age",
                               font=('Inter',16),
                               fg_color="#c7ebed",
                               bg_color="#c7ebed",
                               border_color="#02808A",)
    #age_entry = tk.Entry(add_patient_frame, show="Age", width=120, highlightthickness=.5,borderwidth=0)
    #age_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    age_entry.grid(row=5, column=1)

    surgery_date_label = tk.Label(add_patient_frame, text="             Surgery Date",font=('Bold',15),fg="#02808A",bg="#c7ebed")
    surgery_date_label.grid(row=6, column=0,pady=20,)
    surgery_date_Entry = customtkinter.CTkEntry(master=add_patient_frame,
                               width=610,
                               height=50,
                               corner_radius=20,
                               placeholder_text="Enter Surgery Date",
                               font=('Inter',16),
                               fg_color="#c7ebed",
                               bg_color="#c7ebed",
                               border_color="#02808A",)
    #surgery_date_Spinbox = tk.Spinbox(add_patient_frame,from_='0',to='2023', width=118, highlightthickness=.5,borderwidth=0)
    #surgery_date_Spinbox.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    surgery_date_Entry.grid(row=6, column=1,pady=20,)


    sex_label = tk.Label(add_patient_frame,  justify=LEFT,text="Sex",font=('Bold',15),fg="#02808A",bg="#c7ebed")
    sex_label.grid(row=7, column=0,pady=20)
    sex_entry = customtkinter.CTkComboBox(master=add_patient_frame,
                                 #text="Sex",
                                 font=('Inter',20),
                                 text_color='#000000',
                                 values=["Male", "Female"],
                                 width=248,
                                 height=50,
                                 #border_width=0,
                                 corner_radius=20,
                                 fg_color="#c7ebed",
                                 bg_color="#c7ebed",
                                 border_color="#02808A",

                                 )
    #sex_entry = ttk.Combobox(add_patient_frame, width=50, justify=LEFT,values=["Male","Female"])
    #surgery_date_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    sex_entry.grid(row=7, column=1,pady=20,padx=30)

    add_button = customtkinter.CTkButton(master=add_patient_frame,
                                 text="Login",
                                 font=('Inter',20),
                                 text_color='#FFFFFF',
                                 #command=button_event,
                                 width=149,
                                 height=42,
                                 #border_width=0,
                                 corner_radius=20,
                                 fg_color="#02808A",
                                 bg_color="#c7ebed",
                                 border_color="#02808A",

                                 )
    #add_button = tk.Button(add_patient_frame, text="Add Patient", width=30,font=('Bold',15),fg="#FFFFFF",bg="#02808A")
    add_button.grid(row=8, column=1,pady=10,)




    add_patient_frame.grid(padx=0,pady=0,ipady=100,ipadx=200)
