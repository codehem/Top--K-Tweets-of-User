import tweepy
consumer_key = "kJw5DKyNxQUUgaT5trGZX09a4"
consumer_secret = "HiLwij1CAMB4R618sQ7zFs7mDpEaKkoVaDXpNaN7FjFoGqiDK4"
access_token = "1092953497392242688-dX4PP4DyMtVihRUNnURKnJGTDYaUfk"
access_token_secret = "v8sgivQiAqHv5FRPsupb5YfJTicft35SoxOA6mLozSwJy"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The Twitter user who we want to get tweets from
name = "PuneethRajkumar"
# Number of tweets to pull
tweetCount = 10

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name, count=tweetCount)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print tweet.text
