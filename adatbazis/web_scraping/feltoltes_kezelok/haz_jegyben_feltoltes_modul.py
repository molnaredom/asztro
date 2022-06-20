import time

from selenium.webdriver.support.select import Select
from tqdm import tqdm

from adatbazis.web_scraping.kisegito_modulok.feltoltes_kisegito_modul import feltoltes


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

    for hazszam, haznev in enumerate(tqdm(hazak, desc="Ház Jegyben feltöltése"), kezdohazszam):
        for jegyszam, jegynev in enumerate(jegyek, kezdojegyszam):
            adat_kitoltes(web, hazszam, jegyszam, haznev, jegynev, feltoltendo)
            feltoltes(web)
