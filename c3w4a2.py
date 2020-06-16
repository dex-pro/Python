import urllib.request
from bs4 import BeautifulSoup
l=list()
l2=list()
count=0
fh = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Isla.html')
s=BeautifulSoup(fh,'html.parser')
t=s('a')
for i in t:
    n=i.get('href',None)
    l.append(n)
print(l[17])
for i in range(6):
    fh2 = urllib.request.urlopen(l[17])
    for x in range(len(l)):
        del(l[x-count])
        count=count+1
    count=0
    s2 = BeautifulSoup(fh2, 'html.parser')
    t2 = s2('a')
    for i2 in t2:
        n2=i2.get('href', None)
        l.append(n2)
    print(l[17])