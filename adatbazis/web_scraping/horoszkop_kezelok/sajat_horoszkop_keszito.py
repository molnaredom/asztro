# from bs4 import BeautifulSoup
import requests
from selenium import webdriver

from selenium.webdriver.support.ui import Select

import time


def bolygojegyben_beallit(web, bolygo, jegy, xpath):
    def ekezetnelkul(szo: str):
        szo =szo.replace("á", "a")
        szo =szo.replace("ű", "u")
        szo =szo.replace("ú", "u")
        szo =szo.replace("ó", "o")
        szo =szo.replace("ö", "o")
        szo =szo.replace("ő", "o")
        szo =szo.replace("é", "e")

        return szo.replace("á", "a")


    def szama(keresett_bolygo, keresett_jegy):
        szam = 1
        for akt_bolygo in ["nap", "hold", "merkur", "vénusz", "mars", "jupiter", "szaturnusz", "uránusz", "neptun",
                           "plúto"]:
            for akt_jegy in ["kos", "bika", "ikrek", "rák", "oroszlán", "szűz", "mérleg", "skorpió", "nyilas", "bak",
                             "vízöntő", "halak"]:
                if keresett_bolygo == ekezetnelkul(akt_bolygo) and keresett_jegy == ekezetnelkul(akt_jegy):
                    return szam
                szam += 1

        return None

    select = Select(web.find_element_by_xpath(xpath))
    select.select_by_value(str(szama(bolygo, jegy)))



def hazjegyben_beallit(web, haz, jegy, xpath):
    def ekezetnelkul(szo: str):
        szo =szo.replace("á", "a")
        szo =szo.replace("ű", "u")
        szo =szo.replace("ú", "u")
        szo =szo.replace("ó", "o")
        szo =szo.replace("ö", "o")
        szo =szo.replace("ő", "o")
        szo =szo.replace("é", "e")

        return szo.replace("á", "a")


    def szama(keresett_haz, keresett_jegy):
        szam = 5
        for akt_haz in range(1, 13):
            for akt_jegy in ["kos", "bika", "ikrek", "rák", "oroszlán", "szűz", "mérleg", "skorpió", "nyilas", "bak",
                             "vízöntő", "halak"]:
                if keresett_haz == ekezetnelkul(str(akt_haz)) and keresett_jegy == ekezetnelkul(akt_jegy):
                    return szam
                szam += 1

        return None

    select = Select(web.find_element_by_xpath(xpath))
    select.select_by_value(str(szama(str(haz), jegy)))



def sajat_horoszkopform_kitoltes(horoszkop_adatok, web):
    sajat_web_inditasa(web)

    sajat_weboldal_kitoltes(horoszkop_adatok, web)




def sajat_web_inditasa(web):
    # rendszer = "win10"
    # # rendszer = "linux"
    # if rendszer == "win10":
    #     web = webdriver.Firefox(executable_path=r'../adat_tarolas/geckodriver.exe')
    # else:
    #     web = webdriver.Firefox()
    web.get('http://127.0.0.1:8000/create-horoszkop/')
    time.sleep(2)


def sajat_weboldal_kitoltes(horoszkop_adatok, web):
    egyeb_tulajdonosi_adat_feltoltes(horoszkop_adatok, web)
    bolygo_jegyben_feltoltes(horoszkop_adatok, web)
    haz_jegyben_feltoltes(horoszkop_adatok, web)

    press_submit_button(web)


def egyeb_tulajdonosi_adat_feltoltes(horoszkop_adatok, web):

    for adat_nev in ["tulajdonos_neve","tipus","hely"]:
        hely_xpath = web.find_element_by_xpath(f'//*[@id="id_{adat_nev}"]')
        hely_xpath.send_keys(horoszkop_adatok[f"{adat_nev}"])


def haz_jegyben_feltoltes(horoszkop_adatok, web):
    for haz in range(1, 13):
        hazjegyben_beallit(web, str(haz), horoszkop_adatok[str(haz)][0],
                           f'//*[@id="id_haz_{str(haz)}"]')


def bolygo_jegyben_feltoltes(horoszkop_adatok, web):
    for bolygo in ["nap", "hold", "merkur", "venusz", "mars", "jupiter", "szaturnusz", "uranusz", "neptun", "pluto"]:
        bolygojegyben_beallit(web, bolygo, horoszkop_adatok[bolygo][0],
                              f'//*[@id="id_{bolygo}"]')


def press_submit_button(web):
    adatok_kuldese_gomb = web.find_element_by_xpath(
        '/html/body/div/form/input[2]')
    adatok_kuldese_gomb.click()


def get_web_content():
    url = requests.get("https://astro.cafeastrology.com/natal.php")
    return url.text



def szama(keresett_bolygo, keresett_jegy):
    szam = 22
    for akt_bolygo in ["nap", "hold", "merkur", "venusz", "mars", "jupiter", "szaturnusz", "uranusz", "neptun",
                       "pluto"]:
        for akt_jegy in ["kos", "bika", "ikrek", "rák", "oroszlán", "szűz", "mérleg", "skorpió", "nyilas", "bak",
                         "vízöntő", "halak"]:
            print(akt_bolygo, akt_jegy, szam)
            if keresett_bolygo == akt_bolygo and keresett_jegy == akt_jegy:
                return szam
            szam += 1


