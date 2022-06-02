import os.path
import requests
import pathlib
from pathlib import Path
import json

from bs4 import BeautifulSoup

# открываем json файл
with open ('result.json', 'r', encoding='utf-8') as file:
    text = json.load(file)


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
# url = 'https://topwar.ru/195634-kolt-brauning-posledovatelnyj-put-k-sovershenstvu.html'
i = 0
count_row = int(len(text))
# count_row = 1

for i in range(count_row):


# for i in range(1):
    # берем URL адресс страницы
    # url = 'https://topwar.ru/195634-kolt-brauning-posledovatelnyj-put-k-sovershenstvu.html'

    url = text[i]["url"]
    text_url = text[i]["article_text"]
    data_text = text[i]["article_data"]
    name_title_path = text[i]["article_title"]
    response = requests.get(url)
    name_article_text = text[i]["article_text"]
    soup = BeautifulSoup(response.content, 'lxml')
# указываем местонахождение всех картинок
    images = soup.find('div', class_="pfull-cont text").find_all('img')
# указываем местонахождение подписи всех картинок
    name_images = soup.find('div', class_="pfull-cont text").find_all('span')




# перебор ссылки на картинку и соответствующей картинке подписи
    for image, name in zip(images, name_images):
        src = image.get("src")
        name = name.text.replace('http://www.', '')
        name = name.replace('?', "")
        name = name.replace('!', "")
        name = name.replace('"', "")
        name = name.replace('»', "")
        name = name.replace('«', "")
        name = name.replace(':', "")
        name = name.replace('.', "")
        name = name.replace('"', "")
        name = name.replace('/', "")
        name = name.replace('*', "")
        name = name.replace('(', "")
        name = name.replace(')', "")
        name = name.replace(',', "")
        name = name.replace('–', "")
        name = name.replace('50 Акцион Экспресс 127x326 миллиметра', "")

        name = name.replace('.jpg', "")
        name = name[0:65]



        name_title_path = name_title_path.replace('?', "")
        name_title_path = name_title_path.replace('!', "")
        name_title_path = name_title_path.replace('»', "")
        name_title_path = name_title_path.replace('«', "")
        name_title_path = name_title_path.replace(':', "")
        name_title_path = name_title_path.replace('.', "")
        name_title_path = name_title_path.replace('"', "")
        name_title_path = name_title_path.replace('.jpg', "")
        name_title_path = name_title_path.replace('/', "")

        name_article_text = name_article_text.replace('?', "")
        name_article_text = name_article_text.replace('!', "")
        name_article_text = name_article_text.replace('»', "")
        name_article_text = name_article_text.replace('«', "")
        name_article_text = name_article_text.replace(':', "")
        name_article_text = name_article_text.replace('.', "")
        name_article_text = name_article_text.replace('"', "")
        name_article_text = name_article_text.replace('.jpg', "")
        name_article_text = name_article_text.replace('/', "")


        if not os.path.exists('upload/' + name_title_path):
            os.mkdir('upload/' + name_title_path)
        else:

            if "uploads/posts" in src:

                article_img = f"https://topwar.ru{src}"
                download_picture = requests.get(article_img).content
                name.join('.jpg')

                with open ('upload/' + name_title_path + '/' + name +'.jpg', 'wb') as handler:

                     handler.write(download_picture)
                     print(f'Обработал {i}/ {count_row}')
                with open ('upload/' + name_title_path + '/' + data_text +'.txt', 'w', encoding="utf-8") as file:
                    json.dump(text_url, file, indent=4, ensure_ascii=False, )


