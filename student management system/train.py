from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognition system")
          
        title_lbl = Label(self.root,text= "Train Data Set",font=("Times new Roman",28,"bold"),bg="teal",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=50)
        
        img_top = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\top1.jpg")
        img_top = img_top.resize((1530,325),Image.BICUBIC)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1530,height=325)
        
        # Button
        b1_1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Times new Roman",30,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=325,width=1530,height=50)
        
        img_bottom = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\top4.jpg")
        img_bottom = img_bottom.resize((1530,350),Image.BICUBIC)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=375,width=1530,height=350)
        
    
    def train_classifier(self):
        data_dir = "F:/python course/CLASS01/Python-AI-Course-/student management system/data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        
        for image_path in path:
            img = Image.open(image_path).convert('L')  # Convert to grayscale   
            image_np = np.array(img, 'uint8') 
            id = int(os.path.split(image_path)[1].split('.')[1])
            
            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training", image_np)
            cv2.waitKey(1)  # Wait for a key press, not comparison with 13
        ids = np.array(ids)
        
        # Train the classifier
        # Train the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed")
        

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
