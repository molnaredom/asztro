import time

import requests
from selenium.webdriver.support.select import Select


def kulso_weboldalrol_adatkiszedes(web):
    time.sleep(1)
    return {"bolygok": get_bolygok(web), "hazak": get_hazak(web)}


def kulso_weboldalra_tulajdonosadatok_feltoltese(web, szuletesi_adatok: dict):
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
    # evbase_bolygohazban
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


def select_adat_beallit(web, tartalom, xpath):
    select = Select(web.find_element_by_xpath(xpath))
    select.select_by_value(str(tartalom))


def get_bolygok(web):
    bolygok = {}
    # todo nem biztos hogy az akt szam megfelelo !!!
    for i, bolygonev in enumerate(
            ["Nap", "Hold", "Merkur", "Vénusz", "Mars", "Jupiter", "Szaturnusz", "Uránusz", "Neptun", "Pluto"],
            start=2):
        akt_cellaszam = i
        bolygok[bolygonev] = create_bolygo_dict(szam_xpathoz=akt_cellaszam,web =web)

    return bolygok


def get_hazak(web):
    hazak = {}
    # todo nem biztos hogy az akt szam megfelelo !!!
    for haz_szam in range(1, 13):
        akt_cellaszam = haz_szam + 1
        hazak[haz_szam] = create_haz_dict(akt_cellaszam,web)

    return hazak


def create_bolygo_dict(szam_xpathoz,web):
    return {
        "jegy": get_text(f"/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[{szam_xpathoz}]/td[4]",web),
        "fokszam": get_text(f"/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[{szam_xpathoz}]/td[5]", web)
    }


def create_haz_dict(szam_xpathhoz,web):
    return {"jegy": get_text(f"/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[{szam_xpathhoz}]/td[10]",web),
            "fokszam": get_text(f"/html/body/div[3]/div/div[2]/div[2]/div[1]/table/tbody/tr[{szam_xpathhoz}]/td[11]",web)
            }
def get_text(xpath, web):
    return web.find_element_by_xpath(xpath).text


def get_web_content():
    url = requests.get("https://astro.cafeastrology.com/natal.php")
    return url.text
