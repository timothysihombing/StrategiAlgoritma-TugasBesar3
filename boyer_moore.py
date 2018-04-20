#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Overxfl0w13 #
# Sequential search, boyer moore algorithm #

import tweepy

consumer_key = 	"i5qxQwsMYZOC0ibF5LZVbQ19G"
consumer_secret = "97WmrQgYQqkGdJiDiUp8E5q5xqtR9mvmKo59gxGuPmFL33Y3bJ"
access_token = "731777689028153344-fZu83uU9I2YnokAcbReFaV4wtWO9Z4H"
access_token_secret = "RVgBZU6FPP7wFDWPzcHCVWiOYOqhebQbiHerSF3qrSNTw"

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
	find_string = input('Masukkan string uji: ')
	for tweet in public_tweets:
	    print (tweet.text)
	    # if (boyer_moore(tweet.text,find_string,generate_d_vector(tweet.text,find_string)) == -1):
	    print(boyer_moore(tweet.text,find_string,generate_d_vector(tweet.text,find_string)))
	    print ("---------------------------------------------------------------")