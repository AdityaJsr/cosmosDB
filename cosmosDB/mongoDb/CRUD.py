import pymongo
from decouple import config

client = pymongo.MongoClient(config("uri"))

mydb = client[config("db")]

mycol = mydb[config("mycol")]

# Insert data:
def user_input():
    id = input("Enter the unique id : ")
    name = input("Enter the name of the person : ")
    age = input("Enter the age of the person : ")
    email_id = input("Enter the email_id of the person : ")
    return(id,name,age,email_id)

def insert():
    id, name , age, email_id,  = user_input()
    names = {
        "_id" : id,
        "name" : name,
        "age" : age,
        "email_id" : email_id
    }
    mycol.insert_one(names)

def display():
    print("Loading Please wait....")
    for items in mycol.find():
        print(items)
        # for item in items:
            # print(type(item))
            # id1 = id,
            # name1 = name,
            # age1 = age,
            # email_id1 = email_id
            # print("id = " ,id1, "name = " ,name1, "age = " ,age1, "email_id = " ,email_id1,"\n")


def main():
    ch = input("\nEnter the operation you want to perform \n1) Display data :  \n2) Insert data : \nEnter your choice here : ")
    if ch == "1":
        display()
    elif ch == "2":
        insert()

if __name__ == "__main__":
    main()