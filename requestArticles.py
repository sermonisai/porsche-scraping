import requests
from bs4 import BeautifulSoup
from datetime import datetime

base = 'https://newsroom.porsche.com'

reponse = requests.get(base)

html = reponse.text

soup = BeautifulSoup(html, 'html.parser')

articles = soup.find_all('article', 'teaser')

urls = []

for article in articles:
	try:
		date = article.time['datetime']
		date = datetime.strptime(date, "%d/%m/%Y")
		month = date.month
	except:
		month = '0'
	
	try:
		link = article.find_all('a')[0].get('href')

		if link[0] == "/":
			url = base + link
		else:
			url = link
		
	except:
		url = 'None'
	if month == 6 :
		if(url != "#"):
			urls.append(url)

print(urls)
