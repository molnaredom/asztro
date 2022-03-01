from selenium import webdriver
import warnings
import json

from adatbazis.web_scraping.feltoltes_kezelok.alapanalogia_feltoltes_modul import alapanalogia_feltoltes
from adatbazis.web_scraping.feltoltes_kezelok.bolygo_jegyben_feltoltes_modul import bolygojegyben_feltoltes
from adatbazis.web_scraping.feltoltes_kezelok.haz_jegyben_feltoltes_modul import hazjegyben_kitoltes
from adatbazis.web_scraping.feltoltes_kezelok.hazurahazban_feltoltes_modul import hazurahazban_feltoltes
from adatbazis.web_scraping.horoszkop_kezelok.main_horoszkop_keszito import *

warnings.filterwarnings("ignore", category=DeprecationWarning)


def inditas():
    global web
    # rendszer = "win10"
    rendszer = "linux"
    web = ""
    if rendszer == "win10":
        web = webdriver.Firefox(executable_path=r'adat_tarolas/geckodriver.exe')
    else:
        web = webdriver.Firefox()

    return web


def alapanalogia_beolvas():
    with open("../analogiak/alapanalogiak.json", encoding="utf-8") as f:
        return json.loads(f.read())


def bolygojegyben_beolvas():
    with open("../analogiak/bolygoJegyben_analogiak.json", encoding="utf-8") as f:
        return json.loads(f.read())


def hazjegyben_beolvas():
    with open("../analogiak/hazJegyben_analogiak.json", encoding="utf-8") as f:
        return json.loads(f.read())


def hazurahazban_beolvasas():
    with open("../analogiak/hazUra.json", encoding="utf-8") as f:
        return json.loads(f.read())


import argparse

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-o", "--Output", help="Show Output")
parser.add_argument("-m", "--mode", default= "api",
                    help="Set running mode, which is api or web ")

# Read arguments from command line
args = parser.parse_args()

def main():
    alapadat_feltoltes("alapadat")
    print("kész")
    exit()

    if args.mode == "api":
        print("api mode")
        api_mode()

    elif args.mode == "web":
        print("web mode")
        web_mode()

    elif args.mode == "alapadat":
        print("alapadatok feltöltése mód")
        alapadat_feltoltes("alapadat")



    print("KÉÉSZ")

def web_mode():
    web = inditas()
    domain = "https://asztro.herokuapp.com"
    domain = "http://127.0.0.1:8000"
    print("inditas")

    hazurahazban_feltoltes = False
    #
    uj_horoszkop_keszites_ = True
    bolygojegyben_feltoltes_ = False
    hazjegyben_feltoltes_ = False
    alapanalogia_feltoltes_ = False

    process(bolygojegyben_feltoltes_, hazjegyben_feltoltes_, uj_horoszkop_keszites_, alapanalogia_feltoltes_,
            hazurahazban_feltoltes, web, domain)


def alapadat_feltoltes(mode):
    web = inditas()
    domain = "https://asztro.herokuapp.com"
    domain = "http://127.0.0.1:8000"
    print("inditas")


    process(mode,web = web, domain=domain, bolygojegyben_feltoltes_ = True,
            hazjegyben_feltoltes_ = True, alapanalogia_feltoltes_ = True,
            hazurahazban_= True)




def api_mode():
    web = inditas()
    domain = "http://127.0.0.1:8000"
    process(mode="kulsoapi", uj_horoszkop_keszites_=True, web=web, domain=domain)


def process(mode,bolygojegyben_feltoltes_ = False, hazjegyben_feltoltes_ = False, uj_horoszkop_keszites_ = False,
            alapanalogia_feltoltes_ = False,hazurahazban_ = False, web=None, domain=None):
    if alapanalogia_feltoltes_:
        alapanalogia_feltoltes(web, alapanalogia_beolvas(), domain=domain)
    if bolygojegyben_feltoltes_:
        bolygojegyben_feltoltes(web, bolygojegyben_beolvas(), kezdojegyszam=1, kezdobolygoszam=1, domain=domain)
    if hazjegyben_feltoltes_:
        hazjegyben_kitoltes(web, hazjegyben_beolvas(),kezdojegyszam=1, kezdohazszam=1, domain=domain)
    if uj_horoszkop_keszites_:
        horoszkopok_feltoltese(web, kezdobolygojegyben = 1, kezdohazjegyben = 1, domain=domain, mode=mode)
    if hazurahazban_:
        hazurahazban_feltoltes(web,hazurahazban_beolvasas(), kezdo_alaphazszam=1, kezdojegyszam=1, domain=domain)

    # running modes
    # -kulsoweb
    # -api



if __name__ == '__main__':
    main()
