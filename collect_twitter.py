#Import the necessary methods from tweepy library
from api_keys import *
from mongo_auth import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from pymongo import MongoClient

#This is a basic listener that just prints received tweets to stdout.
class MyListener(StreamListener):

    def on_data(self, data):
        try:
            tweet = json.loads(data)
            print "%s %s" % (tweet['created_at'], tweet['text'])
            client = MongoClient('mongodb://' + MONGO_USERNAME + ':'
                                 + MONGO_PASSWORD + '@watcharaphat.com')
            db = client['twitter_db']
            collection = db['twitter_collection']
            collection.insert(tweet)

            return True

        except BaseException as e:
            print("--> Error on_data: %s" % str(e))
            pass
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_stream = Stream(auth, MyListener())

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    twitter_stream.filter(track=['porn', 'sex', '#porn', '#sex'])
