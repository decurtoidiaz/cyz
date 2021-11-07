#!/bin/bash
# PAC. Pràctica 1. Universitat Oberta de Catalunya.
# J. de Curtò i DíAz decurto@uoc.edu
# I. de Zarzà i Cubero dezarza@uoc.edu

# Need to be on appropriate path of images from Curiosity.

# Create CSV file with complete set of samples. 
'ls' > cyz.csv
echo "Total Number of Images from Curiosity" >> statistics_curiosity_de_curto_and_de_zarza.txt
wc -l cyz.csv >> statistics_curiosity_de_curto_and_de_zarza.txt

# Curiosity
echo "Engineering Cameras:" >> statistics_curiosity_de_curto_and_de_zarza.txt

# Front Hazcam
ls -d *FHAZ* > fhaz.csv

echo "Front Hazcam:" >> statistics_curiosity_de_curto_and_de_zarza.txt
wc -l fhaz.csv >> statistics_curiosity_de_curto_and_de_zarza.txt

# Rear Hazcam
ls -d *RHAZ* > rhaz.csv

echo "Rear Hazcam:" >> statistics_curiosity_de_curto_and_de_zarza.txt
wc -l rhaz.csv >> statistics_curiosity_de_curto_and_de_zarza.txt

# Navigation Camera - Left
ls -d NL*NCAM* > l_ncam.csv

echo "Navigation Camera - Left:" >> statistics_curiosity_de_curto_and_de_zarza.txt
wc -l l_ncam.csv >> statistics_curiosity_de_curto_and_de_zarza.txt

# Navigation Camera - Right
ls -d NR*NCAM* > r_ncam.csv

echo "Navigation Camera - Right:" >> statistics_curiosity_de_curto_and_de_zarza.txt
wc -l r_ncam.csv >> statistics_curiosity_de_curto_and_de_zarza.txt

# Science Cameras
echo "Science Cameras:" >> statistics_curiosity_de_curto_and_de_zarza.txt

# CCAM
ls -d *CCAM* > cc.csv

echo "CCAM:" >> statistics_curiosity_de_curto_and_de_zarza.txt
wc -l cc.csv >> statistics_curiosity_de_curto_and_de_zarza.txt

# MD
ls -d *MD* > md.csv

echo "MD:" >> statistics_curiosity_de_curto_and_de_zarza.txt
wc -l md.csv >> statistics_curiosity_de_curto_and_de_zarza.txt

# MH
ls -d *MH* > mh.csv

echo "MH:" >> statistics_curiosity_de_curto_and_de_zarza.txt
wc -l mh.csv >> statistics_curiosity_de_curto_and_de_zarza.txt

# ML
ls -d *ML* > ml.csv

echo "ML:" >> statistics_curiosity_de_curto_and_de_zarza.txt
wc -l ml.csv >> statistics_curiosity_de_curto_and_de_zarza.txt

