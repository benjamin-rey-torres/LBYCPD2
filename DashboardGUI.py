from tkinter import *

class DashboardGUI:
    def __init__(self):
        dashboardWindow = Tk()
        self.dashboardWindow = dashboardWindow

        #Window
        self.dashboardWindow.geometry("640x640")
        self.dashboardWindow.title("HR Managment Dashboard")
        self.dashboardWindow.config(background="white")

        #Frame
        self.dashboardFrame = Frame(self.dashboardWindow, bg="white")
        self.dashboardWindow.place(relx=0.5, rely=0.5, anchor="center")

        #Buttons
        self.payrollButton = Button(self.dashboardFrame, text='PAYROLL', command=self.showPayroll)
        self.payrollButton.grid(row = 3, column =0) #CHANGE THIS
        