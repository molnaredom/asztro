from selenium import webdriver
from adatbazis.web_scraping.adat_tarolas import tulajdonos_adat_tarolo
import warnings
import time
from adatbazis.web_scraping.bolygojegyben_hazjegyben_feltoltes import *
from adatbazis.web_scraping.horoszkop_kezelok.sajat_horoszkop_keszito import sajat_horoszkopform_kitoltes
from adatbazis.web_scraping.horoszkop_kezelok.kulso_adatgyujto import kulso_weboldalra_tulajdonosadatok_feltoltese, \
    kulso_weboldalrol_adatkiszedes
from adatbazis.web_scraping.kisegito_modulok.nyelvi_kisegito import ekezetnelkul

warnings.filterwarnings("ignore", category=DeprecationWarning)


def inditas():
    global web
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


def hazjegyben_feltoltes(web):
    web.get('http://127.0.0.1:8000/create-hazJegyben/')
    hazjegyben_kitoltes(web)


def alapanalogia_beolvas():
    with open("../../analogiak/alapanalogiak.json", encoding="utf-8") as f:
        return json.loads(f.read())


def bolygojegyben_beolvas():
    with open("../../analogiak/bolygoJegyben_analogiak.json", encoding="utf-8") as f:
        return json.loads(f.read())


def main():
    web = inditas()
    print("inditas")

    uj_horoszkop_keszites_ = False
    bolygojegyben_feltoltes_ = True
    hazjegyben_feltoltes_ = False
    alapanalogia_feltoltes_ = False

    process(bolygojegyben_feltoltes_, hazjegyben_feltoltes_, uj_horoszkop_keszites_, alapanalogia_feltoltes_, web)


def process(bolygojegyben_feltoltes_, hazjegyben_feltoltes_, uj_horoszkop_keszites_,alapanalogia_feltoltes_, web):
    if uj_horoszkop_keszites_:
        horoszkopok_feltoltese(web)
    if bolygojegyben_feltoltes_:
        bolygojegyben_feltoltes(web, bolygojegyben_beolvas())
    if hazjegyben_feltoltes_:
        hazjegyben_kitoltes(web)
    if alapanalogia_feltoltes_:
        alapanalogia_feltoltes(web, alapanalogia_beolvas())



if __name__ == '__main__':
    main()
