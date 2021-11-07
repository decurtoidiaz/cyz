#!/bin/bash
# PAC. Pràctica 1. Universitat Oberta de Catalunya.
# J. de Curtò i DíAz decurto@uoc.edu
# I. de Zarzà i Cubero dezarza@uoc.edu

# Get pip3 on your system.
sudo apt-get update
sudo apt-get -y install python3-pip

# Then install the following dependencies (pip3 may need sudo depending on your configuration):
# Pandas. Usage: create CSV file.
pip3 install pandas
# Validators. Usage: URL Validation.
pip3 install validators
# Requests. Usage: Web scraping.
pip3 install requests
# Beautifulsoup. Usage: Web scraping.
pip3 install beautifulsoup4
# dryscrape. Usage: Web scraping (dynamic content).
sudo apt-get -y install qt5-default libqt5webkit5-dev build-essential python-lxml python-pip xvfb
pip3 install dryscrape
# Selenium. Usage: Web scraping (dynamic content). Able to traverse through several pages of dynamic content.
pip3 install selenium
