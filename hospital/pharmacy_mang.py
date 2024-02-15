import random
import time 
import datetime
import MySQLdb
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class HOSPITAL():
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management system")
        self.root.geometry("1540x800+0+0")
        
        #"nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "nhsnumber", "storage", "pname", "dob", "address"
        self.nameoftablets = StringVar()
        self.ref = StringVar()
        self.dose = StringVar()
        self.nooftablets = StringVar()
        self.lot = StringVar()
        self.issuedate = StringVar()
        self.expdate = StringVar()
        self.dailydose = StringVar()
        self.SideEffect = StringVar()
        self.FutureInfo = StringVar()
        self.BloodPressure = StringVar()
        self.Meddicine= StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowtoUseMedication = StringVar()
        self.PatientId= StringVar()
        self.NhsNumber = StringVar()
        self.PateintName = StringVar()
        self.DateofBirth = StringVar()
        self.PateintAddress = StringVar()
        self.StorageAdvice = StringVar()

               
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="blue", bg="white", font=("times new roman ", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)
        
        #==============DATA FRAME==========================
        dataframe = Frame(self.root, bd=20, relief=RIDGE)
        dataframe.place(x=0, y=100, width=1530, height=400)
        
        dataframeLeft = LabelFrame(dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Patient Information")
        dataframeLeft.place(x=3, y=5, width=980, height=350)
        
        dataframeRight = LabelFrame(dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
        dataframeRight.place(x=990, y=5, width=350, height=350)
        
        #=======================buttons======================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=480, width=1360, height=70)
        
        #=======================details frame======================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=545, width=1360, height=160)
        
        lblNameTalet = Label(dataframeLeft, text="Name of Tablet:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNameTalet.grid(row=0, column=0)
        comNametable = ttk.Combobox(dataframeLeft, state="readonly", textvariable=self.nameoftablets, font=("arial", 12, "bold"), width=33)
        comNametable["values"] = ("Nice", "Corona vaccine", "maleria vaccine", "polio vaccine", "medicines", "ASOZEN FORTE", " Aceclofenac ", " paracetamol", "  Chlorzoxazone", "Amoxible", " Amoxycillin", "MEF Plus", "Mefenamic Acid", " Paracetamol", "NIMSE", " Nimesulid", "Parazex", "Paracetamol")
        comNametable.grid(row=0, column=1)
        
        lblNameref = Label(dataframeLeft, text="Reference NO:", font=("arial", 12, "bold"), padx=2)
        lblNameref.grid(row=1, column=0, sticky=W)
        txtref = Entry(dataframeLeft, textvariable=self.ref, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1)
        
        lblDose = Label(dataframeLeft, text="Dose:", font=("arial", 12, "bold"), padx=6, pady=4)
        lblDose.grid(row=2, column=0)
        txtDose = Entry(dataframeLeft, textvariable=self.dose, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)
        
        lblNoofTablets = Label(dataframeLeft, text="No of Tablets:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoofTablets.grid(row=3, column=0)
        txtnoofTablets = Entry(dataframeLeft, textvariable=self.nooftablets, font=("arial", 13, "bold"), width=35)
        txtnoofTablets.grid(row=3, column=1)
        
        lblLot = Label(dataframeLeft, text="LOT:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLot.grid(row=4, column=0)
        txtLot = Entry(dataframeLeft, textvariable=self.lot, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4, column=1)
        
        lblissueDate = Label(dataframeLeft, text="Issue Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblissueDate.grid(row=5, column=0)
        txtissueDate = Entry(dataframeLeft, textvariable=self.issuedate, font=("arial", 13, "bold"), width=35)
        txtissueDate.grid(row=5, column=1)
        
        lblExpDate = Label(dataframeLeft, text="Expire Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0)
        txtExpDate = Entry(dataframeLeft, textvariable=self.expdate, font=("arial", 13, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)
        
        lblDailyDose = Label(dataframeLeft, text="Daily Dose:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0)
        txtDailyDose = Entry(dataframeLeft, textvariable=self.dailydose, font=("arial", 13, "bold"), width=35)
        txtDailyDose.grid(row=7, column=1)
        
        lblSideEffect = Label(dataframeLeft, text="Side Effect:", font=("arial", 12, "bold"), padx=4, pady=6)
        lblSideEffect.grid(row=8, column=0)
        txtSideEffect = Entry(dataframeLeft, textvariable=self.SideEffect, font=("arial", 13, "bold"), width=35)
        txtSideEffect.grid(row=8, column=1)
        
        lblFutureInfo = Label(dataframeLeft, text="Future Information:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblFutureInfo.grid(row=0, column=2)
        txtFutureInfo = Entry(dataframeLeft, textvariable=self.FutureInfo, font=("arial", 13, "bold"), width=35)
        txtFutureInfo.grid(row=0, column=3)
        
        lblBloodPressure = Label(dataframeLeft, text="Blood Pressure:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2)
        txtbloodPressure = Entry(dataframeLeft, textvariable=self.BloodPressure, font=("arial", 13, "bold"), width=35)
        txtbloodPressure.grid(row=1, column=3)
        
        lblMeddicine = Label(dataframeLeft, text="Medicine:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeddicine.grid(row=2, column=2)
        txtMedicine = Entry(dataframeLeft, textvariable=self.Meddicine, font=("arial", 13, "bold"), width=35)
        txtMedicine.grid(row=2, column=3)
        
        lblPateintId = Label(dataframeLeft, text="Patient Id:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPateintId.grid(row=3, column=2)
        txtpatientId = Entry(dataframeLeft, textvariable=self.PatientId, font=("arial", 13, "bold"), width=35)
        txtpatientId.grid(row=3, column=3)
        
        lblNhsNumber = Label(dataframeLeft, text="Nhs Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNhsNumber.grid(row=4, column=2)
        txtNhsNumber = Entry(dataframeLeft, textvariable=self.NhsNumber, font=("arial", 13, "bold"), width=35)
        txtNhsNumber.grid(row=4, column=3)
        
        lblPateintName = Label(dataframeLeft, text="Patient Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPateintName.grid(row=5, column=2)
        txtpatientName = Entry(dataframeLeft, textvariable=self.PateintName, font=("arial", 13, "bold"), width=35)
        txtpatientName.grid(row=5, column=3)
        
        lblDateofBirth = Label(dataframeLeft, text="DateofBirth:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateofBirth.grid(row=6, column=2)
        txtDateofBirth = Entry(dataframeLeft, textvariable=self.DateofBirth, font=("arial", 13, "bold"), width=35)
        txtDateofBirth.grid(row=6, column=3)
        
        lblPateintAddress = Label(dataframeLeft, text="PatientAddress:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPateintAddress.grid(row=7, column=2)
        txtpatientAddress = Entry(dataframeLeft, textvariable=self.PateintAddress, font=("arial", 13, "bold"), width=35)
        txtpatientAddress.grid(row=7, column=3)
        
        #==============datafrmeright===========================================
        self.txtPrescription = Text(dataframeRight, font=("arial", 12, "bold"), width=35, height=16, padx=0, pady=6)
        self.txtPrescription.grid(row=0, column=0)
        
        #=================================buttons===============================
        btnPrescription = Button(Buttonframe, text="Prescription", font=("arial", 12, "bold"), bg="green", fg="white", width=21, height=2)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=21, height=2)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=21, height=2)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=21, height=2)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=21, height=2)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=21, height=2)
        btnExit.grid(row=0, column=5)

        # =============table================================
        # =============scroll=================================

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("nameoftablet", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "nhsnumber", "storage", "Pname", "dob", "PatientAddress"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Insert headings for columns
        self.hospital_table.heading("nameoftablet", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference NO:")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="LOT")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Expire Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("Pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("PatientAddress", text="Address")

        self.hospital_table["show"] = "headings"
        self.hospital_table.column("nameoftablet", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("Pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("PatientAddress", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)

root = Tk()
obj = HOSPITAL(root)
root.mainloop()
