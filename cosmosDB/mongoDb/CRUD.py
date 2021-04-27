import pymongo
from decouple import config

client = pymongo.MongoClient(config("uri"))

mydb = client[config("db")]

mycol = mydb[config("mycol")]

# Insert data:
def user_input():
    print("I am working")
    nameid = input("Enter the name id of the person : ")
    name = input("Enter the name of the person : ")
    age = input("Enter the age of the person : ")
    return(nameid,name,age)

def insert():
    nameid, name , age = user_input()
    name = {
        "nameid" : nameid,
        "name" : name,
        "age" : age
    }
    mycol.insert_one(name)

def display():
    print("Loading Please wait....")
    for items in mycol.find():
        print(items)


def main():
    ch = input("\nEnter the operation you want to perform \n1) Display data :  \n2) Insert data : \n")
    if ch == "1":
        display()
    elif ch == "2":
        insert()

if __name__ == "__main__":
    main()