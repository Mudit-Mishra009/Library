from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class ReturnBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x300+400+100")
        self.title("Return Book")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)
        query = "SELECT * FROM Books WHERE book_status = 1"
        bookQuery = cur.execute(query).fetchall()
        book_list = []
        for book in bookQuery:
            book_list.append(str(book[0]) + "-" + book[1])


        self.topFrame = Frame(self, height=150, bg="#b3daff")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg="#b3daff")
        self.bottomFrame.pack(fill=X)
        self.topImg = PhotoImage(file="addons/Returnicon2.png")
        self.topImgLabel = Label(self.topFrame, image=self.topImg, bg="#b3daff")
        self.topImgLabel.place(x=70, y=40)
        imgHeading = Label(self.topFrame, text="  Return Book  ", font="Times 30 bold underline", bg="#b3daff", fg="#0059b3")
        imgHeading.place(x=195, y=70)

        self.bookName = StringVar()
        self.nameLabel = Label(self.bottomFrame, text="Book:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=120, y=40)
        self.comboBox = ttk.Combobox(self.bottomFrame, textvariable = self.bookName)
        self.comboBox["values"] = book_list
        self.comboBox.place(x = 192, y = 46)

        self.bookInfoBtn = Button(self.bottomFrame, text= "Return", bg="#b3daff", fg="#0059b3", font="Times 16 bold", command = self.bookIsGiven)
        self.bookInfoBtn.place(x=220, y=100)

    def bookIsGiven(self):
        book_name = self.bookName.get()
        self.book_id = book_name.split("-")[0]
        book_id2 = str(book_name)

        if (book_name!= ""):
            try:
                query3 = "DELETE FROM 'Borrowed' WHERE borrow_book_id = ?"
                bookId = (book_id2, )
                cur.execute(query3, bookId)
                con.commit()
                messagebox.showinfo("Success", "Book successfully returned!")
                cur.execute("UPDATE Books SET book_status=? WHERE book_id=?", (0, self.book_id))
                con.commit()

            except:
                messagebox.showerror("Error", "Return request faulty!")

        else:
            messagebox.showerror("Error", "Either of the fields cannot be empty!")