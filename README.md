# Cars Scraper
Cars Scraper will collect data from Avito and Drom web-sources. 

Its finds cars offers from all Russia, sorts from lowest to highest price and puts it in GUI or in terminal.

# Features Overview
•	Avito Cars scraper

•	Drom scraper

•	Sort by price

# How To Use Scraper
run: pip install -r requirements.txt in your shell 

run: gui.py

Or you can do it manually and use classes, results will be print in terminal.


## Collect data from Avito & Drom
``` python
from avito import Avito
from drom import Drom


def collect_data(model: str, pages: int):
    """Get list of cars from sources"""
    collected_data = []
    for page in range(1, pages):
        # collecting always starts from 1-t page
        print(f"Собираю информацию со страницы - {page}")
        avito_cars = Avito(model, page)
        drom_cars = Drom(model, page)
        # if source havn`t got data on one of the page, it will be empty [] list
        # so we dont need it
        data_from_avito = list(avito_cars.get_content())
        if data_from_avito:
            collected_data += data_from_avito
        data_from_drom = list(drom_cars.get_content())
        if data_from_drom:
            collected_data += data_from_drom
    collected_data.sort(key=lambda i: i[1])
    print("\nВот, что я нашел:")
    for i in range(len(collected_data)):
        print(
            collected_data[i][0] + "г., ",
            "Цена - ", collected_data[i][1], "₽",
            ", Источник: ", collected_data[i][2],
        )
```

## Collect data from Avito
``` python
from avito import Avito


def collect_data(model: str, pages: int):
    """Get list of cars from sources"""
    collected_data = []
    for page in range(1, pages):
        # collecting always starts from 1-t page
        print(f"Собираю информацию со страницы - {page}")
        avito_cars = Avito(model, page)
        data_from_avito = list(avito_cars.get_content())
        # if source havn`t got data on one of the page, it will be empty [] list
        # so we dont need it
        if data_from_avito:
            collected_data += data_from_avito
    # sort from lowest to highest price
    collected_data.sort(key=lambda i: i[1])
    print("\nВот, что я нашел:")
    for i in range(len(collected_data)):
        print(
            collected_data[i][0] + "г., ",
            "Цена - ", collected_data[i][1], "₽",
            ", Источник: ", collected_data[i][2],
        )
```

# Future opportunities
•	Sort by city

•	Save results in excel, csv file

# Author
•	Vlad Dunaev
