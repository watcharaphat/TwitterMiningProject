from mongo_auth import *
import json
from pymongo import MongoClient
from bson.json_util import dumps

if __name__ == '__main__':

    client = MongoClient('mongodb://' + MONGO_USERNAME + ':' + MONGO_PASSWORD
                         + '@watcharaphat.com')
    db = client['twitter_db']
    collection = db['train_tweets']

    with open('bad_tweet_pre.txt') as f:
        content = f.readlines()

    processed_list = [line.decode('utf-8').strip('\n') for line in content]

    for string in processed_list:
        collection.insert(
            {
                "text": string,
                "label": "pos"
            }
        )
        print "inserted: %s" % string
