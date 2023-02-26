from pymongo import MongoClient
import json
import os

# connecting to mongo client using pymongo
mongo_key = os.getenv('DB')

client = MongoClient(mongo_key)

db = client['Cookathon']

collection = db['Cookathon']
collection_user = db['User']

# populate with parsed .csv data as JSON
def populate_db():
    f = open("dump.json")

    json_data= json.load(f)
    collection.insert_many(json_data)

# send query conditions to the db
def query_db(query: dict):
    return collection.find(query)



