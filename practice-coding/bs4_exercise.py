import ssl
import urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#request the user for an url
url = input('Enter an url: ')

#make the request and open the url, ignoring the context and read the whole file
html = urllib.request.urlopen(url, context=ctx).read()

#use the BeautifulSoup library to deal with all the html and parse it
soup = BeautifulSoup(html, 'html.parser')

#retrieve all the <a> tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))



