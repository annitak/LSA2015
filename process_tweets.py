import sys
import re
import operator

def process_tweets(inputFile, outputFile):
    """Read and parse data, get tweets"""
    rawtweets = {}   #{category: speakers of this category}
    positives = {}
    negatives ={}
    o = open(outputFile, 'w')

    for line in open('positive-words.txt'):
        positives[line.strip()] = set()
    for line in open('negative-words.txt'):
        negatives[line.strip()] = set()
    
    posList = list(positives)
    negList = list(negatives)
    posDict = {}
    negDict = {}

    for line in open(inputFile):
        userid, tweet, statusid, date, zero1, zero2 = line.split('\t')
        tweet = tweet.lower()
        if tweet not in rawtweets:
            rawtweets[tweet] = set()

    for tweet in rawtweets:
        newtweet = ""
        line = tweet.split()
        for w in line:
            if re.search("http", w):
                w= ""
            if w[:1] == "#" or w[:1] == "@":
                w = w[1:] + " "
            word =""           
            for c in list(w):  
                if c == ',' or c == '.' or c == '!' or c == '?' or c == ';' or c == ':' or c == "'" or c== '"' or c== "/":
                    word += " "          
                if c != ',' and c != '.' and c != '!' and c != '?' and c != ';' and c != ':' and c != "'" and c!= '"' and c!= "/":
                    word += c
            w = word
            newtweet += w + " "

        cleantweet = newtweet.rstrip('\n').split(' ')                

        posValue = 0
        negValue = 0

        for word in cleantweet:
            if word.strip() in positives:
                posValue += 1
		if word.strip() in posDict:
			posDict[word.strip()] += 1
		else:
			posDict[word.strip()] = 1
            if word.strip() in negatives:
                negValue += 1
		if word.strip() in negDict:
			negDict[word.strip()] += 1
		else:
			negDict[word.strip()] = 1
	
            
            printline = word + ' ' + str(posValue) +  ' ' + str(negValue) + '\n' 
         #   print printline
	


        total = posValue - negValue

        #processed_tweet = cleantweet + '\t' + str(posValue) + '\t' + str(negValue) + '\t' + str(total)
        
        o.write(newtweet + '\t' + str(posValue) + '\t' + str(negValue) + '\t' + str(total) + '\n' )   

    #   Sort words in pos and neg dictionaries by ascending count and print
    posKeys = sorted(posDict.items(), key=operator.itemgetter(1), reverse = True)
    negKeys = sorted(negDict.items(), key=operator.itemgetter(1), reverse = True)
    print (posKeys)
    print ('\n\n\n')
    print (negKeys)

    o.close()

if __name__=='__main__':
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    process_tweets(inputFile, outputFile)  
