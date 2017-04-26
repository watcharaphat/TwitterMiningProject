from mongo_auth import *
import pymongo
import json
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://' + MONGO_USERNAME + ':' + MONGO_PASSWORD
                         + '@watcharaphat.com')
    db = client['twitter_db']
    collection = db['twitter_train']

    cursor = collection.find({})
    for document in cursor:
        print(document)
