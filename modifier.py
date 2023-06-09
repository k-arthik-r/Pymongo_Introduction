import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.student
collection = db.CSE

# we can use modifier to select based on conditions

# get all collection whose grade is greater than 9
query = {'grade' : {"$gt" : 9}}
for index in collection.find(query, {"_id" : 0}):
    print(index)

# get all collection whose grade is less than 9.8
querya = {'grade' : {"$lt" : 9.8}}
for index in collection.find(querya, {"_id" : 0}):
    print(index)

# get all collection whose grade is greater than or equal to 9
queryb = {'grade' : {"$gte" : 9}}
for index in collection.find(queryb, {"_id" : 0}):
    print(index)

# get all collection whose grade is less than or equal to 9.8
queryc = {'grade' : {"$lte" : 9.8}}
for index in collection.find(queryc, {"_id" : 0}):
    print(index)


# get all collection whose names first letter is greater than or equal to K alphabetically. its case sensitive
queryd = {'name' : {"$gt" : 'K' }}
for index in collection.find(queryd, {"_id" : 0}):
    print(index)

# get all collection whose names first letter is lesser than or equal to K alphabetically. its case sensitive
querye = {'name' : {"$lt" : 'K'}}
for index in collection.find(querye, {"_id" : 0}):
    print(index)

# Note- youy can also pass regular expression as parameter for the query
