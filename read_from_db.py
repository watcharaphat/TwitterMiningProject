from mongo_auth import *
import pymongo
import json
from pymongo import MongoClient
from bson.json_util import dumps
import unicodedata
import string

if __name__ == '__main__':
    client = MongoClient('mongodb://' + MONGO_USERNAME + ':' + MONGO_PASSWORD
                         + '@watcharaphat.com')
    db = client['twitter_db']
    collection = db['twitter_train']

    cursor = collection.find(
        {},
        {"text": 1, "_id": 0}
    )

    printable = set(string.printable)

    for document in cursor:
        s = dumps(document)
        print filter(lambda x: x in printable, s)
