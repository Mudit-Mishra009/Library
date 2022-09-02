from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()

class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x500+400+100")
        self.title("Add Member")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)

        #Frames

        self.topFrame = Frame(self, height = 150, bg = "#b3daff")
        self.topFrame.pack(fill = X)
        self.bottomFrame = Frame(self, height = 600, bg = "#b3daff")
        self.bottomFrame.pack(fill = X)
        self.topImg = PhotoImage(file = "addons/addmember2.png")
        self.topImgLabel = Label(self.topFrame, image = self.topImg, bg = "#b3daff")
        self.topImgLabel.place(x = 70, y = 40)
        imgHeading = Label(self.topFrame, text = "  Add Member  ", font = "Times 30 bold underline", bg = "#b3daff", fg = "#0059b3")
        imgHeading.place(x = 195, y = 70)

        #Entries and Button
        self.nameLabel = Label(self.bottomFrame, text = "Name:", fg = "#0059b3", bg = "#b3daff", font = "arial 17 bold")
        self.nameLabel.place(x = 40, y = 40)
        self.nameEntry = Entry(self.bottomFrame, width = 40, bd = 3)
        self.nameEntry.place(x = 168, y = 45)

        self.nameLabel2 = Label(self.bottomFrame, text="Phone:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel2.place(x=40, y=80)
        self.nameEntry2 = Entry(self.bottomFrame, width=40, bd=3)
        self.nameEntry2.place(x=168, y=85)

        self.bookInfoBtn = Button(self.bottomFrame, text = "Add", bg = "#b3daff", fg = "#0059b3", font = "Times 16 bold", command = self.addMember)
        self.bookInfoBtn.place(x = 240, y = 130)

    def addMember(self):
        memberName = self.nameEntry.get()
        contact = self.nameEntry2.get()

        if(memberName and contact != ""):
            try:
                query = "INSERT INTO 'Members' (member_name, member_contact) VALUES(?, ?)"
                cur.execute(query, (memberName, contact))
                con.commit()
                messagebox.showinfo("Success", "Congrats! Membership Granted!", icon = "info")

            except:
                messagebox.showerror("Error", "Membership request faulty!", icon = "warning")

        else:
            messagebox.showerror("Error", "Either of the fields cannot be empty!", icon = "error")