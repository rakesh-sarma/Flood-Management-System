import csv
import mysql.connector
from tkinter import*
root= Tk()
root.title("Flood Management System")
root.geometry("1350x700")
root.minsize(740,380)
Label(text="Flood Relief Management System",font=("goudy old style",25,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
frame = Frame(root)
frame.pack()
canvas=Canvas(root,  height=590, width=1300)
canvas.pack(side=BOTTOM)
img = PhotoImage( file = "/Users/rakeshsarma033gmail.com/Desktop/pythonINT213/pythonnewpic.png")
label1 = Label( canvas, image = img)
label1.place(height=590, width=1300)
#Menu
M_Frame=LabelFrame(text="Menus",font=("times new roman",15),bg="white")
M_Frame.place(x=10,y=70,width=1330,height=80)
#Donation Menu
def donationmenu():
     donation = Toplevel(root)
     donation.geometry("400x300")
     donation.title("Donation Menu")
     Label(donation,text="WELCOME", font="bold 20").grid(row=0, column=3)
     def getvals():
        Name=namevalue.get()
        Amount=amountvalue.get()
        phone=phonevalue.get()
        print("Thank You")
        mydb = mysql.connector.connect(host="localhost",user="root",password="Manash@23",database="pythonproject1")
        mycursor = mydb.cursor()

        sql = "INSERT INTO Donate (Name,Amount,phone) VALUES (%s, %s, %s)"
        val = (Name,Amount,phone)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    #Name from user
     name = Label(donation, text="Name")
     phone = Label(donation, text="Phone")
     amount= Label(donation, text="Enter the Amount")
    #Pack text 
     name.grid(row=1, column=2)
     phone.grid(row=2, column=2)
     amount.grid(row=3, column=2)
    # Tkinter variable for storing entries
     namevalue = StringVar()
     phonevalue = StringVar()
     amountvalue= StringVar()
    #Entries 
     nameentry = Entry(donation, textvariable=namevalue)
     phoneentry = Entry(donation, textvariable=phonevalue)
     amountentry = Entry(donation, textvariable=amountvalue)
    # Packing the Entries
     nameentry.grid(row=1, column=3)
     phoneentry.grid(row=2, column=3)
     amountentry.grid(row=3, column=3)
    #Submit Button
     Button(donation, text="Submit", command= getvals).grid(row=6, column=3)
#Missing people report        
def Missing():
    def response():
        l1=v1.get()
        l2=v2.get()
        l3=v3.get()
        mydb = mysql.connector.connect(host="localhost",user="root",password="Manash@23",database="pythonproject1")
        mycursor = mydb.cursor()

        sql = "INSERT INTO ReportMissingPeople (name,age,gender) VALUES (%s, %s, %s)"
        val = (l1,l2,l3)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        print("Response has been recorded")
    missing=Toplevel(root)
    missing.geometry("380x260")
    Label(missing, text="Missing People Report",font="bold 20").grid(row=0, column=3)
    #Name
    l1=Label(missing, text="Full Name")
    l2=Label(missing, text="Age")
    l3=Label(missing, text="Gender")
    #Pack
    l1.grid(row=1, column=2)
    l2.grid(row=2, column=2)
    l3.grid(row=3, column=2)
    #Variable
    v1 = StringVar()
    v2 = StringVar()
    v3= StringVar()
    #Entries
    l1entry = Entry(missing, textvariable=v1)
    l2entry = Entry(missing, textvariable=v2)
    l3entry = Entry(missing, textvariable=v3)
    #Packing Entries
    l1entry.grid(row=1, column=3)
    l2entry.grid(row=2, column=3)
    l3entry.grid(row=3, column=3)
    #Submit Button
    Button(missing, text="Submit", command= response).grid(row=6, column=3)
    ##Supply information 
def supply():
    file = open("Supply.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    print(rows)
    file.close()

    # Dead people details
def Details_of_Dead_People():
    file = open("Dead People.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    print(rows)
    file.close()
#Home buttons
b1= Button(M_Frame,font=("goudy old style",15,"bold"),bg="#E1E426",fg="blue",text="Donate",cursor="hand2",command=donationmenu).place(x=20,y=5,width=300,height=40)
b2= Button(M_Frame,font=("goudy old style",15,"bold"),bg="#E1E426",fg="blue",text="Supply",cursor="hand2",command=supply).place(x=340,y=5,width=300,height=40)
b3= Button(M_Frame,font=("goudy old style",15,"bold"),bg="#E1E426",fg="blue",text="Details of Dead People",cursor="hand2",command=Details_of_Dead_People).place(x=660,y=5,width=300,height=40)
b4= Button(M_Frame,font=("goudy old style",15,"bold"),bg="#E1E426",fg="blue",text="Report Missing People",cursor="hand2",command=Missing).place(x=980,y=5,width=300,height=40)

root.mainloop()