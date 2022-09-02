from tkinter import *
import editbookinfo, editmemberinfo
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class EditInformation(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x300+400+100")
        self.title("Edit Information")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)


        self.topFrame = Frame(self, height=150, bg="#b3daff")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg="#b3daff")
        self.bottomFrame.pack(fill=X)
        self.topImg = PhotoImage(file="addons/editicon2.png")
        self.topImgLabel = Label(self.topFrame, image=self.topImg, bg="#b3daff")
        self.topImgLabel.place(x=30, y=40)
        imgHeading = Label(self.topFrame, text="  Edit Information  ", font="Times 30 bold underline", bg="#b3daff", fg="#0059b3")
        imgHeading.place(x=145, y=70)


        self.editInfoBtn = Button(self.bottomFrame, text= "Edit Book Information", bg="#b3daff", fg="#0059b3", font="Times 16 bold", command = self.bookInfoEdit)
        self.editInfoBtn.place(x=150, y=30)
        self.editInfoBtn2 = Button(self.bottomFrame, text= "Edit Member Information", bg="#b3daff", fg="#0059b3", font="Times 16 bold", command = self.memberInfoEdit)
        self.editInfoBtn2.place(x=136, y=90)

    def bookInfoEdit(self):
        bookIE = editbookinfo.EditBookInfo()

    def memberInfoEdit(self):
        memberIE = editmemberinfo.EditMemberInfo()