import time

from selenium.webdriver.support.select import Select
from tqdm import tqdm

from adatbazis.web_scraping.kisegito_modulok.feltoltes_kisegito_modul import feltoltes
from weboldal.base.kisegito import kisegito


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

    time.sleep(1)

    bolygok = kisegito.get_bolygo_nevek(fotengelyekkel=True)
    jegyek = kisegito.get_jegy_nevek()

    for bolygoszam, bolygonev in enumerate(tqdm(bolygok, kezdobolygoszam, desc="Bolygó Jegyben feltöltése")):
        for jegyszam, jegynev in enumerate(jegyek,kezdojegyszam):
            adat_kitoltes(web, bolygoszam, jegyszam, bolygonev, jegynev, feltoltendo)
            feltoltes(web)
