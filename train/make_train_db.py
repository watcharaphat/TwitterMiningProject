from mongo_auth import *
import pymongo
import json
from pymongo import MongoClient
from bson.json_util import dumps
import unicodedata
import string
import sys

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    client = MongoClient('mongodb://' + MONGO_USERNAME + ':' + MONGO_PASSWORD
                         + '@watcharaphat.com')
    db = client['twitter_db']
    collection = db['train_tweets']

    cursor = collection.find(
        {},
        {"text": 1, "label": 1, "_id": 0}
    )

    i = 0

    print '['
    for document in cursor:
        if i < 19999:
            print "%s," % dumps(document, ensure_ascii=False)
            i = i + 1
        elif i == 19999:
            print dumps(document, ensure_ascii=False)
            print ']'
            sys.exit()
