import pandas
import nltk #Natural Language Tokenizer
nltk.download('stopwords')
import matplotlib.pyplot as pyplot

tweets = pandas.read_csv("./datasets/trump_tweets.csv")

##########################
#print(tweets)
#print(tweets["text"])

#Ver la estructura de los datos
#print(tweets.shape)

#Ver los primeros 5 o últimos 5 se puede usar .head(5) o .tail(5)

#print(tweets.info())
##########################

tokenized = {}
tweet_tokenizer = nltk.tokenize.casual.TweetTokenizer()
filter_words = ["!", ",", ":", ".", "—", "&", "?", "\'", "\"", ")", "(", "’"]
stopwords = nltk.corpus.stopwords.words('english')

for value in tweets["text"]:
    tokenized[value] = [word for word in tweet_tokenizer.tokenize(value) if word.lower() not in stopwords and word not in filter_words]

counter = {}
for key,value in tokenized.items():
    for word in value:
        if counter.get(word) == None:
            counter[word] = 1
        else:
            counter[word] += 1

sorted_counters = sorted( counter.items(), key=lambda x: x[1], reverse=True )

size_limit = 15
final_counters = dict( list(sorted_counters[0:size_limit]) )

pyplot.bar(list(final_counters.keys()), final_counters.values(), color="g")
pyplot.show()