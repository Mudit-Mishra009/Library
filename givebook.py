from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *
from babel.numbers import *
from babel.dates import *
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x600+400+50")
        self.title("Issue Book")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)
        query = "SELECT * FROM Books WHERE book_status = 0"
        bookQuery = cur.execute(query).fetchall()
        book_list = []
        for book in bookQuery:
            book_list.append(str(book[0]) + "-" + book[1])

        query2 = "SELECT * FROM Members"
        memberQuery = cur.execute(query2).fetchall()
        member_list = []
        for member in memberQuery:
            member_list.append(str(member[0]) + "-" + member[1])

        self.topFrame = Frame(self, height=150, bg="#b3daff")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg="#b3daff")
        self.bottomFrame.pack(fill=X)
        self.topImg = PhotoImage(file="addons/issuebook2.png")
        self.topImgLabel = Label(self.topFrame, image=self.topImg, bg="#b3daff")
        self.topImgLabel.place(x=70, y=40)
        imgHeading = Label(self.topFrame, text="  Issue Book  ", font="Times 30 bold underline", bg="#b3daff", fg="#0059b3")
        imgHeading.place(x=200, y=70)

        self.bookName = StringVar()
        self.nameLabel = Label(self.bottomFrame, text="Book:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=40, y=40)
        self.comboBox = ttk.Combobox(self.bottomFrame, textvariable = self.bookName)
        self.comboBox["values"] = book_list
        self.comboBox.place(x = 150, y = 46)

        self.memberName = StringVar()
        self.nameLabel2 = Label(self.bottomFrame, text="Issue To:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel2.place(x=40, y=80)
        self.comboBox2 = ttk.Combobox(self.bottomFrame, textvariable=self.memberName)
        self.comboBox2["values"] = member_list
        self.comboBox2.place(x=150, y=86)

        self.dateLabel = Label(self.bottomFrame, text = "Date:", fg = "#0059b3", bg="#b3daff", font="arial 17 bold")
        self.dateLabel.place(x=40, y=120)
        self.dateLabelEntry = Calendar(self.bottomFrame, selectmode= "day", year = 2021, month = 1, day = 1,  fg = "#0059b3", bg = "#b3daff")
        self.dateLabelEntry.place(x=150, y=126)

        self.dataLabelInfo = Label(self.bottomFrame, text = "Format: Month/Date/Year", fg = "#0059b3", bg="#b3daff", font = "arial 10")
        self.dataLabelInfo.place(x = 420, y = 126)

        self.bookInfoBtn = Button(self.bottomFrame, text="Issue Book", bg="#b3daff", fg="#0059b3", font="Times 16 bold", command = self.bookIsGiven)
        self.bookInfoBtn.place(x=220, y=320)


    def bookIsGiven(self):
        CalendarData = self.dateLabelEntry.get_date()
        CalendarData2 = str(CalendarData)
        book_name = self.bookName.get()
        self.book_id = book_name.split("-")[0]
        member_name = self.memberName.get()

        if (book_name and member_name and CalendarData2 != ""):
            queryy = "SELECT (book_status) FROM Books WHERE book_id = ?"
            retrieveStatus1 = (self.book_id, )
            retrieveStatus2 = cur.execute(queryy, (retrieveStatus1)).fetchall()
            retrieveStatus3 = int(retrieveStatus2[0][0])
            if (retrieveStatus3 == 0):
                try:
                    query3 = "INSERT INTO 'Borrowed'(borrow_book_id, borrow_member_id, borrow_book_date) VALUES(?, ?, ?)"
                    cur.execute(query3, (book_name, member_name, CalendarData2))
                    con.commit()
                    messagebox.showinfo("Success", "Book successfully issued for 1 month!")
                    cur.execute("UPDATE Books SET book_status=? WHERE book_id=?", (1, self.book_id))
                    con.commit()

                except:
                    messagebox.showerror("Error", "Book could not be issued!")

            else:
                messagebox.showwarning("Warning", "Faulty request! Book unavailable!", icon = "warning")

        else:
            messagebox.showerror("Error", "Either of the fields cannot be empty!")