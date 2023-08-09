import requests
from bs4 import BeautifulSoup
import cfscrape



URL = 'https://hard.rozetka.com.ua/computers/c80095/'

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Alt-Used': 'https://hard.rozetka.com.ua/computers/c80095/',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'https://hard.rozetka.com.ua/computers/c80095/',
        'TE': 'Trailers',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

response = requests.get(URL)
cookies = response.cookies.get_dict()
print(cookies)

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params, cookies=cookies)
    print(r.text)

    # def parse():
    #     html = get_html(URL)
    #     print(html)



if __name__ == '__main__':
    get_html(URL)







    # header = {
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    #     'cache-control': 'max-age=0',
    #     'dnt': '1',
    #     'pragma': 'no-cache',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-site': 'same-origin',
    #     'sec-fetch-user': '?1',
    #     'upgrade-insecure-requests': '1',
    #     'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36'}

    # session = requests.Session()
    # session.headers = header
    # r = session.get(url)
    # print(r)






    # req = requests.get(url, headers=header)
    # soup = BeautifulSoup(req.text, 'html.parser')
    # categori = soup.find_all("div", class_='goods-tile__inner')
    # print(req)


# if __name__ == '__main__':
#     roz()