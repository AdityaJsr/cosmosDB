"""
Title - Write a Python program to create a user defined function in by connecting the age.js file.
Author name - Aditya Kumar
Ceation time - 26 April ‎2021 ‏‎
Modified time - 29 ‎April ‎2021‎

"""

#All the imports required to run the script.
import azure.cosmos.cosmos_client as cosmos_client
from decouple import config
import json

#Credentials kept in a secure .env file.

url = config('url')
key = config('key')
database_name = config('database_name')
container_name = config('container_name')

#Using context manager to open the .JS file

with open('D:/vs studio/bridgeLabz/week 8/mysql/user defined function/age.js') as file:
    file_contents = file.read()
udf_definition = {
    'id': 'name',
    'serverScript': file_contents,
}
#Azure commands to commit the UDFs.

client = cosmos_client.CosmosClient(url, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)
udf = container.scripts.create_user_defined_function(udf_definition)

for item in container.query_items(
    query='SELECT * FROM people WHERE udf.age(people) > 50',
    enable_cross_partition_query=True):    
      print(json.dumps(item, indent=True))