import cv2
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognition System")
        
        # Images 
        title_lbl = Label(self.root, text="Face Recognition", font=("Times New Roman", 28, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=50)
        
        img_top = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\download1.jpg")
        img_top = img_top.resize((650, 700), Image.BICUBIC)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=650, height=700)
        
        img_lef = Image.open(r"F:\python course\CLASS01\Python-AI-Course-\student management system\images\download2.jpg")
        img_lef = img_lef.resize((950, 700), Image.BICUBIC)
        self.photoimg_lef = ImageTk.PhotoImage(img_lef)
        
        f_lbl = Label(self.root, image=self.photoimg_lef)
        f_lbl.place(x=650, y=50, width=950, height=700)
        
        # Button
        b1_1 = Button(self.root, text="Face Recognition", cursor="hand2", font=("Times New Roman", 20, "bold"), bg="darkgreen", fg="white", command=self.face_recog)
        b1_1.place(x=700, y=620, width=210, height=50)
        
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)   
            
            if len(features) == 0:
                return img  # No faces detected, return the original image
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))
                
                if confidence > 77:
                    # Establish database connection
                    conn = mysql.connector.connect(host="localhost", username="root", password="test@123", database="student")
                    my_cursor = conn.cursor()
                    
                    # Retrieve student details from the database
                    my_cursor.execute("SELECT Studentname, Student_id, Department FROM face1 WHERE Student_id=" + str(id))
                    student_data = my_cursor.fetchone()
                    
                    if student_data:
                        s_name, s_id, s_department = student_data
                        # Draw text on the image
                        cv2.putText(img, f"Student Name: {s_name}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Student ID: {s_id}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {s_department}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    else:
                        # If no data found, display "Unknown"
                        cv2.putText(img, "Unknown", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                
            return img
        
        def recognize(img, clf, facecascade):
            img = draw_boundary(img, facecascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        # Load face cascade classifier and trained model
        facecascade = cv2.CascadeClassifier("F:/python course/CLASS01/Python-AI-Course-/student management system/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        # Initialize video capture
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, facecascade)
            cv2.imshow("Welcome to Face Recognition", img)
            
            if cv2.waitKey(1) == 13:  # Press Enter key to exit
                break
        
        # Release video capture and close OpenCV windows
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
