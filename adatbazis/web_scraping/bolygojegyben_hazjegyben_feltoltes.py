import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import json
from adatbazis.web_scraping.kisegito_modulok.nyelvi_kisegito import *


def bolygojegyben_kitoltes(web):
    def adat_kitoltes(web, bolygoszam, jegyszam):
        # bolygo
        select = Select(web.find_element_by_xpath('//*[@id="id_nevID"]'))
        select.select_by_value(str(bolygoszam))

        # jegy
        select = Select(web.find_element_by_xpath('//*[@id="id_jegy"]'))
        select.select_by_value(str(jegyszam))
        # időt adunk a weboldalnak hogy betöltődjön

    def press_submit_button(web):
        adatok_kuldese_gomb = web.find_element_by_xpath('/html/body/div/form/input[2]')
        adatok_kuldese_gomb.click()

    time.sleep(2)
    for bolygo in range(1,11):
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

    def press_submit_button(web):
        adatok_kuldese_gomb = web.find_element_by_xpath('/html/body/div/form/input[2]')
        adatok_kuldese_gomb.click()

    time.sleep(2)
    for haz in range(1, 13):
        for jegy in range(1, 13):
            adat_kitoltes(web, haz, jegy)
            press_submit_button(web)


def alapanalogia_feltoltes(web, alapanalogiak):
    feltoltendo = alapanalogiak
    print(feltoltendo)

    # jegy_feltoltes(web, feltoltendo)
    #bolygo_feltoltes(web, feltoltendo)
    haz_feltoltes(web, feltoltendo)


def jegy_feltoltes(web, feltoltendo):
    web.get('http://127.0.0.1:8000/create-jegyek/')

    for jegy in feltoltendo["jegyek"].keys():
        for adat_nev in ["nevID", "leírás", "elem", "minőség", "paritás", "évszak"]:

            szoveggelkitoltes(web, feltoltendo,"jegyek", jegy, adat_nev)

        feltoltes(web)
        time.sleep(2)


def bolygo_feltoltes(web, feltoltendo:dict):
    web.get('http://127.0.0.1:8000/create-bolygok/')

    for bolygo in feltoltendo["bolygok"].keys():
        for adat_nev in ["nevID", "leírás", "pontérték", "típus"]:

            szoveggelkitoltes(web, feltoltendo,"bolygok", bolygo, adat_nev)

        feltoltes(web)
        time.sleep(2)


def haz_feltoltes(web, feltoltendo):
    web.get('http://127.0.0.1:8000/create-hazak/')

    for haz in feltoltendo["hazak"].keys():
        for adat_nev in ["nevID", "leírás", "mundán jegye", "típus"]:
            szoveggelkitoltes(web, feltoltendo, "hazak", haz, adat_nev)

        feltoltes(web)
        time.sleep(2)


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
    hely_xpath = web.find_element_by_xpath("/html/body/div/form/input[3]")
    hely_xpath.click()


