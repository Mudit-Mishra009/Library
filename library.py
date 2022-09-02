from tkinter import *
from tkinter import ttk
import sqlite3 #database
from tkcalendar import *
import addbook, addmember, givebook, returnbook, deletemember, editinfo, moreinfo
from tkinter import messagebox
from babel.numbers import *
from babel.dates import *

con = sqlite3.connect("Library.db") #database connection setup with the database name as Library!
cur = con.cursor() #creation of cursor

class Main(object):
    def __init__(self,master):
        self.master = master

        def displayStatistics(event):
            countBooks = cur.execute("SELECT count(book_id) FROM Books").fetchall()
            countMembers = cur.execute("SELECT count(member_id) FROM Members").fetchall()
            countBorrowed = cur.execute("SELECT count(book_status) FROM Books WHERE book_status = 1").fetchall()


            self.statsBookCount.config(text = "Total Books : " + str(countBooks[0][0]))
            self.statsMemberCount.config(text = "Total Members : " + str(countMembers[0][0]))
            self.statsIssueCount.config(text = "Books Issued/Unavailable : "+ str(countBorrowed)[2][0])

            displayBooks(self)
            bookssInfo(self)

        def displayMembers(event):
            members = cur.execute("SELECT * FROM Members").fetchall()
            count1 = 0

            self.membersInfo.delete(0, END)
            for member in members:
                self.membersInfo.insert(count1, str(member[0]) + " - " + str(member[1]) + " -    " + member[2])
                count1 += 1

        def displayRequests(event):
            requests = cur.execute("SELECT * FROM Requests").fetchall()
            counter = 0

            self.requestsInfo.delete(0, END)
            for request in requests:
                self.requestsInfo.insert(counter, str(request[1]) + "    requested for       " + str(request[2]))
                counter += 1


        def displayBooks(self):
            books = cur.execute("SELECT * FROM Books").fetchall()
            count = 0

            self.booksList.delete(0, END)
            for book in books:
                self.booksList.insert(count, str(book[0]) + "- " + book[1])
                count+=1

        def bookssInfo(self):
            books = cur.execute("SELECT * FROM Borrowed").fetchall()
            count = 0

            self.booksInfo.delete(0, END)
            for book in books:
                self.booksInfo.insert(count, str(book[1]) + "      issued to      " + str(book[2]) + "      on      " + str(book[3]))
                count+=1


            def bookInfo(event):
                value = str(self.booksList.get(self.booksList.curselection()))
                id = value.split("-")[0]
                book = cur.execute("SELECT * From Books WHERE book_id = ?", (id,))
                infoBook = book.fetchall()


                self.detailsList.delete(0, "end")
                self.detailsList.insert(0, "Book Name: " + infoBook[0][1])
                self.detailsList.insert(1, "Author: " + infoBook[0][2])
                self.detailsList.insert(2, "Pages: " + infoBook[0][3])
                self.detailsList.insert(3, "Language: " + infoBook[0][4])
                self.detailsList.insert(4, "Price: " + infoBook[0][6])
                if infoBook[0][5] == 0:
                    self.detailsList.insert(5, "STATUS: AVAILABLE")
                else:
                    self.detailsList.insert(5, "STATUS: UNAVAILABLE")

            def doubleCLick(event):
                global given_id
                doubleValue = self.booksList.get(self.booksList.curselection())
                given_id = doubleValue.split("-")[0]
                issue_book = issueBook()



            self.booksList.bind("<<ListboxSelect>>", bookInfo)
            self.tabs.bind("<<NotebookTabChanged>>", displayStatistics)
            self.booksList.bind("<Double-Button-1>", doubleCLick)
            self.tabs.bind("<<NotebookT-abChanged>>", bookssInfo)
            self.tabs.bind("<Button-1>", displayMembers)
            self.tabs.bind("<ButtonRelease-1>", displayRequests)

        #Frames
        mainFrame = Frame(self.master)
        mainFrame.pack(fill = X)
        topFrame = Frame(mainFrame, width = 1366, height = 80, bg = "#ccffcc", relief = SUNKEN, borderwidth = 5)
        topFrame.pack(side = TOP, fill = X)
        centreFrame = Frame(mainFrame, width = 1366, height = 688, bg = "#ccffcc", relief = RIDGE)
        centreFrame.pack(side = TOP, fill = X)
        centreLeftFrame = Frame(centreFrame, width = 900, height = 688, bg = "#ccffcc", relief = SUNKEN, borderwidth = 5)
        centreLeftFrame.pack(side = LEFT, fill = Y)
        centreRightFrame = Frame(centreFrame, width = 466, height = 688, bg = "#ccffcc", relief = SUNKEN, borderwidth = 5)
        centreRightFrame.pack(side = RIGHT, fill = Y)

        #Bars
        searchBar = LabelFrame(centreRightFrame, width = 466, height = 70, text = "Search Box", bg = "#f8f8f8")
        searchBar.pack(fill = BOTH)
        self.searchBarLabel = Label(searchBar, text = "Search:", font = "Times 12 bold", fg = "Black", bg = "#f8f8f8")
        self.searchBarLabel.grid(row = 0, column= 0, sticky = W, padx = 5, pady = 5)
        self.searchBarEntry = Entry(searchBar, width = 50, bd = 4)
        self.searchBarEntry.grid(row = 0, column = 1, sticky = W, padx = 5, pady = 5)
        self.searchBarButton = Button(searchBar, text = "Search", font = "Times 10 bold", command = self.bookSearch)
        self.searchBarButton.grid(row = 0, column = 3)
        listBar = LabelFrame(centreRightFrame, width = 460, text = "List Box", bg = "#e6e600")
        listBar.pack(fill = BOTH)
        self.listBarLabel = Label(listBar, text = "Sort By:", font = "Times 15 bold", fg = "#0059b3", bg = "#e6e600")
        self.listBarLabel.grid(row = 0, column = 1, sticky = E)
        self.LibImgHeading = Label(centreRightFrame, text="Welcome to our Library", font="Times 18 bold", bg = "#ccffcc")
        self.LibImgHeading.pack(side = BOTTOM)
        self.LibraryImg = PhotoImage(file="addons/Library.png")
        self.LibraryImgLabel = Label(centreRightFrame, image = self.LibraryImg)
        self.LibraryImgLabel.pack(padx = 10, pady = 10)

        #RadioButtons
        self.sortChoice = IntVar()
        self.radiobtn1 = Radiobutton(listBar, text = "All Books", variable = self.sortChoice, value = 1, bg = "#e6e600", font = "Times 13")
        self.radiobtn2 = Radiobutton(listBar, text = "Currently Available", variable = self.sortChoice, value = 2, bg = "#e6e600", font = "Times 13")
        self.radiobtn3 = Radiobutton(listBar, text = "Unavailable", variable = self.sortChoice, value = 3, bg = "#e6e600", font = "Times 13")
        self.radiobtn1.grid(row = 1, column = 0)
        self.radiobtn2.grid(row = 1, column = 1)
        self.radiobtn3.grid(row = 1, column = 2)
        self.listbtn = Button(listBar, text = "List Books", bg = "#e6e600", fg = "#0059b3", font = "Times 12 bold", command = self.listBooks)
        self.listbtn.grid(row = 2, column = 1, pady = 5, sticky = E)


        #Buttons
        self.bookicon = PhotoImage(file = "addons/addbook.png")
        self.addbookbtn = Button(topFrame, text = "Add Book", image = self.bookicon, bg="#b3daff", compound = LEFT, font = "Times 13 bold",padx = 5, borderwidth = 2, command = self.addBook)
        self.addbookbtn.pack(side = LEFT)
        self.membericon = PhotoImage(file = "addons/addmember.png")
        self.addmemberbtn = Button(topFrame, text = "Add Member",bg="#b3daff", image = self.membericon, compound = LEFT, font = "Times 13 bold", padx = 5,  command = self.addMember)
        self.addmemberbtn.pack(side = LEFT)
        self.issueicon = PhotoImage(file = "addons/issuebook.png")
        self.issuebookbtn = Button(topFrame, text = "Issue Book",bg="#b3daff", image = self.issueicon, compound = LEFT, font = "Times 13 bold", padx = 5, borderwidth = 2, command = self.giveBook)
        self.issuebookbtn.pack(side = LEFT)
        self.returnIcon = PhotoImage(file = "addons/Returnicon.png")
        self.returnbookbtn = Button(topFrame, text = "Return Book",bg="#b3daff", image = self.returnIcon, compound = LEFT, font = "Times 13 bold", padx =5, command = self.returnBook)
        self.returnbookbtn.pack(side = LEFT)
        self.deleteIcon = PhotoImage(file="addons/Deleteicon.png")
        self.deletememberbtn = Button(topFrame, text="Delete Member",bg="#b3daff", image=self.deleteIcon, compound=LEFT, font="Times 13 bold", padx=5, borderwidth = 2, command=self.deleteMember)
        self.deletememberbtn.pack(side=LEFT)
        self.moreIcon = PhotoImage(file="addons/moreicon2.png")
        self.moreInfobtn = Button(topFrame, text="More",bg="#b3daff", image=self.moreIcon, compound=LEFT, font="Times 12 bold", padx=5, command = self.moreInformation)
        self.moreInfobtn.pack(side=LEFT)


        #Tabs
        self.tabs = ttk.Notebook(centreLeftFrame, width = 900, height = 660)
        self.tabs.pack()
        self.tab1Img = PhotoImage(file = "addons/Management.png")
        self.tab2Img = PhotoImage(file = "addons/statistics.png")
        self.tab3Img = PhotoImage(file = "addons/infoicon.png")
        self.tab4Img = PhotoImage(file = "addons/memberinfo.png")
        self.tab5Img = PhotoImage(file = "addons/reqicon.png")
        self.tab4 = ttk.Frame(self.tabs)
        self.tab3 = ttk.Frame(self.tabs)
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tab5 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text = "Management", image = self.tab1Img, compound = LEFT)
        self.tabs.add(self.tab2, text = "Statistics", image = self.tab2Img, compound = LEFT)
        self.tabs.add(self.tab3, text = "Books Info", image = self.tab3Img, compound = LEFT)
        self.tabs.add(self.tab4, text = "Members Info", image = self.tab4Img, compound = LEFT)
        self.tabs.add(self.tab5, text = "Requests", image = self.tab5Img, compound = LEFT)

        #Management Tab1

        #bookslist
        self.booksList = Listbox(self.tab1, width = 50, height = 30, bg = "#ccffcc", bd = 3, font = "Times 13 bold", exportselection = False)
        self.sbar = Scrollbar(self.tab1, orient = VERTICAL)
        self.booksList.grid(row = 0, column = 0, padx = 10, pady =10, sticky  = N+S)
        self.sbar.config(command = self.booksList.yview)
        self.booksList.config(yscrollcommand = self.sbar.set)
        self.sbar.grid(row = 0, column = 0, sticky = N+S+E)

        #detailsList
        self.detailsList = Listbox(self.tab1, width = 44, height = 30, bg = "#ccffcc", bd = 3, font = "Times 13 bold")
        self.detailsList.grid(row = 0, column = 1, padx = 10, pady =10, sticky = N)
        self.sbar4 = Scrollbar(self.tab1, orient = HORIZONTAL)
        self.sbar4.config(command = self.detailsList.xview)
        self.detailsList.config(xscrollcommand = self.sbar4.set)
        self.sbar4.grid(row = 0, column = 1, sticky = W+E+S)

        #Statistics Tab2

        self.statsBookCount = Label(self.tab2, text = "", pady = 10, font = "Verdana 15 bold")
        self.statsBookCount.grid(row = 0, sticky = W)
        self.statsMemberCount = Label(self.tab2, text = "", pady = 10, font = "Verdana 15 bold")
        self.statsMemberCount.grid(row=1, sticky = W)
        self.statsIssueCount = Label(self.tab2, text= "", pady=10, font="Verdana 15 bold")
        self.statsIssueCount.grid(row=2, sticky=W)

        #BooksInfo Tab3

        self.booksInfo = Listbox(self.tab3, width = 97, height = 30, bd = 3, font = "Times 13 bold", bg = "#ccffcc")
        self.sbar2 = Scrollbar(self.tab3, orient=VERTICAL)
        self.booksInfo.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = N)
        self.sbar2.config(command=self.booksList.yview)
        self.booksInfo.config(yscrollcommand=self.sbar2.set)
        self.sbar2.grid(row=0, column=0, sticky=N + S + E)

        #MembersInfo Tab4

        self.membersInfo = Listbox(self.tab4, width = 97, height = 30, bd = 3, font = "Times 13 bold", bg = "#ccffcc")
        self.membersInfo.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = N)
        self.sbar3 = Scrollbar(self.tab4, orient = VERTICAL)
        self.sbar3.config(command=self.booksList.yview)
        self.membersInfo.config(yscrollcommand=self.sbar3.set)
        self.sbar3.grid(row=0, column=0, sticky=N + S + E)

        #Requests Tab5

        self.requestsInfo = Listbox(self.tab5, width = 97, height = 30, bd = 3, font = "Times 13 bold", bg = "#ccffcc")
        self.requestsInfo.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = N)
        self.sbar4 = Scrollbar(self.tab5, orient=VERTICAL)
        self.sbar4.config(command=self.booksList.yview)
        self.membersInfo.config(yscrollcommand=self.sbar4.set)
        self.sbar4.grid(row=0, column=0, sticky=N + S + E)


        #quotelabel
        quote = Label(topFrame, text = '"Books are a uniquely portable magic" - Stephen King', bg = "#ccffcc", font = "Times 14 bold",padx = 10, fg = "red")
        quote.pack(side = RIGHT)

        displayBooks(self)
        displayStatistics(self)
        bookssInfo(self)
        displayMembers(self)
        displayRequests(self)

    def addBook(self):
        add = addbook.AddBook()

    def addMember(self):
        member = addmember.AddMember()

    def giveBook(self):
        giveB = givebook.GiveBook()

    def returnBook(self):
        returnB = returnbook.ReturnBook()

    def deleteMember(self):
        deleteM = deletemember.DeleteMember()

    def moreInformation(self):
        editI = moreinfo.MoreInformation()

    def bookSearch(self):
        bookVal = self.searchBarEntry.get()
        searchVal = cur.execute("SELECT * FROM Books WHERE book_name LIKE ?", ("%"+bookVal+"%",)).fetchall()
        self.booksList.delete(0 , END)
        count = 0
        for books in searchVal:
            self.booksList.insert(count, str(books[0]) + "-" + books[1])
            count =+ 1

    def listBooks(self):
        listVal = self.sortChoice.get()
        if listVal == 1:
            listVal1 = cur.execute("SELECT * FROM Books").fetchall()
            self.booksList.delete(0, END)
            count = 0
            for books in listVal1:
                self.booksList.insert(count, str(books[0]) + "-" + books[1])
                count += 1

        elif listVal == 2:
            listVal2 = cur.execute("SELECT * FROM Books WHERE book_status = ?", (0,)).fetchall()
            self.booksList.delete(0, END)
            count = 0
            for books in listVal2:
                self.booksList.insert(count, str(books[0]) + "-" + books[1])
                count += 1

        else:
            listVal3 = cur.execute("SELECT * FROM Books WHERE book_status = ?", (1,)).fetchall()
            self.booksList.delete(0 ,END)
            count = 0
            for books in listVal3:
                self.booksList.insert(count, str(books[0]) + "-" + books[1])
                count += 1

class issueBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("600x600+400+50")
        global given_id
        book_id = int(given_id)
        self.title("Issue Book")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)
        query = "SELECT * FROM Books"
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
        imgHeading = Label(self.topFrame, text="  Issue Book  ", font="Times 30 bold underline", bg="#b3daff",
                           fg="#0059b3")
        imgHeading.place(x=200, y=70)

        self.bookName = StringVar()
        self.nameLabel = Label(self.bottomFrame, text="Book:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=40, y=40)
        self.comboBox = ttk.Combobox(self.bottomFrame, textvariable=self.bookName)
        self.comboBox["values"] = book_list
        self.comboBox.place(x=150, y=46)
        book_id2 = book_id
        self.comboBox.current(book_id2 - 1)

        self.memberName = StringVar()
        self.nameLabel2 = Label(self.bottomFrame, text="Issue To:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel2.place(x=40, y=80)
        self.comboBox2 = ttk.Combobox(self.bottomFrame, textvariable=self.memberName)
        self.comboBox2["values"] = member_list
        self.comboBox2.place(x=150, y=86)

        self.dateLabel = Label(self.bottomFrame, text="Date:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.dateLabel.place(x=40, y=120)
        self.dateLabelEntry = Calendar(self.bottomFrame, selectmode="day", year=2021, month=1, day=1, fg="#0059b3",
                                       bg="#b3daff")
        self.dateLabelEntry.place(x=150, y=126)

        self.dataLabelInfo = Label(self.bottomFrame, text="Format: Month/Date/Year", fg="#0059b3", bg="#b3daff",
                                   font="arial 10")
        self.dataLabelInfo.place(x=420, y=126)

        self.bookInfoBtn = Button(self.bottomFrame, text="Issue Book", bg="#b3daff", fg="#0059b3", font="Times 16 bold",
                                  command=self.bookIsGiven)
        self.bookInfoBtn.place(x=220, y=320)

    def bookIsGiven(self):
        CalendarData = self.dateLabelEntry.get_date()
        CalendarData2 = str(CalendarData)
        book_name = self.bookName.get()
        self.book_id = book_name.split("-")[0]
        member_name = self.memberName.get()

        if (book_name and member_name and CalendarData2 != ""):
            queryy = "SELECT (book_status) FROM Books WHERE book_id = ?"
            retrieveStatus1 = (self.book_id,)
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
                messagebox.showwarning("Warning", "Faulty request! Book unavailable!", icon="warning")

        else:
            messagebox.showerror("Error", "Either of the fields cannot be empty!")


def main():
    root = Tk()
    app = Main(root)
    root.title("Librarian's Shelf")
    root.geometry("1366x768")
    root.resizable(False, False)
    root.iconbitmap("addons/libicon.ico")
    root.mainloop()
if __name__ == "__main__":
    main()