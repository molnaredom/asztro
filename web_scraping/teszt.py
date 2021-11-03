from bs4 import BeautifulSoup
import requests
import urllib.request
from selenium import webdriver

from selenium.webdriver.support.ui import Select

import time


def select_adat_beallit(web, tartalom, xpath):
    select = Select(web.find_element_by_xpath(xpath))
    select.select_by_value(str(tartalom))


def fill_form(web, szuletesi_adatok: dict):
    # időt adunk a weboldalnak hogy betöltődjön
    time.sleep(2)

    # adatok kitoltese
    hely_adat_kitoltese(szuletesi_adatok["hely"], web)

    szuletesi_adatok_kitoltese(szuletesi_adatok, web)

    press_submit_button(web)


def hely_adat_kitoltese(hely, web):
    # hely
    hely_xpath = web.find_element_by_xpath('//*[@id="cityid"]')
    hely_xpath.send_keys(hely)
    hely_xpath.click()


def szuletesi_adatok_kitoltese(szuletesi_adatok, web):
    # nap
    select_adat_beallit(web, szuletesi_adatok["nap"],
                        "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select[1]")
    # honap
    select_adat_beallit(web, szuletesi_adatok["honap"],
                        "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select[2]")
    # ev
    select_adat_beallit(web, szuletesi_adatok["ev"],
                        "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select[3]")
    # ora
    select_adat_beallit(web, szuletesi_adatok["ora"],
                        "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[3]/td/select[1]")
    # perc
    select_adat_beallit(web, szuletesi_adatok["perc"],
                        "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[3]/td/select[2]")
    # nyelv
    select_adat_beallit(web, "hu",
                        "/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[5]/td/select")


def press_submit_button(web):
    adatok_kuldese_gomb = web.find_element_by_xpath(
        '/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[5]/td/button')
    adatok_kuldese_gomb.click()


def get_web_content():
    url = requests.get("https://astro.cafeastrology.com/natal.php")
    return url.text


bolygok = {
    "Nap": [],
    "Hold": [],
    "Merkur": [],
    "Vénusz": [],
    "Mars": [],
    "Jupiter": [],
    "Szaturnusz": [],
    "Uránusz": [],
    "Neptun": [],
    "Pluto": [],
}


def get_datas():
    create_bolygo("Nap", "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[4]",
                  "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[5]")

    create_bolygo("Hold", "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[3]/td[4]",
                  "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[3]/td[5]")

    create_bolygo("Merkur", "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[4]/td[4]",
                  "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[4]/td[5]")

    create_bolygo("Vénusz", "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[5]/td[4]",
                  "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[5]/td[5]")

    create_bolygo("Mars", "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[6]/td[4]",
                  "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[6]/td[5]")

    create_bolygo("Jupiter", "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[7]/td[4]",
                  "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[7]/td[5]")

    create_bolygo("Szaturnusz", "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[8]/td[4]",
                  "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[8]/td[5]")

    create_bolygo("Uránusz", "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[9]/td[4]",
                  "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[9]/td[5]")

    create_bolygo("Neptun", "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[9]/td[4]",
                  "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[9]/td[5]")

    create_bolygo("Pluto", "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[9]/td[4]",
                  "/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[9]/td[5]")



def create_bolygo(bolygonev, jegy_xpath, fokszam_xpath):
    bolygok[bolygonev].append(get_text(jegy_xpath))
    bolygok[bolygonev].append( get_text(fokszam_xpath))


def get_text(xpath):
    return web.find_element_by_xpath(xpath).text


if __name__ == '__main__':
    web = webdriver.Firefox()
    web.get('https://astro.cafeastrology.com/natal.php')

    szuletesi_adatok = {
        "nev": "adam",
        "ev": 2001,
        "honap": 8,
        "nap": 19,
        "ora": 16,
        "perc": 53,
        "hely": "Szolnok"
    }

    fill_form(web, szuletesi_adatok)

    get_datas()

    print(bolygok)

    for k,i in bolygok.items():
        print(k)
        print(i)
