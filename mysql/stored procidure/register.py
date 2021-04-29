
"""
Title - Write a Python program to create a stored procedure in by connecting the sample.js file.
Author name - Aditya Kumar
Ceation time - 26 April ‎2021 ‏‎
Modified time - ‎‎‎05 ‎April ‎2021‎

""" 
#All the imports required to run the script.
import azure.cosmos.cosmos_client as cosmos_client
from decouple import config
import os
import sys

#Credentials kept in a secure .env file.
url = config("url")
key = config("key")
database_name = config("database_name")
container_name = config("container_name")

#Using context manager to open the .JS file
with open('D:/vs studio/bridgeLabz/week 8/mysql/stored procidure/sample.js') as file:
    file_contents = file.read()

sproc = {
    'id': 'spCreateToDoItem',
    'serverScript': file_contents,
}
client = cosmos_client.CosmosClient(url, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)
created_sproc = container.scripts.create_stored_procedure(body=sproc)