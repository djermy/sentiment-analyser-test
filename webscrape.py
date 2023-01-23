import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from nlp import clean

# scrapers
import argos

def scrape_reviews(url):
    '''
    Uses selenium to scrape reviews from a website and outputs as a pandas
    dataframe.
    '''
    driver = init_driver(url, 3)
    reviews = argos.scrape_reviews(driver)
    driver.quit()
    
    return generate_dataframe(reviews)

def init_driver(url, sleep):
    '''
    Initializes a headless firefox instance using selenium to scrape a website.
    '''
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(sleep)
    return driver

def generate_dataframe(reviews):
    '''
    Converts a dictionary containing titles, descriptions, and ratings into a
    pandas dataframe.
    '''
    df = pd.DataFrame(
        list(zip(
            reviews['titles'],
            reviews['descriptions'],
            reviews['ratings'],
        )),
        columns=['title', 'description', 'rating'])
    df['rating'] = df['rating'].astype(int)

    return df