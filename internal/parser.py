import requests
from bs4 import BeautifulSoup as bs
import shutil

def download_image_from_url(url):
    """ 
    Функция принимает ссылку на изображение и пытается сохранить ее
    в корневую директорию проекта
    """
    response = requests.get(url, stream=True)
    with open('img-' + url.split('/')[-1][:-4] + '.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

def parse_url(r, res):
    """
    Функция принимает html страницы из requests.get() и желаемое разрешение изображения
    Фунция отбирает нужные блоки и ищет a-теги для получения ссылок на изображения
    после чего вызывает функцию сохранения изображения.
    """
    soup = bs(r.text, features="html.parser")
    tables=soup.find('div', {'id': 'article__content'}) #Получаем див с обоями
    tables = tables.find_all('ul') 

    for a_block in tables:
        tmp = a_block.find_all('a')

        for link in tmp:
            if link.text == res:
                href_str = link.get('href')
                if href_str.startswith('http://files.smashingmagazine.com'):
                    download_image_from_url(href_str)
