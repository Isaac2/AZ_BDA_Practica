import pandas
import nltk #Natural Language Tokenizer
nltk.download('stopwords')
import matplotlib.pyplot as pyplot

tweets = pandas.read_csv("./datasets/trump_tweets.csv")

print(tweets.shape)

tokenized = {}
tweet_tokenizer = nltk.tokenize.casual.TweetTokenizer()
filter_words = ["!", ",", ":", ".", "—", "&", "?", "\'", "\"", ")", "(", "’"]
stopwords = nltk.corpus.stopwords.words('english')

for value in tweets["text"]:
    tokenized[value] = [word for word in tweet_tokenizer.tokenize(value) if word.lower() not in stopwords and word not in filter_words]