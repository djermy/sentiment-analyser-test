from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.firefox.options import Options

def find_show_more(driver):
    show_more_button = None
    try:
        show_more_button = driver.find_element_by_css_selector('[data-test="show-x-more-reviews-button"]')
    except:
        show_more_button = None
    return show_more_button

def soup_maker(url):
    '''
    Takes url as input and outputs BeautifulSoup element containing reviews. 
    '''
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    #url = "https://www.argos.co.uk/product/2010517"
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_id('consent_prompt_submit').click()
    driver.find_element_by_id('reviews-accordion-accordion-control-reviews-accordion').click()

    show_more_button = find_show_more(driver)

    while show_more_button:
        show_more_button.click()
        time.sleep(0.4)  
        show_more_button = find_show_more(driver)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    
    review_container = soup.find("div", {"class": "Reviewsstyles__ReviewsContainer-sc-6g3q7a-10"})
    reviews = review_container.find_all('div', {'data-test': 'review-item'})
    
    return reviews

def generate_dataframe(reviews):
    '''
    Takes reviews BeautifulSoup element and returns dataframe with 3 columns:
    title, description, rating.
    '''

    # turning reviews into seperate lists for the dataframe
    titles = [review.find('p', {'class': 'ReviewItemstyle__Title-sc-8dsnp1-0'}).decode_contents() for review in reviews]
    descriptions = [review.find('p', {'itemprop': 'reviewBody'}).decode_contents() for review in reviews]
    ratings = [review.find('span', {'itemprop': 'ratingValue'}).decode_contents() for review in reviews]
    
    # build the dataframe
    df = pd.DataFrame(
        list(zip(titles, descriptions, ratings)),
        columns=['title', 'description', 'rating'])

    return df