import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk
import re
from nltk.corpus import stopwords
import string
from webscrape import soup_maker, generate_dataframe


df = generate_dataframe(soup_maker('https://www.argos.co.uk/product/8275332?clickSR=slp:term:lego%20set:7:247:1'))
print(df.head())

# check if null values exist
df.isnull().sum()

# remove null values
df = df.dropna()

# initialise portstemmer
stemmer = nltk.SnowballStemmer("english")
stopword=set(stopwords.words('english'))

# function to clean, tokenize, remove stopwords, stem and rejoin text
def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text
df["description"] = df["description"].apply(clean)

print(df.head())
'''
# displays stemmed, non stopwords in a wordcloud
text = " ".join(i for i in df.description)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
'''
# adds 3 columns to dataframe with the sentiment scores of the reviews
nltk.download('vader_lexicon')
sentiments = SentimentIntensityAnalyzer()
df["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in df["description"]]
df["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in df["description"]]
df["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in df["description"]]
df = df[["title", "description", "rating", "Positive", "Negative", "Neutral"]]
print(df.head())
'''
# displays wordcloud of positive reviews
positive =' '.join([i for i in df['description'][df['Positive'] > df["Negative"]]])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(positive)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
'''
'''
# displays wordcloud of negative reviews
negative =' '.join([i for i in df['description'][df['Negative'] > df["Positive"]]])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(negative)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
'''
# displays overall sentiment of reviews
x = sum(df["Positive"])
y = sum(df["Negative"])
z = sum(df["Neutral"])

def sentiment_score(a, b, c):
    if (a>b) and (a>c):
        print('Overall reviews are: ' + "Positive")
    elif (b>a) and (b>c):
        print('Overall reviews are: ' + "Negative")
    else:
        print('Overall reviews are: ' + "Neutral")
sentiment_score(x, y, z)

def sentiment_percent(a, b, c):
    total = sum([a, b, c])
    print(str(round(a / total * 100)) + '%' + ' of reviews are Positive')
    print(str(round(b / total * 100)) + '%' + ' of reviews are Negative')
    print(str(round(c / total * 100)) + '%' + ' of reviews are Neutral')
sentiment_percent(x, y, z)

# displays total score of each sentiment
print("Positive score: ", x)
print("Negative score: ", y)
print("Neutral score: ", z)