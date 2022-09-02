from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class FulfilledRequests(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x300+400+100")
        self.title("Delete Fulfilled Requests")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)

        query2 = "SELECT * FROM Requests"
        requestQuery = cur.execute(query2).fetchall()
        request_list = []
        for request in requestQuery:
            request_list.append(str(request[0]) + ") by " + request[1] + "-" + request[2])

        self.topFrame = Frame(self, height=150, bg="#b3daff")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg="#b3daff")
        self.bottomFrame.pack(fill=X)
        self.topImg = PhotoImage(file="addons/fulfillicon.png")
        self.topImgLabel = Label(self.topFrame, image=self.topImg, bg="#b3daff")
        self.topImgLabel.place(x=40, y=40)
        imgHeading = Label(self.topFrame, text="  Fulfilled Requests  ", font="Times 30 bold underline", bg="#b3daff", fg="#0059b3")
        imgHeading.place(x=140, y=70)

        self.requestName = StringVar()
        self.nameLabel = Label(self.bottomFrame, text="Queued Requests:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=85, y=30)
        self.comboBox = ttk.Combobox(self.bottomFrame, textvariable = self.requestName)
        self.comboBox["values"] = request_list
        self.comboBox.place(x = 300, y = 36)

        self.bookInfoBtn = Button(self.bottomFrame, text= "Delete Request", bg="#b3daff", fg="#0059b3", font="Times 16 bold", command = self.requestDeleted)
        self.bookInfoBtn.place(x=190, y=90)

    def requestDeleted(self):
        request_name = self.requestName.get()
        self.request_id2 = request_name.split(")")[0]

        if (request_name != ""):
            try:
                query3 = "DELETE FROM 'Requests' WHERE request_id = ?"
                requestId = (self.request_id2, )
                cur.execute(query3, requestId)
                con.commit()
                messagebox.showinfo("Success", "Fulfilled Request Deleted!")

            except:
                messagebox.showerror("Error", "Deletion request faulty!")

        else:
            messagebox.showerror("Error", "Either of the fields cannot be empty!")