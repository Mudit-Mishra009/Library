from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class DeleteMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x300+400+100")
        self.title("Delete Member")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)

        query2 = "SELECT * FROM Members"
        memberQuery = cur.execute(query2).fetchall()
        member_list = []
        for member in memberQuery:
            member_list.append(str(member[0]) + "-" + member[1])

        self.topFrame = Frame(self, height=150, bg="#b3daff")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg="#b3daff")
        self.bottomFrame.pack(fill=X)
        self.topImg = PhotoImage(file="addons/Deleteicon2.png")
        self.topImgLabel = Label(self.topFrame, image=self.topImg, bg="#b3daff")
        self.topImgLabel.place(x=40, y=40)
        imgHeading = Label(self.topFrame, text="  Delete Member  ", font="Times 30 bold underline", bg="#b3daff", fg="#0059b3")
        imgHeading.place(x=160, y=70)

        self.memberName = StringVar()
        self.nameLabel = Label(self.bottomFrame, text="Member:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=120, y=40)
        self.comboBox = ttk.Combobox(self.bottomFrame, textvariable = self.memberName)
        self.comboBox["values"] = member_list
        self.comboBox.place(x = 225, y = 46)

        self.bookInfoBtn = Button(self.bottomFrame, text= "Delete", bg="#b3daff", fg="#0059b3", font="Times 16 bold", command = self.memberDeleted)
        self.bookInfoBtn.place(x=240, y=90)

    def memberDeleted(self):
        member_name = self.memberName.get()
        self.member_id = member_name.split("-")[0]

        if (member_name != ""):
            try:
                query3 = "DELETE FROM 'Members' WHERE member_id = ?"
                memberId = (self.member_id, )
                cur.execute(query3, memberId)
                con.commit()
                messagebox.showinfo("Success", "Membership Successfully Withdrawn!")

            except:
                messagebox.showerror("Error", "Withdrawal request faulty!")

        else:
            messagebox.showerror("Error", "Either of the fields cannot be empty!")