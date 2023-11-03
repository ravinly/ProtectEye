import cv2 
import tkinter
from function import face_data
from function import Distance_finder
from function import FocalLength
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

previous_distance = 30 
width =14.3 

root=tkinter.Tk()
width= root.winfo_screenwidth()
height= root .winfo_screenheight()
root.geometry("%dx%d" % (width, height))

image1 = Image.open("pic2.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=450, y=50)

def startpgm():
     
    img = cv2.imread("pic3.jpg")
    face_width = face_data(img)
    Focal_length = FocalLength(previous_distance, width,face_width)

    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        if ret==True:
            face_width_in_frame = face_data(frame)
            if face_width_in_frame !=0:
                Distance = round(Distance_finder(Focal_length, width,face_width_in_frame),2)
                if(Distance<=40):
                            messagebox.showwarning("Warning!!","Please go back to maintain a safe distance")
                cv2.putText(frame, "Distance from Camera "+"{}".format(Distance)+"CM", (50,50), cv2.FONT_HERSHEY_COMPLEX,1, (123,246,123),3)
            cv2.imshow("frame", frame )
            if cv2.waitKey(1)==ord("q"):
                break 
    video.release()




myButton1=Button(root,text="Start!",command=startpgm,width=20)

myButton1.pack()
myButton1.grid(row=0 ,column=0)
myButton1.place(x=740 , y=600)
root.mainloop()

cv2.destroyAllWindows()
