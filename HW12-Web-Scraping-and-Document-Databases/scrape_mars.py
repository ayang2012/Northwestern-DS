from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'Templates/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():

    browser = init_browser()
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    news_title = soup.find('div', class_='content_title').find('a').text.strip()
    news_p = soup.find('div', class_='rollover_description_inner').text.strip()

    # nasa images
    url_images = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_images) 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_image = soup.find('a', class_='button fancybox')['data-fancybox-href']
    nasa_base = 'https://www.jpl.nasa.gov'
    f_image = nasa_base + featured_image

    #twitter weather
    url_twitter = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_twitter)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_weather = soup.find_all('div', class_='js-tweet-text-container')
    t_weather = ''
    for tweet in mars_weather:
        if tweet.text.strip().startswith('Sol'):
            t_weather = tweet.text.strip()
            break

    #space facts table
    facts_url = 'https://space-facts.com/mars/'    
    tables = pd.read_html(facts_url)
    df = tables[0]
    df.columns = ['0','1']
    df.rename(columns={'0':'Facts','1':'Data'}, inplace=True)
    df.set_index('Facts', inplace=True)
    html_table = df.to_html()
    html_table.replace('\n', '')
    s_table = html_table

    # hemisphere images
    a_image = []
    a_title = []
    # print(soup.find_all('h3'))
    for i in range(4):#len(browser.find_by_css('h3'))):
        url_mars = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url_mars)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        # print(a_title)
        # print(soup.find_all('h3')[i].text)
        a_title.append(soup.find_all('h3')[i].text)
        browser.find_by_css('h3')[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
#     base = 
        a_image.append(soup.find_all('a')[41]['href'])


     # Store data in a dictionary
    mars_news = {
        "mars_headeline": news_title,
        "mars_p": news_p, 
        "feature_image": f_image,
        "twitter_weather": t_weather,
        "space_table": s_table,
        "hemi_titles": a_title,
        "hemi_links": a_image

        }
    browser.quit()
    print(mars_news)   
    return mars_news


# # Close the browser after scraping
#     browser.quit()