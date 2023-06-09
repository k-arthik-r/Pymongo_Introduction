import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client["student"]
collection = db["CSE"]

#sort() takes in two parameter one is fieldname and other is order.

# it will arrange the names in ascending order
query = collection.find().sort("name")
for x in query:
    print(x)


# it will arrange the names in ascending order
queryb = collection.find().sort("name", 1)
for x in queryb:
    print(x)


# it will arrange the names in descending order
querya = collection.find().sort("name", -1)
for x in querya:
    print(x)

# Ascending = 1 and Descnding = -1