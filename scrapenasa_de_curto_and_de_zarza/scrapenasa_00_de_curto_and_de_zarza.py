# PAC. Pràctica 1. Universitat Oberta de Catalunya.
# J. de Curtò i DíAz decurto@uoc.edu
# I. de Zarzà i Cubero dezarza@uoc.edu

import re
import requests
from bs4 import BeautifulSoup
import dryscrape
import pandas as pd
import os
import validators

# Folder to save samples.
folder = 'samples_00/'
os.makedirs(folder)

# Webpages to scrape:
# site[0]: Curiosity.
# site[1]: Perseverance.
site = ['https://mars.nasa.gov/msl/multimedia/raw-images/', 'https://mars.nasa.gov/mars2020/multimedia/raw-images']

# Start session.
session = dryscrape.Session()
session.visit(site[1])

# Extract source.
response = session.body()
soup = BeautifulSoup(response, 'lxml')

# Find all images in the page.
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
