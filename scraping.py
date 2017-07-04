from bs4 import BeautifulSoup
from urllib import urlopen
html = urlopen("http://10.10.21.130/xml/get_live_status.xml?")
bsObj = BeautifulSoup(html.read(), "xml")
x = bsObj.find("text")
print(x.text)
