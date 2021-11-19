from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def bolygojegyben_kitoltes(web):
    def adat_kitoltes(web, bolygoszam, jegyszam):
        # bolygo
        select = Select(web.find_element_by_xpath('//*[@id="id_bolygo"]'))
        select.select_by_value(str(bolygoszam))

        # jegy
        select = Select(web.find_element_by_xpath('//*[@id="id_jegy"]'))
        select.select_by_value(str(jegyszam))
        # időt adunk a weboldalnak hogy betöltődjön

    def press_submit_button(web):
        adatok_kuldese_gomb = web.find_element_by_xpath('/html/body/div/form/input[2]')
        adatok_kuldese_gomb.click()

    time.sleep(2)
    for bolygo in range(1, 11):
        for jegy in range(1, 13):
            adat_kitoltes(web, bolygo, jegy)
            press_submit_button(web)

def hazjegyben_kitoltes(web):
    def adat_kitoltes(web, hazszam, jegyszam):
        # haz
        select = Select(web.find_element_by_xpath('//*[@id="id_haz"]'))
        select.select_by_value(str(hazszam))

        # jegy
        select = Select(web.find_element_by_xpath('//*[@id="id_jegy"]'))
        select.select_by_value(str(jegyszam))
        # időt adunk a weboldalnak hogy betöltődjön

    def press_submit_button(web):
        adatok_kuldese_gomb = web.find_element_by_xpath('/html/body/div/form/input[2]')
        adatok_kuldese_gomb.click()

    time.sleep(2)
    for haz in range(1, 13):
        for jegy in range(1, 13):
            adat_kitoltes(web, haz, jegy)
            press_submit_button(web)



if __name__ == '__main__':

    rendszer = "win10"
    # rendszer = "linux"
    web = ""
    if rendszer == "win10":
        web = webdriver.Firefox(executable_path=r'geckodriver.exe')
    else:
        web = webdriver.Firefox()


    #web.get('http://127.0.0.1:8000/create-bolygoJegyben/')
    web.get('http://127.0.0.1:8000/create-hazJegyben/')

    # TODO beallitani a redirectet createre

    # bolygojegyben_kitoltes(web)
    hazjegyben_kitoltes(web)
