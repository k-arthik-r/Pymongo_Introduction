import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.student
collection = db.CSE

# When to want to fetch the first entry of The Database and print it.
data = collection.find_one()
print(data)


# This will return the the first document in which name is Karthik you can use any attribute insted of name, since find_one it will return only one document.
datay = collection.find_one({ 'name' : "Karthik"})
print(datay)

# if you use find_one inside for loop it will return only the attributes of the first entry.


# find() always return cursor object, iterate through it to fetch data

# When you want to print every entry present in the database use find() inside for loop. 
# inside the same program during same runtime the first find() will fetch first entry and the recurring find() will fetch next recurring entry.
# calling it N times will fetch all the entries form the database until its all in the same runtime of the program.
# always use find() inside forloop else it will return only object not data.
for datax in collection.find():
    print(datax)


# when you want to display data which satisfies only a specific condition use sttribute parameter inside find()
# it will return all the document with name as Karthik
for dataz in collection.find({ 'name' : "Karthik"}):
    print(dataz)



# another parameter of find() or find_many() method is an object describing which fields to include in the result.
# 0 = not required and 1 = required
# note - id, by default will be 1, and all 0 and 1 rule will be not applicable as a part for others attribute in the document
# if you make any attribute as 1 then all other attribute will be 0 and vice versa, bute this will not be applicabe for id.

# return first collection without printing the id
dataa = collection.find_one({}, {"_id" : 0})
print(dataa)


# return first collection without printing the id and name
datab = collection.find_one({}, {"_id" : 0, 'name' : 0})
print(datab)


# return first collection without printing the name whose name is Karthik
datac = collection.find_one({'name' : "Karthik"}, {"_id" : 0, 'name' : 0})
print(datac)
# first `{}` for condition and second '{}' for include or not


# The Same can be applicable also for find() 

# return all collection without printing the id
for datad in collection.find({}, {"_id" : 0}):
    print(datad)


# return all collection without printing the id and name
for datae in collection.find({}, {"_id" : 0, 'name' : 0}):
    print(datae)


# return all collection without printing the name whose name is Karthik
for dataf in collection.find({'name' : "Karthik"}, {"_id" : 0, 'name' : 0}):
    print(dataf)

# Note - cannot declare two attribute as 0 and 1 at the same time.
