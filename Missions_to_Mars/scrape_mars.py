from splinter import Browser
from bs4 import BeautifulSoup
import requests

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # ******** NASA Mars News scrape *************
    #*********************************************
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    # Retrieve page with the requests module
    response = requests.get(url)
    #response
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')
    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())
    news_title = soup.find('div', class_="content_title").text.strip()
    #print(news_title)
    news_teaser_title = soup.find('div', class_="rollover_description_inner").text.strip()
    #print(news_teaser_title)

    # ******** JPL Mars Space Images - Featured Image *************
    #**************************************************************
    # Splinter is used here to navigate the website, by finding 
    # and clicking on buttons.
    from splinter import Browser

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    # Visit the JPL web site.
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Instantiate the HTML object of the initial page
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())

    # After identifying the "full image" button on the page - click it to navigate to the next page.
    browser.links.find_by_partial_text('FULL IMAGE').click()

    # Instantiate the HTML object of the "full image" page
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())

    # After identifying the "more info" button on the page - click it to navigate to the next page which contains the full jpg image.
    browser.links.find_by_partial_text('more info').click()

    # Instantiate the HTML object of the "more info" page which contains a link to the full jpg image
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # The section of the HTML that contains the href to the full jpg image
    results = soup.find('figure', class_="lede")
    #results

    # Grab href element of full jpeg image
    link = results.a['href']
    # link

    # Build the full URL by concatenating "link" and the initial string of the JPL url
    featured_image_url = "https://www.jpl.nasa.gov" + link
    featured_image_url

    # Close the browser after scraping
    browser.quit()

    # ******** Mars Facts - Table scrape of Mars Facts table using Pandas *************
    #**********************************************************************************
    import pandas as pd
    url = 'https://space-facts.com/mars/'

    tables_list = pd.read_html(url)
    #tables_list

    mars_profile_df = tables_list[0]
    mars_profile_df.columns = ['Attribute', 'Value']
    mars_profile_df.set_index ('Attribute', inplace = True)
    #mars_profile_df

    # Convert to HTML table
    html_table = mars_profile_df.to_html()
    html_table = html_table.replace('\n', '')
    # html_table

    # Close the browser after scraping
    # browser.quit()

    #******************************************************
    #******** Mars Hemispheres Scrape -*******************
    #******************************************************
    import time
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    # Visit the USGS web site.
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(1)

    # Instantiate the HTML object of the initial page
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())
    hemisphere_url= []
    # Build list of Hemisphere names, searching for h3s
    h3s = soup.find_all('h3')
    hemispheres = []
    # Loop over td elements
    for h3 in h3s:
        hemispheres.append(h3.text)

    # Loop through each of the hemispheres and find the associated link
    # on a separate page to the link to the full resolution image 
    for hemi in hemispheres:

        # After identifying the "full image" button on the page - click it to navigate to the next page.
        # browser.links.find_by_partial_text('Cerberus').click()
        browser.links.find_by_partial_text(hemi).click()
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup.prettify())

        browser.links.find_by_partial_text('Open').click()
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup.prettify()

        # The section of the HTML that contains the href to the full jpg image
        results = soup.find('img', class_="wide-image")
        #results
        # Grab href element of full jpeg image
        sublink = results['src']

        image_url = "https://astrogeology.usgs.gov" + sublink

        hemisphere_url.append(image_url)
        
        browser.back()
        time.sleep(1)    


    # Now make a list of dictionaries of the two lists containing the hemisphere names
    # and associated high resolution image links.
    hemisphere_image_urls = [{'title': hemispheres[i], 'img_url': hemisphere_url[i]} for i in range(len(hemispheres))]
    #hemisphere_image_urls

    mars_data = {
        "news_title": news_title,
        "news_teaser_title" : news_teaser_title,
        "Featured_Mars_Image": featured_image_url,
        "Mars_Facts" : html_table,
        "Mars_Hemispheres" : hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    return mars_data