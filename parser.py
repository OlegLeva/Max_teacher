import requests
from bs4 import BeautifulSoup

def get_html(url):
    result = requests.get(url)
    return result.text

def get_title(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('title')
    print(title.text)


def main():
    html = get_html('https://www.python.org/')
    get_title(html)

if __name__ == '__main__':
    main()