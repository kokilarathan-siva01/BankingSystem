#imports
from tkinter import *
import os
from PIL import ImageTk, Image

# HomePage
MainPage = Tk()



Label(MainPage, text = "BankOfCeylon", font=('Modern',28)).pack()
Label(MainPage, text = "A simple banking system designed to be used by all type of audience.", font=('Modern',12)).pack()
Label(MainPage, image=LogoImage).pack()


Button(MainPage, text="Register", font=('Modern',12),width=20,command=register).pack()
Button(MainPage, text="Login", font=('Modern',12),width=20,command=login).pack()

MainPage.title('BankingSystem')
MainPage.mainloop()