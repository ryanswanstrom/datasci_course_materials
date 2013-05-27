import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary for sentiment
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    # a dict to hold words(key) not in the sentiment file and 
    # a list of tweet sentiment scores for the tweets that word appears in
    no_sent = {}
    # read through lines in the file
    for line in tweet_file:
        js = json.loads(line)
        tweet_text = js.get('text').replace('\n',' ') if 'text' in js else ''
        tweet_words = tweet_text.split(' ')
        tweet_sentiment = 0.0
        tmp_no_sent = []
        # read all the words in the tweet
        for word in tweet_words:
            if word in scores:
                tweet_sentiment += scores.get(word)
            else:
                tmp_no_sent.append(word)
        
        # for all the words that were not in the sentiment file, but were in the tweet
        for word in tmp_no_sent:
            if word in no_sent:
                no_sent.get(word).append(tweet_sentiment)
            else:
                no_sent[word] = [tweet_sentiment]
            
    # loop through all words in no_sent and calculate the average of the tweet sentiment values
    for word in no_sent.keys():
        avg = sum(no_sent.get(word))/len(no_sent.get(word))
        print word + ' ' + str(avg)

if __name__ == '__main__':
    main()
