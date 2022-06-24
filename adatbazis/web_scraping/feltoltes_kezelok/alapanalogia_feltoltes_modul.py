import time
from tqdm import tqdm
from adatbazis.web_scraping.kisegito_modulok.feltoltes_kisegito_modul import szoveggelkitoltes, feltoltes


def alapanalogia_feltoltes(web, alapanalogiak, domain):
    time.sleep(0.5)
    jegy_feltoltes(web, alapanalogiak, domain)
    time.sleep(0.5)
    bolygo_feltoltes(web, alapanalogiak, domain)
    time.sleep(0.5)
    haz_feltoltes(web, alapanalogiak, domain)


def jegy_feltoltes(web, feltoltendo, domain):

    web.get(f'{domain}/create-jegyek/')

    for jegy in tqdm(feltoltendo["jegyek"].keys(), desc="Jegyek feltöltése"):
        for adat_nev in ["nevID", "leírás", "elem", "minőség", "paritás", "évszak", "uralkodo_bolygo"]:

            szoveggelkitoltes(web, feltoltendo,"jegyek", jegy, adat_nev)

        feltoltes(web)
        time.sleep(0.5)


def bolygo_feltoltes(web, feltoltendo:dict, domain):
    web.get(f'{domain}/create-bolygok/')

    for bolygo in tqdm(feltoltendo["bolygok"].keys(), desc="Bolygók feltöltése"):
        for adat_nev in ["nevID", "leírás", "pontérték", "típus"]:

            szoveggelkitoltes(web, feltoltendo,"bolygok", bolygo, adat_nev)

        feltoltes(web)
        time.sleep(0.5)


def haz_feltoltes(web, feltoltendo, domain):
    web.get(f'{domain}/create-hazak/')

    for haz in tqdm(feltoltendo["hazak"].keys(), desc="Házak feltöltése"):
        for adat_nev in ["nevID", "leírás", "mundán jegye", "típus"]:
            szoveggelkitoltes(web, feltoltendo, "hazak", haz, adat_nev)

        feltoltes(web)
        time.sleep(0.5)
