from selenium.webdriver.support.ui import Select
import time
from adatbazis.web_scraping.kisegito_modulok.nyelvi_kisegito import *


def bolygojegyben_feltoltes(web,feltoltendo, kezdobolygoszam, kezdojegyszam , domain):
    web.get(f'{domain}/create-bolygoJegyben/')

    def adat_kitoltes(web, bolygoszam, jegyszam, bolygonev, jegynev, feltoltendo):
        # bolygo
        select = Select(web.find_element_by_xpath('//*[@id="id_bolygo"]'))
        select.select_by_value(str(bolygoszam))

        # jegy
        select = Select(web.find_element_by_xpath('//*[@id="id_jegy"]'))
        select.select_by_value(str(jegyszam))

        # adatok
        hely_xpath = web.find_element_by_xpath(f'//*[@id="id_adatok"]')
        hely_xpath.clear()
        jsonban_analogia = feltoltendo["analogiak"][bolygonev][jegynev]
        jsonban_analogia= str(jsonban_analogia).replace("'", '"')
        hely_xpath.send_keys(jsonban_analogia)

    time.sleep(2)

    bolygok = ["nap", "hold", "merkúr", "vénusz", "mars", "jupiter", "szaturnusz", "uránusz", "neptun",
                       "pluto"]
    jegyek = ["kos", "bika", "ikrek", "rák", "oroszlán", "szűz", "mérleg", "skorpió", "nyilas", "bak",
                         "vízöntő", "halak"]

    for bolygoszam, bolygonev in enumerate(bolygok, kezdobolygoszam):
        for jegyszam, jegynev in enumerate(jegyek,kezdojegyszam):
            adat_kitoltes(web, bolygoszam, jegyszam, bolygonev, jegynev, feltoltendo)
            feltoltes(web)


def hazjegyben_kitoltes(web, feltoltendo, kezdojegyszam, kezdohazszam, domain):
    web.get(f'{domain}/create-hazJegyben/')

    def adat_kitoltes(web, hazszam, jegyszam, haznev, jegynev, feltoltendo):
        # bolygo
        select = Select(web.find_element_by_xpath('//*[@id="id_haz"]'))
        select.select_by_value(str(hazszam))

        # jegy
        select = Select(web.find_element_by_xpath('//*[@id="id_jegy"]'))
        select.select_by_value(str(jegyszam))

        # adatok
        hely_xpath = web.find_element_by_xpath(f'//*[@id="id_leiras"]')
        hely_xpath.clear()
        jsonban_analogia = "{ \"analogiak\" : \"" + \
                           str(feltoltendo["analogiak"][haznev][jegynev]).strip() \
                           + "\" }"
        hely_xpath.send_keys(jsonban_analogia)

    time.sleep(2)

    hazak = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    jegyek = ["kos", "bika", "ikrek", "rák", "oroszlán", "szűz", "mérleg", "skorpió", "nyilas", "bak",
              "vízöntő", "halak"]

    for hazszam, haznev in enumerate(hazak, kezdohazszam):
        for jegyszam, jegynev in enumerate(jegyek, kezdojegyszam):
            adat_kitoltes(web, hazszam, jegyszam, haznev, jegynev, feltoltendo)
            feltoltes(web)


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


def szoveggelkitoltes(web,feltoltendo,foanalogia, al_analogia, konkret_analogia ):

    hely_xpath = web.find_element_by_xpath(f'//*[@id="id_{ekezetnelkul( konkret_analogia)}"]')
    hely_xpath.clear()
    if konkret_analogia == "leírás":
        jsonban_analogia = "{ \"analogiak\" : \"" + \
                           str(feltoltendo[foanalogia][al_analogia][konkret_analogia]).strip() \
                           + "\" }"
        hely_xpath.send_keys(jsonban_analogia)

    elif konkret_analogia != "nevID":
        hely_xpath.send_keys(feltoltendo[foanalogia][al_analogia][konkret_analogia])
    else:
        hely_xpath.send_keys(al_analogia) # az analógia neve



def feltoltes(web):
    hely_xpath = web.find_element_by_xpath("/html/body/div/form/input[3]")
    hely_xpath.click()


