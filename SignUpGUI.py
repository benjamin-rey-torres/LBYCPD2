from tkinter import *

class SignupWindow:
    def __init__(self):
        signupWindow = Tk()
        self.signupWindow = signupWindow
        # window attributes
        self.signupWindow.geometry("640x640")#change later
        self.signupWindow.title("HR Management System Sign-up")
        self.signupWindow.config(background = "white")

        #Frame 
        self.signupFrame = Frame(self.signupWindow, bg="white")
        self.signupFrame.place(relx=0.5, rely=0.5, anchor="center")

        #Text field to collect info

        #Name Label
        self.nameLabel = Label(self.signupFrame, text='Name:', bg="white")
        self.nameLabel.grid(row = 0, column = 0)
        #Name Field
        self.nameField = Entry(self.signupFrame, bg='#f8fab4')
        self.nameField.grid(row=0, column = 1)

        #Username Label
        self.usernameLabel = Label(self.signupFrame, text='Username:', bg="white")
        self.usernameLabel.grid(row = 1, column = 0)
        #Username Field
        self.usernameField = Entry(self.signupFrame, bg='#f8fab4')
        self.usernameField.grid(row=1, column = 1)

        #Password Label
        self.passwordLabel = Label(self.signupFrame, text='Password:', bg="white")
        self.passwordLabel.grid(row = 2, column = 0)
        self.passwordField = Entry(self.signupFrame, bg='#f8fab4', show="*")
        self.passwordField.grid(row=2, column = 1)


        #BUTTONS
        self.confirmButton = Button(self.signupFrame, text='confirm', command=self.confirmController)
        self.confirmButton.grid(row=3, column=0, columnspan =2)

        #Labels
        self.signupLabel = Label(self.signupWindow, text='Sign up', bg="white", font=("Consolas", 25))
        self.signupLabel.place(relx=0.5, rely=0.2, anchor="center")

    #Functions
    def confirmController(self):
        nameInput = self.nameField.get()
        usernameInput = self.usernameField.get()
        passwordInput = self.passwordField.get()
        #save the data
        print(nameInput)
        print(usernameInput)
        print(passwordInput)

        #Closes window
        self.signupWindow.destroy()
    
    def signupMainLoop(self): #Runs the sign up loop
        self.signupWindow.mainloop()
