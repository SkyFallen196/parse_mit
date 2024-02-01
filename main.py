import requests
from bs4 import BeautifulSoup

url = 'https://news.mit.edu/topic/machine-learning'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')

titles = data.find_all('h3', class_='term-page--news-article--item--title')
descriptions = data.find_all('p', class_='term-page--news-article--item--dek')
dates = data.find_all('p', class_='term-page--news-article--item--publication-date')

for title, description, date in zip(titles, descriptions, dates):
    print("Title:", title.a.span.text)
    print("Description:", description.span.text)
    print("Date:", date.time.text)
    print("\n")