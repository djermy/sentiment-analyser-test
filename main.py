import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import re
from nltk.corpus import stopwords
import string
from webscrape import soup_maker, generate_dataframe
import os

def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')

url = input('Please enter a valid product link to argos.co.uk: ')
df = generate_dataframe(soup_maker(url))
print(df.head())

# initialise portstemmer
stemmer = nltk.SnowballStemmer("english")
stopword = set(stopwords.words('english'))

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
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text = " ".join(text)
    return text

df["description"] = df["description"].apply(clean)

#print(df.head())

# adds 3 columns to dataframe with the sentiment scores of the reviews
sentiments = SentimentIntensityAnalyzer()
df["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in df["description"]]
df["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in df["description"]]
df["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in df["description"]]
df = df[["title", "description", "rating", "Positive", "Negative", "Neutral"]]

# displays overall sentiment of reviews
x = sum(df["Positive"])
y = sum(df["Negative"])
z = sum(df["Neutral"])

def sentiment_score(a, b, c):
    '''
    Takes 3 sums of sentiments as input and displays overall sentiment.
    '''
    if (a>b) and (a>c):
        print('Overall reviews are: ' + "Positive")
    elif (b>a) and (b>c):
        print('Overall reviews are: ' + "Negative")
    else:
        print('Overall reviews are: ' + "Neutral")

def sentiment_percent(a, b, c):
    '''
    Takes 3 sums of sentiments as input and displays rounded, percentage values \
        of each sentiment.
    '''
    total = sum([a, b, c])
    print(str(round(a / total * 100)) + '%' + ' of reviews are Positive')
    print(str(round(b / total * 100)) + '%' + ' of reviews are Negative')
    print(str(round(c / total * 100)) + '%' + ' of reviews are Neutral')


clear_screen()
sentiment_score(x, y, z)
sentiment_percent(x, y, z)

# displays total score of each sentiment
print("Positive score: ", round(x, 2))
print("Negative score: ", round(y, 2))
print("Neutral score: ", round(z, 2))