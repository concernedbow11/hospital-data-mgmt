import sqlite3
def sqltime(db):
    ch=1
    while choice>0 and choice <6:
        print "\n\n\n\n\t\t\tSQL MENU"
        print "\t\t\t--------"
        print "\n1.Insert patient details into the database\n2.Fetch a patient's details\n3.Modify a patient's details\n4.Delete a patient's details\n5.Display all the records\n6.Exit"
        ch=input("\nEnter your choice: ")
        if ch==1:
            conn = sqlite3.connect(db)
            print "------------------------------------------------------"
            print "\n\nConnection to database established successfully! \n\n"
            print "------------------------------------------------------\n\n"
            print "Enter the details to be added \n\n"
            pno=raw_input("Enter the patient number: ")
            nam=raw_input("Enter the name: ")
            gen=raw_input("Enter the gender: ")
            age=raw_input("Enter the age: ")
            adr=raw_input("Enter the address: ")
            dat=raw_input("Enter the date of admission: ")
            doc=raw_input("Enter the consultant's name: ")
            stri="INSERT INTO HOSPITAL_RECORDS VALUES ("+pno+",'"+nam+"','"+gen+"',"+age+",'"+adr+"','"+dat+"','"+doc+"');"
            conn.execute(stri)
            conn.commit()
            print "Executed properly"
            conn.close()
        elif ch==2:
            conn = sqlite3.connect(db)
            print "------------------------------------------------------"
            print "\n\nConnection to database established successfully! \n\n"
            print "------------------------------------------------------\n\n"
            pno = raw_input("Enter the patient number to locate: ")
            cursor = conn.execute("SELECT PNO,NAME,GENDER,AGE,ADDRESS,DATE_OF_ADMISSION,CONSULTANT from HOSPITAL_RECORDS;") 
            print '\n\n'
            flag=0
            for row in cursor:
                if str(row[0])==pno:
                    print "PNO: ",row[0]
                    print "Name: ",row[1]
                    print "Gender: ",row[2]
                    print "Age: ",row[3]
                    print "Address: ",row[4]
                    print "Date of admission: ",row[5]
                    print "Consultant: ",row[6]
                    flag=1
                    break
            if flag==0:
                print "Entry Not found !!"
            conn.close()
        elif ch==3:
            conn = sqlite3.connect(db)
            print "------------------------------------------------------"
            print "\n\nConnection to database established successfully! \n\n"
            print "------------------------------------------------------\n\n"
            pno=raw_input("Enter the pno of the entry to update: ")
            col=raw_input("Enter which detail to update: ")
            val=raw_input("Enter the new value: ")
            conn.execute("UPDATE HOSPITAL_RECORDS set "+col+" = "+val+" where PNO = "+pno)
            conn.commit()
            cursor = conn.execute("SELECT PNO,NAME,GENDER,AGE,ADDRESS,DATE_OF_ADMISSION,CONSULTANT from HOSPITAL_RECORDS;") 
            print '\n\nUpdated Entry:\n\n'
            for row in cursor:
                if str(row[0])==pno:
                    print "PNO: ",row[0]
                    print "Name: ",row[1]
                    print "Gender: ",row[2]
                    print "Age: ",row[3]
                    print "Address: ",row[4]
                    print "Date of admission: ",row[5]
                    print "Consultant: ",row[6]
                    break
            print "Executed properly"
            conn.close()
        elif ch==4:
            conn = sqlite3.connect(db)
            print "------------------------------------------------------"
            print "\n\nConnection to database established successfully! \n\n"
            print "------------------------------------------------------\n\n"
            pno=raw_input("Enter the pno of the entry to delete: ")
            conn.execute("DELETE from HOSPITAL_RECORDS where PNO = "+pno+";")
            conn.commit()
            print "\n\nDeletion Successful!\n"
        elif ch==5:
            conn = sqlite3.connect(db)
            print "------------------------------------------------------"
            print "\n\nConnection to database established successfully! \n\n"
            print "------------------------------------------------------\n\n"
            print "Printing all the entries: \n\n\n"
            cursor = conn.execute("SELECT PNO,NAME,GENDER,AGE,ADDRESS,DATE_OF_ADMISSION,CONSULTANT from HOSPITAL_RECORDS;")
            flag=0
            for row in cursor:
                print "PNO: ",row[0]
                print "Name: ",row[1]
                print "Gender: ",row[2]
                print "Age: ",row[3]
                print "Address: ",row[4]
                print "Date of admission: ",row[5]
                print "Consultant: ",row[6]
                print "-------------------------\n-------------------------\n"
                flag=1
            if flag==0:
                print "The database  is empty!!!"
            print "\n\nExecuted Successfully..."
            conn.close()
        else:
            return

def sqlmake(db):
    conn = sqlite3.connect(db)
    conn.execute('''CREATE TABLE HOSPITAL_RECORDS (PNO INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,GENDER TEXT,AGE INT NOT NULL,ADDRESS CHAR(50),DATE_OF_ADMISSION DATE NOT NULL,CONSULTANT TEXT);''')
    print "Table created successfully!!"
    conn.close()

print "\n\n\n"
choice=2
while(choice>=1 and choice<4):
    print "Would you like to: \n1. Connect to a database \n2. Create a new database for your hospital records?\n3. Exit\n\nChoice: "
    choice=int(input())
    if choice==1:
        db=raw_input("Enter the name of your database: ")
        sqltime(db)
    elif choice==2:
        db=raw_input("Enter the name of your new database: ")
        sqlmake(db)