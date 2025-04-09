from tkinter import *
from tkinter import ttk
import datetime
import dataImportAndExport
import passwordHashing
import employeeInformationMangement

class DashboardWindow:
    def __init__(self,id,usertype):
        dashboardWindow = Tk()
        self.dashboardWindow = dashboardWindow

        #Window
        self.dashboardWindow.geometry("640x640")
        self.dashboardWindow.title("HR Managment Dashboard")
        self.dashboardWindow.config(background="white")

        #Main Frame
        self.dashboardFrame = Frame(self.dashboardWindow, bg="white")
        self.dashboardFrame.place(relx=0.5, rely=0.5, anchor="center")

        #Tabs Frame
        self.tabsFrame = Frame(self.dashboardFrame, bg="#f8fab4")
        self.tabsFrame.config(width = 500, height = 300)
        self.tabsFrame.pack(side = LEFT)

        #Buttons in Tabs Frame
        self.attendanceButton = Button(self.tabsFrame, text='ATTENDANCE', command=self.showAttendanceGUI)
        self.attendanceButton.pack(side = TOP)

        self.payrollButton = Button(self.tabsFrame, text='PAYROLL', command=self.showPayrollGUI)
        self.payrollButton.pack(side = TOP)

        
        self.profileButton = Button(self.tabsFrame,text = 'PROFILE', command = self.showProfileGUI)
        self.profileButton.pack(side = TOP)


        self.employeeinfoButton = Button(self.tabsFrame, text='EMPLOYEE_INFO', command=self.showEmployeeInfo)
        self.employeeinfoButton.pack(side = TOP)

        # Employee Info Frame
        self.employeeInfoFrame = Frame(self.dashboardFrame, bg="#f8fab4")
        self.employeeInfoFrame.config(width=500, height=300)


        # Employee Info Content
        self.treeview1 = ttk.Treeview(self.employeeInfoFrame)
        self.treeview1.pack(fill="both")

        treescrolly = Scrollbar(self.employeeInfoFrame, orient="vertical", command=self.treeview1.yview) 
        treescrollx = Scrollbar(self.employeeInfoFrame, orient="horizontal", command=self.treeview1.xview) 
        self.treeview1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y") 

        self.updateDataButton = Button(self.employeeInfoFrame, text='UPDATE Data', command = self.update_treeview)
        self.updateDataButton.pack()
        
        # Attendance Frame
        self.attendanceFrame = Frame(self.dashboardFrame, bg="#f8fab4")
        self.attendanceFrame.config(width=500, height=300)
        self.attendanceFrame.pack()
        
        # Attendance Frame Content
        self.timeLabel = Label(self.attendanceFrame, text=datetime.datetime.now().strftime("%H:%M:%S"))
        self.timeLabel.pack()
        
        self.updateButton = Button(self.attendanceFrame, text='UPDATE TIME', command = self.updateTime)
        self.updateButton.pack()
        self.timeInButton = Button(self.attendanceFrame,text='Time-In', command = self.timeIn)
        self.timeInButton.pack()
        self.timeOutButton = Button(self.attendanceFrame,text='Time-Out', command = self.timeOut)
        self.timeOutButton.pack()
        
        # Payroll Frame
        self.payrollFrame = Frame(self.dashboardFrame, bg="#f8fab4")
        self.payrollFrame.config(width=500, height=300)
            #ADD Payroll widgets here

        # Profile Frame
        self.profileFrame = Frame(self.dashboardFrame, bg="#f8fab4")
        self.profileFrame.config(width=500, height=300)

        #Profile Frame Content

        # temp database frame
        tempframe = dataImportAndExport.import_csv_to_dataframe('employeedata')

        #First Name
        self.firstNameLabel = Label(self.profileFrame, text='First Name:', bg="white")
        self.firstNameLabel.grid(row = 0, column = 0)
        self.firstNameField = Entry(self.profileFrame, bg='#f8fab4')
        oldFirstName = tempframe.loc[id,'firstName']
        self.firstNameField.insert(END, oldFirstName)
        self.firstNameField.grid(row=0, column = 1)
        #Last Name
        self.lastNameLabel = Label(self.profileFrame, text='Last Name:', bg="white")
        self.lastNameLabel.grid(row = 1, column = 0)
        self.lastNameField = Entry(self.profileFrame, bg='#f8fab4')
        oldLastName = tempframe.loc[id,'lastName']
        self.lastNameField.insert(END, oldLastName)
        self.lastNameField.grid(row=1, column = 1)
        #Username
        self.usernameLabel = Label(self.profileFrame, text='Username:', bg="white")
        self.usernameLabel.grid(row = 2, column = 0)
        self.usernameField = Entry(self.profileFrame, bg='#f8fab4')
        oldUsername = tempframe.loc[id,'username']
        self.usernameField.insert(END, oldUsername)
        self.usernameField.grid(row=2, column = 1)
        #Password 
        self.passwordLabel = Label(self.profileFrame, text='Password:', bg="white")
        self.passwordLabel.grid(row = 3, column = 0)
        self.passwordField = Entry(self.profileFrame, bg='#f8fab4')
        self.passwordField.grid(row=3, column = 1)

        #BUTTONS
        self.editFirstNameButton = Button(self.profileFrame, text='edit', command=lambda:self.editFirstNameController(id))
        self.editFirstNameButton.grid(row=0, column=2)
        self.editLastNameButton = Button(self.profileFrame, text='edit', command=lambda:self.editLastNameController(id))
        self.editLastNameButton.grid(row=1, column=2)
        self.editUsernameButton = Button(self.profileFrame, text='edit', command=lambda:self.editUsernameController(id))
        self.editUsernameButton.grid(row=2, column=2)
        self.editPasswordButton = Button(self.profileFrame, text='edit', command=lambda:self.editPasswordController(id))
        self.editPasswordButton.grid(row=3, column=2)
        
    # Tab Switching Button
    def showPayroll(self):
        self.attendanceFrame.pack_forget()
        self.employeeInfoFrame.pack_forget()
        self.employeeInfoFrame.pack_forget()
        self.payrollFrame.pack(side = LEFT)
        print("show payroll")

    # Tab Switching Controllers
    def showAttendanceGUI(self):
        self.payrollFrame.pack_forget()
        self.profileFrame.pack_forget()
        self.employeeInfoFrame.pack_forget()
        self.attendanceFrame.pack(side = LEFT)
        print("Attendance GUI")
    
    def showEmployeeInfo(self):
        self.payrollFrame.pack_forget()
        self.profileFrame.pack_forget()
        self.attendanceFrame.pack_forget()
        self.employeeInfoFrame.pack(side = LEFT)
        print("Employee Info GUI")

    def showPayrollGUI(self):
        self.attendanceFrame.pack_forget()
        self.profileFrame.pack_forget()
        self.employeeInfoFrame.pack_forget()
        self.payrollFrame.pack(side = LEFT)
        print("show payroll")

    def showProfileGUI(self):
        self.attendanceFrame.pack_forget()
        self.payrollFrame.pack_forget()
        self.employeeInfoFrame.pack_forget()
        self.profileFrame.pack(side = LEFT)


    #Attendance Button Controllers
    def timeIn(self):
        timeIn = datetime.datetime.now().strftime("%H:%M:%S") #Save this
        self.updateTime()
        print('Time in:' + timeIn)

    def timeOut(self):
        timeOut = datetime.datetime.now().strftime("%H:%M:%S") #Save this
        self.updateTime()
        print('Time out: ' + timeOut)

    def updateTime(self):
        self.timeLabel.config(text = datetime.datetime.now().strftime("%H:%M:%S"))

    def update_treeview(self):
        df = dataImportAndExport.import_csv_to_dataframe("employeedata")
        self.treeview1['column'] = ["firstName","lastName","department"]
        self.treeview1['show'] = "headings"
        for column in self.treeview1['column']:
            self.treeview1.heading(column, text=column)

        self.treeview1.delete(*self.treeview1.get_children())
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            self.treeview1.insert("","end",values=row)

        
    
    #Edit Profile Controllers
    def editFirstNameController(self,id):
        newFirstName = self.firstNameField.get()
        employeeInformationMangement.add_employee_data(id,"firstName",newFirstName)
        self.firstNameField.delete(0,END)
        self.firstNameField.insert(0, newFirstName)


    def editLastNameController(self,id):
        newLastName = self.lastNameField.get()
        employeeInformationMangement.add_employee_data(id,"lastName",newLastName)
        self.lastNameField.delete(0,END)
        self.lastNameField.insert(0, newLastName)

    def editUsernameController(self,id):
        newUsername = self.usernameField.get()
        employeeInformationMangement.add_employee_data(id,"username",newUsername)
        self.usernameField.delete(0,END)
        self.usernameField.insert(0, newUsername)
      
    def editPasswordController(self,id):
        newPassword = self.passwordField.get()
        employeeInformationMangement.add_employee_data(id,"username",passwordHashing.returnHashPass(newPassword))

    #Main Loop
    def dashboardMainLoop(self):
        self.dashboardWindow.mainloop()
    
        