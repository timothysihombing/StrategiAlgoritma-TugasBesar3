import tweepy
import sys

consumer_key = 	"capwg9T5wxa5AW9XbxpxnxqTY"
consumer_secret = "WdrXpwaK9iRgW53xNTyEIL6z7sJp9NOHe9faq9xmucVHi64C9x"
access_token = "988072781370703872-hGlq63NYvRRKr99SKCYBPah66YMYU2N"
access_token_secret = "XVL4F8YA5QW0PfM4lKi8QOI6aJQOH3WRsS31wKBasZJFV"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def generate_d_vector(text,pattern):
	d = {}
	for char in text: 
		founded = pattern.rfind(char)
		if char not in d:
			d[char] = len(pattern)-1-pattern.rfind(char) if founded != -1 else len(pattern)
	return d

def boyer_moore(text,pattern,d):
	j = len(pattern)-1
	while j<len(text):
		i = len(pattern)-1
		while i>0 and pattern[i]==text[j]: 
			i,j = i-1,j-1		
		if i==0: return j
		else:
			if len(pattern)-1-i>d[text[j]]: j = j + len(pattern)-1- i + 1
			else: j = j + d[text[j]]
	return -1
	
if __name__ == "__main__":
	public_tweets = api.home_timeline()
	find_string = sys.argv[1]
	for tweet in public_tweets:
		print("@"+str(tweet.user.screen_name)+ " : ")
		print(tweet.text+" | ")
		print(str(tweet.created_at))
		if (boyer_moore(tweet.text,find_string,generate_d_vector(tweet.text,find_string)) != -1):
			print("==> Spam detected!")
		print ("---------------------------------------------------------------")