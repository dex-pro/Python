import json
import urllib.request , urllib.parse , urllib.error
url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_495534.json')
data=url.read().decode()
info = json.loads(data)
l=list()
print('User count:', len(info))
try:
    js=json.loads(data)
except:
    js=None
if not js or 'status' not in js or js['status']!='OK':
    print('Failed')
for i in js:
    r=js['comments']
for m in range(len(r)):
    n=r[m]
    l.append(int(n['count']))
print(sum(l))