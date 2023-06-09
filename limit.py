import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.student
collection = db.CSE

data = collection.find().limit(3) # Fetch only first 3 document of the collection. 

for index in data:
    print(index)