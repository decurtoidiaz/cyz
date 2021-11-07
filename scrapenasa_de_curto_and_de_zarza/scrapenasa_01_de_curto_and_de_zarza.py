# PAC. Pràctica 1. Universitat Oberta de Catalunya.
# J. de Curtò i DíAz decurto@uoc.edu
# I. de Zarzà i Cubero dezarza@uoc.edu

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup
import pandas as pd

# Webpages to scrape:
# site[0]: Curiosity.
# site[1]: Perseverance.
site = ['https://mars.nasa.gov/msl/multimedia/raw-images/', 'https://mars.nasa.gov/mars2020/multimedia/raw-images']

# Start session in Firefox.
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to given site.
driver.get(site[0]) # Curiosity

# Slightly scroll the window to have header in view.
driver.execute_script("window.scrollTo(0, 400)") 

# Extract source.
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

# Get number of pages to crawl.
numberpages = driver.find_element_by_css_selector("span.total_pages")
npages = int(numberpages.text.replace(',', ''))

# Find all images in the first page.
img_tags = soup.findAll('img')
urls = [img['src'] for img in img_tags]

# Save URLs to CSV.
df = pd.DataFrame({"url" : urls})
df.to_csv("cyz.csv", index = False)

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
      # Extract source and images. Then save them to CSV.
      page_source = driver.page_source
      soup = BeautifulSoup(page_source, 'lxml')
      img_tags = soup.findAll('img')
      urls = [img['src'] for img in img_tags]
      df = pd.DataFrame({"url" : urls})
      df.to_csv("cyz.csv", mode = 'a', index = False, header = False)
      # Add delay to avoid unattended requests from the server.
      time.sleep(1)
      # Update counter.
      c += 1      
     
# Close browser window.
driver.quit()
