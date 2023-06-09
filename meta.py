import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.student
collection = db.CSE

No_of_DB = client.list_database_names() # Provide names of all the databases in the db connection inside a list
print(No_of_DB)

No_of_Coll = db.list_collection_names() # Provide names of all the Collections in the dtabase student inside a list
print(No_of_Coll)