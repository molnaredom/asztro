from selenium import webdriver
from adatbazis.web_scraping.adat_tarolas import tulajdonos_adat_tarolo
import warnings

from adatbazis.web_scraping.bolygojegyben_hazjegyben_feltoltes import bolygojegyben_kitoltes, hazjegyben_kitoltes
from adatbazis.web_scraping.horoszkop_kezelok.sajat_horoszkop_keszito import sajat_horoszkopform_kitoltes
from adatbazis.web_scraping.horoszkop_kezelok.kulso_adatgyujto import kulso_weboldalra_tulajdonosadatok_feltoltese, \
    kulso_weboldalrol_adatkiszedes
from adatbazis.web_scraping.kisegito_modulok.nyelvi_kisegito import ekezetnelkul

warnings.filterwarnings("ignore", category=DeprecationWarning)

import time


def inditas():
    global web
    from selenium.webdriver.firefox.options import Options
    # rendszer = "win10"
    rendszer = "linux"
    web = ""
    if rendszer == "win10":
        web = webdriver.Firefox(executable_path=r'../adat_tarolas/geckodriver.exe')
    else:
        web = webdriver.Firefox()

    return web




def get_kulso_web():
    return web


def egy_horoszkop_feltoltese(tulajodonosi_adatok, web):
    kulso_weboldal_lehivasa(web)

    kulso_weboldalra_tulajdonosadatok_feltoltese(web, tulajodonosi_adatok)

    kinyert_kulso_bolygo_es_haz_adatok = kulso_weboldalrol_adatkiszedes(web)
    print(kinyert_kulso_bolygo_es_haz_adatok)

    horoszkop_feltolt_adatok = get_analogiak_horoszkopkitolteshez(tulajodonosi_adatok,
                                                                  kinyert_kulso_bolygo_es_haz_adatok)
    sajat_horoszkopform_kitoltes(horoszkop_feltolt_adatok,web)


def kulso_weboldal_lehivasa(web):
    web.get('https://astro.cafeastrology.com/natal.php')
    time.sleep(2)


def get_analogiak_horoszkopkitolteshez(tulajodonosi_adatok, kinyert_kulso_bolygo_es_haz_adatok):
    horoszkop_feltolt_adatok = {}

    horoszkop_feltolt_adatok["tulajdonos_neve"] = tulajodonosi_adatok["nev"]
    horoszkop_feltolt_adatok["tipus"] = tulajodonosi_adatok["horoszkoptipus"]
    horoszkop_feltolt_adatok["hely"] = tulajodonosi_adatok["hely"]
    horoszkop_feltolt_adatok["tipus"] = tulajodonosi_adatok["horoszkoptipus"]

    for bolygonev, bolygo_tulajdonsagok in kinyert_kulso_bolygo_es_haz_adatok["bolygok"].items():
        horoszkop_feltolt_adatok[ekezetnelkul(bolygonev.lower())] = \
            [ekezetnelkul(bolygo_tulajdonsagok["jegy"].lower()),
             bolygo_tulajdonsagok["fokszam"]]

    for haznev, haz_tulajdonsagok in kinyert_kulso_bolygo_es_haz_adatok["hazak"].items():
        horoszkop_feltolt_adatok[str(haznev)] = \
            [ekezetnelkul(haz_tulajdonsagok["jegy"].lower()),
             haz_tulajdonsagok["fokszam"]]

    return horoszkop_feltolt_adatok


def horoszkopok_feltoltese(web):
    for tulajodonosi_adatok in tulajdonos_adat_tarolo.horoszkop_tarolo:
        egy_horoszkop_feltoltese(tulajodonosi_adatok, web)


def bolygojegyben_feltoltes(web):
    web.get('http://127.0.0.1:8000/create-bolygoJegyben/')
    bolygojegyben_kitoltes(web)


def hazjegyben_feltoltes(web):
    web.get('http://127.0.0.1:8000/create-hazJegyben/')
    hazjegyben_kitoltes(web)

def main():
    web = inditas()

    uj_horoszkop_keszites_ = True
    bolygojegyben_feltoltes_ = False
    hazjegyben_feltoltes_ = False

    process(bolygojegyben_feltoltes_, hazjegyben_feltoltes_, uj_horoszkop_keszites_, web)
    # TODO beallitani a redirectet createre


def process(bolygojegyben_feltoltes_, hazjegyben_feltoltes_, uj_horoszkop_keszites_, web):
    if uj_horoszkop_keszites_:
        horoszkopok_feltoltese(web)
    if bolygojegyben_feltoltes_:
        bolygojegyben_feltoltes(web)
    if hazjegyben_feltoltes_:
        hazjegyben_kitoltes(web)


if __name__ == '__main__':
    main()
