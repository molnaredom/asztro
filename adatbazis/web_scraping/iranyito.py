import os
import socket
import argparse
import platform

from selenium import webdriver
import warnings
import json

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

from adatbazis.web_scraping.feltoltes_kezelok.alapanalogia_feltoltes_modul import alapanalogia_feltoltes
from adatbazis.web_scraping.feltoltes_kezelok.analogia_gyakorlo_feltoltes_modul import analogiagyakorlo_feltoltes
from adatbazis.web_scraping.feltoltes_kezelok.bolygo_hazban_feltoltes_modul import bolygohazban_feltoltes
from adatbazis.web_scraping.feltoltes_kezelok.bolygo_jegyben_feltoltes_modul import bolygojegyben_feltoltes
from adatbazis.web_scraping.feltoltes_kezelok.haz_jegyben_feltoltes_modul import hazjegyben_kitoltes
from adatbazis.web_scraping.feltoltes_kezelok.hazurahazban_feltoltes_modul import hazurahazban_feltoltes
from adatbazis.web_scraping.horoszkop_kezelok.main_horoszkop_keszito import *

warnings.filterwarnings("ignore", category=DeprecationWarning)


def inditas(mode):
    print("INDITAS")
    global web
    options = webdriver.FirefoxOptions()
    if "b" in mode:
        options.add_argument('--headless')
        print("   Háttérben futás bekapcsolva")
    else:
        print("   A program az előtérben fut")

    web = ""
    if platform.system() == "Windows":
        print("   Windows platform felismerve")
        web = webdriver.Firefox(executable_path='adat_tarolas/geckodriver.exe', options=options)
    elif platform.system() == "Linux":
        print("   Linux platform felismerve")
        web = webdriver.Firefox(executable_path='adat_tarolas/geckodriver/linux/geckodriver', options=options)

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


def bolygohazban_beolvasas():
    with open("../analogiak/bolygo_hazban_analogiak.json", encoding="utf-8") as f:
        return json.loads(f.read())


def main():
    """
    Use external webpage to gain basic horoscope datas
    """

    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-o", "--Output",
                        help="Show Output")
    parser.add_argument("-m", "--mode", default="-",
                        help="Set running mode, which is api or web ")

    # Read arguments from command line
    args = parser.parse_args()

    mode = args.mode
    print(f"MODE: [{mode}]", end=" ")

    if "api" in mode:
        print("api mode")
        api_mode(mode)

    elif "web" in mode:
        print("web mode")
        web_mode(mode)

    elif "alapadat" in mode:
        print("alapadatok feltöltése mód")
        alapadat_feltoltes(mode=args.mode)

    elif "egyeni" in mode:
        print("egyeni feltöltése mód")
        egyeni_feltoltes(mode)

    elif "gyakorlo" in mode:
        print("gyakorló feltöltés mód")
        gyakorlo_feltoltes(mode= mode)

    elif args.mode == "-":
        print("Nem adtál meg semilyen argumentumot, így nem lehet futtatni")

    print("KÉÉSZ")


def set_domain():
    print("SET DOMAIN")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    vizsgalt_port = 8000
    is_port_exists = sock.connect_ex(('127.0.0.1', vizsgalt_port))
    if is_port_exists != 0:
        # toto set server
        print(f"   Port {vizsgalt_port} szabad, django server futtatása")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

        application = get_wsgi_application()
        call_command('runserver', '127.0.0.1:8000')
    else:
        print(f"   port {vizsgalt_port} foglalt: feltételezzük a django szerver futását")

    sock.close()

    return "http://127.0.0.1:8000"



def web_mode(mode):
    web = inditas(mode)

    domain = set_domain()

    hazurahazban_feltoltes = False
    uj_horoszkop_keszites_ = True
    bolygojegyben_feltoltes_ = False
    hazjegyben_feltoltes_ = False
    alapanalogia_feltoltes_ = False

    process(bolygojegyben_feltoltes_, hazjegyben_feltoltes_, uj_horoszkop_keszites_, alapanalogia_feltoltes_,
            hazurahazban_feltoltes, web, domain)


def alapadat_feltoltes(mode):

    web = inditas(mode)
    domain = set_domain()

    process(mode, web=web, domain=domain, bolygojegyben_feltoltes_=True,
            hazjegyben_feltoltes_=True, alapanalogia_feltoltes_=True,
            hazurahazban_=True,bolygo_hazban_feltoltes_=True)


def egyeni_feltoltes(mode):
    web = inditas(mode)
    domain = set_domain()

    process(mode, web=web, domain=domain, bolygo_hazban_feltoltes_=True)


def gyakorlo_feltoltes(mode):
    web = inditas(mode)
    domain = set_domain()

    process(mode, domain=domain, web=web, gyakorlo_feltoltes_=True)


def api_mode(mode):
    web = inditas(mode)
    domain = set_domain()
    process(mode="kulsoapi", uj_horoszkop_keszites_=True, web=web, domain=domain)



def process(mode="", bolygojegyben_feltoltes_=False, hazjegyben_feltoltes_=False, uj_horoszkop_keszites_=False,
            alapanalogia_feltoltes_=False, hazurahazban_=False, gyakorlo_feltoltes_=False,bolygo_hazban_feltoltes_ =None,
    web=None, domain=None):
    if alapanalogia_feltoltes_:
        alapanalogia_feltoltes(web, alapanalogia_beolvas(), domain=domain)
    if bolygo_hazban_feltoltes_:
        bolygohazban_feltoltes(web, bolygohazban_beolvasas(), kezdohazszam=1, kezdobolygoszam=1, domain=domain)
    if bolygojegyben_feltoltes_:
        bolygojegyben_feltoltes(web, bolygojegyben_beolvas(), kezdojegyszam=1, kezdobolygoszam=1, domain=domain)
    if hazjegyben_feltoltes_:
        hazjegyben_kitoltes(web, hazjegyben_beolvas(), kezdojegyszam=1, kezdohazszam=1, domain=domain)
    if uj_horoszkop_keszites_:
        horoszkopok_feltoltese(web, kezdobolygojegyben=1, kezdohazjegyben=1, domain=domain, mode=mode)
    if hazurahazban_:
        hazurahazban_feltoltes(web, hazurahazban_beolvasas(), kezdo_alaphazszam=1, kezdojegyszam=1, domain=domain)
    if gyakorlo_feltoltes_:

        feltoltendo_adatok = {
            "bolygojegyben" : bolygojegyben_beolvas()
        }

        analogiagyakorlo_feltoltes(web, domain, feltoltendo_adatok)

    # running modes
    # -kulsoweb
    # -api


if __name__ == '__main__':
    main()
