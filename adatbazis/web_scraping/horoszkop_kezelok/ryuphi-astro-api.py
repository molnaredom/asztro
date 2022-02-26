import datetime
import requests


def get_basic_datas(ev, honap, nap, ora, perc, mp, varos):
    szelesseg, hosszusag = varos_poz(varosnev=varos.lower())
    start = datetime.datetime.now()
    adat = requests.get(
        f'https://dev-astrology-api.herokuapp.com/'
        f'horoscope?time={ev}-{honap}-{nap}T{ora}:{perc}:{mp}%2B02:00&latitude={szelesseg}&longitude={hosszusag}')

    end = datetime.datetime.now()
    print("runtime api", end - start)

    return adat.json()["data"]["houses"]


def varos_poz(varosnev):
    if varosnev == "szolnok": return "47.11", "20.12"
    if varosnev == "vac": return "47.11", "20.12"
    if varosnev == "budapest": return "47.11", "20.12"
    if varosnev == "siofok": return "47.11", "20.12"
    if varosnev == "szeged": return "47.11", "20.12"
    if varosnev == "pecs": return "47.11", "20.12"
    if varosnev == "debrecen": return "47.11", "20.12"
    if varosnev == "sopron": return "47.11", "20.12"
    if varosnev == "keszthely": return "47.11", "20.12"
    if varosnev == "veszprem": return "47.11", "20.12"
    if varosnev == "gyor": return "47.11", "20.12"
    if varosnev == "": return "47.11", "20.12"
    if varosnev == "szolnok": return "47.11", "20.12"


print(get_basic_datas("2001", "08", "19", "16", "54", "00", "Szolnok"))

## todo timezone
