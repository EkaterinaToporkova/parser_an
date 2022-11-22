import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas


data = []  # список анекдотов с указанных страниц

for p in range(100, 102):
    url = f'https://anek.ws/anekdot.php?a={p}'
    r = requests.get(url)  # получаем URL страницы
    sleep(3)  # после запроса делаем паузу на 3 секунды
    soup = BeautifulSoup(r.text, 'html.parser')
    anecdote = soup.find('div', {'id': 'anek'}).text

    data.append(anecdote.replace('\n', ''))

# запишем анекдоты в таблицу
header = ['anecdote']
df = pd.DataFrame(data, columns=header)
df.to_csv('data.csv', sep=';', encoding='utf8')
