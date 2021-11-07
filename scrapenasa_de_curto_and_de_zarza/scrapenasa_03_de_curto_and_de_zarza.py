# PAC. Pràctica 1. Universitat Oberta de Catalunya.
# J. de Curtò i DíAz decurto@uoc.edu
# I. de Zarzà i Cubero dezarza@uoc.edu

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import validators
    
# Folder to save samples.
folder = 'samples_03/'
os.makedirs(folder)

# Webpages to scrape:
# site[0]: Curiosity.
# site[1]: Perseverance.
site = ['https://mars.nasa.gov/msl/multimedia/raw-images/', 'https://mars.nasa.gov/mars2020/multimedia/raw-images/']

# Start Firefox session.
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to given site.
driver.get(site[1]) # Perseverance

# Slightly scroll the window to have button in view.
driver.execute_script("window.scrollTo(0, 400)") 

# Extract source.
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

# Find all images in the first page.
img_tags = soup.findAll('img')
urls = [img['src'] for img in img_tags]

# Then add one by one to CSV and download them.
for url in urls:
    # URL Validation. 
    if not validators.url(url):
         print("Not a correct url: {}" .format(url))
         continue
    # Get filename.         
    filename = re.search(r'/([\w_-]+[.](jpg|png|JPG|PNG))$', url)
    if not filename:
         print("Regular expression didn't match with the url: {}".format(url))
         continue
    # Add file to CSV.
    df = pd.DataFrame({"url" : [url]})
    df.to_csv("cyz.csv", mode = 'a', index = False, header = False)
    # Download image.
    with open(folder+filename.group(1), 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)

# Select next button to proceed to following page.
next_button = driver.find_elements_by_class_name("next")

# Do the same for the following pages.
while next_button:
      # Click on next button to load new content.
      ActionChains(driver).click(next_button[0]).perform()
      # Select next button for the following iteration.
      next_button = driver.find_elements_by_class_name("next")
      time.sleep(1)
      # Extract source and images.
      page_source = driver.page_source
      soup = BeautifulSoup(page_source, 'lxml')
      img_tags = soup.findAll('img')
      urls = [img['src'] for img in img_tags]
      # Then add one by one to CSV and download them.
      for url in urls:
            # URL Validation. 
            if not validators.url(url):
                  print("Not a correct url: {}" .format(url))
                  continue
            # Get filename.
            filename = re.search(r'/([\w_-]+[.](jpg|png|JPG|PNG))$', url)
            if not filename:
                  print("Regular expression didn't match with the url: {}".format(url))
                  continue
            # Add file to CSV.
            df = pd.DataFrame({"url" : [url]})
            df.to_csv("cyz.csv", mode = 'a', index = False, header = False)
            # Download image.      
            with open(folder+filename.group(1), 'wb') as f:	
                  if 'http' not in url:
                        url = '{}{}'.format(site, url)
                  response = requests.get(url)
                  f.write(response.content)
            # Add delay to avoid unattended requests from the server.
            time.sleep(1)
            
# Close browser window
driver.quit()
