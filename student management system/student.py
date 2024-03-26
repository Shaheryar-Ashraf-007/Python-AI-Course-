from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student_detail import Student
import os
import mysql.connector
from train import Train
from face_recognition import FaceRecognition


class  Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognition system")
        
        #IMAGES 
        
        img = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\recog5.jpg")
        img = img.resize((500,130),Image.BICUBIC)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl =Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        img1 = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\face.jpg")
        img1 = img1.resize((500,130),Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl =Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        
        img2 = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\recog11.jpg")
        img2 = img2.resize((500,130),Image.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl =Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
        img3 = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\recog13.jpg")
        img3 = img3.resize((1530,800),Image.BICUBIC)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img =Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=800)
        
        
        title_lbl = Label(bg_img,text= "FACE RECOGNITION ATTENDANCE SOFTWARE SYSTEM",font=("Times new Romen",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=50)
        
        
        # BUTTONS AND LABELS 
        img4 = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\recog14.jpg")
        img4 = img4.resize((180,180),Image.BICUBIC)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        
        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details , cursor="hand2")
        b1.place(x=100,y=90,width=180,height=180)
        
        b1_1 = Button(bg_img,text="Student Details",command=self.student_details ,cursor="hand2",font=("Times new Romen",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=240,width=180,height=40)
        
        
        #detect face 
        
        img5 = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\pic3.jpg")
        img5 = img5.resize((180,180),Image.BICUBIC)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        
        b1 = Button(bg_img,image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=400,y=90,width=180,height=180)
        
        b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Times new Romen",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=240,width=180,height=40)
        
        
        img6 = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\pic4.jpg")
        img6 = img6.resize((180,180),Image.BICUBIC)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        
        b2 = Button(bg_img,image=self.photoimg6, cursor="hand2")
        b2.place(x=740,y=90,width=180,height=180)
        
        b1_2 = Button(bg_img,text="Attandence",cursor="hand2",font=("Times new Romen",15,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=740,y=240,width=180,height=40)
        
        
        img7 = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\pic7.jpg")
        img7 = img7.resize((180,180),Image.BICUBIC)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        
        b2 = Button(bg_img,image=self.photoimg7, cursor="hand2")
        b2.place(x=1070,y=90,width=180,height=180)
        
        b1_2 = Button(bg_img,text="Help",cursor="hand2",font=("Times new Romen",15,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=1070,y=240,width=180,height=40)
        
        
        img8 = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\pic8.jpg")
        img8 = img8.resize((180,180),Image.BICUBIC)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        
        b2 = Button(bg_img,image=self.photoimg8,cursor="hand2",command= self.train_data)
        b2.place(x=100,y=350,width=180,height=180)
        
        b1_2 = Button(bg_img,text="Train Data",cursor="hand2",command= self.train_data,font=("Times new Romen",15,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=100,y=500,width=180,height=40)
        
        
        img9 = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\pic1.jpg")
        img9 = img9.resize((180,180),Image.BICUBIC)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        
        b2 = Button(bg_img,image=self.photoimg9, cursor="hand2",command=self.open_img,)
        b2.place(x=400,y=350,width=180,height=180)
        
        b1_2 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Times new Romen",15,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=400,y=500,width=180,height=40)
        
        
        
        img10 = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\pic6.jpg")
        img10 = img10.resize((180,180),Image.BICUBIC)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        
        b2 = Button(bg_img,image=self.photoimg10, cursor="hand2")
        b2.place(x=740,y=350,width=180,height=180)
        
        b1_2 = Button(bg_img,text="Developer",cursor="hand2",font=("Times new Romen",15,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=740,y=500,width=180,height=40)
        
        
        
        img11 = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\pic5.jpg")
        img11 = img11.resize((200,145),Image.BICUBIC)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        
        b2 = Button(bg_img,image=self.photoimg11, cursor="hand2")
        b2.place(x=1070,y=350,width=180,height=180)
        
        b1_2 = Button(bg_img,text="Exit",cursor="hand2",font=("Times new Romen",15,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=1070,y=500,width=180,height=40)
        
        
        
    def open_img(self):
        os.startfile("F:\python course\CLASS01\Python-AI-Course-\student management system\data")
        
        
        #==================Function Details =====================
    
    def student_details(self):
        self.new_window  = Toplevel(self.root)
        self.app = Student(self.new_window)
        
        
    def train_data(self):
        self.new_window  = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_data(self):
        self.new_window  = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)
        
        

        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    
        
    

