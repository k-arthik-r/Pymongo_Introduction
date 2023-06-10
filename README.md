<div align="center">
  <h1>Pymongo Introduction</h1>
</div>
    
 <div align='center'>
       <a><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" /></a> &nbsp;
        <a><img src="https://img.shields.io/badge/Pymongo-3CB043?style=for-the-badge&logo=python&logoColor=ffdd54" /></a> &nbsp;
       <a><img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white" /></a> &nbsp;
</div>

--------------------------
  
A Repository created to describe the usage of pymongo a Python-MongoDB driver to connect, insert, select, update and delete Documents from MongoDB database.

--------------------------

## Installation

Install pymongo using pip

```bash
  pip install pymongo
```

Or visit [Here](https://pypi.org/project/pymongo/) For Manual Download
 
 ------------------------
    
## Requirements
* Python 3.11
* pip install pymongo==3.7.2 - MongoDB Python Driver
* MongoDB 4.0.4 - Database Server
* (Optional)MongoDB Compass 1.16.3 - To view database

 --------------------------
    
## Imports

Import the package

```bash
  import pymongo
```

----------------------------

## Making a Connection with MongoClient

The first step when working with PyMongo is to create a MongoClient to the running mongod instance. Doing so is easy:

```bash
from pymongo import MongoClient
client = MongoClient()
```

The above code will connect on the default host and port. We can also specify the host and port explicitly, as follows:

```bash
client = MongoClient('localhost', 27017)
```

Or use the MongoDB URI format:
```bash
client = MongoClient('mongodb://localhost:27017/')
```
-----------------------

## Getting a Database

A single instance of MongoDB can support multiple independent databases. When working with PyMongo you access databases using attribute style access on MongoClient instances:

```bash
db = client.test_database
```

If your database name is such that using attribute style access won’t work (like test-database), you can use dictionary style access instead:

```bash
db = client['test-database']
```

----------------------

## Getting a Collection
A collection is a group of documents stored in MongoDB, and can be thought of as roughly the equivalent of a table in a relational database. Getting a collection in PyMongo works the same as getting a database:
```bash
collection = db.test_collection
```
or (using dictionary style access):
```bash
collection = db['test-collection']
```
An important note about collections (and databases) in MongoDB is that they are created lazily - none of the above commands have actually performed any operations on the MongoDB server. Collections and databases are created when the first document is inserted into them.

----------------------

## Query Code

* [Connect](connect.py)
* [Insert](insert.py)
* [Select](find.py)
* [Update](update.py)
* [Delete](delete.py)
* [DropCollection](dropcollection.py)
* [Modifiers](modifier.py)
* [Sort](sort.py)
* [Limit](limit.py)
* [MetaData](meta.py)

-----------------------

## Database











