"""
KMP Text Search - O(m + n)
m = haystack
n = needle
"""

import tweepy

consumer_key =  "i5qxQwsMYZOC0ibF5LZVbQ19G"
consumer_secret = "97WmrQgYQqkGdJiDiUp8E5q5xqtR9mvmKo59gxGuPmFL33Y3bJ"
access_token = "731777689028153344-fZu83uU9I2YnokAcbReFaV4wtWO9Z4H"
access_token_secret = "RVgBZU6FPP7wFDWPzcHCVWiOYOqhebQbiHerSF3qrSNTw"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def kmp(strings, find_string):
    n = len(strings)
    m = len(find_string)
    j = 0
    k = 0
    fail = kmp_fail(find_string)
    while j < n:
        if strings[j].lower() == find_string[k].lower():
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1
        
        
def kmp_fail(find_string):
    n = len(find_string)
    fail = [0] * n
    j = 1
    k = 0
    while j < n:
        if find_string[j].lower() == find_string[k].lower():
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return fail

public_tweets = api.home_timeline()
find_string = "RT"#input('Masukkan string uji: ')""
for tweet in public_tweets:
    print (tweet.text)
    if (kmp(tweet.text,find_string) != -1):
        print("Spam detected!")
    print ("---------------------------------------------------------------")