import datetime
import socket

import requests

from ..kisegito import kisegito, idoszamitas


def ryuphi_api_adatlehivo_manager(tulajdonso_adatok):
    kinyert_adatok = init_api(tulajdonso_adatok)
    return {"bolygok": get_bolygok(kinyert_adatok), "hazak": get_hazak(kinyert_adatok)}


def char2(char):
    if len(str(char)) == 1:
        return "0" + str(char)
    return char


def init_api(obj):
    datumido = obj.idopont

    szelesseg, hosszusag = kisegito.varos_poz(varosnev=kisegito.ekezetnelkul(str(obj.hely).lower()))

    start = datetime.datetime.now()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 3000))

    datumido_teljes_str = f'{char2(datumido.year)}-{char2(datumido.month)}-{char2(datumido.day)}T' \
                          f'{char2(datumido.hour)}:{char2(datumido.minute)}:{char2(datumido.second)}'

    idozona = idoszamitas.idoszamitas(datumido)

    if result == 0:
        print("Port is open : 3000")
        adat = requests.get(
            f'http://127.0.0.1:3000/'
            f'horoscope?time='
            f'{datumido_teljes_str}'
            f'%2B0{idozona}:00&latitude={szelesseg}&longitude={hosszusag}')
    else:
        print("Port is not open --> web api")
        adat = requests.get(
            f'https://dev-astrology-api.herokuapp.com/'
            f'horoscope?time='
            f'{datumido_teljes_str}'
            f'%2B0{idozona}:00&latitude={szelesseg}&longitude={hosszusag}')

    sock.close()

    end = datetime.datetime.now()
    print("API Futásidő: ", end - start)

    return adat.json()


def get_bolygok(chart):
    bolygok = dict()

    bolygo_objektumok = chart["data"]["astros"]
    for key, value in bolygo_objektumok.items():
        if key == "chiron":
            break

        fokszam = float(get_fokszam(value["position"]))
        print(key,fokszam)
        tizedesresz = (fokszam-int(fokszam))/10*6
        korrigalt_fokszam = int(fokszam) + tizedesresz
        print(key,korrigalt_fokszam)
        bolygok[kisegito.bolygo_to_hun(key)] = {
            "jegy": kisegito.jegy_num_to_hun(str(value["sign"])),
            "fokszam": korrigalt_fokszam,
            "retográd": value["retrograde"],
            "gyorsaság": value["speed"]
        }
    # [print(i) for i in bolygok.items()]
    return bolygok


def get_fokszam(position):
    return str(float(position["longitude"]) % 30)


def get_hazak(chart):
    hazak = dict()

    hazakiter = chart["data"]["houses"]
    for i, value in enumerate(hazakiter, 1):
        hazak[i] = {"jegy": kisegito.jegy_num_to_hun(str(value["sign"])),
                    "fokszam": get_fokszam(value["position"])}
        print(hazak[i])

    # [print(i) for i in hazak.items()]
    return hazak
