import requests
from bs4 import BeautifulSoup
import sqlite3


def base_roz():
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    query = '''CREATE TABLE IF NOT EXISTS roza(
    Title TEXT,
    Image TEXT,
    Price TEXT,
    Status TEXT
    )'''

    cursor.execute(query)

    url = "https://hard.rozetka.com.ua/computers/c80095/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    page_count = int(soup.find("div", class_="pagination ng-star-inserted").find_all("li",
                                                                        class_="ng-star-inserted")[-1].text.strip())
    print(f"Всего страниц: {page_count}")
    for page in range(1, page_count + 1):
        print(f'[INFO] Обработка {page} страницы')
        url = f"https://hard.rozetka.com.ua/computers/c80095/page={page}/"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        items = soup.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
        for item in items:
            try:
                title = item.find('a', class_='goods-tile__heading ng-star-inserted').text.strip()
                image = item.find('a', class_='goods-tile__picture ng-star-inserted').get('href').strip()
                price = item.find('div', class_='goods-tile__prices').find('p', class_='ng-star-inserted').text.strip()
                status = item.find('div', class_='goods-tile__availability').text.strip()

                cursor.execute('INSERT INTO roza VALUES(?,?,?,?)', (title, image, price, status))
                db.commit()
            except:
                ValueError()


if __name__ == '__main__':
    base_roz()







