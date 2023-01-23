import matplotlib.pyplot as plt
from util import clear_screen

def display_ratings_bar_chart(ratings):
    '''
    Generates a bar chart showing how many reviews of each rating there are.
    '''
    # count how many of each star rating exist in the dataframe
    ratings = [
        len([i for i in ratings if i == 1]),
        len([i for i in ratings if i == 2]),
        len([i for i in ratings if i == 3]),
        len([i for i in ratings if i == 4]),
        len([i for i in ratings if i == 5])
    ]
    x_labels = ['1 Star', '2 Star', '3 Star', '4 Star', '5 Star']
    plt.bar(range(len(ratings)), ratings)
    plt.title('Star Ratings')
    ax = plt.subplot()
    ax.set_xticks(range(len(x_labels)))
    ax.set_xticklabels(x_labels)
    plt.show()

def display_results(overall, score, percentages, mean):
    '''
    Output sentiment analysis data to the terminal.
    '''
    clear_screen()

    # output results to the user
    print('Overall results were: ' + overall)
    print(str(percentages['positive']) + '% of reviews were positive')
    print(str(percentages['negative']) + '% of reviews were negative')
    print(str(percentages['neutral']) + '% of reviews were neutral')
    
    # displays total score of each sentiment
    print("Positive score: ", round(score['positive'], 2))
    print("Negative score: ", round(score['negative'], 2))
    print("Neutral score: ", round(score['neutral'], 2))

    # displays average star rating
    print('Average rating is: ' + str(round(mean, 2)) + ' out of 5 stars')