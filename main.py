

import json

import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}


def get_articles_urls(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    pagination_count = int(soup.find('nav', class_='pages-list').find_all('a')[-1].text)

    articles_urls_list = []
    # print(pagination_count)
    for page in range(1, pagination_count + 1):
        # for page in range(1, 100):

        response = s.get(url=f'https://topwar.ru/armament/page/{page}/', headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        articles_urls = soup.find_all('a', class_='item-link')

        for au in articles_urls:
            art_url = au.get('href')
            articles_urls_list.append(art_url)

        # time.sleep(randrange(2, 5))
        print(f'Обработал {page}/{pagination_count}')
    # заменить txt файл
    with open('new_art.txt', 'w') as file:
        for url in articles_urls_list:
            file.write(f'{url}\n')

    return 'Работа по сбору ссылок выполнена!'


def get_data(file_path):
    with open(file_path) as file:
        urls_list = [line.strip() for line in file.readlines()]

    urls_count = len(urls_list)

    s = requests.Session()
    i = 0

    result_data = []

    for url in enumerate(urls_list):
        # print(url)
        response = s.get(url=url[1], headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        article_title = soup.find('article').find("h1", {'class': 'heading fs-15 fs-sm-2 fs-md-2 font'}).text.strip()
        article_data = soup.find('div', class_="meta fs-0875 c-muted fw-b").find('time',
                                                                                 class_='meta__time').text.strip()
        article_img = f"https://topwar.ru{soup.find('img').get('src')}"
        article_text = soup.find('div', class_='pfull-cont text').text.strip().replace("\n", "")
        # print(article_img)

        result_data.append(
            {
                'url': url[1],
                'article_title': article_title,
                'article_data': article_data,
                'article_img': article_img,
                "article_text": article_text

            }
        )
        # print(f"{article_title}\n {article_data}\n{article_img}\n {10 * '*' }")
        print(f'Обработал {url[0] + 1}/ {urls_count}')

    with open('result.json', 'w', encoding="utf-8") as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)
#
#
def main():
    get_data('new_art.txt')
    # print(get_articles_urls(url="https://topwar.ru/armament/"))


if __name__ == '__main__':
    main()
