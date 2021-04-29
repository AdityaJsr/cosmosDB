"""
Title - Write a Python program to to perform CRUD operations on the mongodb api (azure).
Author name - Aditya Kumar
Ceation time - 23 April ‎2021 ‏‎
Modified time - 29 ‎April ‎2021‎

""" 
#All the imports required to run the script.
import pymongo
from decouple import config

'''
Connection to azure mongodb API.
Credentials kept in a secure .env file.
'''

try:

    client = pymongo.MongoClient(config("uri"))

    mydb = client[config("db")]

    mycol = mydb[config("mycol")]
except Exception as e:
    print("Could not connect to the database", e)

'''
Function:
        The function user_input() is to take user input to add items in DB.
Arguments:
        none
Returns:
        id,name,age,email_id : These items are returned to the insert() function.
Errors:
        none.
'''
def user_input():
    try:
        id = input("Enter the unique id : ")
        name = input("Enter the name of the person : ")
        age = input("Enter the age of the person : ")
        email_id = input("Enter the email_id of the person : ")
        return(id,name,age,email_id)
    except Exception as e:
        print("Invalid inputs")

'''
Function:
        The function insert() is to commit user input to the container in DB.
Arguments:
        user_input() :  The user input function is called to take input for new entry.
Returns:
        none.
Errors:
        none.
'''
def insert():
    try:
        id, name , age, email_id,  = user_input()
        names = {
            "_id" : id,
            "name" : name,
            "age" : age,
            "email_id" : email_id
        }
        mycol.insert_one(names)
    except Exception as e:
        print("An exception has occured", e)

'''
Function:
        The function display() is to depict data retrived from mongo DB.
Arguments:
        none.
Returns:
        none.
Errors:
        none.
'''

def display():
    try:
        print("Loading Please wait....")
        for items in mycol.find():
            id1 = items['_id']
            name1 = items['name']
            age1 = items['age']
            email_id1 = items['email_id']
            print("id = " ,id1, "name = " ,name1, "age = " ,age1, "email_id = " ,email_id1,"\n")
    except Exception as e:
        print("Exception occured", e)

def delete():
    try:
        email_id = input("Enter the email id of the user you want to remove : ")
        query = { "email_id": email_id }
        deleted_val=mycol.delete_one(query)
        print(deleted_val.deleted_count, "Deleted document successfull")
    except Exception as e:
        print("Exception occured as", e)
'''
Function:
        The function update() is to update a single item identified byuser input to the container in DB.
Arguments:
        none.
Returns:
        none.
Errors:
        none.
'''
def update():
    try:
        email_id = input("Enter the email id of the user you want to update : ")
        update = input("Enter the updated name : ")
        query = { "email_id": email_id }
        update_val ={"$set": { "name": update }}
        mycol.update_one(query, update_val)
        print(update_val, "Updated document successfull")
    except Exception as e:
        print("Exception occured as", e)
'''
Function:
        The function find() is to a specific single value from mongo DB.
Arguments:
        none.
Returns:
        none.
Errors:
        none.
'''
def find():
    try:
        email_id = input("Enter the email id of the user you want to find : ")
        query = { "email_id": email_id }
        mycol.find_one(query)
        print("Updated document successfull")
    except Exception as e:
        print("Exception occured as", e)

'''
Function:
        The function main() is the main file for CRUD.py.
Arguments:
        none.
Returns:
        none.
Errors:
        none.
'''

def main():
    try:
        ch = int(input("\nEnter the operation you want to perform \n1) Display data :\
            \n2) Insert data : \n3) Delete data : \n4) Update data : \nEnter your choice here : "))
        if ch == 1:
            display()
        elif ch == 2:
            insert()
        elif ch == 3:
            delete()
        elif ch == 4:
            update()
        elif ch == 5:
            find()
        else:
            print("Enter a valid option : ")
    except Exception as e:
        print("Exception occured as", e)

if __name__ == "__main__":
    main()