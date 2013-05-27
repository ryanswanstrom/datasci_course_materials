import sys
import json
import collections

# returns term frequency: 
# [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
def main():
    tweet_file = open(sys.argv[1])

    terms = {}
    total_terms = 0.0

    for line in tweet_file:
        #print line
        js = json.loads(line)
        tweet_text = js.get('text').encode('utf-8').replace('\n','') if 'text' in js else ''
        tweet_terms = tweet_text.split(' ')
        for term in tweet_terms:
            if term in terms:
                terms[term] += 1.0
            else:
                terms[term] = 1.0
        total_terms += 1.0

    for key in terms.keys():
        print key + ' ' + str( terms.get(key)/total_terms )

if __name__ == '__main__':
    main()
