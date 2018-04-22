import re
import tweepy
import sys

consumer_key =  "capwg9T5wxa5AW9XbxpxnxqTY"
consumer_secret = "WdrXpwaK9iRgW53xNTyEIL6z7sJp9NOHe9faq9xmucVHi64C9x"
access_token = "988072781370703872-hGlq63NYvRRKr99SKCYBPah66YMYU2N"
access_token_secret = "XVL4F8YA5QW0PfM4lKi8QOI6aJQOH3WRsS31wKBasZJFV"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

if __name__ == "__main__":
    public_tweets = api.home_timeline()
    find_string = sys.argv[1]
    for tweet in public_tweets:
        print ("@"+str(tweet.user.screen_name)+ " : ")
        print (tweet.text+" | ")
        print (str(tweet.created_at))
        m = re.findall(find_string, tweet.text)
        if (len(m) != 0):
            print("==> Spam detected!")
        print ("---------------------------------------------------------------")