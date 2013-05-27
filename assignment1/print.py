import urllib
import json
import sys

# command line arguement sys.argv[1] is number of pages
pages = int(sys.argv[1]) if len(sys.argv) >= 2 else 10

for page in range( pages ):
    response = urllib.urlopen("http://search.twitter.com/search.json?q=datascience&page=" + str(page + 1))
    jsn = json.load(response)
    res = jsn.get('results')
    for i in res:
        print i.get('from_user') + ': ' + i.get('text')


#[u'iso_language_code', u'profile_image_url_https', u'from_user_id_str', u'text', u'from_user_name', u'profile_image_url', u'id', u'source', u'id_str', u'from_user', u'from_user_id', u'geo', u'created_at', u'metadata']

