import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://news.mit.edu/topic/machine-learning?page='
page_num = 0
urls = []

while True:
    url = base_url + str(page_num)
    response = requests.get(url).text
    data = BeautifulSoup(response, 'html.parser')
    topic = data.find('h1').text
    titles = data.find_all('h3', class_='term-page--news-article--item--title')
    descriptions = data.find_all('p', class_='term-page--news-article--item--dek')
    dates = data.find_all('p', class_='term-page--news-article--item--publication-date')

    if len(titles) == 0:
        break

    for title, description, date in zip(titles, descriptions, dates):
        urls.append({
            'Topic': topic,
            'Title': title.a.span.text,
            'Description': description.span.text,
            'Date': date.time.text
        })

    page_num += 1

    df = pd.DataFrame(urls)
    df.to_csv('machine_learning_news.csv', index=False)
