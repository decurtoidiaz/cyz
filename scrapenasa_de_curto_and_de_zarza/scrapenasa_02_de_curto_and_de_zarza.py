# PAC. Pràctica 1. Universitat Oberta de Catalunya.
# J. de Curtò i DíAz decurto@uoc.edu
# I. de Zarzà i Cubero dezarza@uoc.edu

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd

# Webpage to scrape:
# Perseverance.
site = 'https://mars.nasa.gov/mars2020/multimedia/raw-images'

# Start Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to given site.
driver.get(site) # Perseverance

# Slightly scroll the window to have button in view.
driver.execute_script("window.scrollTo(0, 400)") 

# Extract source.
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

# Find all images and comments in the first page.
img_tags = soup.findAll('img')
urls = [img['src'] for img in img_tags]
alts = [img['alt'] for img in img_tags]

# Save them to CSV.
df = pd.DataFrame({"url" : urls, "description" : alts})
df.to_csv("cyz.csv", index = False)

# Select next button to proceed to following page.
next_button = driver.find_elements_by_class_name("next")

# Do the same for the following pages.
while next_button:
      # Click on next button to load new content.
      driver.execute_script("arguments[0].click();", next_button[0])
      # Select next button for the following iteration.
      next_button = driver.find_elements_by_class_name("next")
      # Extract source and images. Then save them to CSV.
      page_source = driver.page_source
      soup = BeautifulSoup(page_source, 'lxml')
      img_tags = soup.findAll('img')
      urls = [img['src'] for img in img_tags]
      alts = [img['alt'] for img in img_tags]     
      df = pd.DataFrame({"url" : urls, "description" : alts})
      df.to_csv("cyz.csv", mode='a', index = False, header = False)
      # Add delay to avoid unattended requests from the server.
      time.sleep(1)

# Close browser window
driver.quit()
