from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x500+400+100")
        self.title("Add Book")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)

        #Frames

        self.topFrame = Frame(self, height = 150, bg = "#b3daff")
        self.topFrame.pack(fill = X)
        self.bottomFrame = Frame(self, height = 600, bg = "#b3daff")
        self.bottomFrame.pack(fill = X)
        self.topImg = PhotoImage(file = "addons/addbook2.png")
        self.topImgLabel = Label(self.topFrame, image = self.topImg, bg = "#b3daff")
        self.topImgLabel.place(x = 70, y = 40)
        imgHeading = Label(self.topFrame, text = "  Add Book  ", font = "Times 30 bold underline", bg = "#b3daff", fg = "#0059b3")
        imgHeading.place(x = 200, y = 70)

        #Entries and Button
        self.nameLabel = Label(self.bottomFrame, text = "Name:", fg = "#0059b3", bg = "#b3daff", font = "arial 17 bold")
        self.nameLabel.place(x = 40, y = 40)
        self.nameEntry = Entry(self.bottomFrame, width = 40, bd = 3)
        self.nameEntry.place(x = 168, y = 45)

        self.nameLabel2 = Label(self.bottomFrame, text="Author:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel2.place(x=40, y=80)
        self.nameEntry2 = Entry(self.bottomFrame, width=40, bd=3)
        self.nameEntry2.place(x=168, y=85)

        self.pageLabel = Label(self.bottomFrame, text="Pages:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.pageLabel.place(x=40, y=120)
        self.pageEntry = Entry(self.bottomFrame, width=40, bd=3)
        self.pageEntry.place(x=168, y=125)

        self.languageLabel = Label(self.bottomFrame, text="Language:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.languageLabel.place(x=40, y=160)
        self.languageEntry = Entry(self.bottomFrame, width=40, bd=3)
        self.languageEntry.place(x=168, y=165)

        self.priceLabel = Label(self.bottomFrame, text="Price:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.priceLabel.place(x=40, y=200)
        self.priceEntry = Entry(self.bottomFrame, width=40, bd=3)
        self.priceEntry.place(x=168, y=205)

        self.bookInfoBtn = Button(self.bottomFrame, text = "Add", bg = "#b3daff", fg = "#0059b3", font = "Times 16 bold", command = self.addBook)
        self.bookInfoBtn.place(x = 240, y = 245)

    def addBook(self):
        bookName = self.nameEntry.get()
        authorName = self.nameEntry2.get()
        pageNum = self.pageEntry.get()
        langEntry = self.languageEntry.get()
        costEntry = self.priceEntry.get()

        if(bookName and authorName and pageNum and langEntry and costEntry != ""):
            try:
                query = "INSERT INTO 'Books' (book_name, book_author, book_pages, book_language, book_price) VALUES(?, ?, ?, ?, ?  )"
                cur.execute(query, (bookName, authorName, pageNum, langEntry, costEntry))
                con.commit()
                messagebox.showinfo("Success", "Successfully added to the Library!", icon = "info")

            except:
                messagebox.showerror("Error", "Addition to the library failed!", icon = "warning")

        else:
            messagebox.showerror("Error", "Either of the fields cannot be empty!", icon = "error")