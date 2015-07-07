# -*- coding: utf-8 -*-
"""Mine tweets from Streaming API"""

from twython import TwythonStreamer
import time
import codecs
import sys
import json
import string
from utilities import ProcessedTweet                    

class CustomStreamer(TwythonStreamer):
    def __init__(self, app_key, app_secret, oauth_token, oauth_token_secret, start_time, maxsecs):
        TwythonStreamer.__init__(self, app_key, app_secret, oauth_token, oauth_token_secret)
        self.userinfo = {}   
        self.start_time = start_time
        self.maxsecs = maxsecs
        print "initialized"
    
    def on_error(self, status_code, tweet):
        print status_code, tweet
        self.disconnect()
        
    def on_success(self, tweet):
        if tweet:
            ptweet = ProcessedTweet()
            success = ptweet.process_raw(tweet, self.userinfo, requiregeo=True)
            if success:
                o.write(ptweet.__str__())
                if ptweet.inreply:
                    orep.write('/'.join([ptweet.user, ptweet.status_id])
                               +': '
                               +'/'.join(ptweet.inreply)+'\n')
        #check if max time has lapsed
        if time.time()-self.start_time>maxsecs:
            self.disconnect()
                    
if __name__=='__main__':
    
    OAUTH_TOKEN = "14656609-IzjpUGipO5uDse1rFr3nXfBvVbX9T4hMHjkAvwA55"
    OAUTH_SECRET = "JYZoOPQK28fFv98d4zZg1OUBqIUKJQ6poQglmioz4"
    CONSUMER_KEY = "JksOBh39nyd95jagJQTZ8Q"
    CONSUMER_SECRET = "kx87N1Ge8iWuzwcWUH55PhUDOFCqBju6UqUtroYFo"

    basename, maxhours = sys.argv[1:3]
    
    maxsecs = float(maxhours)*60*60  #how long to stream
    start_time = time.time()

    o = codecs.open(basename+'.statuses.tsv', 'w', 'utf-8')
    orep = codecs.open(basename+'.replies.txt', 'w', 'utf-8')
    
    stream = CustomStreamer(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET, start_time, maxsecs)
    while time.time()-start_time<maxsecs:
        try:
            stream.statuses.filter(locations='-138, 24, -52, 80') #US and Canada; change bounding box for other locations
        except Exception as e:
            print e
            continue

    oj = open(basename+'.userinfo.json', 'w')
    json.dump(stream.userinfo, oj)
    oj.close()
    
    orep.close()
    o.close()
