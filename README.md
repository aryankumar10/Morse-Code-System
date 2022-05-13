# Morse-Code-System
Source code for the morse code system using bolt IoT module and python

1. Create a file named conf.py and store your personal device ID and API key in it.
2. Content of conf.py :<br/>
``` API_KEY = "api_key"```<br/>
```DEVICE_ID = "device_id"```<br/>
Replace the value inside the double quotes with your personal API key and device ID
3. Save the file in the same directory as the source code.
4. Install required libraries :<br/>
```sudo apt-get update```<br/>
```sudo pip3 install boltiot```<br/>
```sudo pip3 install pyOpenSSL ndg-httpsclient pyasn1```<br/>
```sudo pip3 install 'requests[security]'```<br/>
5. Run morse.py
