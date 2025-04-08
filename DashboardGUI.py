from tkinter import *

class DashboardWindow:
    def __init__(self):
        dashboardWindow = Tk()
        self.dashboardWindow = dashboardWindow

        #Window
        self.dashboardWindow.geometry("640x640")
        self.dashboardWindow.title("HR Managment Dashboard")
        self.dashboardWindow.config(background="white")

        #Frame
        self.dashboardFrame = Frame(self.dashboardWindow, bg="white")
        self.dashboardFrame.place(relx=0.5, rely=0.5, anchor="center")

        #Buttons
        self.payrollButton = Button(self.dashboardFrame, text='PAYROLL', command=self.showPayroll)
        self.payrollButton.grid(row = 3, column =0) #CHANGE THIS

        self.attendanceButton = Button(self.dashboardFrame, text='Attendance', command=self.showAttendanceGUI)
        self.attendanceButton.grid(row = 3, column =1) #CHANGE THIS

        #Frames within dashboardFrame
        # Attendance Frame
        self.attendanceFrame = Frame(self.dashboardFrame, bg="#f8fab4")
        self.attendanceFrame.grid(row = 0, column = 1, rowspan=2)

        # Payroll Frame
        self.payrollFrame = Frame(self.dashboardFrame, bg="#f8fab4")
        

    def showPayroll(self):
        self.payrollFrame.place(relx = 1, rely = 0,anchor = NE)
        print("show payroll")

    def showAttendanceGUI(self):
        self.attendanceFrame.place(relx = 1, rely = 0,anchor = NE)
        print("Attendance GUI")

    def dashboardMainLoop(self):
        self.dashboardWindow.mainloop()
    
        