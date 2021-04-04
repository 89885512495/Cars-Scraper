import PySimpleGUI as sg
from app import collect_data

# sg.theme_previewer()

sg.ChangeLookAndFeel("SystemDefault")

layout = [
    [sg.Text("Выберите марку автомобиля:", font=("Bahnschrift Light", 14))],
    [
        sg.InputCombo(
            ("audi", "bmw", "chery", "chevrolet", "citroen",
             "daewoo", "ford", "honda", "hyundai", "kia",
             "lifan", "land_rover", "lexus", "mazda", "mercedes-benz",
             "mitsubishi","nissan", "opel", "peugeot", "renault",
             "skoda", "ssangyong", "suzuki", "toyota", "volkswagen",
             "vaz_lada", "gaz", "uaz"),
            default_value="honda",
            key="-CARS-",
            size=(24, 0),
            font=("Bahnschrift Light", 12),
        )
    ],
    [sg.Text("Выберите кол-во страниц для поиска:", font=("Bahnschrift Light", 14))],
    [
        sg.InputCombo(
            ("5", "10", "25", "50", "100",),
            default_value="5",
            key="-PAGES-",
            size=(24, 0),
            font=("Bahnschrift Light", 12),
        )
    ],
    [sg.Output(size=(130, 25), font=("Bahnschrift Light", 12))],
    [
        sg.Button("Поиск", size=(10, 1), font=("Bahnschrift Light", 12)),
        sg.Exit("Выход", size=(10, 1), font=("Bahnschrift Light", 12)),
    ],
]

window = sg.Window("Поиск предложений по автомобилям", layout, icon="src/parser.ico")

while True:

    event, values = window.read()
    if event in (None, "Выход"):
        break
    elif event == "Поиск":
        collect_data(values["-CARS-"], int(values["-PAGES-"]))


window.close()
