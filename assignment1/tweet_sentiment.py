import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)
    scores = {} # initialize an empty dictionary for sentiment
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    #print scores.get('warmth')

    for line in tweet_file:
        #print line
        js = json.loads(line)
        #print type(js)
        print js.keys()
        tweet_text = js.get('text') if 'text' in js else ''
        tweet_words = tweet_text.split(' ')
        tweet_sentiment = 0.0
        for word in tweet_words:
            tweet_sentiment += scores.get(word) if word in scores else 0.0
            #print '[' + word + '] ' + str(scores.get(word) )
        
        print str(tweet_sentiment)
    #hw()

if __name__ == '__main__':
    main()
