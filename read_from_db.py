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
                         + '@watcharaphat.com/twitter_db')
    db = client['twitter_db']

    if(len(sys.argv) < 2):
        print "usage: python read_from_db [collection_name]"
        sys.exit()

    collection = db[sys.argv[1]]

    cursor = collection.find(
        {},
        {"text": 1, "_id": 0}
    )

    i = 0
    for document in cursor:
        if (i < 10000):
            print dumps(document, ensure_ascii=False)
            i = i + 1
        else:
            sys.exit()
