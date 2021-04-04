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
    # sort from lowest to highest price
    collected_data.sort(key=lambda i: i[1])
    print("\nВот, что я нашел:")
    for i in range(len(collected_data)):

        print(
            collected_data[i][0] + "г., ",
            "Цена - ", collected_data[i][1], "₽",
            ", Источник: ", collected_data[i][2],
        )


if __name__ == "__main__":
    collect_data("toyota", pages=2)
