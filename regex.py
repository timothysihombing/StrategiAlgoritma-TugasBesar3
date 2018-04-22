import re
import tweepy
import sys

consumer_key =  "i5qxQwsMYZOC0ibF5LZVbQ19G"
consumer_secret = "97WmrQgYQqkGdJiDiUp8E5q5xqtR9mvmKo59gxGuPmFL33Y3bJ"
access_token = "731777689028153344-fZu83uU9I2YnokAcbReFaV4wtWO9Z4H"
access_token_secret = "RVgBZU6FPP7wFDWPzcHCVWiOYOqhebQbiHerSF3qrSNTw"

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