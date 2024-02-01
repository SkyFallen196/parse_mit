import requests
from bs4 import BeautifulSoup

base_url = 'https://news.mit.edu/topic/machine-learning?page='
page_num = 0
urls = []

while True:
    url = base_url + str(page_num)
    response = requests.get(url).text
    data = BeautifulSoup(response, 'html.parser')
    topic = ... # get the topic name
    titles = data.find_all('h3', class_='term-page--news-article--item--title')
    descriptions = data.find_all('p', class_='term-page--news-article--item--dek')
    dates = data.find_all('p', class_='term-page--news-article--item--publication-date')

    if len(titles) == 0:
        break

    for title, description, date in zip(titles, descriptions, dates):
        print(title.a.span.text, description.span.text, date.time.text, sep=';')

    page_num += 1
