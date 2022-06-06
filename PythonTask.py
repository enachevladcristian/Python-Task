import re
from os import system
import mysql.connector
# Making a Database
#con = mysql.connector.connect(host="localhost", user="root", password="")
#mycursor = con.cursor()
#mycursor.execute("CREATE DATABASE EmployeeFinal")

con = mysql.connector.connect(host="localhost", user="root", password="",database="employeefinal")
mycursor = con.cursor()

#making a connection
#mycursor.execute("CREATE TABLE empdata(Id INT(11) PRIMARY KEY,f_name VARCHAR(1000),l_name VARCHAR(1000),"
                #"age INT(11), job TEXT(1000), Salary BIGINT(20), Bonus BIGINT(20))")
# Functia Add_Employ
def Add_Employ():
    print("{:>60}".format("-->>Add Employee Record<<--"))
    Id = input("Enter employee record Id: ")
    if (check_employee_id(Id)== True):
        print("Employee ID already exists\n Try again...")
        press = input("Press any key to continue")
        Add_Employ()
    f_Name = input("Enter employee name: ")
    l_Name = input("Enter employee last name")
    #checking if Employee name exists or not
    if (check_employee_name(f_Name)== True):
        print("Employee already exists\n Try again...")
        press = input("Press any key to continue")
        Add_Employ()
    age = input("Enter employee age: ")
    Job = input("Enter employee Job: ")
    Salary = input("Enter employee salary: ")
    Bonus = input("Entere employee Bonus: ")
    data = (Id, f_Name,l_Name, age, Job,Salary, Bonus)
    #Tabelul Employee (empdata)
    sql ='insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()

    #Executam Queryul SQL
    c.execute(sql,data)
    #Facem commit acestei metode pentru a schimba in tabel
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any key to continue")
    menu()

def check_employee_name(employee_name):
    # We create a query to select all rows from employee table
    sql = 'select * from empdata where f_Name=%s'
    # now we make the cursor buffered to make the rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_name,)
    # Execute the sql query
    c.execute(sql, data)
    # rowcount method to find number of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def check_employee_id(employee_id):
    # We create a query to select all rows from employee table
    sql = 'select * from empdata where Id=%s'
    # now we make the cursor buffered to make the rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)
    # Execute the sql query
    c.execute(sql, data)
    # rowcount method to find number of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def Display_Employ():
    print("{:>60}".format("-->> Display the existing employees <<--"))
    # A query that selects all rows from employee Table
    sql = 'select * from empdata'
    c = con.cursor()
    # Execute the Sql query
    c.execute(sql)

    # Fetching all the details of the Employees in the Employee table
    r = c.fetchall()
    for i in r:
        print("Employee Id:", i[0])
        print("Employee First Name:", i[1])
        print("Employee Last Name:", i[2])
        print("Employee age:", i[3])
        print("Employee job:", i[4])
        print("Employee Salary:", i[5])
        print("Employee Bonus:", i[6])
        print("Employee Total Salary: ", i[5]+i[6])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()
    #Function to check if employee with given name exists or not

def Apply_bonus():
    print("{:>60}".format("-->> Apply bonus to the employee <<--\n"))
    Id = input("Enter Employee Id: ")
    if (check_employee_id(Id) == False):
        print("Employee Record Does Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Amount = int(input("Enter Increase Bonus: "))
        sql = 'select Salary from empdata where Id=%s'
        data = (Id,)
        c = con.cursor
        c.execute(sql, data)
        r = c.fetchone()
        t = r[0] + Amount
        sql = 'update empdata set Salary=%s where Id =%s'
        d = (t, Id)
        c.execute(sql, d)
        con.commit()
        print("Bonus was applied")
        press = input("Press any key to continue")
        menu()

def Remove_Employ():
    print("{:>60}".format("-->> Remove Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if (check_employee_id(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        # query to delete Employee from empdata table
        sql = 'delete from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql, data)

        # commit() method to make changes in the empdata table
        con.commit()
        print("Employee Removed")
        press = input("Press Any key To Continue..")
        menu()


def Search_Employ():
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        # query to search Employee from empdata table
        sql = 'select * from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql, data)

        # fetching all details of all the employee
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email Id: ", i[2])
            print("Employee Phone No.: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary: ", i[6])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()
def menu():
    system("cls")
    print("{:>60}".format("**************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("*************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Remove Employee Record")
    print("5. Search Employee Record")
    print("6. Apply Bonus")
    #print("7. Display Department")
    print("8. Exit\n")
    print("{:>60}".format("-->> Choose options : [1/2/3/4/5/6/7/8] <<--"))

    ch = int(input("Enter your choice: "))
    if ch == 1:
        system("cls")
        Add_Employ()
    elif ch == 2:
        system("cls")
        Display_Employ()
    elif ch == 3:
        system("cls")
        Update_Employ()
    elif ch == 4:
        system("cls")
        Remove_Employ()
    elif ch ==5:
        system("cls")
        Search_Employ()
    elif ch == 6:
        system("cls")
        Apply_bonus()
    elif ch == 8:
        system("cls")
        print("{:>60}".format("Have a nice day"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press any key to continue")
menu()