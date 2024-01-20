import cv2
import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from datetime import datetime

cam_on = False
cap = None
out = None
mainWindow = Tk()

# CREATE FOLDER
path = ''
path2 = ''

def create_folder():
    global path
    now = datetime.now()
    month = now.month
    year = now.year
    day = now.day

    path = "./" + str(year) + "" + str(month) + "" + str(day)

    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)

def create_patient_folder():
    global path2
    create_folder()
    now = datetime.now()
    month = now.month
    year = now.year
    day = now.day
    path2 = os.path.join("./" + str(year) + "" + str(month) + "" + str(day), )
    print(path2)

    try:
        os.mkdir(path2)
        print("Folder %s created!" % path2)
    except FileExistsError:
        print("Folder %s already exists" % path2)

def show_frame():
    global frame, out
    if cam_on:
        ret, frame = cap.read()

        if ret:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image).resize((810, 640))
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
    global out
    stop_vid()

    file_types = [("MP4 Files", "*.mp4")]
    file_path = filedialog.asksaveasfile(filetypes=file_types, defaultextension=file_types)

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

create_patient_folder = Button(mainWindow, text="Create Patient Folder", command=create_patient_folder)
create_patient_folder.pack()

mainFrame = Frame(mainWindow, height=640, width=810)
mainFrame.place(x=350, y=0)

cameraFrame = Frame(mainWindow, height=640, width=405)
cameraFrame.place(x=0, y=0)

vid_lbl = Label(mainFrame)
vid_lbl.pack()

# Buttons
TurnCameraOn = Button(cameraFrame, text="Start Video", command=start_vid)
TurnCameraOn.place(x=0, y=0)
TurnCameraOff = Button(cameraFrame, text="Stop Video", command=stop_vid)
TurnCameraOff.place(x=0, y=300)

SaveVideoButton = Button(cameraFrame, text="Save Video", command=save_vid)
SaveVideoButton.place(x=0, y=600)

mainWindow.mainloop()