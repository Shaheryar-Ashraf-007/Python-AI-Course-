import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class HOSPITAL():
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management system")
        self.root.geometry("1540x800+0+0")
        
        #"nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "nhsnumber", "storage", "pname", "dob", "address"
        self.NameofTablet = StringVar()
        self.Reference_NO = StringVar()
        self.Dose = StringVar()
        self.NoofTablets = StringVar()
        self.LOT = StringVar()
        self.IssueDate = StringVar()
        self.ExpireDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FutureInfo = StringVar()
        self.BloodPressure = StringVar()
        self.Meddicine= StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowtoUseMedication = StringVar()
        self.PatientId= StringVar()
        self.NHSNumber = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.Address = StringVar()
        self.Storage = StringVar()
        
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
        comNametable = ttk.Combobox(dataframeLeft, state="readonly", textvariable=self.NameofTablet, font=("arial", 12, "bold"), width=33)
        comNametable["values"] = ("Nice", "Corona vaccine", "maleria vaccine", "polio vaccine", "medicines", "ASOZEN FORTE", " Aceclofenac ", " paracetamol", "  Chlorzoxazone", "Amoxible", " Amoxycillin", "MEF Plus", "Mefenamic Acid", " Paracetamol", "NIMSE", " Nimesulid", "Parazex", "Paracetamol")
        comNametable.grid(row=0, column=1)
        
        lblNameref = Label(dataframeLeft, text="Reference NO", font=("arial", 12, "bold"), padx=2)
        lblNameref.grid(row=1, column=0, sticky=W)
        txtref = Entry(dataframeLeft, textvariable=self.Reference_NO, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1)
        
        lblDose = Label(dataframeLeft, text="Dose:", font=("arial", 12, "bold"), padx=6, pady=4)
        lblDose.grid(row=2, column=0)
        txtDose = Entry(dataframeLeft, textvariable=self.Dose, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)
        
        lblNoofTablets = Label(dataframeLeft, text="No of Tablets:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoofTablets.grid(row=3, column=0)
        txtnoofTablets = Entry(dataframeLeft, textvariable=self.NoofTablets , font=("arial", 13, "bold"), width=35)
        txtnoofTablets.grid(row=3, column=1)
        
        lblLot = Label(dataframeLeft, text="LOT:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLot.grid(row=4, column=0)
        txtLot = Entry(dataframeLeft, textvariable=self.LOT, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4, column=1)
        
        lblissueDate = Label(dataframeLeft, text="Issue Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblissueDate.grid(row=5, column=0)
        txtissueDate = Entry(dataframeLeft, textvariable=self.IssueDate, font=("arial", 13, "bold"), width=35)
        txtissueDate.grid(row=5, column=1)
        
        lblExpDate = Label(dataframeLeft, text="Expire Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0)
        txtExpDate = Entry(dataframeLeft, textvariable=self.ExpireDate, font=("arial", 13, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)
        
        lblDailyDose = Label(dataframeLeft, text="Daily Dose:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0)
        txtDailyDose = Entry(dataframeLeft, textvariable=self.DailyDose, font=("arial", 13, "bold"), width=35)
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
        
        lblMeddicine = Label(dataframeLeft, text="Storage:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeddicine.grid(row=2, column=2)
        txtMedicine = Entry(dataframeLeft, textvariable=self.Meddicine, font=("arial", 13, "bold"), width=35)
        txtMedicine.grid(row=2, column=3)
        
        lblPateintId = Label(dataframeLeft, text="Patient Id:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPateintId.grid(row=3, column=2)
        txtpatientId = Entry(dataframeLeft, textvariable=self.PatientId, font=("arial", 13, "bold"), width=35)
        txtpatientId.grid(row=3, column=3)
        
        lblNhsNumber = Label(dataframeLeft, text="NHS Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNhsNumber.grid(row=4, column=2)
        txtNhsNumber = Entry(dataframeLeft, textvariable=self.NHSNumber, font=("arial", 13, "bold"), width=35)
        txtNhsNumber.grid(row=4, column=3)
        
        lblPateintName = Label(dataframeLeft, text="Patient Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPateintName.grid(row=5, column=2)
        txtpatientName = Entry(dataframeLeft, textvariable=self.PatientName, font=("arial", 13, "bold"), width=35)
        txtpatientName.grid(row=5, column=3)
        
        lblDateofBirth = Label(dataframeLeft, text="Date of Birth:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDateofBirth.grid(row=6, column=2)
        txtDateofBirth = Entry(dataframeLeft, textvariable=self.DateofBirth, font=("arial", 13, "bold"), width=35)
        txtDateofBirth.grid(row=6, column=3)
        
        lblPateintAddress = Label(dataframeLeft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPateintAddress.grid(row=7, column=2)
        txtpatientAddress = Entry(dataframeLeft, textvariable=self.Address, font=("arial", 13, "bold"), width=35)
        txtpatientAddress.grid(row=7, column=3)
        
        #==============datafrmeright===========================================
        self.txtPrescription = Text(dataframeRight, font=("arial", 12, "bold"), width=35, height=16, padx=0, pady=6)
        self.txtPrescription.grid(row=0, column=0)
        
        #=================================buttons===============================
        btnPrescription = Button(Buttonframe,command=self.Prescription, text="Prescription", font=("arial", 12, "bold"), bg="green", fg="white", width=21, height=2,)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe,command=self.PrescriptionData, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=21, height=2)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe,command=self.update, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=21, height=2)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe,command=self.idelete, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=21, height=2)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe,command= self.clear, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=21, height=2)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, command=self.iExit, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=21, height=2)
        btnExit.grid(row=0, column=5)

        # =============table================================
        # =============scroll=================================

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("NameofTablet", "Reference_NO", "Dose", "NoofTablets ", "LOT", "IssueDate", "ExpireDate", "DailyDose", "NHSNumber", "Storage", "PatientName", "DateofBirth", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Insert headings for columns
        self.hospital_table.heading("NameofTablet", text="Name of Tablets")
        
        self.hospital_table.heading("Reference_NO", text="Reference NO:")
        
        self.hospital_table.heading("Dose", text="Dose")
        
        self.hospital_table.heading("NoofTablets ", text="No of Tablets")
        
        self.hospital_table.heading("LOT", text="LOT")
        
        self.hospital_table.heading("IssueDate", text="Issue Date")
        
        self.hospital_table.heading("ExpireDate", text="Expire Date")
        
        self.hospital_table.heading("DailyDose", text="Daily Dose")
        
        self.hospital_table.heading("Storage", text="Storage")
        
        self.hospital_table.heading("NHSNumber", text="NHS Number")
        
        self.hospital_table.heading("PatientName", text="Patient Name")
        
        self.hospital_table.heading("DateofBirth", text="Date of Birth")
        
        self.hospital_table.heading("Address", text="Address")

        self.hospital_table["show"] = "headings"
        
        self.hospital_table.column("NameofTablet", width=100)
        
        self.hospital_table.column("Reference_NO", width=100)
        
        self.hospital_table.column("Dose", width=100)
        
        self.hospital_table.column("NoofTablets ", width=100)
        
        self.hospital_table.column("LOT", width=100)
        
        self.hospital_table.column("IssueDate", width=100)
        
        self.hospital_table.column("ExpireDate", width=100)
        
        self.hospital_table.column("DailyDose", width=100)
        
        self.hospital_table.column("Storage", width=100)
    
        self.hospital_table.column("NHSNumber", width=100)
        
        self.hospital_table.column("PatientName", width=100)
        
        self.hospital_table.column("DateofBirth", width=100)
        
        self.hospital_table.column("Address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        self.fatch_data()
        
    def PrescriptionData(self):
        if self.NameofTablet.get() == "" or self.Reference_NO.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn= mysql.connector.connect(host = "localhost", user = "root", password = "test@123", db ="mydata2")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO hospital2(NameofTablet, Reference_NO, Dose, NoofTablets, LOT, IssueDate, ExpireDate, DailyDose, Storage, NHSNumber, PatientName, DateofBirth, Address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.NameofTablet.get(),
                    
                    self.Reference_NO.get(),
                    
                    self.Dose.get(),
                    
                    self.NoofTablets.get(),
                    
                    self.LOT.get(),
                    
                    self.IssueDate.get(),
                    
                    self.ExpireDate.get(),
                    
                    self.DailyDose.get(),
                    
                    self.Storage.get(),
                    
                    self.NHSNumber.get(),
                    
                    self.PatientName.get(),
                    
                    self.DateofBirth.get(),
                    
                    self.Address.get(),        
                ))
                
                conn.commit()
                
                self.fatch_data()
                
                conn.close()
                
                messagebox.showinfo("Success", "Prescription data saved successfully")
                
            except mysql.connector.Error as error:
                
                messagebox.showerror("Error", f"Failed to insert data into MySQL table: {error}")
                
                
    def update(self):
        try:
            conn= mysql.connector.connect(host = "localhost", user = "root", password = "test@123", db ="mydata2")
            
            my_cursor = conn.cursor()
            
            my_cursor.execute =("UPDATE hospital2 SET Nameoftablet = %s,Reference_NO = %s Dose = %s NoofTablets = %s LOT= %s IssueDate = %s ExpireDate = %s Storage = %s NHSNumber = %s PatientName = %s DateofBirth = %s Address = %s",(
                
                self.NameofTablet.get(),
                
                self.Reference_NO.get(),
                
                self.Dose.get(),
                
                self.NoofTablets.get(),
                
                self.LOT.get(),
                
                self.IssueDate.get(),
                
                self.ExpireDate.get(),
                
                self.DailyDose.get(),
                
                self.Storage.get(),
                
                self.NHSNumber.get(),
                
                self.PatientName.get(),
                
                self.DateofBirth.get(),
                
                self.Address.get(),      
                
            ))
            
            conn.commit()
            
            self.fatch_data()
            
            conn.close()
            
            messagebox.showinfo("Success", "Data updated successfully")
            
        except mysql.connector.Error as error:
            
            messagebox.showerror("Error", f"Failed to update data: {error}")

        
        
    def fatch_data(self):
    
        conn= mysql.connector.connect(host = "localhost", user = "root", password = "test@123", db ="mydata2")
        
        my_cursor = conn.cursor()
        
        my_cursor.execute("select * from hospital2")
        
        rows= my_cursor.fetchall()
        
        if len(rows)!=0:
            
            self.hospital_table.delete(*self.hospital_table.get_children())
            
            for i in rows:
                
                self.hospital_table.insert("",END,values=i)
                
            conn.commit()
            
            conn.close()
            
    def get_cursor(self, event = ""):
        
        cursor_row = self.hospital_table.focus()
        
        content = self.hospital_table.item(cursor_row)
        
        row = content["values"]
        
        self.NameofTablet.set(row[0])
        
        self.Reference_NO.set(row[1])
        
        self.Dose.set(row[2])
        
        self.NoofTablets.set(row[3])
        
        self.LOT.set(row[4])
        
        self.IssueDate.set(row[5])
        
        self.ExpireDate.set(row[6])
        
        self.DailyDose.set(row[7])
        
        self.Storage.set(row[8])
        
        self.NHSNumber.set(row[9])
        
        self.PatientName.set(row[10])
        
        self.DateofBirth.set(row[11])
        
        self.Address.set(row[12])
        
    def Prescription(self):
        self.txtPrescription.insert(END,"Name of tablet:\t\t\t"+self.NameofTablet.get()+"\n")
        
        self.txtPrescription.insert(END,"Reference NO:\t\t\t"+self.Reference_NO.get()+"\n")
        
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        
        self.txtPrescription.insert(END,"No of Tablets:\t\t\t"+self.NoofTablets.get()+"\n")
        
        self.txtPrescription.insert(END,"LOT:\t\t\t"+self.LOT.get()+"\n")
        
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.IssueDate.get()+"\n")
        
        self.txtPrescription.insert(END,"Expire Date:\t\t\t"+self.ExpireDate.get()+"\n")
        
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        
        self.txtPrescription.insert(END,"Storage:\t\t\t"+self.Storage.get()+"\n")
        
        self.txtPrescription.insert(END,"NHS Number:\t\t\t"+self.NHSNumber.get()+"\n")
        
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        
        self.txtPrescription.insert(END,"Date of Birth:\t\t\t"+self.DateofBirth.get()+"\n")
        
        self.txtPrescription.insert(END,"Address:\t\t\t"+self.Address.get()+"\n")
        
    def idelete(self):
        conn= mysql.connector.connect(host = "localhost", user = "root", password = "test@123", db ="mydata2")
        
        my_cursor = conn.cursor()
        
        query = "delete from hospital2 where Reference_NO = %s"
        
        value = (self.Reference_NO.get(),)
        
        my_cursor.execute(query,value)
        
        conn.commit()
        
        conn.close()
        
        self.fatch_data()
        
        messagebox.showinfo("Delete","Patient has been deleted successfully")
    
    
    def clear(self):
        
        self.NameofTablet.set("")
        
        self.Reference_NO.set("")
        
        self.Dose.set("")
        
        self.NoofTablets.set("")
        
        self.LOT.set("")
        
        self.IssueDate.set("")
        
        self.ExpireDate.set("")
        
        self.DailyDose.set("")
        
        self.SideEffect.set("")
        
        self.FutureInfo.set("")
        
        self.Storage.set("")
        
        self.DrivingUsingMachine.set("")
        
        self.HowtoUseMedication.set("")
        
        self.PatientId.set("")
        
        self.NHSNumber.set("")
        
        self.DateofBirth.set("")
        
        self.Address.set("")
        
        self.txtPrescription.delete("1.0",END)
        
        self.NameofTablet.set("")
        
    def iExit(self):
        iExit = messagebox.askyesno(("Hospital Management System", "confirm you want to exit"))
        if iExit>0:
            root.destroy()
            return
        

root = Tk()
obj = HOSPITAL(root)
root.mainloop()
