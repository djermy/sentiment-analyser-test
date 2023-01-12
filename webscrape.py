from bs4 import BeautifulSoup
import requests

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

def get_data(url):
    r = requests.get(url, headers=HEADERS)
    return r.text

def html_code(url):

    # pass the url
    # into getdata function
    htmldata = get_data(url)
    soup = BeautifulSoup(htmldata, 'html.parser')

    # display html code
    return (soup)

url = "https://www.amazon.co.uk/Maynards-Bassetts-Giant-Sweets-Sharing/dp/B08ZTFLZWJ/ref=sr_1_2?crid=1GJQZIFB8DM2E&keywords=wine+gums&qid=1673521299&sprefix=wine+gum%2Caps%2C149&sr=8-2"
soup = html_code(url)
print(soup)

if '!DOCTYPE' in soup:
    print('yes!')
else:
    print('no =(')