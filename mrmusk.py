from twitter_keys import consumer_key, consumer_secret, access_key, access_token
from keys import api_key, secret_key
import tweepy
from binance.client import Client

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_key)

client = Client(api_key, secret_key)

tickers = ['BTCEUR', 'DOGEEUR']
list_of_tickers = client.get_all_tickers()

api = tweepy.API(auth)
user = 'elonmusk'

tweets = api.user_timeline(id = user, count=3)
past_tweets = []
count = 0
tweet_texts = []
for tweet in tweets:
    if tweet not in past_tweets:
        tweet_texts.append(tweet.text)
    count+=1
    # past_tweets.drop[count]
    past_tweets.append(tweet.text)

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze(arg):
    sid = SentimentIntensityAnalyzer()
    polarity = sid.polarity_scores(arg)
    return polarity

coins = ['dogecoin', 'bitcoin', 'btc', 'doge']

def sentiments(tweets):
    for tweet in tweet_texts:
        print("Tweet: {} | Sentiment: {}".format(tweet, analyze(tweet)))
    
print(sentiments(tweet_texts))


def getWhichCoin():
    for tweet in tweet_texts:
        for word in coins:
            if word in tweet:
                compound = analyze(tweet)['compound']
                if compound['compound'] >= 0:
                    which_coin = word
                    return which_coin

def Symbol():
    coin = getWhichCoin()
    symbol = ''
    if coin == 'btc' or 'bitcoin':
        symbol = 'BTCEUR'
    elif coin == 'doge' or 'dogecoin':
        symbol = 'DOGEEUR'
    return symbol

#EXECUTAR A ORDEM 

def BuyOrder(symbol):
    order = client.create_test_order(
    symbol=Symbol(),
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=100)
    return order
def sellOrder(symbol):
    order = client.create_test_order(
    symbol=Symbol(),
    side=Client.SIDE_SELL,
    type=Client.ORDER_TYPE_MARKET,
    quantity=100)
    return order

#programar tempo

BuyOrder()
# time.sleep('definir tempo')
sellOrder()




