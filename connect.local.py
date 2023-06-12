import pymongo

# Connecting to mongodb local. client is a element used to access the mongodb and set connections.
# MongoClient takes "connection string" as its parameter.
client = pymongo.MongoClient("mongodb://localhost:27017")
print(client) # Provides connection proof.

# Creating a database, db as database instence
db = client["student"]

# creating a collection
collection = db["CSE"]


# it will try to search for 'CSE' collection or 'student' database in local machine if not found then it will create a new one with the name as given by the user.

# Even after you create a database and collection the db will not be active and wont appear in the compass until a entry is made in that collection the dictionary element is created to insert that entry.

dictionary = {
    "_id":"4VV21CS073",
    'name':'chinmaya',
    'grade': 9.5
}

collection.insert_one(dictionary)

# after this a databse with collection CSE must have been created.

# Enter Mongo db provides a Hirarchy where client is used to create a database, databse contains collection of collections, and each collection contain n number of inputs.
#as many time you run the same file the same copy in added into the database.