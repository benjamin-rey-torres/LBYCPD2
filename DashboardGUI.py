from tkinter import *
from tkinter import ttk
import datetime
import dataImportAndExport
import passwordHashing
import employeeInformationMangement
import AttendanceManagement

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

        self.profileButton = Button(self.tabsFrame,text = 'PROFILE', command = self.showProfileGUI)
        self.profileButton.pack(side = TOP)

        if usertype == "manager" or usertype == "admin":
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

            # update data button
            self.updateDataButton = Button(self.employeeInfoFrame, text='UPDATE Data', command = lambda:
                                           self.update_treeview(dataImportAndExport.import_csv_to_dataframe("employeedata"),import_data=False))
            self.updateDataButton.pack()

            # add data  button
            self.addDataButton = Button(self.employeeInfoFrame, text='ADD Data', command = lambda:self.add_data(usertype))
            self.addDataButton.pack()
            self.add_userFrame = Frame(self.employeeInfoFrame)

            # edit data button
            self.editDataButton = Button(self.employeeInfoFrame, text='EDIT Data', command = lambda:self.edit_data(usertype))
            self.editDataButton.pack()
            self.edit_userFrame = Frame(self.employeeInfoFrame)

            if usertype == "admin":
                # delete data button
                self.deleteDataButton = Button(self.employeeInfoFrame, text='DELETE Data', command = self.delete_data)
                self.deleteDataButton.pack()
                self.delete_userFrame = Frame(self.employeeInfoFrame)

            # search data button
            self.searchField = Entry(self.employeeInfoFrame)
            self.searchField.pack()
            self.searchButton = Button(self.employeeInfoFrame, text="SEARCH",
                                       command=lambda: self.update_treeview(
                                        df=employeeInformationMangement.query_data(self.searchField.get(),
                                                                                   query_columns=["firstName","lastName","department","salary","username"])))
            self.searchButton.pack()

        # Attendance Frame
        self.attendanceFrame = Frame(self.dashboardFrame, bg="#f8fab4")
        self.attendanceFrame.config(width=500, height=300)
        self.attendanceFrame.pack()
        
        # Attendance Frame Content
        self.timeLabel = Label(self.attendanceFrame, text=datetime.datetime.now().strftime("%H:%M:%S"))
        self.timeLabel.pack()
        
        self.updateButton = Button(self.attendanceFrame, text='UPDATE TIME', command = self.updateTime)
        self.updateButton.pack()
        self.timeInButton = Button(self.attendanceFrame,text='Time-In', command = lambda:self.timeIn(id))
        self.timeInButton.pack()
        self.timeOutButton = Button(self.attendanceFrame,text='Time-Out', command = lambda:self.timeOut(id))
        self.timeOutButton.pack()
        
    

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
        
    # Tab Switching Controllers
    def showAttendanceGUI(self):
        try:
            self.profileFrame.pack_forget()
            self.employeeInfoFrame.pack_forget()
        except:
            pass
        self.attendanceFrame.pack(side = LEFT)
        print("Attendance GUI")
    
    def showEmployeeInfo(self):
        try:
            self.profileFrame.pack_forget()
            self.attendanceFrame.pack_forget()
        except:
            pass
        self.employeeInfoFrame.pack(side = LEFT)
        self.update_treeview(dataImportAndExport.import_csv_to_dataframe("employeedata"),import_data=False)
        print("Employee Info GUI")

    def showProfileGUI(self):
        try:
            self.attendanceFrame.pack_forget()
            self.employeeInfoFrame.pack_forget()
        except:
            pass
        self.profileFrame.pack(side = LEFT)


    #Attendance Button Controllers
    def timeIn(self,id):
        timeIn = datetime.datetime.now()
        self.updateTime()
        AttendanceManagement.log_time(timeIn,id,"TimeIn")


    def timeOut(self,id):
        timeOut = datetime.datetime.now()
        AttendanceManagement.log_time(timeOut,id,"TimeOut")
        self.updateTime()


    def updateTime(self):
        self.timeLabel.config(text = datetime.datetime.now().strftime("%H:%M:%S"))

    def update_treeview(self,df,import_data=False):
        # get columnns for treeview
        if import_data:
            df = dataImportAndExport.import_csv_to_dataframe("employeedata")
        df = df.loc[:,["firstName","lastName","department","salary","username"]].reset_index()
        self.treeview1['column'] = ["ID","firstName","lastName","department","salary","username"]
        self.treeview1['show'] = "headings"
        for column in self.treeview1['column']:
            self.treeview1.heading(column, text=column)

        # clear treeview / table
        self.treeview1.delete(*self.treeview1.get_children())

        # insert row data
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            self.treeview1.insert("","end",values=row)

    def add_data(self,usertype):
        #show add-user frame and import data
        self.add_userFrame.pack(side="right")
        tempframe = dataImportAndExport.import_csv_to_dataframe("employeedata")

        entry_list = []

        # field to put id number
        id_number_label = Label(self.add_userFrame,text="Id Number")
        id_number_label.grid(column=0,row=0)
        id_number_field = Entry(self.add_userFrame)
        id_number_field.grid(column=1,row=0)

        entry_list.append(id_number_field)
        #loop to add other fields
        for index, column in enumerate(tempframe.columns):
            add_data_label = Label(self.add_userFrame,text=column)
            add_data_label.grid(column=0,row=index+1)
            add_data_field = Entry(self.add_userFrame)
            add_data_field.grid(column=1,row=index+1)
            entry_list.append(add_data_field)

        if usertype == 'manager':
            entry_list[-1].insert(END,"employee")
            entry_list[-1].configure(state="disabled")

        # entry list is used to keep track of fields

        def add_user():
            # go through columns and add information to database for each field with information in it
            for index, column in enumerate(tempframe.columns):
                entry_data = entry_list[index+1].get()
                id_number = id_number_field.get()
                if entry_data == "":
                    continue
                if column == "passwordHash":
                    employeeInformationMangement.add_employee_data(int(id_number),column,passwordHashing.returnHashPass(entry_data))
                else:
                    employeeInformationMangement.add_employee_data(int(id_number),column,entry_data)
            # hide add user frame after done
            self.add_userFrame.forget()
            self.update_treeview(dataImportAndExport.import_csv_to_dataframe("employeedata"))

        # button to do add user command
        add_button = Button(self.add_userFrame,text="add_user",command=add_user)
        add_button.grid(column=0,row=8)

        # button to exit add user command
        def exit():
            self.add_userFrame.forget()

        x_button2 = Button(self.add_userFrame,text="X",command=exit)
        x_button2.grid(column = 2, row = 0)

    def edit_data(self,usertype):
        #show edit-user frame and import data
        self.edit_userFrame.pack(side="right")
        tempframe = dataImportAndExport.import_csv_to_dataframe("employeedata")
        if usertype == "manager":
            tempframe = tempframe.drop('userType',axis=1)

        entry_list = []


        id_number_label = Label(self.edit_userFrame,text="Id Number")
        id_number_label.grid(column=0,row=0)
        id_number_field = Entry(self.edit_userFrame)
        id_number_field.grid(column=1,row=0)

        list_of_users = tempframe[["firstName","lastName"]].apply(lambda x: ' '.join(x), axis=1).to_list()
        index_list = tempframe.index.to_list()

        entry_list.append(id_number_field)
        for index, column in enumerate(tempframe.columns):
            edit_data_label = Label(self.edit_userFrame,text=column)
            edit_data_label.grid(column=0,row=index+1)
            edit_data_field = Entry(self.edit_userFrame)
            edit_data_field.grid(column=1,row=index+1)
            entry_list.append(edit_data_field)

        def edit_user():
            for index, column in enumerate(tempframe.columns):
                entry_data = entry_list[index+1].get()
                id_number = id_number_field.get()
                if entry_data == "":
                    continue
                if column == "passwordHash":
                    employeeInformationMangement.add_employee_data(int(id_number),column,passwordHashing.returnHashPass(entry_data))
                else:
                    employeeInformationMangement.add_employee_data(int(id_number),column,entry_data)
            self.edit_userFrame.forget()
            self.update_treeview(dataImportAndExport.import_csv_to_dataframe("employeedata"))

        edit_button = Button(self.edit_userFrame,text="add_user",command=edit_user)
        edit_button.grid(column=0,row=8)

        def exit():
            self.edit_userFrame.forget()

        x_button = Button(self.edit_userFrame,text="X",command=exit)
        x_button.grid(column = 2, row = 0)

        def add_details(input_name):
             tempframe2 = dataImportAndExport.import_csv_to_dataframe("employeedata")
             id = index_list[list_of_users.index(input_name)]
             id_number_field.delete(0,END)
             id_number_field.insert(0,id)
             for index, column in enumerate(tempframe.columns):
                if column == "passwordHash":
                    continue
                else:
                    entry_list[index+1].delete(0,END)
                    entry_list[index+1].insert(0,tempframe2.loc[id,column])

        variable = StringVar(self.edit_userFrame)
        drop_down = OptionMenu(self.edit_userFrame,variable,*list_of_users, command=add_details)
        drop_down.grid(row = 0, column = 9)

    def delete_data(self):
        #show delete-user frame and import data
        self.delete_userFrame.pack(side="right")
        tempframe = dataImportAndExport.import_csv_to_dataframe("employeedata")

        entry_list = []


        id_number_label = Label(self.delete_userFrame,text="Id Number")
        id_number_label.grid(column=0,row=0)
        id_number_field = Entry(self.delete_userFrame,state="disabled")
        id_number_field.grid(column=1,row=0)

        list_of_users = tempframe[["firstName","lastName"]].apply(lambda x: ' '.join(x), axis=1).to_list()
        index_list = tempframe.index.to_list()

        entry_list.append(id_number_field)
        for index, column in enumerate(tempframe.columns):
            delete_data_label = Label(self.delete_userFrame,text=column)
            delete_data_label.grid(column=0,row=index+1)
            delete_data_field = Entry(self.delete_userFrame,state="disabled")
            delete_data_field.grid(column=1,row=index+1)
            entry_list.append(delete_data_field)
        def delete_user():
            id = entry_list[0].get()
            employeeInformationMangement.remove_user(int(id))
            self.delete_userFrame.forget()
            self.update_treeview(dataImportAndExport.import_csv_to_dataframe("employeedata"))

        delete_button = Button(self.delete_userFrame,text="delete,_user",command=delete_user)
        delete_button.grid(column=0,row=8)

        def exit():
            self.delete_userFrame.forget()

        x_button = Button(self.delete_userFrame,text="X",command=exit)
        x_button.grid(column = 2, row = 0)

        def add_details(input_name):
             tempframe2 = dataImportAndExport.import_csv_to_dataframe("employeedata")
             id = index_list[list_of_users.index(input_name)]
             id_number_field.configure(state="normal")
             id_number_field.delete(0,END)
             id_number_field.insert(0,id)
             id_number_field.configure(state="disabled")
             for index, column in enumerate(tempframe.columns):
                if column == "passwordHash":
                    continue
                else:
                    entry_list[index+1].configure(state="normal")
                    entry_list[index+1].delete(0,END)
                    entry_list[index+1].insert(0,tempframe2.loc[id,column])
                    entry_list[index+1].configure(state="disabled")

        variable = StringVar(self.delete_userFrame)
        drop_down = OptionMenu(self.delete_userFrame,variable,*list_of_users, command=add_details)
        drop_down.grid(row = 0, column = 9)

        

        
    
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
    
        