import requests
from bs4 import BeautifulSoup
from headers import headers


class Drom:
    """
        Drom scraper
        -----------------------
        https://www.drom.ru
        -----------------------
        i won't use class tags, no need to do it there.
    """
    headers = headers

    def __init__(self, brand: str, page: int):
        """Init instance of the class"""
        self.brand = brand
        self.page = page
        self.url = f"https://auto.drom.ru/{self.brand}/all/page{self.page}/"

    def _get_request(self) -> object:
        """Get response from resource"""
        self.response = requests.get(self.url, headers=Drom.headers)
        if self.response.status_code:
            return self.response.content
        return

    def get_body(self) -> object:
        """Get body"""
        body = self._get_request()
        soup = BeautifulSoup(body, 'html.parser')
        return soup

    def get_content(self) -> list:
        """Get content from body"""
        content = self.get_body()
        for i in content.find_all('a', class_='css-1hgk7d1 eiweh7o2'):
            yield (
                # ad titile
                i.find('span').get_text(),
                # car price
                int(i.find(
                    'span', class_='css-jnatj e162wx9x0').get_text(strip=True).replace('q', '').replace(' ', '')),

                i.get('href')  # link

            )


if __name__ == '__main__':

    for page in range(1, 2):
        drom = Drom('honda', page)
        print(list(drom.get_content()))
