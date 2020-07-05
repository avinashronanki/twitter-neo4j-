import tweepy
consumer_key = "jzHxDLhKGEsftNwvR6AZKPTsv"
consumer_secret = "1UQfqY3FgCPa4Ro1eOPrkfDoSEDNrfhfgrROsIZfmDDmB3wrKz"
access_token = "1159119959647301632-5lNhV30P9ZR0bR6TEWR0EL7ABZSeX4"
access_token_secret = "9oeXAFa3uo5gSFuPhxjIcBCz00NfNSzYfn8pNa4vJHPUP"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)