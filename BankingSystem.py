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

def deposit():

global amount
global buttonDeposit
global avaliableBalanceDisplay
amount = StringVar()
customerInfo = open(nameCheckLogin, "r")
customerInfoDist = customerInfo.read()
customerInfoAll = customerInfoDist.split('\n')
customerBalanceAll = customerInfoAll[4]
#Deposit Screen
depositPage = Toplevel(MainPage)
depositPage.title('Deposit')

Label(depositPage, text="Deposit", font=('Modern',12)).pack()
avaliableBalanceDisplay = Label(depositPage, text="Current Balance : £"+customerBalanceAll, font=('Modern',12))
avaliableBalanceDisplay.pack()
Label(depositPage, text="Amount : ", font=('Modern',12)).pack()
buttonDeposit = Label(depositPage,font=('Modern',12))
buttonDeposit.pack()

Entry(depositPage, textvariable=amount).grid(row=2,column=1)
Button(depositPage,text="Finish",font=('Modern',12),command=completeDeposit).pack()

def completeDeposit():
if amount.get() == "":
buttonDeposit.config(text='Valid amount is needed!',fg="red")
return
if float(amount.get()) <=0:
buttonDeposit.config(text='The entered value is invalid!', fg='red')
return

customerInfo = open(nameCheckLogin, 'r+')
customerInfoDist = customerInfo.read()
details = customerInfoDist.split('\n')
balanceAvaliable = details[4]
balanceNew = balanceAvaliable
balanceNew = float(balanceNew) + float(amount.get())
customerInfoDist = customerInfoDist.replace(balanceAvaliable, str(balanceNew))
customerInfo.seek(0)
customerInfo.truncate(0)
customerInfo.write(customerInfoDist)
customerInfo.close()

avaliableBalanceDisplay.config(text="Current Balance : £"+str(balanceNew),fg="green")
buttonDeposit.config(text='Balance Updated', fg='green')


def withdraw():

global withdrawNeededAmount
global buttonWithdraw_1
global avaliableBalanceDisplay
withdrawNeededAmount = StringVar()
customerInfo = open(nameCheckLogin, "r")
customerInfoDist = customerInfo.read()
customerInfoAll = customerInfoDist.split('\n')
customerBalanceAll = customerInfoAll[4]
#Withdraw Page
withdrawPage = Toplevel(MainPage)
withdrawPage.title('Withdraw')

Label(withdrawPage, text="Deposit", font=('Modern',12)).pack()
avaliableBalanceDisplay = Label(withdrawPage, text="Current Balance : £"+customerBalanceAll, font=('Modern',12))
avaliableBalanceDisplay.pack()
Label(withdrawPage, text="Amount : ", font=('Modern',12)).pack()
buttonWithdraw_1 = Label(withdrawPage,font=('Modern',12))
buttonWithdraw_1.pack()

Entry(withdrawPage, textvariable=withdrawNeededAmount).pack()

Button(withdrawPage,text="Finish",font=('Modern',12),command=completeWithdraw).pack()

def completeWithdraw():
if withdrawNeededAmount.get() == "":
buttonWithdraw_1.config(text='Amount is required!',fg="red")
return
if float(withdrawNeededAmount.get()) <=0:
buttonWithdraw_1.config(text='PLease do not exceed the avaliable balance.', fg='red')
return

customerInfo = open(nameCheckLogin, 'r+')
customerInfoDist = customerInfo.read()
details = customerInfoDist.split('\n')
balanceAvaliable = details[4]

if float(withdrawNeededAmount.get()) >float(balanceAvaliable):
buttonWithdraw_1.config(text='Insufficient Funds!', fg='red')
return

balanceNew = balanceAvaliable
balanceNew = float(balanceNew) - float(withdrawNeededAmount.get())
customerInfoDist = customerInfoDist.replace(balanceAvaliable, str(balanceNew))
customerInfo.seek(0)
customerInfo.truncate(0)
customerInfo.write(customerInfoDist)
customerInfo.close()

avaliableBalanceDisplay.config(text="Current Balance : £"+str(balanceNew),fg="green")
buttonWithdraw_1.config(text='Balance has been Updated.', fg='green')

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