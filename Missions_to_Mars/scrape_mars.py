#Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
import requests
import pandas as pd
from splinter import Browser
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import re 


def init_browser():
    executable_path = {"executable_path": '/usr/local/bin/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # create mars dictionary for mongo
    mars_data = {}

    #Opens the browser for control
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Mars News Site
    #Sets URL of site to be scraped / page data
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    #Pulling in data
    html = browser.html

    # Parse with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    #Mars News Site
    #Latest article title
    news_title = soup.find('div', class_='content_title').text
    #print(news_title)

    #Mars News Site
    #Latest article text
    news_p = soup.find('div', class_='article_teaser_body').text
    #print(news_p)

    #Featured Space Image
    #Sets URL of page to be scraped
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars+Feature"

    #Pulling in data
    browser.visit(image_url)

    #Sets the base URL
    baseurl = 'https://www.jpl.nasa.gov'

    #Parse with Beautiful Soup
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')
    
    #Scrape the URL
    image_url = image_soup.find('a', {'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')
    #image_url

    #Create the final URL
    featured_image_url = baseurl + image_url

    #featured_image_url


    weather = requests.get("https://twitter.com/marswxreport?lang=en")
    wsoup = bs(weather.text, "html.parser")

    latest = wsoup.find('div', {'class': 'ProfileTimeline'})
    latest = latest.find("p", {'class': "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
    mars_weather = latest.text

    mars_data = mars_weather


    #Mars Facts
    #Sets URL of page to be scraped
    url = 'https://space-facts.com/mars/'

    #Loads the data
    html = browser.html

    #Read the data to a pandas table
    table = pd.read_html(url)
    marstab=table[1]

    #Mars Facts
    #Converts the table to HTML
    print(marstab.to_html())

    #Mars Facts
    #Saving the file
    marstab.to_csv('mars_raw_data.csv', encoding='utf-8', index=False)


    #Mars Hemispheres
    #URL of page to be scraped - Cerberus
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)

    #Pulling in data
    html = browser.html

    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(html, 'html.parser')

    #Image url
    cerberus_url = soup.find('div', class_='downloads')
    link = cerberus_url.find('a')
    cerberus_href = link['href']

    #print(cerberus_href)


    #Mars Hemispheres
    #URL of page to be scraped - Schiaparelli
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)

    #Pulling in data
    html = browser.html

    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(html, 'html.parser')

    #Image url
    schia_url = soup.find('div', class_='downloads')
    link = schia_url.find('a')
    schia_href = link['href']

    #print(schia_href)

    #Mars Hemispheres
    #URL of page to be scraped - Syrtis
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)

    #Pulling in data
    html = browser.html

    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(html, 'html.parser')

    #Image url
    syrtis_url = soup.find('div', class_='downloads')
    link = syrtis_url.find('a')
    syrtis_href = link['href']
    
    #print(syrtis_href)

    #Mars Hemispheres
    #URL of page to be scraped - Syrtis
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)

    #Pulling in data
    html = browser.html

    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(html, 'html.parser')

    #Image url
    valles_url = soup.find('div', class_='downloads')
    link = valles_url.find('a')
    valles_href = link['href']

    #print(valles_href)

    #Mars Hemispheres
    #Library of hemisphere images

    hemisphere_image_urls = [
        {'title': 'Valles Marineris Hemisphere', 'img_url': valles_href},
        {'title': 'Syrtis Major Hemisphere', 'img_url': syrtis_href},
        {'title': 'Schiaparelli Hemisphere', 'img_url': schia_href},
        {'title': 'Cerberus Hemisphere', 'img_url': cerberus_href}
    ]

    return mars_data

if __name__ == "__main__":
    scrape()