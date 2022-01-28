import time

from adatbazis.web_scraping.kisegito_modulok.feltoltes_kisegito_modul import szoveggelkitoltes, feltoltes


def alapanalogia_feltoltes(web, alapanalogiak, domain):
    feltoltendo = alapanalogiak

    jegy_feltoltes(web, feltoltendo, domain)
    bolygo_feltoltes(web, feltoltendo, domain)
    haz_feltoltes(web, feltoltendo, domain)


def jegy_feltoltes(web, feltoltendo, domain):
    web.get(f'{domain}/create-jegyek/')

    for jegy in feltoltendo["jegyek"].keys():
        for adat_nev in ["nevID", "leírás", "elem", "minőség", "paritás", "évszak", "uralkodo_bolygo"]:

            szoveggelkitoltes(web, feltoltendo,"jegyek", jegy, adat_nev)

        feltoltes(web)
        time.sleep(2)


def bolygo_feltoltes(web, feltoltendo:dict, domain):
    web.get(f'{domain}/create-bolygok/')

    for bolygo in feltoltendo["bolygok"].keys():
        for adat_nev in ["nevID", "leírás", "pontérték", "típus"]:

            szoveggelkitoltes(web, feltoltendo,"bolygok", bolygo, adat_nev)

        feltoltes(web)
        time.sleep(2)


def haz_feltoltes(web, feltoltendo, domain):
    web.get(f'{domain}/create-hazak/')

    for haz in feltoltendo["hazak"].keys():
        for adat_nev in ["nevID", "leírás", "mundán jegye", "típus"]:
            szoveggelkitoltes(web, feltoltendo, "hazak", haz, adat_nev)

        feltoltes(web)
        time.sleep(2)