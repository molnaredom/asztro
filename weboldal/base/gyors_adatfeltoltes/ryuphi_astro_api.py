import datetime
import requests

from feltoltes_kisegito_modul import *
from ..default_parameters import *

## todo timezone


def ryuphi_api_adatlehivo_manager(tulajdonso_adatok):
    # print("tulajdonos adatok",tulajdonso_adatok)
    kinyert_adatok = init_api(tulajdonso_adatok)
    # print("kinyert adatok",kinyert_adatok)
    return {"bolygok": get_bolygok(kinyert_adatok), "hazak": get_hazak(kinyert_adatok)}


def char2(char):
    if len(char) == 1:
        return "0" + char
    return char


def init_api(tulajdonos_adatok):
    printd(tulajdonos_adatok)
    ev = char2(str(tulajdonos_adatok["hi"]))
    honap = char2(str(tulajdonos_adatok["honap"]))
    nap = char2(str(tulajdonos_adatok["nap"]))
    ora = char2(str(tulajdonos_adatok["ora"]))
    perc = char2(str(tulajdonos_adatok["perc"]))
    mp = "00"  # tulajdonos_adatok["mp"]
    varos = char2(str(tulajdonos_adatok.hely))

    szelesseg, hosszusag = varos_poz(varosnev=ekezetnelkul(varos.lower()))

    start = datetime.datetime.now()
    adat = requests.get(
        # f'https://dev-astrology-api.herokuapp.com/'
        f'http://127.0.0.1:3000/'
        f'horoscope?time={ev}-{honap}-{nap}T{ora}:{perc}:{mp}%2B02:00&latitude={szelesseg}&longitude={hosszusag}')

    end = datetime.datetime.now()
    printi("API runtime", end - start)

    return adat.json()


def get_bolygok(chart):
    bolygok = dict()

    bolygo_objektumok = chart["data"]["astros"]
    for key, value in bolygo_objektumok.items():
        #print(key, value, )
        if key == "chiron":
            break
        bolygok[bolygo_to_hun(key)] = {"jegy": jegy_num_to_hun(str(value["sign"])),
                                       "fokszam": get_fokszam(value["position"]),
                                       "retográd": value["retrograde"],
                                       "gyorsaság": value["speed"]
                                       }
    # print(bolygok)

    #[print(i) for i in bolygok.items()]
    return bolygok


def get_fokszam(position):
    return str(float(position["longitude"]) % 30)


def get_hazak(chart):
    hazak = dict()

    hazakiter = chart["data"]["houses"]
    for i, value in enumerate(hazakiter, 1):
        hazak[i] = {"jegy": jegy_num_to_hun(str(value["sign"])), "fokszam": get_fokszam(value["position"])}

    #[print(i) for i in hazak.items()]

    return hazak


def jegy_num_to_hun(eng_jegy):
    if eng_jegy == "1":
        return "kos"
    elif eng_jegy == "2":
        return "bika"
    elif eng_jegy == "3":
        return "ikrek"
    elif eng_jegy == "4":
        return "rák"
    elif eng_jegy == "5":
        return "oroszlán"
    elif eng_jegy == "6":
        return "szűz"
    elif eng_jegy == "7":
        return "mérleg"
    elif eng_jegy == "8":
        return "skorpió"
    elif eng_jegy == "9":
        return "nyilas"
    elif eng_jegy == "10":
        return "bak"
    elif eng_jegy == "11":
        return "vízöntő"
    elif eng_jegy == "12":
        return "halak"


def bolygo_to_hun(eng_bolygo):
    if eng_bolygo == "sun":
        return "Nap"
    elif eng_bolygo == "moon":
        return "Hold"
    elif eng_bolygo == "mercury":
        return "Merkur"
    elif eng_bolygo == "venus":
        return "Mars"
    elif eng_bolygo == "mars":
        return "Jupiter"
    elif eng_bolygo == "jupiter":
        return "szűz"
    elif eng_bolygo == "saturn":
        return "Szaturnusz"
    elif eng_bolygo == "uranus":
        return "Uránusz"
    elif eng_bolygo == "neptune":
        return "Neptun"
    elif eng_bolygo == "pluto":
        return "Pluto"

#
# print(get_basic_datas("2001", "08", "19", "16", "54", "00", "Szolnok"))
