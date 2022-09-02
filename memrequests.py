from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class MemberRequests(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x400+400+100")
        self.title("Member Requests")
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
        self.topImg = PhotoImage(file="addons/addicon.png")
        self.topImgLabel = Label(self.topFrame, image=self.topImg, bg="#b3daff")
        self.topImgLabel.place(x=25, y=40)
        imgHeading = Label(self.topFrame, text="  Member Requests  ", font="Times 30 bold underline", bg="#b3daff", fg="#0059b3")
        imgHeading.place(x=135, y=70)

        self.memberName = StringVar()
        self.nameLabel = Label(self.bottomFrame, text="Member:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=120, y=40)
        self.comboBox = ttk.Combobox(self.bottomFrame, textvariable = self.memberName)
        self.comboBox["values"] = member_list
        self.comboBox.place(x = 225, y = 46)

        self.bookReqLabel = Label(self.bottomFrame, text = "Requested Book:", fg = "#0059b3", bg="#b3daff", font="arial 17 bold")
        self.bookReqLabel.place(x=25, y = 80)
        self.bookReqEntry = Entry(self.bottomFrame, width = 40, bd = 3)
        self.bookReqEntry.place(x=225, y = 86)

        self.bookInfoBtn = Button(self.bottomFrame, text= "Queue Request", bg="#b3daff", fg="#0059b3", font="Times 16 bold", command = self.memberRequested)
        self.bookInfoBtn.place(x=210, y=130)

    def memberRequested(self):
        member_name = self.memberName.get()
        self.member_id = member_name.split("-")[0]
        reqBook = self.bookReqEntry.get()

        if (member_name and reqBook != "" ):
            try:
                query3 = "INSERT INTO 'Requests' (request_mem_name, request_book_name) VALUES (?, ? )"
                cur.execute(query3, (member_name, reqBook))
                con.commit()
                messagebox.showinfo("Success", "Request successfully queued!")

            except:
                messagebox.showerror("Error", "Queue request faulty!")

        else:
            messagebox.showerror("Error", "Either of the fields cannot be empty!")