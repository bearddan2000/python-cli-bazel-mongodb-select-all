import pymongo
import pprint

client = pymongo.MongoClient('db', 27017)

db = client.test

print("[INFO] Before Insert empty collection")
pprint.pprint(db.list_collection_names())

shiv = {"name": "shiv"}

collection = db.weapon

collection.insert_one(shiv)

print("[INFO] After Insert 1 collection")
pprint.pprint(db.list_collection_names())

print("[INFO] Select all")
for item in collection.find():
    pprint.pprint(item)

collection.create_index(
    [
        ("name", pymongo.ASCENDING)
    ],
    unique=True
)
pprint.pprint(sorted(list(collection.index_information())))
