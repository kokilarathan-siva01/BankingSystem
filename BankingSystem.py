#imports
from tkinter import *
import os
from PIL import ImageTk, Image

# HomePage
MainPage = Tk()
def login():

    global loginNameCheck_
    global loginPassCheck_
    global loginButtonT
    global loginPage
    loginNameCheck_ = StringVar()
    loginPassCheck_ = StringVar()
    loginPage = Toplevel(MainPage)
    loginPage.title('Login')
    Label(loginPage, text="Login to your account", font=('Modern',12)).pack()
    Label(loginPage, text="Username", font=('Modern',12)).pack()
    Label(loginPage, text="Password", font=('Modern',12)).pack()
    loginButtonT = Label(loginPage, font=('Modern',12))
    loginButtonT.pack()

    Entry(loginPage, textvariable=loginNameCheck_).pack()
    Entry(loginPage, textvariable=loginPassCheck_,show="*").pack()
    Button(loginPage, text="Login", command=loginButton, width=15,font=('Modern',12)).pack()


def loginButton():
    global nameCheckLogin
    allCustomerInformation = os.listdir()
    nameCheckLogin = loginNameCheck_.get()
    passLoginCheck = loginPassCheck_.get()

    for name in allCustomerInformation:
        if name == nameCheckLogin:
            customerInfo = open(name,"r")
            customerInfoDist = customerInfo.read()
            customerInfoDist = customerInfoDist.split('\n')
            password  = customerInfoDist[1]

            #Customer Account Details
            if passLoginCheck == password:
                loginPage.destroy()
                coustomerAccountDetails = Toplevel(MainPage)
                coustomerAccountDetails.title('Details')

                Label(coustomerAccountDetails, text="Customer Account Details", font=('Modern',12)).pack()
                Label(coustomerAccountDetails, text="Hello "+ name, font=('Modern',12)).pack()
                
                Button(coustomerAccountDetails, text="Customer's Personal Details",font=('Modern',12),width=30,command=customerPersonalDetail).pack()
                Button(coustomerAccountDetails, text="Deposit",font=('Modern',12),width=30,command=deposit).pack()
                Button(coustomerAccountDetails, text="Withdraw",font=('Modern',12),width=30,command=withdraw).pack()
                Label(coustomerAccountDetails).grid(row=5,sticky=N,pady=10)
                return
            else:
                loginButtonT.config(fg="red", text="ERROR!!! Password incorrect!!")
                return
    loginButtonT.config(fg="red", text=" account invalid. ")

def register():
    
    global cusotmerName
    global customerAge
    global cusotmerGender
    global customerPass

    cusotmerName = StringVar()
    customerAge = StringVar()
    cusotmerGender = StringVar()
    customerPass = StringVar()
    
    
    
    #Register Page
    registerPage = Toplevel(MainPage)
    registerPage.title('Register')
    global button_1

    Label(registerPage, text="Input credientails to open an bank account.", font=('Modern',12)).pack()
    Label(registerPage, text="Name", font=('Modern',12)).pack()
    Label(registerPage, text="Age", font=('Modern',12)).pack()
    Label(registerPage, text="Gender", font=('Modern',12)).pack()
    Label(registerPage, text="Password", font=('Modern',12)).pack()
    button_1 = Label(registerPage, font=('Modern',12))
    button_1.pack()

    Entry(registerPage,textvariable=cusotmerName).pack()
    Entry(registerPage,textvariable=customerAge).pack()
    Entry(registerPage,textvariable=cusotmerGender).pack()
    Entry(registerPage,textvariable=customerPass,show="*").pack()


    Button(registerPage, text="Register", command = registerButton, font=('Modern',12)).pack()


def registerButton():
    name = cusotmerName.get()
    age = customerAge.get()
    gender = cusotmerGender.get()
    password = customerPass.get()
    allCustomerInformation = os.listdir()


    if name == "" or age == "" or gender == "" or password == "":
        button_1.config(fg="red",text="All fields requried * ")
        return

    for name_check in allCustomerInformation:
        if name == name_check:
            button_1.config(fg="red",text="Please re-try, Account already exists")
            return
        else:
            new_customerInfo = open(name,"w")
            new_customerInfo.write(name + '\n')   
            new_customerInfo.write(password + '\n')
            new_customerInfo.write(age + '\n')
            new_customerInfo.write(gender +'\n')
            new_customerInfo.write('0')
            new_customerInfo.close()
            button_1.config(fg="green", text="Account has been created")



# Images used for visual purposes
LogoImage = Image.open('Bank_of_Ceylon.svg.png')
LogoImage = LogoImage.resize((185,185))
LogoImage = ImageTk.PhotoImage(LogoImage)


Label(MainPage, text = "BankOfCeylon", font=('Modern',28)).pack()
Label(MainPage, text = "A simple banking system designed to be used by all type of audience.", font=('Modern',12)).pack()
Label(MainPage, image=LogoImage).pack()


Button(MainPage, text="Register", font=('Modern',12),width=20,command=register).pack()
Button(MainPage, text="Login", font=('Modern',12),width=20,command=login).pack()

MainPage.title('BankingSystem')
MainPage.mainloop()