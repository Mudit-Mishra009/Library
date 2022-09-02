from tkinter import *
import editinfo, deletebooks, availablility, memrequests, fulfilled, cleardata, aboutData
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class MoreInformation(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("550x500+400+80")
        self.title("More")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)


        self.topFrame = Frame(self, height=150, bg="#b3daff")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg="#b3daff")
        self.bottomFrame.pack(fill=X)
        imgHeading = Label(self.topFrame, text="  Additional Options  ", font="Times 30 bold underline", bg="#b3daff", fg="#0059b3")
        imgHeading.place(x=100, y=20)

        self.editInfoBtnn = Button(self.bottomFrame, text= "3. Edit Information", bg="#b3daff", fg="#0059b3", font="Times 18 bold", command = self.InfoEdit)
        self.editInfoBtnn.place(x=170, y=62)
        self.delBookBtn = Button(self.bottomFrame, text="2. Delete Books", bg="#b3daff", fg="#0059b3", font="Times 18 bold", command = self.DelBooks)
        self.delBookBtn.place(x=190, y=2)
        self.chngAvailBtn = Button(self.bottomFrame, text="5. Change Availability", bg="#b3daff", fg="#0059b3", font="Times 18 bold", command = self.chngAvailablity)
        self.chngAvailBtn.place(x=155, y=182)
        self.memberReqBtn = Button(self.bottomFrame, text="4. Member Requests", bg="#b3daff", fg="#0059b3", font="Times 18 bold", command = self.memberReqs)
        self.memberReqBtn.place(x=164, y=122)
        self.memberReqDelBtn = Button(self.bottomFrame, text="6. Delete Fulfilled Requests", bg="#b3daff", fg="#0059b3", font="Times 18 bold", command=self.Fulfillment)
        self.memberReqDelBtn.place(x=130, y=242)
        self.clearDataBtn = Button(self.topFrame, text="1. Clear Data", bg="#b3daff", fg="#0059b3", font="Times 18 bold", command = self.dataReset)
        self.clearDataBtn.place(x=198, y=92)
        self.aboutMeBtn = Button(self.bottomFrame, text=" About ", bg="#b3daff", fg="#0059b3", font="Times 12 bold", command=self.abtData)
        self.aboutMeBtn.place(x=480, y=310)


    def InfoEdit(self):
        bookIE = editinfo.EditInformation()

    def DelBooks(self):
        bookDel = deletebooks.DeleteBooks()

    def chngAvailablity(self):
        chAvlbl = availablility.ChangeAvailability()

    def memberReqs(self):
        memReq = memrequests.MemberRequests()

    def Fulfillment(self):
        fulReq = fulfilled.FulfilledRequests()

    def dataReset(self):
        dataRes = cleardata.ClearData()

    def abtData(self):
        dataAbout = aboutData.AboutData()