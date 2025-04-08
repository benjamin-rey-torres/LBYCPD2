from tkinter import *
from SignUpGUI import SignupWindow
from DashboardGUI import DashboardWindow

class LoginWindow:
    def __init__(self, loginWindow):
        self.loginWindow = loginWindow
        self.loginWindow.geometry("640x640") #window dimensions
        self.loginWindow.title("HR Management System Login")
        self.loginWindow.config(background="white")#put hex-color or "black"
        
        ## HOW TO PUT WINDOW ICON
            #iconVariable = PhotoImage(file = 'icon.png') 
            #window.iconphoto(True, iconVariable)

        #Frame
        self.loginFrame = Frame(self.loginWindow, bg = "white")
        self.loginFrame.place(relx=0.5, rely=0.5, anchor="center")

        # Username Label
        self.usernameLabel = Label(self.loginFrame, text='Username:', bg="white")
        self.usernameLabel.grid(row=1, column = 0)
        # Username Text Field
        self.usernameField = Entry(self.loginFrame, bg='#f8fab4')
        self.usernameField.grid(row=1, column=1)

        # Password Label
        self.passwordLabel = Label(self.loginFrame, text='Password:', bg="white")
        self.passwordLabel.grid(row=2, column = 0)
        # Password Text Field
        self.passwordField = Entry(self.loginFrame, bg='#f8fab4', show ="*")
        self.passwordField.grid(row=2, column=1)

        ##HOW TO ASSIGN FUNCTION TO BUTTON:
            #Assign function to button
            #func1() {.......}
            #NOTE: for func1(), do not include ()
            #signInButton.config(command = func1)
        # BUTTONS
        self.signInButton = Button(self.loginFrame, text = 'sign-in', command = self.signInController)
        self.signInButton.grid(row=3, column=0) #"add "command = signInFunction" to Button() arguments
        self.loginButton = Button(self.loginFrame, text = 'login', command=self.loginController)
        self.loginButton.grid(row=3, column=1) #"add "command = loginFunction" to Button() arguments

        # App Label
        self.AppLabel = Label(self.loginWindow, text='HR Management System', bg="white", font=("Consolas", 25))
        self.AppLabel.place(relx=0.5, rely=0.2, anchor="center")

    # BUTTON CONTROLLER
    def loginController(self):
        usernameInput = self.usernameField.get()
        passwordInput = self.passwordField.get()
        print(usernameInput) #Remove 
        print(passwordInput) #Remove
        #if(usernameInput == "user" and passwordInput == "password"):
        dashboardWindow = DashboardWindow()
        dashboardWindow.dashboardMainLoop()

    def signInController(self):
        signupWindow = SignupWindow()
        signupWindow.signupMainLoop()
        print("sign in")


if __name__ == "__main__":
    loginWindow = Tk() #instantiate window
    LoginGUI = LoginWindow(loginWindow)
    loginWindow.mainloop()    
