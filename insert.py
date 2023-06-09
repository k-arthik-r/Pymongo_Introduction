import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.student
collection = db.CSE

# when you need to insert only one entry into the DB use insert_one() of pymongo

dictionary = {
    '_id' : '4VV21CS073',
    'name' : 'Karthik R',
    'grade' : 9.8
}

data = collection.insert_one(dictionary)
print(data)


# when you need to insert many entry at a time into to the DB create a list of disctionaries and pass it to insert_many() of pymongo

listofdata = [
    {
        '_id' : '4VV21CS011',
        'name' : 'Akshatha',
        'grade' : 9

    },
    {
        '_id' : '4VV21CS117',
        'name' : 'preethi',
        'grade' : 9.6

    },
    {
        '_id' : '4VV21CS018',
        'name' : 'Ananya',
        'grade' : 10

    }
]

info = collection.insert_many(listofdata)
print(info)