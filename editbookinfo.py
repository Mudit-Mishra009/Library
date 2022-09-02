from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class EditBookInfo(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x500+400+100")
        self.title("Edit Book Information")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)
        query = "SELECT * FROM Books"
        bookQuery = cur.execute(query).fetchall()
        book_list = []
        for book in bookQuery:
            book_list.append(str(book[0]) + "-" + book[1])


        self.topFrame = Frame(self, height=150, bg="#b3daff")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg="#b3daff")
        self.bottomFrame.pack(fill=X)
        imgHeading = Label(self.topFrame, text="  Edit Book Information  ", font="Times 30 bold underline", bg="#b3daff", fg="#0059b3")
        imgHeading.place(x=40, y=70)

        self.bookName = StringVar()
        self.nameLabel = Label(self.bottomFrame, text="Book:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=40, y=40)
        self.comboBox = ttk.Combobox(self.bottomFrame, textvariable = self.bookName)
        self.comboBox["values"] = book_list
        self.comboBox.place(x = 168, y = 45)

        self.nameLabel = Label(self.bottomFrame, text="Name:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=40, y=80)
        self.nameEntry = Entry(self.bottomFrame, width=40, bd=3)
        self.nameEntry.place(x=168, y=85)

        self.nameLabel2 = Label(self.bottomFrame, text="Author:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel2.place(x=40, y=120)
        self.nameEntry2 = Entry(self.bottomFrame, width=40, bd=3)
        self.nameEntry2.place(x=168, y=125)

        self.pageLabel = Label(self.bottomFrame, text="Pages:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.pageLabel.place(x=40, y=160)
        self.pageEntry = Entry(self.bottomFrame, width=40, bd=3)
        self.pageEntry.place(x=168, y=165)

        self.languageLabel = Label(self.bottomFrame, text="Language:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.languageLabel.place(x=40, y=200)
        self.languageEntry = Entry(self.bottomFrame, width=40, bd=3)
        self.languageEntry.place(x=168, y=205)

        self.priceLabel = Label(self.bottomFrame, text="Price:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.priceLabel.place(x=40, y=240)
        self.priceEntry = Entry(self.bottomFrame, width=40, bd=3)
        self.priceEntry.place(x=168, y=245)

        self.bookInfoBtn = Button(self.bottomFrame, text= "Update", bg="#b3daff", fg="#0059b3", font="Times 16 bold", command = self.bookIsEdited)
        self.bookInfoBtn.place(x=240, y=285)

    def bookIsEdited(self):
        book_name = self.bookName.get()
        self.book_id = book_name.split("-")[0]
        book_id2 = str(book_name)
        new_book_name = self.nameEntry.get()
        new_book_name2 = str(new_book_name)
        new_author_name = self.nameEntry2.get()
        new_author_name2 = str(new_author_name)
        new_page_num = self.pageEntry.get()
        new_page_num2 = str(new_page_num)
        new_lang = self.languageEntry.get()
        new_lang2 = str(new_lang)
        new_price = self.priceEntry.get()
        new_price2 = str(new_price)

        if (book_name!= ""):
            try:
                if new_book_name2 and new_author_name2 and new_page_num2 and new_lang2 and new_price2 != "":
                    query = "UPDATE Books SET book_name = ? WHERE book_id = ?"
                    Book_Name = (new_book_name2, self.book_id, )
                    cur.execute(query, (Book_Name))
                    con.commit()
                    query2 = "UPDATE Books SET book_author = ? WHERE book_id = ?"
                    Book_Name2 = (new_author_name2, self.book_id,)
                    cur.execute(query2, (Book_Name2))
                    con.commit()
                    query3 = "UPDATE Books SET book_pages = ? WHERE book_id = ?"
                    Book_Name3 = (new_page_num2, self.book_id,)
                    cur.execute(query3, (Book_Name3))
                    con.commit()
                    query4 = "UPDATE Books SET book_language = ? WHERE book_id = ?"
                    Book_Name4 = (new_lang2, self.book_id,)
                    cur.execute(query4, (Book_Name4))
                    con.commit()
                    query5 = "UPDATE Books SET book_price = ? WHERE book_id = ?"
                    Book_Name5 = (new_price2, self.book_id,)
                    cur.execute(query5, (Book_Name5))
                    con.commit()

                    messagebox.showinfo("Success", "Information successfully updated!")

                else:
                    messagebox.showerror("Error", "Either of the fields cannot be empty!")

            except:
                messagebox.showerror("Error", "Updation request faulty!")

        else:
            messagebox.showerror("Error", "The field 'Book' cannot be empty!")