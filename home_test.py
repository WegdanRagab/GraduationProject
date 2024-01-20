import os
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk, filedialog
from tkinter.filedialog import asksaveasfile
from datetime import datetime
import cv2
import numpy as np
from PIL import Image, ImageTk
import customtkinter
from webcam import webcam

root = tk.Tk()
root.geometry('1440x1024')
root.title('Barrett’s Esophagus')
photo = PhotoImage(file="Logo/img.png")
root.iconphoto(False, photo)

cam_on = False
cap = None
out = None

now = datetime.now()
month = now.month
year = now.year
day = now.day
path = tk.StringVar()  # Receiving user's file_path selection
folder = tk.StringVar()

path = "./" + str(year) + "_" + str(month) + "_" + str(day)+str(folder)



def Report_page():
    def upload_file():
        f_types = [('Jpg Files', '*.jpg'),
                   ('PNG Files', '*.png')]  # type of files to select
        filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types)

        for f in filename:
            img = Image.open(f)  # read the image file
            img = img.resize((220, 190))  # new width & height
            img = ImageTk.PhotoImage(img)
            e1 = tk.Label(root)
            e1.place(x=1100, y=70)
            e1.image = img  # keep a reference! by attaching it to a widget attribute
            e1['image'] = img  # Show Image
        filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types)
        for f in filename:
            img = Image.open(f)  # read the image file
            img = img.resize((220, 190))  # new width & height
            img = ImageTk.PhotoImage(img)
            e2 = tk.Label(root)
            e2.place(x=1100, y=260)
            e2.image = img  # keep a reference! by attaching it to a widget attribute
            e2['image'] = img  # Show Image
        filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types)
        for f in filename:
            img = Image.open(f)  # read the image file
            img = img.resize((220, 190))  # new width & height
            img = ImageTk.PhotoImage(img)
            e3 = tk.Label(root)
            e3.place(x=1100, y=450)
            e3.image = img  # keep a reference! by attaching it to a widget attribute
            e3['image'] = img  # Show Image


    report_frame = tk.Frame(main_frame)

    # report_frame.config(bg="#D1EAF0")
    def on_resize(event):
        photo = Image.open('background/img.png')  # load the background image
        image = photo.resize((event.width, event.height))
        # update the image of the label
        img.image = ImageTk.PhotoImage(image)
        img.config(image=img.image)

    img = tk.Label()
    img.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
    img.bind('<Configure>', on_resize)  # on_resi

    input_text = StringVar()

    # top = Tk()
    label_head_result = Label(text="   Name:  ", bg="#D1EAF0",
                              fg='black', font=("Inter,bold"))
    label_head_result.place(x=15, y=40)
    entry = tk.Entry(bd=1)
    entry.place(x=80, y=42, width=160)

    age = Label(text="   Age:  ", bg='#D1EAF0',
                fg='black', font=("Inter,bold"))
    age.place(x=235, y=40)
    entry = tk.Entry(bd=1)
    entry.place(x=285, y=42, width=50)

    data = Label(text="First Data:  ", bg='#D1EAF0',
                 fg='black', font=("Inter,bold"))
    data.place(x=350, y=40)
    entry = tk.Entry(bd=1)
    entry.place(x=430, y=42)

    data_up = Label(text="Follow UP Data:  ", bg='#D1EAF0',
                    fg='black', font=("Inter,bold"))
    data_up.place(x=570, y=40)
    entry = tk.Entry(bd=1)
    entry.place(x=688, y=42)

    file = Label(text="fileNO:  ", bg='#D1EAF0',
                 fg='black', font=("Inter,bold"))
    file.place(x=820, y=40)
    entry = tk.Entry(bd=1)
    entry.place(x=875, y=42, width=120)

    sex = Label(text="Sex:  ", bg='#D1EAF0',
                fg='black', font=("Inter,bold"))
    sex.place(x=999, y=40)
    entry = tk.Entry(bd=1)
    entry.place(x=1035, y=42, width=80)

    rd = Label( text="Reffering Doctor:  ", bg='#D1EAF0', fg='#02808A', font=("Inter,bold", 16))

    rd.place(x=10, y=100)
    entry = tk.Entry( bd=1)
    entry.place(x=181, y=104, width=250)

    PR = Label(text="Premedication:  ", bg='#D1EAF0', fg='#02808A', font=("Inter,bold", 16))

    PR.place(x=455, y=100)
    entry = tk.Entry(bd=1)
    entry.place(x=610, y=104, width=250)
    scrolW = 90
    scrolH = 3

    label1 = Label(text='Procedure\nTechnique:', fg="#02808A", font=("Inter,bold", 16),
                   background="#D1EAF0")
    label1.place(x=10, y=150)
    scr = scrolledtext.ScrolledText(width=scrolW, height=scrolH, wrap=tk.WORD, bd=3)
    scr.place(x=130, y=150)

    label2 = Label(text='Indication:', fg="#02808A", font=("Inter,bold", 16), background="#D1EAF0")
    label2.place(x=10, y=220)
    scr2 = scrolledtext.ScrolledText(bd=4, width=scrolW, height=scrolH, wrap=tk.WORD)
    scr2.place(x=130, y=210)

    label3 = Label(text='Esophagus:', fg="#02808A", font=("Inter,bold", 16), background="#D1EAF0")
    label3.place(x=10, y=290)
    scr3 = scrolledtext.ScrolledText(width=scrolW, height=scrolH, wrap=tk.WORD, bd=3)
    scr3.place(x=130, y=280)

    label4 = Label(text='Stomach:', fg="#02808A", font=("Inter,bold", 16), background="#D1EAF0")
    label4.place(x=10, y=360)
    scr3 = scrolledtext.ScrolledText(width=scrolW, height=scrolH, wrap=tk.WORD, bd=3)
    scr3.place(x=130, y=350)

    label5 = Label(text='Pyloric Ring:', fg="#02808A", font=("Inter,bold", 15), background="#D1EAF0")
    label5.place(x=10, y=430)
    scr5 = scrolledtext.ScrolledText(width=scrolW, height=scrolH, wrap=tk.WORD, bd=3)
    scr5.place(x=130, y=420)

    label6 = Label(text='Duodenum:', fg="#02808A", font=("Inter,bold", 16), background="#D1EAF0")
    label6.place(x=10, y=500)
    scr6 = scrolledtext.ScrolledText(width=scrolW, height=scrolH, wrap=tk.WORD, bd=3)
    scr6.place(x=130, y=490)

    label7 = Label(text='Conclusion:', fg="#02808A", font=("Inter,bold", 16), background="#D1EAF0")
    label7.place(x=10, y=570)
    scr6 = scrolledtext.ScrolledText(width=scrolW, height=scrolH, wrap=tk.WORD, bd=3)
    scr6.place(x=130, y=560)

    label7 = Label(text='Signature:', fg="black", font=("Inter,bold", 15), background="#D1EAF0")
    label7.place(x=20, y=640)
    entry1 = tk.Entry( bd=1)
    entry1.place(x=140, y=645, width=180, height=20)

    label8 = Label(text='Patient ID:', fg="black", font=("Inter,bold" ,15), background="#D1EAF0")
    label8.place(x=470, y=640)
    entry1 = tk.Entry(bd=1)
    entry1.place(x=575, y=645, width=50)

    # t1=Label(root,text="Result",fg="#02808A" ,font=("Bold", 15 ),background="white")
    # t1.place(x=1100 ,y=70)
    fram1 = ttk.Frame(width=220, height=190, relief=SUNKEN)
    fram1.place(x=1100, y=70)

    # t2=Label(root ,text= "follow", fg="#02808A" , font=('Bold',16),background="white")
    # t2.place (x=1100 ,y=360)
    fram2 = ttk.Frame(width=220, height=190, relief=SUNKEN)
    fram2.place(x=1100, y=260)

    fram2 = ttk.Frame(width=220, height=190, relief=SUNKEN)
    fram2.place(x=1100, y=450)

    # b1= button (root,text='Result',width=10 , background="white",fg="#02808A"  )
    def subscribe():
        return messagebox.showinfo('', 'The report was successfully saved')

    b1 = Button(text="Save", width=12, height=1, bg="#02808A", cursor="watch", fg="white",
                command=subscribe)
    b1.place(x=760, y=630)

    b2 = Button(text="Print", width=12, height=1, bg="white", cursor="watch", fg="#0C5B61" , command=all_patient_page )
    b2.place(x=860, y=630)

    b1 = tk.Button(root, text='Upload Images', width=15, bg="#02808A",fg="white",command=lambda: upload_file())

    b1.place(x=1150, y=650)

    b3 = Button(text="Update", width=12, height=1, bg="#02808A", cursor="watch", fg="white",
                )
    b3.place(x=760, y=660)

    b4 = Button(text="Delete", width=12, height=1, bg="#02808A", cursor="watch", fg="white", )
    b4.place(x=860, y=660)


# ==========================================================================================================================

def result_page():
    global img, image
    video_frame = tk.Frame(main_frame)
    video_frame.configure(bg="#c7ebed")

    def on_resize(event):
        # resize the background image to the size of label
        # photo = ImageTk.PhotoImage(Image.open("images/bg.jpg"))
        photo = Image.open('background/img.png')  # load the background image
        image = photo.resize((event.width, event.height))
        # update the image of the label
        img.image = ImageTk.PhotoImage(image)

    img = tk.Label(video_frame)
    img.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
    img.bind('<Configure>', on_resize)  # on_resi

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    imgTemp = Image.open("background/img.png")
    img2 = imgTemp.resize((height, 1800))
    img2 = imgTemp.resize((width, height))
    img = ImageTk.PhotoImage(img2)

    label = Label(video_frame, image=img)
    label.pack(side='top', fill=Y, expand=True)
    frame = tk.Frame(video_frame, width=500, height=300, relief=SUNKEN)
    frame.place(x=70, y=50)
    frame1 = tk.Frame(video_frame, width=500, height=300, relief=SUNKEN)
    frame1.place(x=70, y=370)

    def upload_file():
        f_types = [('Jpg Files', '*.jpg'),
                   ('PNG Files', '*.png')]  # type of files to select
        filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types,initialfile=path)

        for f in filename:
            img = Image.open(f)  # read the image file
            img = img.resize((500, 300))  # new width & height
            img = ImageTk.PhotoImage(img)
            e1 = tk.Label(video_frame, width=500, height=300, )
            e1.place(x=70, y=50)
            # cv2.imshow("imgageee", img_up)
            e1.image = img  # keep a reference! by attaching it to a widget attribute
            e1['image'] = img
            img = ImageTk.PhotoImage(img)
            img_up = img.cv2.copy()
            print(img_up)
            # cv2.imshow("hj",img_up)
        # Show Image
        # filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)

    def result():
        global line_image, panel, img_up
        # Load the image
        image = cv2.imread("F:/final project/Desktop_app_python/Freezing Images/1.jpeg")
        width = 250
        height = 250
        Original_Image = cv2.resize(image, (width, height))

        # Create a mask for the ROI using the grabcut algorithm
        mask = np.zeros(Original_Image.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        rect = (10, 10, 225, 225)  # define the rectangle ROI here
        cv2.grabCut(Original_Image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        img = Original_Image * mask2[:, :, np.newaxis]
        cv2.imwrite("F:/final project/Desktop_app_python/Freezing Images/sample/ROI5.jpg", img)
        # cv2.imshow("Original Image", Original_Image)
        # cv2.imshow("ROI", img)

        # Convert the ROI to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        a_component = gray[:, :, 1]

        # binary threshold the a-channel
        th = cv2.threshold(a_component, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # function to obtain the largest contour in given image after filling it
        def get_region(image):
            contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            c = max(contours, key=cv2.contourArea)
            black = np.zeros((image.shape[0], image.shape[1]), np.uint8)
            mask = cv2.drawContours(black, [c], 0, 255, -1)
            return mask

        mask = get_region(th)

        # turning the region outside the green block white
        green_block = cv2.bitwise_and(img, img, mask=mask)
        green_block = (255, 255, 255)

        road = cv2.subtract(mask, th)
        # `road` contains some unwanted spots/contours which are removed using the function "get_region"
        only_road = get_region(road)

        road_colored = cv2.bitwise_and(img, img, mask=only_road)
        road_colored[only_road == 0] = (255, 255, 255)
        # converting to grayscale and applying threshold
        th2 = cv2.threshold(road_colored[:, :, 1], 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # using portion of the code from fmw42's answer, to get contours above certain area
        contours = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        result = img.copy()
        for c in contours:
            area = cv2.contourArea(c)
            if area > 1000:
                cv2.drawContours(result, [c], -1, (0, 255, 0), 2)
        # important###cv2.imshow("Contours", result)
        # important###cv2.imwrite("F:/final project/Desktop_app_python/contour5.jpg",result)

        # Find the longest contour (i.e., the green border)
        longest_contour = max(contours, key=cv2.contourArea)

        # Find the two farthest points on the contour
        farthest_points = cv2.approxPolyDP(longest_contour, epsilon=0.01 * cv2.arcLength(longest_contour, True),
                                           closed=True)
        print(farthest_points)

        max_distance = 0
        farthest_points = None
        for i in range(len(longest_contour)):
            for j in range(i + 1, len(longest_contour)):
                distance = np.linalg.norm(longest_contour[i] - longest_contour[j])
                if distance > max_distance:
                    max_distance = distance
                    farthest_points = (longest_contour[i], longest_contour[j])

        # Print the coordinates of the farthest points and the maximum distance between them
        if farthest_points is not None:
            pt1, pt2 = farthest_points
            line_img = result.copy()
            cv2.line(line_img, tuple(pt1[0]), tuple(pt2[0]), (255, 0, 0), 2)
            print("The farthest points are", farthest_points[0], "and", farthest_points[1])
            print("The distance between them is", int(max_distance))
        else:
            print("Could not find farthest points on contour.")
        # cv2.imshow("Line", line_img)
        # cv2.imwrite("F:/final project/Desktop_app_python/Freezing Images/Line5.jpg", line_img)

        text = "P"

        # Define the font properties
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_color = (255, 255, 255)  # white
        thickness = 2

        # Get the size of the number and text
        max_distance_size, _ = cv2.getTextSize(str(max_distance), font, font_scale, thickness)
        text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)

        # Calculate the position of the number and text
        max_distance_x = 170
        max_distance_y = 225
        text_x = max_distance_x + max_distance_size[0]
        text_y = max_distance_y

        # Write the number and text on the image
        line_img = cv2.putText(line_img, "{:.2f}".format(max_distance) + " " + text, (max_distance_x, max_distance_y),
                               font, font_scale, font_color, thickness)

        cv2.imwrite("F:/final project/Desktop_app_python/Freezing Images/Line5.jpg", line_img)
        # line_image = cv2.imread("F:/final project/Desktop_app_python/Freezing Images/Line5.jpg")
        line_image = ImageTk.PhotoImage(Image.open('F:/final project/Desktop_app_python/Freezing Images/Line5.jpg'))
        # cv2.imshow('image2', line_image)


        panel = Label(video_frame, image=line_image, width=500, height=300, )
        panel.place(x=70, y=400)
        # fram2=ttk.Frame(root, width=200,height=200,image = line_image, relief=SUNKEN)
        # fram2.place(x=1000 ,y=270)

        # cv2.waitKey(0)


    def save():
        path = "./" + str(year) + "_" + str(month) + "_" + str(day)

        files = [('Jpg Files', '*.jpg'),
                 ('PNG Files', '*.png')]  # type of files to select

        file = asksaveasfile(filetypes=files, defaultextension=files, initialfile=path)
        cv2.imwrite(img)

    button = customtkinter.CTkButton(master=video_frame,
                                     text="Upload Image",
                                     font=('Inter', 20),
                                     text_color='#02808A',
                                     command=upload_file,
                                     width=120,
                                     height=35,
                                     border_width=1,
                                     corner_radius=2,
                                     fg_color="#FFFFFF",
                                     border_color="#02808A",
                                     hover_color="#CED2D2"
                                     )
    button.place(relx=0.59, rely=0.36, anchor=tkinter.CENTER)

    button = customtkinter.CTkButton(master=video_frame,
                                     text="Result",
                                     font=('Inter', 20),
                                     text_color='#02808A',
                                     command=result,
                                     width=120,
                                     height=35,
                                     border_width=1,
                                     corner_radius=2,
                                     fg_color="#FFFFFF",
                                     border_color="#02808A",
                                     hover_color="#CED2D2"

                                     )
    button.place(relx=0.59, rely=0.43, anchor=tkinter.CENTER)

    button = customtkinter.CTkButton(master=video_frame,
                                     text="Save",
                                     font=('Inter', 20),
                                     text_color='#FFFFFF',
                                     command=save,
                                     width=120,
                                     height=35,
                                     border_width=1,
                                     corner_radius=2,
                                     fg_color="#00B2C6",
                                     border_color="#02808A",

                                     )
    button.place(relx=0.59, rely=0.50, anchor=tkinter.CENTER)

    def button_event():
        print("button pressed"),

    button = customtkinter.CTkButton(master=video_frame,
                                     text="FPS | 1",
                                     font=('Inter', 20),
                                     text_color='#000000',
                                     command=button_event,
                                     width=80,
                                     height=35,
                                     border_width=1,
                                     corner_radius=2,
                                     fg_color="#FFFFFF",
                                     border_color="#02808A",
                                     hover_color="#CED2D2"

                                     )
    button.place(relx=0.56, rely=0.66, anchor=tkinter.CENTER)

    video_frame.grid(padx=0, pady=0, ipady=0, ipadx=0)


##########################################################################################################################

def all_patient_page():
    all_patient_frame = tk.Frame(main_frame)


    search_frame= Frame(all_patient_frame,bg='#D1EAF0',)
    search_frame.grid(ipady=20,ipadx=700,padx=1)

    search= Label(search_frame,text="Search of patient report",bg='#D1EAF0', fg='#02808A', font=("Inter,bold", 12))
    search.grid(ipadx=1,ipady=20)

    search_entry = customtkinter.CTkEntry(master=search_frame,
                                          font=('Inter', 20),
                                          text_color='#000000',
                                          width=200,
                                          height=40,
                                          placeholder_text="Search",
                                          # border_width=0,
                                          corner_radius=10,
                                          fg_color="#c7ebed",
                                          bg_color="#c7ebed",
                                          border_color="#02808A",

                                          )
    search_entry.grid(padx= 10, pady= 22,row=0,column= 2,ipadx=25,ipady=5)
    search_button1 = customtkinter.CTkButton(master=search_frame,
                                           text="Search",
                                           font=('Inter', 20),
                                             text_color='#FFFFFF',
                                             # command=button_event,
                                             width=120,
                                             height=30,
                                             # border_width=0,
                                             corner_radius=8,
                                             fg_color="#02808A",
                                             bg_color="#c7ebed",
                                             border_color="#02808A",

                                             )
    search_button1.grid(padx= 20, pady= 22,row=0,column= 3,ipadx=10,ipady=5)

    detail_frame= Frame(all_patient_frame,bg="#F2F4F4")
    detail_frame.place(relx=0.001,rely=0.190,width=1050,height=600)


    scroll_x= Scrollbar(detail_frame,orient=HORIZONTAL)
    scroll_y= Scrollbar(detail_frame,orient=VERTICAL)
    patient_table= ttk.Treeview(detail_frame)
    patient_table.configure(yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
    patient_table.configure(selectmode='extended')
    scroll_y.configure(command=patient_table.yview)
    scroll_x.configure(command=patient_table.xview)
    scroll_x.place(relx=0.0001,rely=0.910,width=1070,height=40)
    scroll_y.place(relx=0.990, rely=0.195, width=30, height=620)

    patient_table.configure(
        columns=('Patient_Name', 'Age', 'FirstData', 'FollowUpData', 'FileNo', 'Sex',)

    )
    patient_table.heading('#0',text='Id',anchor=W)
    patient_table.heading("Patient_Name", text='PatientName', anchor=W)
    patient_table.heading("Age", text='Age',anchor=W)
    patient_table.heading("FirstData", text='FirstData',anchor=W)
    patient_table.heading("FollowUpData", text='FollowUpData',anchor=W)
    patient_table.heading("FileNo", text='FileNo',anchor=W)
    patient_table.heading("Sex", text='Sex',anchor=W)

    patient_table.column('#0', stretch=NO,minwidth=25,width=110)
    patient_table.column('#0', stretch=NO,minwidth=0,width=150)
    patient_table.column('#0', stretch=NO,minwidth=0,width=110)
    patient_table.column('#0', stretch=NO,minwidth=0,width=130)
    patient_table.column('#0', stretch=NO,minwidth=25,width=130)
    patient_table.column('#0', stretch=NO,minwidth=25,width=110)
    patient_table.column('#0', stretch=NO,minwidth=25,width=130)


    patient_table.place(x=0,y=1,width=1040,height=560)


    all_patient_frame.pack(expand=True, fill="both")



############################################################################################################################
def video_recording_page():
    video_rec_frame = tk.Frame(main_frame)

    video_frame = Frame(video_rec_frame, bg='#D1EAF0', )
    video_frame.grid(ipady=600, ipadx=600)
    frame1 = Frame(video_frame, width=600, height=500, relief=SUNKEN)

    frame1.place(x=50, y=80)

    frame2 = Frame(video_frame, width=400, height=200, relief=SUNKEN)

    frame2.place(x=50, y=80)

    path = tk.StringVar()  # Receiving user's file_path selection
    folder = tk.StringVar()
    # Receiving user's folder_name selection



    # Capture from camera
    def show_frame():
        global frame, out
        if cam_on:
            ret, frame = cap.read()

            if ret:
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image).resize((600, 500))
                imgtk = ImageTk.PhotoImage(image=img)
                vid_lbl.imgtk = imgtk
                vid_lbl.configure(image=imgtk)

                if out is not None:
                    out.write(frame)  # Write the frame to the video file

            vid_lbl.after(10, show_frame)

    def find_camera_index():
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                print("Camera index found:", i)
                cap.release()
                return i
        print("No camera index found.")
        return -1

    def start_vid():
        global cam_on, cap, out
        stop_vid()

        # Open the video capture
        cap = cv2.VideoCapture(0)

        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

        # Start capturing and recording
        cam_on = True
        show_frame()

    def stop_vid():
        global cam_on, cap, out
        cam_on = False

        if cap:
            cap.release()
        if out:
            out.release()
            out = None

    def save_vid():
        now = datetime.now()
        month = now.month
        year = now.year
        day = now.day
        path = tk.StringVar()  # Receiving user's file_path selection
        folder = tk.StringVar()
        path = "./" + str(year) + "_" + str(month) + "_" + str(day) + str(folder)
        global out
        stop_vid()

        file_types = [("MP4 Files", "*.mp4")]
        file_path = filedialog.asksaveasfile(filetypes=file_types, defaultextension=file_types,initialdir=path)

        if file_path is not None:
            # Open the saved video file and write the frames from the captured video
            saved_cap = cv2.VideoCapture('output.avi')
            out = cv2.VideoWriter(file_path.name, cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (640, 480))

            while True:
                ret, frame = saved_cap.read()

                if not ret:
                    break

                out.write(frame)

            saved_cap.release()
            out.release()
            print("Video saved successfully!")
    vid_lbl = Label(frame2)
    vid_lbl.pack()

    def upload_video():
        now = datetime.now()
        month = now.month
        year = now.year
        day = now.day
        path = tk.StringVar()  # Receiving user's file_path selection
        folder = tk.StringVar()
        path = "./" + str(year) + "_" + str(month) + "_" + str(day) + str(folder)


        # Create a tkinter root window (it won't be shown)
        root = tk.Tk()
        root.withdraw()

        video_file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")],initialdir=path)

        # Check if the user selected a video file
        if not video_file_path:
            print("No video file selected.")
            exit()

        # Open the video file
        cap = cv2.VideoCapture(video_file_path)

        # Check if the video file was opened successfully
        if not cap.isOpened():
            print("Error opening video file")
            exit()

        # Initialize the image counter
        img_counter = 0

        # Get the directory of the selected video file
        video_directory = "/".join(video_file_path.split("/")[:-1])

        # Loop through the video frames
        while True:
            # Read a frame from the video
            ret, frame = cap.read()

            # Check if the frame was read successfully
            if not ret:
                break

            # Display the frame
            cv2.imshow('frame', frame)

            # Wait for the user to press a key
            key = cv2.waitKey(50)

            # Check if the user pressed the spacebar to capture an image
            if key == ord(' '):
                # Increment the image counter
                img_counter += 1

                # Generate a unique filename for the captured image in the selected video's folder
                img_name = "{}/image_{}.jpg".format(video_directory, img_counter)

                # Save the current frame as an image
                cv2.imwrite(img_name, frame)

                # Print a message to the console
                print("Image captured:", img_name)

            # Check if the user pressed the 'q' key to quit
            if key == ord('q'):
                break

            # Release the video capture object and close all windows
        cap.release()




    def selectPath():
        path_ = "./" + str(year) + "_" + str(month) + "_" + str(day)
        path.set(path_)

    def create_file():
        print("folder_name: ", folder.get())
        print("path_name: ", path.get())
        dirs = os.path.join(path.get(), folder.get())
        if not os.path.exists(dirs):
            os.makedirs(dirs)
            tkinter.messagebox.showinfo('Tips:', 'Folder name created successfully!')
        else:
            tkinter.messagebox.showerror('Tips', 'The folder name exists, please change it')

    label1=Label(video_frame, text="Target path:", background="#D1EAF0", font=("Inter", 12), fg="#02808A")
    label1.grid(padx=692,pady=201)
    entry1=Entry(video_frame ,textvariable=path, width=18)
    entry1.place(x=788,y=200)

    sel_path = Button(video_frame,
                         text="Select Path",
                         width=12,
                         height=1,
                         font=('Inter', 12),
                         fg="#02808A",
                         background="#FFFFFF",
                         borderwidth=1,
                         command=selectPath,
                         )
    sel_path.place(x=920,y=195)

    label2=Label(video_frame, text="Folder name:", background="#D1EAF0", font=("Inter", 11), fg="#02808A")
    label2.place(x=692,y=241)

    entry2=Entry(video_frame, textvariable=folder,width=18)
    entry2.place(x=788,y=242)

    create_btn = Button(master=video_frame,
                           text="Create Folder",
                           width=12,
                           height=1,
                           font=('Inter', 12),
                           fg="#02808A",
                           background="#FFFFFF",
                           borderwidth=1,
                           command=create_file,

                           )
    create_btn.place(x=920,y=240)

    vid_rec_btn = Button(master=video_frame,
                            text="Video Recorder",
                            width=18,
                            height=1,
                            font=('Inter', 15),
                            command=start_vid,
                            fg="#02808A",
                            background="#FFFFFF",
                            borderwidth=1,
                            )

    vid_rec_btn.place(x=720,y=300)

    upload_btn = Button(master=video_frame,
                          text="Upload Video",
                           width=18,
                           height=1,
                           font=('Inter', 15),
                           command=upload_video,
                           fg="#02808A",
                           background="#FFFFFF",
                           borderwidth=1,
                           )
    upload_btn.place(x=720,y=350)

    stop_btn = Button(master=video_frame,
                         text="Stop",
                         width=10,
                         height=1,
                         font=('Inter', 15),
                         command=stop_vid,
                         fg="#FFFFFF",
                         background="#02808A",
                         borderwidth=1,
                         )
    stop_btn.place(x=700,y=450)

    save_btn = Button(master=video_frame,
                         text="Save",
                         width=10,
                         height=1,
                         command=save_vid,
                         font=('Inter', 15),
                         fg="#FFFFFF",
                         background="#02808A",
                         borderwidth=1,
                         )
    save_btn.place(x=850,y=450)

    video_rec_frame.grid(padx=0, pady=0, ipady=0, ipadx=0)


##########################################################################################################################
def add_patient_page():
    add_patient_frame = tk.Frame(main_frame)

    def on_resize(event):
        # resize the background image to the size of label
        # photo = ImageTk.PhotoImage(Image.open("images/bg.jpg"))
        photo = Image.open('background/img.png')  # load the background image
        image = photo.resize((event.width, event.height))
        # update the image of the label
        img.image = ImageTk.PhotoImage(image)
        img.config(image=img.image)

    img = tk.Label(add_patient_frame)
    img.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
    img.bind('<Configure>', on_resize)  # on_resi

    # patient_name_label = tk.Label(add_patient_frame, text="Add Patient Data",font=('Bold',20),fg="#02808A",bg="#c7ebed")
    # patient_name_label.place(rely=.02,relx=.3)

    patient_name_label = tk.Label(add_patient_frame, text="Patient Name        ", font=('Bold', 15), fg="#02808A",
                                  bg="#c7ebed")
    patient_name_label.place(rely=.05, relx=.02)
    patient_name_entry = customtkinter.CTkEntry(master=add_patient_frame,
                                                width=610,
                                                height=50,
                                                corner_radius=8,
                                                placeholder_text="Enter Patient Name",
                                                font=('Inter', 16),
                                                fg_color="#c7ebed",
                                                bg_color="#c7ebed",
                                                border_color="#02808A", )
    # patient_name_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,border=0)
    # patient_name_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    patient_name_entry.place(rely=.05, relx=.25)

    patient_id_label = tk.Label(add_patient_frame, text="Patient ID              ", font=('Bold', 15), fg="#02808A",
                                bg="#c7ebed")
    patient_id_label.place(rely=.15, relx=.02)
    patient_id_entry = customtkinter.CTkEntry(master=add_patient_frame,
                                              width=610,
                                              height=50,
                                              corner_radius=8,
                                              placeholder_text="Enter Patient ID",
                                              font=('Inter', 16),
                                              fg_color="#c7ebed",
                                              bg_color="#c7ebed",
                                              border_color="#02808A", )
    # patient_id_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,borderwidth=0)
    # patient_id_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    patient_id_entry.place(rely=.15, relx=.25)

    hospital_id_label = tk.Label(add_patient_frame, text="Hospital ID", font=('Bold', 15), fg="#02808A", bg="#c7ebed")
    hospital_id_label.place(rely=.25, relx=.02)
    hospital_id_entry = customtkinter.CTkEntry(master=add_patient_frame,
                                               width=610,
                                               height=50,
                                               corner_radius=8,
                                               placeholder_text="Enter Hospital ID",
                                               font=('Inter', 16),
                                               fg_color="#c7ebed",
                                               bg_color="#c7ebed",
                                               border_color="#02808A", )
    # hospital_id_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,borderwidth=0)
    # hospital_id_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    hospital_id_entry.place(rely=.25, relx=.25)

    phone_num_label = tk.Label(add_patient_frame, text="Phone Number", font=('Bold', 15), fg="#02808A", bg="#c7ebed")
    phone_num_label.place(rely=.35, relx=.02)
    phone_num_entry = customtkinter.CTkEntry(master=add_patient_frame,
                                             width=610,
                                             height=50,
                                             corner_radius=8,
                                             placeholder_text="Enter Phone Number",
                                             font=('Inter', 16),
                                             fg_color="#c7ebed",
                                             bg_color="#c7ebed",
                                             border_color="#02808A", )
    # phone_num_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,borderwidth=0)
    # phone_num_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    phone_num_entry.place(rely=.35, relx=.25)

    age_label = tk.Label(add_patient_frame, text="Birth Date", font=('Bold', 15), fg="#02808A", bg="#c7ebed")
    age_label.place(rely=.45, relx=.02)
    age_entry = customtkinter.CTkEntry(master=add_patient_frame,
                                       width=248,
                                       height=50,
                                       corner_radius=8,
                                       placeholder_text="Enter Birth Date",
                                       font=('Inter', 16),
                                       fg_color="#c7ebed",
                                       bg_color="#c7ebed",
                                       border_color="#02808A", )
    # age_entry = tk.Entry(add_patient_frame, show="Age", width=120, highlightthickness=.5,borderwidth=0)
    # age_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    age_entry.place(rely=0.45, relx=.25)

    surgery_date_label = tk.Label(add_patient_frame, text="Surgery Date           ", font=('Bold', 15), fg="#02808A",
                                  bg="#c7ebed")
    surgery_date_label.place(rely=.55, relx=.02)
    surgery_date_Entry = customtkinter.CTkEntry(master=add_patient_frame,
                                                width=248,
                                                height=50,
                                                corner_radius=8,
                                                placeholder_text="Enter Surgery Date",
                                                font=('Inter', 16),
                                                fg_color="#c7ebed",
                                                bg_color="#c7ebed",
                                                border_color="#02808A", )
    # surgery_date_Spinbox = tk.Spinbox(add_patient_frame,from_='0',to='2023', width=118, highlightthickness=.5,borderwidth=0)
    # surgery_date_Spinbox.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    surgery_date_Entry.place(rely=0.55, relx=.25)

    sex_label = tk.Label(add_patient_frame, justify=LEFT, text="Sex                         ", font=('Bold', 15),
                         fg="#02808A", bg="#c7ebed")
    sex_label.place(rely=.65, relx=.02)
    sex_entry = customtkinter.CTkComboBox(master=add_patient_frame,
                                          # text="Sex",
                                          font=('Inter', 20),
                                          text_color='#000000',
                                          values=["Male", "Female"],
                                          width=248,
                                          height=50,
                                          # border_width=0,
                                          corner_radius=8,
                                          fg_color="#c7ebed",
                                          bg_color="#c7ebed",
                                          border_color="#02808A",

                                          )
    # sex_entry = ttk.Combobox(add_patient_frame, width=50, justify=LEFT,values=["Male","Female"])
    # surgery_date_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    sex_entry.place(rely=.65, relx=.25)

    add_button = customtkinter.CTkButton(master=add_patient_frame,

                                         text="Add Patient",
                                         font=('Inter', 20),
                                         text_color='#FFFFFF',
                                         command=lambda: pages(video_recording_page),
                                         width=149,
                                         height=42,
                                         # border_width=0,
                                         corner_radius=8,
                                         fg_color="#02808A",
                                         bg_color="#c7ebed",
                                         border_color="#02808A",

                                         )
    # add_button = tk.Button(add_patient_frame, text="Add Patient", width=30,font=('Bold',15),fg="#FFFFFF",bg="#02808A")
    add_button.place(rely=0.68, relx=.8)

    add_button = customtkinter.CTkButton(master=add_patient_frame,

                                         text="Next",
                                         font=('Inter', 20),
                                         text_color='#FFFFFF',
                                         command=lambda: pages(video_recording_page),
                                         width=149,
                                         height=42,
                                         # border_width=0,
                                         corner_radius=8,
                                         fg_color="#02808A",
                                         bg_color="#c7ebed",
                                         border_color="#02808A",

                                         )
    # add_button = tk.Button(add_patient_frame, text="Add Patient", width=30,font=('Bold',15),fg="#FFFFFF",bg="#02808A")
    add_button.place(rely=0.75, relx=.8)

    add_patient_frame.pack(expand=True, fill="both")


###############################################################################################################################
main_frame = tk.Frame(root)


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def pages(page):
    delete_pages()
    page()


options_frame = tk.Frame(root, bg='#03B5C7')

icon1 = ImageTk.PhotoImage(Image.open("icons/add patient data.png"))
patient_btn = customtkinter.CTkButton(master=options_frame,
                                      text="Add patient\'s ",
                                      font=('Inter', 20, 'bold'),
                                      text_color='#02808A',
                                      command=lambda: pages(add_patient_page),
                                      width=259,
                                      height=56,
                                      image=icon1,
                                      anchor="w",
                                      # border_width=0,
                                      corner_radius=8,
                                      fg_color="#FFFFFF",
                                      bg_color="#03B5C7",
                                      border_color="#02808A",
                                      hover_color="#F5F3F3"

                                      )
# patient_btn = tk.Button(options_frame,width=25,text='Add patient\'s data',font=('Bold',15),fg='#03B5C7',bd=0, command=lambda:pages(add_patient_page))
patient_btn.place(x=20, y=20)

icon2 = ImageTk.PhotoImage(Image.open("icons/all patient data.png"))
all_patient_btn = customtkinter.CTkButton(master=options_frame,
                                          text="All patient\'s",
                                          font=('Inter', 20, 'bold'),
                                          text_color='#02808A',
                                          command=lambda: pages(all_patient_page),
                                          width=259,
                                          height=56,
                                          image=icon2,
                                          anchor="w",
                                          # border_width=0,
                                          corner_radius=8,
                                          fg_color="#FFFFFF",
                                          bg_color="#03B5C7",
                                          border_color="#02808A",
                                          hover_color="#F5F3F3"

                                          )
# images_btn = tk.Button(options_frame,width=25, text='All patient page',font=('Bold',15),fg='#03B5C7',bd=0, command=lambda:pages(all_patient_page))
all_patient_btn.place(x=20, y=100)

icon3 = ImageTk.PhotoImage(Image.open("icons/video.png"))
video_btn = customtkinter.CTkButton(master=options_frame,
                                    text="Result",
                                    font=('Inter', 20, "bold"),
                                    text_color='#02808A',
                                    command=lambda: pages(result_page),
                                    width=259,
                                    height=56,
                                    image=icon3,
                                    anchor="w",
                                    # border_width=0,
                                    corner_radius=8,
                                    fg_color="#FFFFFF",
                                    bg_color="#03B5C7",
                                    border_color="#02808A",
                                    hover_color="#F5F3F3"

                                    )
# video_btn = tk.Button(options_frame,width=25, text='Video',font=('Bold',15),fg='#03B5C7',bd=0, command=lambda:pages(video_page))
video_btn.place(x=20, y=180)

icon4 = ImageTk.PhotoImage(Image.open("icons/report.png"))
report_btn = customtkinter.CTkButton(master=options_frame,
                                     text="Report",
                                     font=('Inter', 20, 'bold'),
                                     text_color='#02808A',
                                     command=lambda: pages(Report_page),
                                     width=259,
                                     height=56,
                                     image=icon4,
                                     anchor="w",
                                     # border_width=0,
                                     corner_radius=8,
                                     fg_color="#FFFFFF",
                                     bg_color="#03B5C7",
                                     border_color="#02808A",
                                     hover_color="#F5F3F3"

                                     )
# report_btn = tk.Button(options_frame,width=25, text='Report',font=('Bold',15),fg='#03B5C7',bd=0, command=lambda:pages(Report_page))
report_btn.place(x=20, y=260)


def close():
    # win.destroy()
    root.quit()

icon5 = ImageTk.PhotoImage(Image.open("icons/exit.png"))
Exit_btn = customtkinter.CTkButton(master=options_frame,
                                   text="Exit",
                                   font=('Inter', 20, 'bold'),
                                   text_color='#02808A',
                                   anchor="w",
                                   width=259,
                                   height=56,
                                   image=icon5,
                                   # border_width=0,
                                   corner_radius=8,
                                   fg_color="#FFFFFF",
                                   bg_color="#03B5C7",
                                   border_color="#02808A",
                                   hover_color="#F5F3F3",
                                   command=close,

                                   )
# Exit_btn = tk.Button(options_frame,width=25, text='Exit',font=('Bold',15),fg='#03B5C7',bd=0)
Exit_btn.place(x=20, y=440)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=304, height=955)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=1406, height=1024, bg="#c7ebed")


def on_resize(event):
    # resize the background image to the size of label
    # photo = ImageTk.PhotoImage(Image.open("images/bg.jpg"))
    photo = Image.open('background/background.png')  # load the background image
    image = photo.resize((event.width, event.height))
    # update the image of the label
    img.image = ImageTk.PhotoImage(image)
    img.config(image=img.image)


img = tk.Label(main_frame)
img.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
img.bind('<Configure>', on_resize)  # on_resi

root.mainloop()
