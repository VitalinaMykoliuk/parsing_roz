import requests
from bs4 import BeautifulSoup
import logging


logging.basicConfig(level=logging.INFO)


def roz():
    url = "https://hard.rozetka.com.ua/computers/c80095/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    page_count = int(soup.find("div", class_="pagination ng-star-inserted").find_all("li",
                                                                      class_="ng-star-inserted")[-1].text.strip())


    print(f"Всего страниц: {page_count}")
    for page in range(1, page_count + 1):
        logging.info(f'Обработка {page} страницы')
        url = f"https://hard.rozetka.com.ua/computers/c80095/page={page}/"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        items = soup.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
        for item in items:
            try:
                title = item.find('a', class_='goods-tile__heading ng-star-inserted').text.strip()
                image = item.find('a', class_='goods-tile__picture ng-star-inserted').get('href').strip()
                link = item.find('a', class_='goods-tile__heading')['href']
                price = item.find('div', class_='goods-tile__prices').find('p', class_='ng-star-inserted').text.strip()
                status = item.find('div', class_='goods-tile__availability').text.strip()
                await asyncio.sleep(2)
                await bot.send_photo(call.from_user.id, image, caption="<b>" + title + "</b>\n<i>" +
                                     price + "</i>\n<i>" + status + f"</i>\n<a href='{link}'>Ссылка на фильм</a>",
                                     parse_mode='html')

            except:
                ValueError()


if __name__ == '__main__':
    roz()



