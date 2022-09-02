from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class ClearData(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x300+400+100")
        self.title("Clear Data")
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
        clearHeading = Label(self.topFrame, text="  Clear Data  ", font="Times 30 bold underline", bg="#b3daff", fg="#0059b3")
        clearHeading.place(x=160, y=20)

        warnHeading = Label(self.topFrame, text="  Note -  ", font="Times 20 underline", bg="#b3daff", fg="#0059b3")
        warnHeading.place(x=0, y=80)
        warnHeading1 = Label(self.topFrame, text=" Clicking the button below will result  ", font="Times 20 ", bg="#b3daff", fg="#0059b3")
        warnHeading1.place(x=83, y=80)
        warnHeading2 = Label(self.topFrame, text=" in permanent deletion of all types of  ", font="Times 20 ", bg="#b3daff", fg="#0059b3")
        warnHeading2.place(x=83, y=115)
        warnHeading3 = Label(self.bottomFrame, text=" data. Proceed at your own discretion.  ", font="Times 20 ", bg="#b3daff", fg="#0059b3")
        warnHeading3.place(x=83, y=0)
        warnHeading4= Label(self.bottomFrame, text=" Again, deleted data cannot be recovered.  ", font="Times 20 ", bg="#b3daff", fg="#0059b3")
        warnHeading4.place(x=45, y=35)

        self.deleteDataBtn = Button(self.bottomFrame, text= "Clear All Data", bg="#b3daff", fg="#0059b3", font="Times 16 bold", command = self.dataDeleted)
        self.deleteDataBtn.place(x=200, y=90)

    def dataDeleted(self):

        cur.execute("DELETE FROM 'Books'")
        cur.execute("DELETE FROM 'Members'")
        cur.execute("DELETE FROM 'Borrowed'")
        cur.execute("DELETE FROM 'Requests'")
        cur.execute("DELETE FROM 'sqlite_sequence' WHERE name = 'Books'")
        cur.execute("DELETE FROM 'sqlite_sequence' WHERE name = 'Members'")
        cur.execute("DELETE FROM 'sqlite_sequence' WHERE name = 'Borrowed'")
        cur.execute("DELETE FROM 'sqlite_sequence' WHERE name = 'Requests'")
        con.commit()
        messagebox.showinfo("Success", "All data has been successfully deleted!", icon = "info")