import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx= ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

Url= input("Enter URL:  ")
count=int(input("Enter count: "))
position=int(input("Enter position: "))

for count in range(count): 
    html= urllib.request.urlopen(Url,context=ctx).read()
    soup=BeautifulSoup(html ,'html.parser')
    tags=soup('a')
    i=0
    for tag in tags:
        i=i+1
        if(i==position):
            Url=tag.get('href',0)
            print("Retrieving: ",Url)
