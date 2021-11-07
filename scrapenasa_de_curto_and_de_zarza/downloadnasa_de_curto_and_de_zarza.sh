#!/bin/bash
# PAC. Pràctica 1. Universitat Oberta de Catalunya.
# J. de Curtò i DíAz decurto@uoc.edu
# I. de Zarzà i Cubero dezarza@uoc.edu

# Get unique URLs from crawled CSV.
sort -u cyz.csv -o cyz+.csv
# Download images with proper delay. You can run this command more than once if
# the connection gets unstable and will check whether the files are already there.
wget -w 3 --random-wait -c -i cyz+.csv
# Convert to PNG (or other) using Imagemagick. > sudo apt install imagemagick
mogrify -format png *.jpg
