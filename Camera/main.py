import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import uuid
import os

def takePhoto():
    ret, frame = video_capture.read()
    if ret:
        file_name = os.path.join("photos", str(uuid.uuid4()) + ".png")
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

window = tk.Tk()
window.title("Camera")
window.geometry("800x550")
window.resizable(False, False)

video_source = 0
video_capture = cv2.VideoCapture(video_source)

canvas = tk.Canvas(window, width=600, height=450)
canvas.pack()

frame = tk.Frame(window)
frame.pack()

btn_takePhoto = tk.Button(frame, text="Take photo", width=20, command=takePhoto)
btn_takePhoto.pack(pady=10)

updateFrame()

btn_exit = tk.Button(frame, text="Exit", width=20, command=exitApp)
btn_exit.pack(pady=10)

window.mainloop()
