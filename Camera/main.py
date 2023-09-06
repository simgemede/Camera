import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import uuid
import os
import datetime

def takePhoto():
    ret, frame = video_capture.read()
    if ret:
        file_name = os.path.join("photos", str(uuid.uuid4()) + ".png")

        if var_date_time.get() == 1:
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            frame = cv2.putText(frame, current_datetime, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imwrite(file_name, frame)
        print(f"Photo was saved.: {file_name}")

def updateFrame():
    ret, frame = video_capture.read()
    if ret:
        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        canvas.photo = photo
    window.after(10, updateFrame)

def exitApp():
    video_capture.release()
    window.quit()

if not os.path.exists("photos"):
    os.makedirs("photos")

def onKeyPress(event):
    if event.keysym == "Return":
        takePhoto()

window = tk.Tk()
window.title("Camera")
window.geometry("800x600")
window.resizable(False, False)

video_source = 0
video_capture = cv2.VideoCapture(video_source)

canvas = tk.Canvas(window, width=600, height=450)
canvas.pack()

frame = tk.Frame(window)
frame.pack()

var_date_time = tk.IntVar()
chk_date_time = tk.Checkbutton(frame, text="Adding a Date and Time", variable=var_date_time)
chk_date_time.pack(pady=5)

btn_takePhoto = tk.Button(frame, text="Take photo", width=20, command=takePhoto)
btn_takePhoto.pack(pady=10)

updateFrame()

btn_exit = tk.Button(frame, text="Exit", width=20, command=exitApp)
btn_exit.pack(pady=10)

window.bind("<KeyPress>", onKeyPress)

window.mainloop()