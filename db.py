import mysql.connector


try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",    
        database="tea"
    )
    print("Database connected successfully")

except Exception as e:
    print(e)

cursor = db.cursor()

#-----------Admin--------------------
def loginAdmin(data):
    try:
        cursor.execute("SELECT * FROM admin_account WHERE admin_username=%s AND admin_password=%s", data)
        return cursor.fetchone()
    except Exception as e:
        print(e)



#-----------user--------------------

def registerUser(data):

    try:                                                                      
        cursor.execute("insert into user (name,email,password,mobile) values(%s,%s,%s,%s)",data)
        db.commit()  
        return True
    except Exception as e:
        print("error",e)
        return False

def loginUser(data):
    try:
        cursor.execute("SELECT * FROM user WHERE name=%s AND password=%s", data)
        return cursor.fetchone()
    except Exception as e:
        print(e)

def veiwUser():
    try:
        cursor.execute("SELECT * FROM user")
        return cursor.fetchall()
    except Exception as e:
        print(e)

def singleUser(id):
    try:
        cursor.execute("SELECT * FROM user WHERE id=%s", id)
        return cursor.fetchone()
    except Exception as e:
        print(e)

def deleteUser(id):
    try:
        cursor.execute("DELETE FROM user WHERE id=%s", id)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False

def updateUser(data):
    try:
        cursor.execute("UPDATE user SET name=%s, email=%s, password=%s WHERE id=%s", data)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
#----------------menu-------------------

def addMenu(data):
    try:
        cursor.execute("insert into coffee_category (item_name,category_id,price,image,description) values (%s, %s, %s, %s, %s)", data)
        db.commit()
        return True
    except Exception as e:
        print(e)

def viewMenu():
    try:
        cursor.execute("SELECT * FROM coffee_category")
        return cursor.fetchall()
    except Exception as e:
        print(e)

def singleMenu(id):
    try:
        cursor.execute("SELECT * FROM coffee_category WHERE coffee_id=%s", (id,))
        return cursor.fetchone()
    except Exception as e:
        print(e)

def deleteMenu(id):
    try:
        cursor.execute("DELETE FROM coffee_category WHERE coffee_id=%s", (id,))
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False

def updateMenu(data):
    try:
        cursor.execute("UPDATE coffee_category SET item_name=%s,category_id=%s,price=%s,image=%s,description=%s WHERE coffee_id=%s", data)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False

#------------employee------------------

def addEmployee(data):
    try:
        cursor.execute("INSERT INTO employee_account (emp_name, emp_email, emp_password) VALUES (%s, %s, %s)", data)
        db.commit()
        return True
    except Exception as e:
        print(e)

def viewEmployee():
    try:
        cursor.execute("SELECT * FROM employee_account")
        return cursor.fetchall()
    except Exception as e:
        print(e)

def singleEmployee(id):
    try:
        cursor.execute("SELECT * FROM employee_account WHERE id=%s", id)
        return cursor.fetchone()
    except Exception as e:
        print(e)

def deleteEmployee(id):
    try:
        cursor.execute("DELETE FROM employee_account WHERE id=%s", id)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False

def updateEmployee(data):
    try:
        cursor.execute("UPDATE employee_account SET emp_name=%s, emp_email=%s, emp_password=%s WHERE id=%s", data)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
#------------order------------------

# def addOrder(data):
#     try:
#         cursor.execute("INSERT INTO orders (user_id, item_id, quantity) VALUES (%s, %s, %s)", data)
    
def viewOrder(data):
    print("id is ",data)
    data=int(data)
    try:
        cursor.execute("SELECT * FROM `orders` WHERE bill_id=%s", (data,))
        return cursor.fetchone()
    except Exception as e:
        print(e)
def viewAllOrder():
    try:
        cursor.execute("SELECT * FROM `orders`")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
    

import datetime

now = datetime.datetime.now()
d = now.strftime("%Y-%m-%d %H:%M:%S")
print(d)
def add_payment(data):
    try:
        cursor.execute('insert into orders (payment,method, contact,email,date) values (%s,%s,%s,%s,%s)',(data))
        db.commit()
        return True
    except Exception as e:
        print("Error is",e)
        return False
    
    
    
    






