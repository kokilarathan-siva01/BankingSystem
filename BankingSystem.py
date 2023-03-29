#imports
from tkinter import *
import os
from PIL import ImageTk, Image

# HomePage
MainPage = Tk()

# Images used for visual purposes
LogoImage = Image.open('Bank_of_Ceylon.svg.png')
LogoImage = LogoImage.resize((185,185))
LogoImage = ImageTk.PhotoImage(LogoImage)


Label(MainPage, text = "BankOfCeylon", font=('Modern',28)).grid(row=0,sticky=N,pady=10)
Label(MainPage, text = "A simple banking system designed to be used by all type of audience.", font=('Modern',12)).grid(row=1,sticky=N)
Label(MainPage, image=LogoImage).grid(row=2,sticky=N,pady=15)


Button(MainPage, text="Register", font=('Modern',12),width=20,command=register).grid(row=3,sticky=N)
Button(MainPage, text="Login", font=('Modern',12),width=20,command=login).grid(row=4,sticky=N,pady=10)


MainPage.title('BankingSystem')
MainPage.mainloop()