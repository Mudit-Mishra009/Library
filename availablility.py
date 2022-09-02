from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()

class ChangeAvailability(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x400+400+100")
        self.title("Change Availability")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)

        query2 = "SELECT * FROM Books"
        bookQuery = cur.execute(query2).fetchall()
        book_list = []
        for book in bookQuery:
            book_list.append(str(book[0]) + "-" + book[1])

        #Frames

        self.topFrame = Frame(self, height = 150, bg = "#b3daff")
        self.topFrame.pack(fill = X)
        self.bottomFrame = Frame(self, height = 600, bg = "#b3daff")
        self.bottomFrame.pack(fill = X)
        self.topImg = PhotoImage(file = "addons/redicon.png")
        self.topImgLabel = Label(self.topFrame, image = self.topImg, bg = "#b3daff")
        self.topImgLabel.place(x = 20, y = 40)
        imgHeading = Label(self.topFrame, text = "  Change Availability  ", font = "Times 30 bold underline", bg = "#b3daff", fg = "#0059b3")
        imgHeading.place(x = 110, y = 70)

        #Entries and Button
        self.bookName = StringVar()
        self.nameLabel = Label(self.bottomFrame, text="Book:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=150, y=40)
        self.comboBox = ttk.Combobox(self.bottomFrame, textvariable=self.bookName)
        self.comboBox["values"] = book_list
        self.comboBox.place(x=230, y=46)
        self.avlblLabel = Label(self.bottomFrame, text="Change to:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.avlblLabel.place(x=95, y=80)
        self.avlblEntry = Entry(self.bottomFrame, width=23, bd=3)
        self.avlblEntry.place(x=230, y=85)
        self.avlblLabel2 = Label(self.bottomFrame, text="(Enter 0 for available and 1 for unavailable)", fg="#0059b3", bg="#b3daff", font="arial 15")
        self.avlblLabel2.place(x=65, y=115)

        self.bookInfoBtn = Button(self.bottomFrame, text = "Change", bg = "#b3daff", fg = "#0059b3", font = "Times 16 bold", command = self.chngeAvail)
        self.bookInfoBtn.place(x = 240, y = 155)

    def chngeAvail(self):
        booksName = self.bookName.get()
        booksName2 = booksName.split("-")[0]
        self.avlblVal = self.avlblEntry.get()
        self.avlblVal2 = self.avlblVal

        if(booksName != ""):
            if(self.avlblVal2 == 0 or self.avlblVal2 == 1):

                self.avlblVal2 = int(self.avlblVal2)
                try:
                    query = "UPDATE Books SET book_status = ? WHERE book_id = ?"
                    bookieBook = (self.avlblVal2, booksName2, )
                    cur.execute(query, (bookieBook))
                    con.commit()
                    messagebox.showinfo("Success", "Successfully updated availability status!", icon="info")

                except:
                    messagebox.showerror("Error", "Updation Failed!", icon="warning")

            else:
                messagebox.showerror("Error", "Enter either of the provided values!", icon="error")
        else:
            messagebox.showerror("Error", "Either of the fields cannot be empty!", icon = "error")