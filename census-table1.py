from bs4 import BeautifulSoup
import urllib.request
import csv

start_url = 'https://www.census.gov/quickfacts/ks'
html = urllib.request.urlopen(start_url).read()
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('tbody', attrs={'data-topic':'Population'})

f = csv.writer(open("ks-data.csv", "w"))

rows = table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if len(cols) > 0:
    	f.writerow([cols[0], cols[1]])