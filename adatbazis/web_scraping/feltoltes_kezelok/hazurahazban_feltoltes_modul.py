import time

from selenium.webdriver.support.select import Select
from tqdm import tqdm

from adatbazis.web_scraping.kisegito_modulok.feltoltes_kisegito_modul import feltoltes


def hazurahazban_feltoltes(web, feltoltendo, kezdo_alaphazszam, kezdojegyszam, domain):
    web.get(f'{domain}/create-hazUraHazban/')

    def adat_kitoltes(web, alap_hazszam, uramelyikhazban_szam, alap_haz_nev, uramelyikhazban_nev, feltoltendo):
        # alap haz
        select = Select(web.find_element_by_xpath('//*[@id="id_alap_haz"]'))
        select.select_by_value(str(alap_hazszam))

        # ura melyik hazban
        select = Select(web.find_element_by_xpath('//*[@id="id_ura_melyik_hazban"]'))
        select.select_by_value(str(uramelyikhazban_szam))

        # adatok
        hely_xpath = web.find_element_by_xpath(f'//*[@id="id_tulajdonsagok"]')
        hely_xpath.clear()
        jsonban_analogia = "{ \"analogiak\" : \"" + \
                           str(feltoltendo[alap_haz_nev][uramelyikhazban_nev]).strip() \
                           + "\" }"
        hely_xpath.send_keys(jsonban_analogia)

    time.sleep(2)

    alaphazak = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    uraakmelyikhazakban_tomb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

    for hazszam, haznev in enumerate(tqdm(alaphazak, desc="Ház ura házban feltöltése"), kezdo_alaphazszam):
        for uramelyikhazban, jegynev in enumerate(uraakmelyikhazakban_tomb, kezdojegyszam):
            adat_kitoltes(web, hazszam, uramelyikhazban, haznev, jegynev, feltoltendo)
            feltoltes(web)
