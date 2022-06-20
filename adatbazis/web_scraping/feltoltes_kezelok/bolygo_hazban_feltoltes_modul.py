import time

from selenium.webdriver.support.select import Select
from tqdm import tqdm

from adatbazis.web_scraping.kisegito_modulok.feltoltes_kisegito_modul import feltoltes


def bolygohazban_feltoltes(web,feltoltendo, kezdobolygoszam, kezdohazszam, domain):
    web.get(f'{domain}/create-bolygoHazban/')

    def adat_kitoltes(web, bolygoszam, hazszam, bolygonev, haznev, feltoltendo):
        # bolygo
        select = Select(web.find_element_by_xpath('//*[@id="id_bolygo"]'))
        select.select_by_value(str(bolygoszam))

        # jegy
        select = Select(web.find_element_by_xpath('//*[@id="id_haz"]'))
        select.select_by_value(str(hazszam))

        # adatok
        hely_xpath = web.find_element_by_xpath(f'//*[@id="id_leiras"]')
        hely_xpath.clear()
        jsonban_analogia = feltoltendo[bolygonev][haznev]
        jsonban_analogia= str(jsonban_analogia).replace("'", '"')
        hely_xpath.send_keys(jsonban_analogia)

    time.sleep(2)

    bolygok = ["nap", "hold", "merkúr", "vénusz", "mars", "jupiter", "szaturnusz", "uránusz", "neptun",
                       "pluto"]
    hazak = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

    for bolygoszam, bolygonev in enumerate(tqdm(bolygok, desc="Bolygó Házban feltöltése"), kezdobolygoszam):
        for hazszam, haznev in enumerate(hazak, kezdohazszam):
            adat_kitoltes(web, bolygoszam, hazszam, bolygonev, haznev, feltoltendo)
            feltoltes(web)
