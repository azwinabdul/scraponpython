import urllib
from BeautifulSoup import BeautifulSoup

url = 'http://10.10.21.130/xml/get_live_status.xml?'
res = urllib.urlopen(url)
html = res.read()

soup = BeautifulSoup(html)

soup.prettify()

data_web = soup.findAll('data')

for eachdata in data_web:
    another_duration = eachdata('duration')
    print eachdata
