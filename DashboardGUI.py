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
        self.attendanceButton = Button(self.tabsFrame, text='Attendance', command=self.showAttendanceGUI)
        self.attendanceButton.pack(side = TOP)

        self.payrollButton = Button(self.tabsFrame, text='PAYROLL', command=self.showPayroll)
        self.payrollButton.pack(side = TOP)

        
        # Attendance Frame
        self.attendanceFrame = Frame(self.dashboardFrame, bg="#f8fab4")
        self.attendanceFrame.config(width=500, height=300)
        self.attendanceFrame.pack(side = LEFT)
        
        # Attendance Frame Content
        #TODO maybe add clock above th buttons
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
        


    def showPayroll(self):
        self.attendanceFrame.Place_forget()
        self.payrollFrame.pack(side = LEFT)
        
        print("show payroll")

    def showAttendanceGUI(self):
        self.payrollFrame.Place_forget()
        self.attendanceFrame.pack(side = LEFT)
        print("Attendance GUI")

    def timeIn(self):
        timeIn = datetime.datetime.now()

    def timeOut(self):
        timeOut = datetime.datetime.now()

    def updateTime(self):
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_var.set('Current Time: ' + currentTime)
    

    def dashboardMainLoop(self):
        self.dashboardWindow.mainloop()
    
        