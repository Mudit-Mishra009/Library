from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class DeleteBooks(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x300+400+100")
        self.title("Delete Book")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)

        query2 = "SELECT * FROM Books"
        bookQuery = cur.execute(query2).fetchall()
        book_list = []
        for book in bookQuery:
            book_list.append(str(book[0]) + "-" + book[1])

        self.topFrame = Frame(self, height=150, bg="#b3daff")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg="#b3daff")
        self.bottomFrame.pack(fill=X)
        self.topImg = PhotoImage(file="addons/Deleteicon2.png")
        self.topImgLabel = Label(self.topFrame, image=self.topImg, bg="#b3daff")
        self.topImgLabel.place(x=40, y=40)
        imgHeading = Label(self.topFrame, text="  Delete Book  ", font="Times 30 bold underline", bg="#b3daff", fg="#0059b3")
        imgHeading.place(x=160, y=70)

        self.bookName = StringVar()
        self.nameLabel = Label(self.bottomFrame, text="Book:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=150, y=40)
        self.comboBox = ttk.Combobox(self.bottomFrame, textvariable = self.bookName)
        self.comboBox["values"] = book_list
        self.comboBox.place(x = 230, y = 46)

        self.bookInfoBtn = Button(self.bottomFrame, text= "Delete", bg="#b3daff", fg="#0059b3", font="Times 16 bold", command = self.bookDeleted)
        self.bookInfoBtn.place(x=240, y=90)

    def bookDeleted(self):
        book_name = self.bookName.get()
        self.book_id = book_name.split("-")[0]

        if (book_name != ""):
            try:
                query3 = "DELETE FROM 'Books' WHERE book_id = ?"
                bookId = (self.book_id, )
                cur.execute(query3, bookId)
                con.commit()
                messagebox.showinfo("Success", "Book Successfully Deleted!")

            except:
                messagebox.showerror("Error", "Deletion request faulty!")

        else:
            messagebox.showerror("Error", "Either of the fields cannot be empty!")