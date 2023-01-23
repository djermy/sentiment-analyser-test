import sys

from webscrape import scrape_reviews
from nlp import analyse_sentiment, calculate_score, sentiment_overall, sentiment_percent
from render import display_ratings_bar_chart, display_results

def main():
    # take url from user.
    url = input('Please enter a valid product link to argos.co.uk: ')

    # extract and analyse reviews
    reviews_df = scrape_reviews(url)
    sentiment_df = analyse_sentiment(reviews_df)

    # calculate sentiment data results
    score = calculate_score(sentiment_df)
    overall = sentiment_overall(score)
    percentages = (sentiment_percent(score))
    mean = sentiment_df['rating'].mean()

    # display results to user
    display_results(overall, score, percentages, mean)
    display_ratings_bar_chart(sentiment_df['rating'])
    return 0
    
if __name__ == '__main__':
    sys.exit(main())