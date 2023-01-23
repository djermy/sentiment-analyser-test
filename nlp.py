import re, string, nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

def analyse_sentiment(df):
    '''
    Cleans the description text field, and generates polarity scores for
    positive, negative, and neutral reviews.
    '''
    # clean description text field
    df["description"] = df["description"].apply(clean)

    # adds 3 columns to dataframe with the sentiment scores of the reviews
    sentiments = SentimentIntensityAnalyzer()
    df["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in df["description"]]
    df["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in df["description"]]
    df["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in df["description"]]
    df = df[["title", "description", "rating", "Positive", "Negative", "Neutral"]]
    return df

def calculate_score(df):
    '''
    Calulates the sum of each category of review.
    '''
    return {
        'positive': sum(df['Positive']),
        'negative': sum(df['Negative']),
        'neutral': sum(df['Neutral'])
    }

def sentiment_overall(score):
    '''
    Calculates whether the overall sentiment is positive, negative, or neutral.
    '''
    # displays overall sentiment of reviews
    a = score["positive"]
    b = score["negative"]
    c = score["neutral"]

    if (a > b) and (a > c):
        return 'positive'
    elif (b > a) and (b > c):
        return 'negative'
    else:
        return 'neutral'


def sentiment_percent(score):
    '''
    Calculates the overall percentage of each category of review.
    '''
    a = score['positive']
    b = score['negative']
    c = score['neutral']

    total = sum([a, b, c])
    return {
        'positive': round(a / total * 100),
        'negative': round(b / total * 100),
        'neutral': round(c / total * 100),
    }

def clean(text):
    '''
    Function to clean, tokenize, remove stopwords, stem and rejoin text.
    '''
    # initialise portstemmer
    stemmer = nltk.SnowballStemmer("english")
    stopword = set(stopwords.words('english'))

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