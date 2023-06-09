import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client["student"]
collection = db["CSE"]

# update the first document with the data as of given by query.
query = {"name" : "Karthik"} # for recognition and can also use other attribute, since we have used update_one only with first match will be updated.
newquery = {"$set" : {"grade" : 9.9}} # for update

collection.update_one(query, newquery)



# if the stated attribute is not present then it will create one.
querya = {"name" : "Karthik"} # for recognition and can also use other attribute, since we have used update_one only with first match will be updated.
newqueryb = {"$set" : {"gender" : "Male"}} # for update

collection.update_one(querya, newqueryb)



# upadte all the document which staisfies the given condition i.e it will change or create the attribute if required where grade is 9.9
queryb = {"grade" : 9.9} # for recognition and can also use other attribute.
newqueryb = {"$set" : {"grade" : 9.8}} # for update the grade as 9.8 where ever the grade is 9.9

x = collection.update_many(queryb, newqueryb)

modified = x.modified_count # To print the number of collection modified to that point. 
print(modified) 


# Update one only updates the first docuent that satisfies the given condition attribute but update many updates all the document that satisfies the given condition.



# To delete a particular attribute from a document in a collection
queryc = {"_id" : "4VV21CS073"} # for recognition and can also use other attribute.
newqueryc = {"$unset" : {"gender" : ""}} # deletes a particualr attribute from the document, whatever the datatype is it should be replaced with "" its not like its only or strings.
collection.update_many(queryc, newqueryc)