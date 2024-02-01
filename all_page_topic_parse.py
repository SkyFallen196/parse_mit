import requests
from bs4 import BeautifulSoup
import pandas as pd

topics = ['machine-learning', 'social-justice', 'startups', 'black-holes', 'classes-and-programs']
base_url = 'https://news.mit.edu/topic/'

all_urls = []

for topic in topics:
    page_num = 0
    urls = []
    while True:
        url = base_url + topic + '?page=' + str(page_num)
        response = requests.get(url).text
        data = BeautifulSoup(response, 'html.parser')
        titles = data.find_all('h3', class_='term-page--news-article--item--title')
        descriptions = data.find_all('p', class_='term-page--news-article--item--dek')
        dates = data.find_all('p', class_='term-page--news-article--item--publication-date')

        if len(titles) == 0:
            break

        for title, description, date in zip(titles, descriptions, dates):
            urls.append({
                'Topic': topic.replace('-', ' ').title(),
                'Title': title.a.span.text,
                'Description': description.span.text,
                'Date': date.time.text
            })

        page_num += 1

    all_urls.extend(urls)

df = pd.DataFrame(all_urls)
df.to_csv('mit_news_articles.csv', index=False)