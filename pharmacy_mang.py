   
import random
import time 
import datetime
import MySQLdb
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class HOSPITAL():
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management system")
        self.root.geometry("1540x800+0+0")
        
        lbltitle = Label(self.root,bd = 20, relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="blue",bg="white",font=("times new roman ",50,"bold"))
        lbltitle.pack(side=TOP, fill= X)
    #==============DATA FRAME==========================
    
    
    
    
        dataframe = Frame(self.root,bd=20,relief=RIDGE)
        
        
        dataframe.place(x = 0,y= 130,width = 1530,height = 400)
        
        
        dataframeLeft =LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Information" )
        dataframeLeft.place(x=0,y=5,width= 980,height=350)
        
        
        dataframeRight = LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription" )
        
        
        dataframeRight.place(x=990,y=5,width= 460,height=350)
        
        
        
        
    #=======================buttons======================
    
    
        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x = 0,y=530,width = 1530,height = 70)
    #=======================details frame======================
    
    
        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x = 0,y=600,width = 1530,height = 190)
        lblNameTalet = Label(dataframeLeft,text="Name of Tablet:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTalet.grid(row = 0,column = 0)
        comNametable = ttk.Combobox(dataframeLeft,font=("arial",12,"bold"),width=33)
        comNametable ["values"] = ("Nice","Corona vaccine","maleria vaccine", "polio vaccine", "medicines","ASOZEN FORTE"," Aceclofenac "," paracetamol","  Chlorzoxazone",
                                                                                                                                        "Amoxible"," Amoxycillin",
                                                                                                                                        "MEF Plus", "Mefenamic Acid"," Paracetamol", 
                                                                                                                                        "NIMSE"," Nimesulid" ,"Parazex" ,"Paracetamol")
        comNametable.grid(row=0,column=1)
        lblNameref = (Label(dataframeLeft,text="Reference NO:",font=("arial",12,"bold"),padx=2))
        lblNameref.grid(row = 1,column = 0,sticky=W)
        txtref = Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)
        
        
        lblDose = Label(dataframeLeft,text="Dose:",font=("arial",12,"bold"),padx=6,pady=4)
        lblDose.grid(row = 2,column = 0)
        txtDose= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)
        
        
        lblNoofTablets  = Label(dataframeLeft,text="No of Tablets:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoofTablets.grid(row = 3,column = 0)
        txtnoofTablets = Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtnoofTablets.grid(row=3,column=1)
        
        
        lblLot = Label(dataframeLeft,text="LOT:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLot.grid(row = 4,column = 0)
        txtLot= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1)
        
        
        lblissueDate = Label(dataframeLeft,text="Issue Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lblissueDate.grid(row = 5,column = 0)
        txtissueDate = Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtissueDate.grid(row=5,column=1)
        
        
        lblExpDate = Label(dataframeLeft,text="Expire Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lblExpDate.grid(row = 6,column = 0)
        txtExpDate= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)
        
        
        lblDailyDose = Label(dataframeLeft,text="Daily Dose:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDailyDose.grid(row = 7,column = 0)
        txtDailyDose= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)
        
        lblSideEffect = Label(dataframeLeft,text="Side Effect:",font=("arial",12,"bold"),padx=4,pady=6)
        lblSideEffect.grid(row = 8,column = 0)
        txtSideEffect= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)
        
        lblFutureInfo = Label(dataframeLeft,text="Future Information:",font=("arial",12,"bold"),padx=2,pady=6)
        lblFutureInfo.grid(row = 0,column = 2)
        txtFutureInfo= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtFutureInfo.grid(row=0,column=3)
        
        
        lblBloodPressure = Label(dataframeLeft,text="Blood Pressure:",font=("arial",12,"bold"),padx=2,pady=6)
        lblBloodPressure.grid(row = 1,column = 2)
        txtbloodPressure= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtbloodPressure.grid(row=1,column=3)
        
        lblMeddicine = Label(dataframeLeft,text="Medicine:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeddicine.grid(row = 2,column = 2)
        txtMedicine= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtMedicine.grid(row=2,column=3)
        
        lblPateintId = Label(dataframeLeft,text="Patient Id:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPateintId.grid(row = 3,column = 2)
        txtpatientId= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtpatientId.grid(row=3,column=3)
        
        lblNhsNumber = Label(dataframeLeft,text="Nhs Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNhsNumber.grid(row = 4,column = 2)
        txtNhsNumber= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtNhsNumber.grid(row=4,column=3)
        
        lblPateintName = Label(dataframeLeft,text="Patient Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblPateintName.grid(row = 5,column = 2)
        txtpatientName= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtpatientName.grid(row=5,column=3)
        
        
        lblDateofBirth = Label(dataframeLeft,text="Date of Birth:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateofBirth.grid(row = 6,column = 2)
        txtDateofBirth= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtDateofBirth.grid(row=6,column=3)
        
        lblPateintAddress = Label(dataframeLeft,text="Patient Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPateintAddress.grid(row = 7,column = 2)
        txtpatientAddress= Entry(dataframeLeft,font=("arial",13,"bold"),width=35)
        txtpatientAddress.grid(row=7,column=3)
        
     #==============datafrmeright==============================
     
        
root = Tk()
obj = HOSPITAL(root)
root.mainloop()

