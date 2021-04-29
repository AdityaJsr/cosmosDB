import azure.cosmos.cosmos_client as cosmos_client
from decouple import config
import os
import sys

url = config("url")
key = config("key")
database_name = config("database_name")
container_name = config("container_name")

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