import tweepy
import sys

consumer_key =  "capwg9T5wxa5AW9XbxpxnxqTY"
consumer_secret = "WdrXpwaK9iRgW53xNTyEIL6z7sJp9NOHe9faq9xmucVHi64C9x"
access_token = "988072781370703872-hGlq63NYvRRKr99SKCYBPah66YMYU2N"
access_token_secret = "XVL4F8YA5QW0PfM4lKi8QOI6aJQOH3WRsS31wKBasZJFV"

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
find_string = sys.argv[1]
for tweet in public_tweets:
    print ("@"+str(tweet.user.screen_name)+ " : ")
    print (tweet.text+" | ")
    print (str(tweet.created_at))
    if (kmp(tweet.text,find_string) != -1):
        print("==> Spam detected!")
    print ("---------------------------------------------------------------")

