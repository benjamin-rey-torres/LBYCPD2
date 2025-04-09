from tkinter import *
import datetime


class DashboardWindow:
    def __init__(self):
        dashboardWindow = Tk()
        self.dashboardWindow = dashboardWindow

        #Window
        self.dashboardWindow.geometry("640x640")
        self.dashboardWindow.title("HR Managment Dashboard")
        self.dashboardWindow.config(background="white")

        #Main Frame
        self.dashboardFrame = Frame(self.dashboardWindow, bg="white")
        self.dashboardFrame.place(relx=0.5, rely=0.5, anchor="center")

        #Frames within dashboardFrame
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
        
        # Attendance Frame
        self.attendanceFrame = Frame(self.dashboardFrame, bg="#f8fab4")
        self.attendanceFrame.config(width=500, height=300)
        self.attendanceFrame.pack(side = LEFT)
        
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
        #First Name
        self.firstNameLabel = Label(self.profileFrame, text='First Name:', bg="white")
        self.firstNameLabel.grid(row = 0, column = 0)
        self.firstNameField = Entry(self.profileFrame, bg='#f8fab4')
        oldFirstName = "Old First Name"    #TODO Change this based on users old info
        self.firstNameField.insert(END, oldFirstName)
        self.firstNameField.grid(row=0, column = 1)
        #Last Name
        self.lastNameLabel = Label(self.profileFrame, text='Last Name:', bg="white")
        self.lastNameLabel.grid(row = 1, column = 0)
        self.lastNameField = Entry(self.profileFrame, bg='#f8fab4')
        oldLastName = "Old Last Name"    #TODO Change this based on users old info
        self.lastNameField.insert(END, oldLastName)
        self.lastNameField.grid(row=1, column = 1)
        #Username
        self.usernameLabel = Label(self.profileFrame, text='Username:', bg="white")
        self.usernameLabel.grid(row = 2, column = 0)
        self.usernameField = Entry(self.profileFrame, bg='#f8fab4')
        oldUsername = "Old Username"    #TODO Change this based on users old info
        self.usernameField.insert(END, oldUsername)
        self.usernameField.grid(row=2, column = 1)
        #Password 
        self.passwordLabel = Label(self.profileFrame, text='Password:', bg="white")
        self.passwordLabel.grid(row = 3, column = 0)
        self.passwordField = Entry(self.profileFrame, bg='#f8fab4')
        oldPassword = "Old Password" #TODO Change this based on users old info
        self.passwordField.insert(END, oldPassword)
        self.passwordField.grid(row=3, column = 1)

        #BUTTONS
        self.editFirstNameButton = Button(self.profileFrame, text='edit', command=self.editFirstNameController)
        self.editFirstNameButton.grid(row=0, column=2)
        self.editLastNameButton = Button(self.profileFrame, text='edit', command=self.editLastNameController)
        self.editLastNameButton.grid(row=1, column=2)
        self.editUsernameButton = Button(self.profileFrame, text='edit', command=self.editUsernameController)
        self.editUsernameButton.grid(row=2, column=2)
        self.editPasswordButton = Button(self.profileFrame, text='edit', command=self.editPasswordController)
        self.editPasswordButton.grid(row=3, column=2)

    # Tab Switching Button
    def showAttendanceGUI(self):
        self.payrollFrame.pack_forget()
        self.profileFrame.pack_forget()
        self.attendanceFrame.pack(side = LEFT)
        print("Attendance GUI")

    def showPayrollGUI(self):
        self.attendanceFrame.pack_forget()
        self.profileFrame.pack_forget()
        self.payrollFrame.pack(side = LEFT)
        print("show payroll")

    def showProfileGUI(self):
        self.attendanceFrame.pack_forget()
        self.payrollFrame.pack_forget()
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
    
    #Edit Profile Controllers
    def editFirstNameController(self):
        newFirstName = self.firstNameField.get()
        print(newFirstName)
        #TODO Save to Database

    def editLastNameController(self):
        newLastName = self.lastNameField.get()
        print(newLastName)
        #TODO Save to Database

    def editUsernameController(self):
        newUsername = self.usernameField.get()
        print(newUsername)
        #TODO Save to Database
      
    def editPasswordController(self):
        newPassword = self.passwordField.get()
        print(newPassword)
        #TODO Save to Database

    #Main Loop
    def dashboardMainLoop(self):
        self.dashboardWindow.mainloop()
    
        