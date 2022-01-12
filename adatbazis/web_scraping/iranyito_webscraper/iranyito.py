from selenium import webdriver
import warnings
import json
from adatbazis.web_scraping.bolygojegyben_hazjegyben_feltoltes import *
from adatbazis.web_scraping.horoszkop_kezelok.main_horoszkop_keszito import horoszkopok_feltoltese

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


def alapanalogia_beolvas():
    with open("../../analogiak/alapanalogiak.json", encoding="utf-8") as f:
        return json.loads(f.read())


def bolygojegyben_beolvas():
    with open("../../analogiak/bolygoJegyben_analogiak.json", encoding="utf-8") as f:
        return json.loads(f.read())


def hazjegyben_beolvas():
    with open("../../analogiak/hazJegyben_analogiak.json", encoding="utf-8") as f:
        return json.loads(f.read())


def main():
    web = inditas()
    print("inditas")

    uj_horoszkop_keszites_ = True
    bolygojegyben_feltoltes_ = False
    hazjegyben_feltoltes_ = False
    alapanalogia_feltoltes_ = False

    process(bolygojegyben_feltoltes_, hazjegyben_feltoltes_, uj_horoszkop_keszites_, alapanalogia_feltoltes_, web)

    print("KÉÉSZ")


def process(bolygojegyben_feltoltes_, hazjegyben_feltoltes_, uj_horoszkop_keszites_,alapanalogia_feltoltes_, web):
    if uj_horoszkop_keszites_:
        horoszkopok_feltoltese(web, kezdobolygojegyben = 1, kezdohazjegyben = 4)
    if bolygojegyben_feltoltes_:
        bolygojegyben_feltoltes(web, bolygojegyben_beolvas(), kezdojegyszam=1, kezdobolygoszam=1)
    if hazjegyben_feltoltes_:
        hazjegyben_kitoltes(web, hazjegyben_beolvas(),kezdojegyszam=1, kezdohazszam=1)
    if alapanalogia_feltoltes_:
        alapanalogia_feltoltes(web, alapanalogia_beolvas())



if __name__ == '__main__':
    main()
