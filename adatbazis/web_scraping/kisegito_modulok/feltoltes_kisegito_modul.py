import time

from adatbazis.web_scraping.kisegito_modulok.alap_webscraper_parancsok import raklikkeles
from adatbazis.web_scraping.kisegito_modulok.nyelvi_kisegito import *


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
    raklikkeles(web, "/html/body/div/form/button[2]" )



