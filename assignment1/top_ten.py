import sys
import json
import collections


def main():
    tweet_file = open(sys.argv[1])

    hashtags = {}

    for line in tweet_file:
        #print line
        js = json.loads(line)
        tweet_ent = js.get('entities') if 'entities' in js else {}
        tweet_tags = tweet_ent.get('hashtags') if 'hashtags' in tweet_ent else []
        for tag in tweet_tags:
            hashtag = tag.get('text').encode('utf-8')
            if hashtag in hashtags:
                hashtags[hashtag] = (hashtags.get(hashtag) + 1.0)
            else:
                hashtags[hashtag] = 1.0
        #print type(tweet_ent)
    
    ordered_hashtags = collections.OrderedDict(sorted(hashtags.items(), key=lambda t: t[1], reverse=True))

    row = 0;
    for key in ordered_hashtags.keys():
        if row < 10:
            print key + ' ' + str( ordered_hashtags.get(key) )
            row += 1

if __name__ == '__main__':
    main()
