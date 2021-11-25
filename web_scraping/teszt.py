

import requests
from selenium import webdriver
import horoszkop_keszito

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

hazak = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: []
}


def get_datas():
    get_bolygok()
    get_hazak()



def get_bolygok():
    for i in zip(range(2, 12),
                 ["Nap", "Hold", "Merkur", "Vénusz", "Mars", "Jupiter", "Szaturnusz", "Uránusz", "Neptun", "Pluto"]):
        bolygonev = i[1]
        akt_cellaszam = i[0]
        create_bolygo(bolygonev, f"/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[{akt_cellaszam}]/td[4]",
                      f"/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[{akt_cellaszam}]/td[5]")


def get_hazak():
    for i in range(1,13):
        hazszam = i
        akt_cellaszam = i+1
        create_haz(hazszam, f"/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[{akt_cellaszam}]/td[10]",
                      f"/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[{akt_cellaszam}]/td[11]")


def create_bolygo(bolygonev, jegy_xpath, fokszam_xpath):
    bolygok[bolygonev].append(get_text(jegy_xpath))
    bolygok[bolygonev].append( get_text(fokszam_xpath))

def create_haz(hazszam, jegy_xpath, fokszam_xpath):
    hazak[hazszam].append(get_text(jegy_xpath))
    hazak[hazszam].append(get_text(fokszam_xpath))

def get_text(xpath):
    return web.find_element_by_xpath(xpath).text

if __name__ == '__main__':



    rendszer ="win10"
    #rendszer = "linux"
    web = ""
    if rendszer == "win10":
        web = webdriver.Firefox(executable_path=r'geckodriver.exe')
    else:
        web = webdriver.Firefox()

    web.get('https://astro.cafeastrology.com/natal.php')

    szuletesi_adatok = {
        "nev": "teszt",
        "horoszkoptipus": "solar",
        "ev": 1977,
        "honap": 5 ,
        "nap": 29,
        "ora": 10,
        "perc":  31,
        "hely": "Budapest"
    }

    fill_form(web, szuletesi_adatok)

    get_datas()


    def ekezetnelkul(szo: str):
        szo =szo.replace("á", "a")
        szo =szo.replace("ű", "u")
        szo =szo.replace("ú", "u")
        szo =szo.replace("ó", "o")
        szo =szo.replace("ö", "o")
        szo =szo.replace("ő", "o")
        szo =szo.replace("é", "e")

        return szo.replace("á", "a")

    horoszkop_adatok= {}

    horoszkop_adatok["tulajdonos_neve"] = szuletesi_adatok["nev"]
    horoszkop_adatok["tipus"] = szuletesi_adatok["horoszkoptipus"]
    horoszkop_adatok["hely"] = szuletesi_adatok["hely"]
    horoszkop_adatok["tipus"] = szuletesi_adatok["horoszkoptipus"]


    print(horoszkop_adatok["tulajdonos_neve"])
    for k, v in bolygok.items():
        horoszkop_adatok[ekezetnelkul(k.lower())] = [ekezetnelkul( v[0].lower()) ,v[1]]


    for k,v in hazak.items():
        horoszkop_adatok[str(k)] = [ekezetnelkul( v[0].lower()) ,v[1]]


    print(horoszkop_adatok)


    horoszkop_keszito.horoszkop_kitoltes(horoszkop_adatok)





