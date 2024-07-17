import pandas as pd
from bs4 import BeautifulSoup
import requests
'''
import pandas as pd
urls = ['https://casa-musica.com/ru/19-muzyka-cd-mp3']
alb = []
for i in range(2, 89):
    urls.append(f'https://casa-musica.com/ru/19-muzyka-cd-mp3?page={i}')

df = pd.DataFrame(urls)
df.to_csv('urls.csv', index=False)
'''
file = pd.read_csv('urls.csv')
alb = []
for i in range(2):
    try:
        url = file['0'][i]
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        heads = soup.find_all('div', class_='product-meta')
        for head in heads:
            title = head.find('h3', class_='h3 product-title').text.replace('\n', '')
            url = head.find('h3', class_='h3 product-title').find('a')['href'].replace('\n', '')
            artist_name = head.find('div', class_='artist-name').text.replace('\n', '')
            price = head.find('div', class_='price').text.replace('\n', '').replace('\xa0', '')
            alb.append([title, url, artist_name, price])
    except:
        print(f'Ошибка в парсинге страницы №{i+1}')

alb = pd.DataFrame(alb)
alb.to_csv('alb.csv', index=False)
