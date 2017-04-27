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

            if not tweet['text'].startswith('RT'):
                print "%s %s" % (tweet['created_at'], tweet['text'])
                collection.insert(
                    {
                        "user": {
                            "screen_name": tweet['user']['screen_name'],
                            "id_str": tweet['user']['id_str']
                        },
                        "time": tweet['created_at'],
                        "text": tweet['text']
                    }
                )

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

    client = MongoClient('mongodb://' + MONGO_USERNAME + ':' + MONGO_PASSWORD
                         + '@watcharaphat.com')
    db = client['twitter_db']
    collection = db['bad_tweets']

    #This line filter Twitter Streams to capture data by the keywords: '
    twitter_stream.filter(languages=["en"],
                          track=['porn', 'sex', 'cock', 'dick', 'blowjob',
                                 'handjob', 'pussy', 'MILF', 'gangbang',
                                 '#porn', '#sex', '#cock', '#dick', '#blowjob',
                                 "#handjob", '#pussy', '#MILF', '#gangbang']
                          )
