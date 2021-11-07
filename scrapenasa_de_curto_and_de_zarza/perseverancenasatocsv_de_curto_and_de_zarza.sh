#!/bin/bash
# PAC. Pràctica 1. Universitat Oberta de Catalunya.
# J. de Curtò i DíAz decurto@uoc.edu
# I. de Zarzà i Cubero dezarza@uoc.edu

# Need to be on appropriate path of images from Perseverance.

# Create CSV file with complete set of samples. 
'ls' > cyz.csv
echo "Total Number of Images from Perseverance" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l cyz.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Engineering Cameras
echo "Engineering Cameras:" >> statistics_perseverance_de_curto_and_de_zarza.txt

# Left Navigation Camera
ls -d NL*NCAM* > l_ncam.csv
echo "Left Navigation Camera:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l l_ncam.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Right Navigation Camera
ls -d NR*NCAM* > r_ncam.csv
echo "Right Navigation Camera:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l r_ncam.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Front Hazcam - left
ls -d FL*FHAZ* > l_fhaz.csv

echo "Front Hazcam - left:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l l_fhaz.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Front Hazcam - right
ls -d FR*FHAZ* > r_fhaz.csv

echo "Front Hazcam - right:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l r_fhaz.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Rear Hazcam - left
ls -d RL*RHAZ* > l_rhaz.csv

echo "Rear Hazcam - left:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l l_rhaz.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Rear Hazcam - right
ls -d RR*RHAZ* > r_rhaz.csv

echo "Rear Hazcam - right:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l r_rhaz.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# CacheCam
ls -d CC*CACH* > cc.csv

echo "CacheCam:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l cc.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Science Cameras
echo "Science Cameras:" >> statistics_perseverance_de_curto_and_de_zarza.txt
# Mastcam-Z Left
ls -d ZL*ZCAM* > l_zcam.csv

echo "Mastcam-Z Left:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l l_zcam.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Mastcam-Z Right
ls -d ZR*ZCAM* > r_zcam.csv

echo "Mastcam-Z Right:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l r_zcam.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# MEDA Skycam
ls -d WS*MEDA* > meda.csv

echo "MEDA Skycam:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l meda.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# PIXL Camera
ls -d PC* > pc.csv

echo "PIXL Camera:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l pc.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# SHERLOC - WATSON
ls -d SI*SRLC* > w_srlc.csv

echo "SHERLOC - WATSON:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l w_srlc.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# SHERLOC Context Imager
ls -d SC*SRLC* > context_srlc.csv

echo "SHERLOC Context Imager:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l context_srlc.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Supercam
ls -d *SCAM* > supercam.csv

echo "Supercam:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l supercam.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Entry, Descent and Landing
echo "Entry, Descent and Landing:" >> statistics_perseverance_de_curto_and_de_zarza.txt

# Parachute Up - A
ls -d EA*EDLC* > a_edlc.csv

echo "Parachute Up - A:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l a_edlc.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Parachute Up - B
ls -d EB*EDLC* > b_edlc.csv

echo "Parachute Up - B:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l b_edlc.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Descent Stage Down
ls -d ES*EDLC* > s_edlc.csv

echo "Descent Stage Down:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l s_edlc.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Rover Up 
ls -d EU*EDLC* > u_edlc.csv

echo "Rover Up:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l u_edlc.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Rover Down
ls -d ED*EDLC* > d_edlc.csv

echo "Rover Down:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l d_edlc.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Lander Vision System
ls -d EL*LVS* > lvs.csv

echo "Lander Vision System:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l lvs.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Ingenuity
echo "Ingenuity:" >> statistics_perseverance_de_curto_and_de_zarza.txt

# Navigation Camera
ls -d HN*HELI* > n_helicopter.csv
echo "Navigation Camera:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l n_helicopter.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

# Color
ls -d HS*HELI* > c_helicopter.csv
echo "Color:" >> statistics_perseverance_de_curto_and_de_zarza.txt
wc -l c_helicopter.csv >> statistics_perseverance_de_curto_and_de_zarza.txt

