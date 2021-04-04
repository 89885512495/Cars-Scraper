import requests
from bs4 import BeautifulSoup
from headers import headers


class Avito:
    """
    Avito avtomobili scraper
    -----------------------
    https://www.avito.ru
    -----------------------
    Tag <div> - info car container,
    Tag <h3> - ad title (cars model and year),
    Tag <span> - the price of car,
    Tag <a> - link of ad.
    """

    tags = [
        (
            "div",
            "iva-item-root-G3n7v photo-slider-slider-3tEix "
            "iva-item-list-2_PpT items-item-1Hoqq items-listItem-11orH js-catalog-item-enum",
        ),
        (
            "h3",
            "title-root-395AQ iva-item-title-1Rmmj title-list-1IIB_ "
            "title-root_maxHeight-3obWc text-text-1PdBw text-size-s-1PUdo text-bold-3R9dt",
        ),
        ("span", "price-root-1n2wM price-list-14p4v"),
        (
            "a",
            "link-link-39EVK link-design-default-2sPEv title-root-395AQ "
            "iva-item-title-1Rmmj title-list-1IIB_ title-root_maxHeight-3obWc",
        ),
    ]

    headers = headers

    def __init__(self, brand: str, page: int):
        """Init instance of the class"""
        self.brand = brand
        self.page = page
        self.url = f"https://www.avito.ru/rossiya/avtomobili/{self.brand}?p={page}"

    def _get_request(self) -> object:
        """Get response from resource"""
        self.response = requests.get(self.url, headers=Avito.headers)
        if self.response.status_code:
            return self.response.content
        return

    def get_body(self) -> object:
        """Get body"""
        body = self._get_request()
        soup = BeautifulSoup(body, "html.parser")
        return soup

    def get_content(self) -> list:
        """Get content from body"""
        content = self.get_body()

        # find_all('div', class_="")
        for i in content.find_all(Avito.tags[0][0], class_=Avito.tags[0][1]):
            # then add cars to our data
            yield (
                i.find(Avito.tags[1][0], class_=Avito.tags[1][1]).get_text(
                    strip=True
                ),  # ad titile
                int(
                    i.find(Avito.tags[2][0], class_=Avito.tags[2][1])
                    .get_text(strip=True)[:8]
                    .replace("₽", "")
                    .replace(" ", "")
                    .replace("от", "")
                    .replace("_", "")
                    .replace("безскидки", "")
                ),  # car price
                "https://www.avito.ru"
                + i.find(Avito.tags[3][0], class_=Avito.tags[3][1]).get(
                    "href"
                ),  # link
            )


if __name__ == "__main__":

    for page in range(1, 2):
        avito = Avito("honda", page)
        print(list(avito.get_content()))
