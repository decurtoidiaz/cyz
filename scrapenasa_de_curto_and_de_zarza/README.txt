/* CyZ: MARS Space Exploration Dataset. 	    

   Authors: De Curtò i DíAz and De Zarzà i Cubero.
   c@decurto.be z@dezarza.be 						    */
                                          
                              ,----, 
  ,----..                   .'   .`| 
 /   /   \               .'   .'   ; 
|   :     :            ,---, '    .' 
.   |  ;. /            |   :     ./  
.   ; /--`      .--,   ;   | .'  /   
;   | ;       /_ ./|   `---' /  ;    
|   : |    , ' , ' :     /  ;  /     
.   | '___/___/ \: |    ;  /  /--,   
'   ; : .'|.  \  ' |   /  /  / .`|   
'   | '/  : \  ;   : ./__;       :   
|   :    /   \  \  ; |   :     .'    
 \   \ .'     :  \  \;   |  .'       
  `---`        \  ' ;`---'           
                `--`                 
README

To run the examples, install dependencies:
	
	$ bash dependencies_scrapenasa_de_curto_and_de_zarza.sh

In order to use selenium (https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/) you need to have on path the webdriver of Firefox (geckodriver: https://github.com/mozilla/geckodriver/releases). Download it and add to path appropriately:

	$ export PATH=$PATH:/path/to/geckodriver >> ~/.profile
	$ source ~/.profile

Then run one of the scripts:
		
	$ python3 scrapenasa_04_de_curto_and_de_zarza.py

Key: scrapenasa_0-4_de_curto_and_de_zarza.py
	00: Curiosity and Perseverance. Load dynamic content using dryscrape and beautifulsoup from one page, download images and output CSV file.
	01: Curiosity and Perseverance. Load dynamic content using selenium and beautifulsoup from all pages by changing the value of the header by doing double-click. Output: CSV file with URLs.
	02: Perseverance. Load dynamic content using selenium and beautifulsoup from all pages by doing click on next button. Output: CSV file with URLs.
	03: Curiosity and Perseverance. Load dynamic content using selenium and beautifulsoup from all pages by doing click on next button. Output: downloaded images and CSV file with URLs.
	04: Curiosity and Perseverance. Load dynamic content using selenium and beautifulsoup from all pages by changing the value of the header by doing double-click. Additional URL validation and regular expression to check for well-defined samples. Output: CSV file with URLs.
	
There are several utilities to extract images for a given camera from Perseverance or Curiosity. For example, run:

	$ bash perseverancenasatocsv_de_curto_and_de_zarza.sh

To download images given an output CSV and convert them to PNG format using imagemagick use:

	$ bash downloadnasa_de_curto_and_de_zarza.sh
