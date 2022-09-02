from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

con = sqlite3.connect("Library.db")
cur = con.cursor()


class EditMemberInfo(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x500+400+100")
        self.title("Edit Member Information")
        self.iconbitmap("addons/libicon.ico")
        self.resizable(False, False)
        query = "SELECT * FROM Members"
        memberQuery = cur.execute(query).fetchall()
        member_list = []
        for member in memberQuery:
            member_list.append(str(member[0]) + "-" + member[1])


        self.topFrame = Frame(self, height=150, bg="#b3daff")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=600, bg="#b3daff")
        self.bottomFrame.pack(fill=X)
        imgHeading = Label(self.topFrame, text="  Edit Member Information  ", font="Times 30 bold underline", bg="#b3daff", fg="#0059b3")
        imgHeading.place(x=3, y=70)

        self.memberName = StringVar()
        self.nameLabel = Label(self.bottomFrame, text="Member:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=40, y=40)
        self.comboBox = ttk.Combobox(self.bottomFrame, textvariable = self.memberName)
        self.comboBox["values"] = member_list
        self.comboBox.place(x = 168, y = 45)

        self.nameLabel = Label(self.bottomFrame, text="Name:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel.place(x=40, y=80)
        self.nameEntry = Entry(self.bottomFrame, width=40, bd=3)
        self.nameEntry.place(x=168, y=85)

        self.nameLabel2 = Label(self.bottomFrame, text="Phone:", fg="#0059b3", bg="#b3daff", font="arial 17 bold")
        self.nameLabel2.place(x=40, y=120)
        self.nameEntry2 = Entry(self.bottomFrame, width=40, bd=3)
        self.nameEntry2.place(x=168, y=125)


        self.memberInfoBtn = Button(self.bottomFrame, text= "Update", bg="#b3daff", fg="#0059b3", font="Times 16 bold", command = self.memberIsEdited)
        self.memberInfoBtn.place(x=240, y=165)

    def memberIsEdited(self):
        member_name = self.memberName.get()
        self.member_id = member_name.split("-")[0]
        member_id2 = str(member_name)
        new_member_name = self.nameEntry.get()
        new_member_name2 = str(new_member_name)
        new_phone_num = self.nameEntry2.get()
        new_phone_num2 = str(new_phone_num)

        if (member_name!= ""):
            try:
                if new_member_name2 and new_phone_num2 != "":
                    query = "UPDATE Members SET member_name = ? WHERE member_id = ?"
                    Member_Name = (new_member_name2, self.member_id, )
                    cur.execute(query, (Member_Name))
                    con.commit()
                    query2 = "UPDATE Members SET member_contact = ? WHERE member_id = ?"
                    Member_Name2 = (new_phone_num2, self.member_id, )
                    cur.execute(query2, (Member_Name2))
                    con.commit()

                    messagebox.showinfo("Success", "Information successfully updated!")

                else:
                    messagebox.showerror("Error", "Either of the fields cannot be empty!")

            except:
                messagebox.showerror("Error", "Updation request faulty!")

        else:
            messagebox.showerror("Error", "The field 'Member' cannot be empty!")