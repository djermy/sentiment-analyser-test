import time
from bs4 import BeautifulSoup

def scrape_reviews(driver):
    '''
    Scrapes all reviews from argos and returns the data in a dictionary with the keys
    titles, descriptions, and ratings.
    '''
    accept_cookies(driver)
    open_review_accordion(driver)
    show_all_reviews(driver, 0.4)
    return extract_review_data(driver)

def find_show_more_button(driver):
    '''
    Attempt to find the show more button in the reviews section and click if available.
    '''
    show_more_button = None
    try:
        show_more_button = driver.find_element_by_css_selector('[data-test="show-x-more-reviews-button"]')
    except:
        show_more_button = None
    return show_more_button

def accept_cookies(driver):
    '''
    Finds and clicks cookie consent prompt.
    '''
    driver.find_element_by_id('consent_prompt_submit').click()

def open_review_accordion(driver):
    '''
    Click the reviews accordion to view the reviews available on argos.
    '''
    driver.find_element_by_id('reviews-accordion-accordion-control-reviews-accordion').click()

def show_all_reviews(driver, sleep):
    '''
    Keep clicking the show more button until it is no longer present in an attempt to show all reviews.
    '''
    show_more_button = find_show_more_button(driver)
    while show_more_button:
        show_more_button.click()
        time.sleep(sleep)  
        show_more_button = find_show_more_button(driver)

def extract_review_data(driver):
    '''
    Collect all of the review data from argos, then transform into a dictionary with
    the keys titles, descriptions, and ratings.
    '''
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    review_container = soup.find("div", {"class": "Reviewsstyles__ReviewsContainer-sc-6g3q7a-10"})
    reviews = review_container.find_all('div', {'data-test': 'review-item'})
    
    return {
        'titles': [review.find('p', {'class': 'ReviewItemstyle__Title-sc-8dsnp1-0'}).decode_contents() for review in reviews],
        'descriptions': [review.find('p', {'itemprop': 'reviewBody'}).decode_contents() for review in reviews],
        'ratings': [review.find('span', {'itemprop': 'ratingValue'}).decode_contents() for review in reviews]
    }