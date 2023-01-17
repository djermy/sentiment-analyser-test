from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Firefox()
url = "https://www.argos.co.uk/product/2010517"
driver.get(url)
time.sleep(3)
driver.find_element_by_id('consent_prompt_submit').click()
driver.find_element_by_id('reviews-accordion-accordion-control-reviews-accordion').click()
show_more_button = None

try:
    show_more_button = driver.find_element_by_css_selector('[data-test="show-x-more-reviews-button"]')
except:
    show_more_button = None

while show_more_button:
    show_more_button.click()
    time.sleep(0.4)  
    try:
        show_more_button = driver.find_element_by_css_selector('[data-test="show-x-more-reviews-button"]')
    except:
        show_more_button = None
        
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

review_container = soup.find("div", {"class": "Reviewsstyles__ReviewsContainer-sc-6g3q7a-10"})
reviews = review_container.find_all('div', {'data-test': 'review-item'})
print('Total Reviews: ' + str(len(reviews)))
print(type(reviews))
def make_df_lists(reviews):
    '''
    Takes 
    '''

    # turning reviews into seperate lists for 
    titles = [review.find('p', {'class': 'ReviewItemstyle__Title-sc-8dsnp1-0'}).decode_contents() for review in reviews]
    descriptions = [review.find('p', {'itemprop': 'reviewBody'}).decode_contents() for review in reviews]
    ratings = [review.find('span', {'itemprop': 'ratingValue'}).decode_contents() for review in reviews]
    return titles, descriptions, ratings