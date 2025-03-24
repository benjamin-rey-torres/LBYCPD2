from tkinter import *

loginWindow = Tk() #instantiate window

#window attributes
loginWindow.geometry("640x640") #window dimensions
loginWindow.title("HR Management System") 
loginWindow.config(background="white") #put hex-color or "black"

## HOW TO PUT WINDOW ICON
    #iconVariable = PhotoImage(file = 'icon.png') 
    #window.iconphoto(True, iconVariable)

#Frame
signInFrame = Frame(loginWindow, bg = "white")
signInFrame.place(relx=0.5, rely=0.5, anchor="center")

# Username Label
usernameLabel = Label(signInFrame, text='Username:')
usernameLabel.grid(row=1, column = 0)
# Username Text Field
usernameField = Entry(signInFrame, bg='#f8fab4')
usernameField.grid(row=1, column=1)

# Password Label
passwordLabel = Label(signInFrame, text='Password:')
passwordLabel.grid(row=2, column = 0)
# Password Text Field
passwordField = Entry(signInFrame, bg='#f8fab4', show ="*")
passwordField.grid(row=2, column=1)

##HOW TO ASSIGN FUNCTION TO BUTTON:
    #Assign function to button
    #func1() {.......}
    #NOTE: for func1(), do not include ()
    #signInButton.config(command = func1)

# BUTTON CONTROLLER
def loginController():
    usernameInput = usernameField.get()
    passwordInput = passwordField.get()
    print(usernameInput) #Remove 
    print(passwordInput) #Remove

def signInController():
    #bring to sign in window
    print("sign in")

# BUTTONS
signInButton = Button(signInFrame, text = 'sign-in', command = signInController).grid(row=3, column=0) #"add "command = signInFunction" to Button() arguments
loginButton = Button(signInFrame, text = 'login', command=loginController).grid(row=3, column=1) #"add "command = loginFunction" to Button() arguments

# App Label
AppLabel = Label(loginWindow, text='HR Management System', font=("Consolas", 25))
AppLabel.place(relx=0.5, rely=0.2, anchor="center")

loginWindow.mainloop()
