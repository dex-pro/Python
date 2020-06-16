import urllib.request , urllib.error
import xml.etree.ElementTree as ET
import ssl
c=0
url = 'http://py4e-data.dr-chuck.net/comments_495533.xml'
l=list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
file = urllib.request.urlopen(url, context=ctx)
data=file.read()
commentinfo=ET.fromstring(data)
l=commentinfo.findall('comments/comment')
for i in l:
    print(i.find('count').text)
    m=int(i.find('count').text)
    c=c+m
print(c)