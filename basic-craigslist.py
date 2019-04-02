from bs4 import BeautifulSoup
import urllib.request

start_url = 'https://newyork.craigslist.org/search/bar'
html = urllib.request.urlopen(start_url).read()
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.hdrlnk')

for title in titles:
    print (title.text)