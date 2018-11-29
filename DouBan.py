import requests
import re
from requests.exceptions import RequestException


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def pares_page(html):
    pattern = re.compile(
        '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'url':item[0],
            'name':item[1],
            'author':item[2],
            'date':item[3]
        }


if __name__ == "__main__":
    url = 'https://book.douban.com/'
    html = get_page(url)
    for item in pares_page(html):
        print(item)
 
