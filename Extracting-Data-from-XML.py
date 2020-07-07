import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


Url = input('Enter location: ')

uh = urllib.request.urlopen(Url, context=ctx)
print('Retrieving', Url)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

total = sum([int(count.text) for count in tree.findall('comments/comment/count')])
count = len([count.text for count in tree.findall('comments/comment/count')])
print('Count',count)
print('Sum:',total)
