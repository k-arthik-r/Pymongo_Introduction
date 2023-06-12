from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "<Connection String>"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Program to check Successfull MongoDB Connection

#Or

# import pymongo

# client = pymongo.MongoClient("<MongoDB Atlas Connection String>")
# db = client["<Database_Name>"]
# collection = db["<Collection_Name>"]

# dictionary = {
    # "_id" : "id",
    # "Data" : "Data"
# }

# collection.insert_one(dictionary)