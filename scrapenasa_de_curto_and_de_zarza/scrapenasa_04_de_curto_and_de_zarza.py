# PAC. Pràctica 1. Universitat Oberta de Catalunya.
# J. de Curtò i DíAz decurto@uoc.edu
# I. de Zarzà i Cubero dezarza@uoc.edu

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
from bs4 import BeautifulSoup
import pandas as pd
import validators

# Webpages to scrape:
# site[0]: Curiosity.
# site[1]: Perseverance.
site = ['https://mars.nasa.gov/msl/multimedia/raw-images/', 'https://mars.nasa.gov/mars2020/multimedia/raw-images/']

# Start Firefox session
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

# Get number of pages.
numberpages = driver.find_element_by_css_selector("span.total_pages")
npages = int(numberpages.text.replace(',', ''))

# Find all images in the first page.
img_tags = soup.findAll('img')
urls = [img['src'] for img in img_tags]

# Then add one by one to CSV.
for url in urls:
    # URL Validation. 
    if not validators.url(url):
         print("Not a correct url: {}" .format(url))
         continue
    # Get filename. 
    filename = re.search(r'/([\w_-]+[.](jpg|png|PNG|JPG))$', url)
    if not filename:
         print("Regular expression didn't match with the url: {}".format(url))
         continue
    # Add file to CSV.
    df = pd.DataFrame({"url" : [url]})
    df.to_csv("cyz.csv", mode = 'a', index = False, header = False)

# Do the same for the remaining pages.
c = 2
# Select header to proceed to following page.
next_button = driver.find_elements_by_class_name("page_num")

# Iterate through number of pages.
while c <= npages:
      # Double click on header and change its value.
      ActionChains(driver).double_click(next_button[0]).send_keys(str(c)).perform()
      # Select header to proceed to following page.
      next_button = driver.find_elements_by_class_name("page_num")
      # Extract source and images. Then save them to CSV one by one.
      page_source = driver.page_source
      soup = BeautifulSoup(page_source, 'lxml')
      img_tags = soup.findAll('img')
      urls = [img['src'] for img in img_tags]
      for url in urls:
            # URL Validation. 
            if not validators.url(url):
                 continue
            # Get filename.
            filename = re.search(r'/([\w_-]+[.](jpg|png|JPG|PNG))$', url)
            if not filename:
                  print("Regular expression didn't match with the url: {}".format(url))
                  continue
            # Add file to CSV.
            df = pd.DataFrame({"url" : [url]})
            df.to_csv("cyz.csv", mode = 'a', index = False, header = False)
      # Add delay to avoid unattended requests from the server.
      time.sleep(1)
      # Update counter.
      c += 1

# Close browser window
driver.quit()
