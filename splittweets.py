import sys
import re

def get_tweets(filename):
    """Read and parse data, get tweets"""
    rawtweets = {}   #{category: speakers of this category}
    finaltweets = {}

    for line in open(filename):
        userid, tweet, statusid, date, zero1, zero2 = line.split('\t')
        
        if tweet.lower() not in rawtweets:
            rawtweets[tweet.lower()] = set()

    for tweet in rawtweets:
        newtweet = ""
        line = tweet.split()
        for w in line:
            if re.search('^http', w):
                newtweet += " "
            elif re.search('^#', w):
                newtweet += w[1:] + " "
            elif re.search(',', w): 
                word =""
                for c in list(w):
                    if c!=",":
                        word += c
                newtweet += word + " "
            elif re.search('.', w): 
                word =""
                for c in list(w):
                    if c!=".":
                        word += c
                newtweet += word + " "            
            elif re.search('?', w): 
                word =""
                for c in list(w):
                    if c!="?":
                        word += c
                newtweet += word + " "            
            elif re.search('!', w): 
                word =""
                for c in list(w):
                    if c!="!":
                        word += c
                newtweet += word + " "
            elif re.search("'", w):
                word =""
                for c in list(w):
                    if c!="'":
                        word += c
                newtweet += word + " "
            elif re.search(':', w): 
                word =""
                for c in list(w):
                    if c!=":":
                        word += c
                newtweet += word + " "
            elif re.search(';', w): 
                word =""
                for c in list(w):
                    if c!=";":
                        word += c
                newtweet += word + " "

            else:
                newtweet += w + " "
        finaltweets[newtweet] = set()                


    print "Tweets found"

    for c in finaltweets:
        print c   


if __name__=='__main__':
    filename = sys.argv[1]
    get_tweets(filename)  
