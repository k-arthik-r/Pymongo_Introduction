import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client["student"]
collection = db["CSE"]

# Delete the entire first document which satisfies the condition where name is Akshatha.
collection.delete_one({"name" : "Akshatha"})



# Delete all the document whose grade is less tyhan 9.9
query = {"grade":{"$lt" : 9.9}}
collection.delete_many(query)



# Delete all the document whose grade is 10
x = collection.delete_many({"grade": 10})

deleted = x.deleted_count # To print the number of collection deleted to that point in the database.
print(deleted)



# Delete all the document from the collection
collection.delete_many({})