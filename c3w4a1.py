# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl
import re
l=list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
s = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
t = s('td')
for i in t:
    if i is None:
        continue
    i=str(i)
    n=re.findall('[0-9]+',i)
    if n!=[]:
        n[0]=int(n[0])
        l.append(n[0])
print(sum(l))
