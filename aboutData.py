from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class AboutData(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x500+400+100")
        self.title("About")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)


        self.topFrame = Frame(self, height=170, bg="#b3daff")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg="#b3daff")
        self.bottomFrame.pack(fill=X)

        self.aboutIcon = PhotoImage(file = "addons/Libraryicon2.png")
        aboutIconLabel = Label(self.topFrame, image = self.aboutIcon, bg="#b3daff")
        aboutIconLabel.place(x=205, y=60)
        aboutIconLabel2 = Label(self.bottomFrame, text=" Librarian's Shelf v1.0.0  ", font="Times 20 underline ", bg="#b3daff", fg="Black")
        aboutIconLabel2.place(x=123, y=0)
        aboutIconLabel3 = Label(self.bottomFrame, text=" Developer E-email : jamesirvin3321@gmail.com  ", font="Times 18 ", bg="#b3daff", fg="Black")
        aboutIconLabel3.place(x=13, y=50)
        aboutIconLabel4 = Label(self.bottomFrame, text=" Telegram : @Bytestroke  ", font="Times 18 ", bg="#b3daff", fg="Black")
        aboutIconLabel4.place(x=104, y=80)