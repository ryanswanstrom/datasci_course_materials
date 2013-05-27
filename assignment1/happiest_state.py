import sys
import json
import collections

# calculates the sentiment of text based upon sent_dict which
# is a dictionary of terms(key) and sentiment values
# the calculation is just the sum of sentiment of the individual terms
# in the tweet
def calc_sent(sent_dict, text):
    words = text.split(' ')
    sentiment = 0.0
    for word in words:
        sentiment += sent_dict.get(word) if word in sent_dict else 0.0
    return sentiment

# find the happiest state
# 
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary for sentiment
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    # read tweet
    # find location "place"."country_code" == 'US'
    # or "user"."location"
    # or "user"."time_zone" contains US or Hawaii

    states = {'WA': 'Washington', 'DE': 'Delaware', 'DC': 'District of Columbia', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'HI': 'Hawaii', 'FL': 'Florida', 'WY': 'Wyoming', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'TX': 'Texas', 'LA': 'Louisiana', 'NA': 'National', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'TN': 'Tennessee', 'NY': 'New York', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'NV': 'Nevada', 'VA': 'Virginia', 'GU': 'Guam', 'CO': 'Colorado', 'VI': 'Virgin Islands', 'AK': 'Alaska', 'AL': 'Alabama', 'AS': 'American Samoa', 'AR': 'Arkansas', 'VT': 'Vermont', 'IL': 'Illinois', 'GA': 'Georgia', 'IN': 'Indiana', 'IA': 'Iowa', 'OK': 'Oklahoma', 'AZ': 'Arizona', 'CA': 'California', 'ID': 'Idaho', 'CT': 'Connecticut', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'OH': 'Ohio', 'UT': 'Utah', 'MO': 'Missouri', 'MN': 'Minnesota', 'MI': 'Michigan', 'KS': 'Kansas', 'MT': 'Montana', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'SC': 'South Carolina', 'KY': 'Kentucky', 'OR': 'Oregon', 'SD': 'South Dakota'}
    

    num_US_place = 0.0
    num_US_user = 0.0

    # this is dict, the keys should be state abbreviations,
    # the values should be a list of sentiment values for a tweet from that state
    state_tweets = {}
    
    for line in tweet_file:        
        js = json.loads(line)
        #print str(js.keys())
        #tweet_place = js.get('place') if 'place' in js else {}
        #if tweet_place and tweet_place is not None:
        #    #print str(tweet_place)
        #    if tweet_place.get('country_code') == 'US':
        #        num_US_place += 1.0
        
        tweet_user = js.get('user') if 'user' in js else {}
        if tweet_user and tweet_user is not None:
            #print str(tweet_user)
            loc = tweet_user.get('location').replace('\n',' ')
            #print loc
            tz = tweet_user.get('time_zone')
            if tz and tz is not None and ('US' in tz or 'Hawaii' in tz):
                #print tz + ', ' + loc
                num_US_user += 1.0
                #loop all states codes and check if in location
                for state_abbr in states.keys():
                    if state_abbr in loc:
                        #print state_abbr + ": " + loc
                        # now we have a tweet with a state
                        # calc sentiment of the tweet
                        sentiment = calc_sent(scores, (js.get('text') if 'text' in js else '') )
                        # add to state tweets
                        if state_abbr in state_tweets:
                            state_tweets.get(state_abbr).append(sentiment)
                        else:
                            state_tweets[state_abbr] = [sentiment]
                        break
        
    # now loop through state_tweets and calc averages
    # initialize with bogus state
    happy_state = 'NA'
    top_val = -10000.0
    for state in state_tweets.keys():
        sent_list = state_tweets.get(state)
        avg_sent = sum( sent_list )/len(sent_list)
        print state + ": " + str(avg_sent) + ": " + str(sent_list)
        if avg_sent > top_val:
            top_val = avg_sent
            happy_state = state
        

    print happy_state
    #print str(top_val)
    #print "by place " + str(num_US_place)
    #print "by user " + str(num_US_user)

if __name__ == '__main__':
    main()
