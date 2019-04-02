from bs4 import BeautifulSoup
import urllib.request
import csv

start_url = 'https://www.census.gov/quickfacts/ks'
html = urllib.request.urlopen(start_url).read()

soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('tbody')

f = csv.writer(open("ks-data-tables.csv", "w"))

for table in tables:
	heading = table.find('th')
	heading = heading.text
	f.writerow([heading])
	rows = table.find_all('tr')
	for row in rows:
	    cols = row.find_all('td')
	    cols = [ele.text.encode('utf-8').strip() for ele in cols]
	    if len(cols) > 0:
	    	f.writerow([cols[0], cols[1]])
	f.writerow(["", ""])