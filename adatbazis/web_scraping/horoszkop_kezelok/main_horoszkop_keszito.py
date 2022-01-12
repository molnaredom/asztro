import time

from adatbazis.web_scraping.adat_tarolas import tulajdonos_adat_tarolo
from adatbazis.web_scraping.horoszkop_kezelok.kulso_adatgyujto import kulso_weboldalra_tulajdonosadatok_feltoltese, \
    kulso_weboldalrol_adatkiszedes
from adatbazis.web_scraping.horoszkop_kezelok.sajat_horoszkop_keszito import sajat_horoszkopform_kitoltes
from adatbazis.web_scraping.kisegito_modulok.nyelvi_kisegito import ekezetnelkul


def kulso_weboldal_lehivasa(web):
    web.get('https://astro.cafeastrology.com/natal.php')
    time.sleep(2)


def egy_horoszkop_feltoltese(tulajodonosi_adatok, web, kezdobolygojegyben, kezdohazjegyben):
    kulso_weboldal_lehivasa(web)

    kulso_weboldalra_tulajdonosadatok_feltoltese(web, tulajodonosi_adatok)

    kinyert_kulso_bolygo_es_haz_adatok = kulso_weboldalrol_adatkiszedes(web)
    print(kinyert_kulso_bolygo_es_haz_adatok)


    horoszkop_feltolt_adatok = get_analogiak_horoszkopkitolteshez(tulajodonosi_adatok,
                                                                  kinyert_kulso_bolygo_es_haz_adatok,
                                                                  )
    sajat_horoszkopform_kitoltes(horoszkop_feltolt_adatok, web, kezdobolygojegyben, kezdohazjegyben)


def get_analogiak_horoszkopkitolteshez(tulajodonosi_adatok, kinyert_kulso_bolygo_es_haz_adatok):

    def datumido_keszit():
        t = tulajodonosi_adatok
        return f"{t['ev']}-{t['honap']}-{t['nap']} {t['ora']}:{t['perc']}:00"

    def float_fokszam(strfok:str):
        fperc,fmp = strfok.split("°")
        return str(float(fperc)+float(fmp[:-1])*(1/6)/10)


    horoszkop_feltolt_adatok = {}

    horoszkop_feltolt_adatok["tulajdonos_neve"] = tulajodonosi_adatok["nev"]
    horoszkop_feltolt_adatok["tipus"] = tulajodonosi_adatok["horoszkoptipus"]
    horoszkop_feltolt_adatok["hely"] = tulajodonosi_adatok["hely"]
    horoszkop_feltolt_adatok["tipus"] = tulajodonosi_adatok["horoszkoptipus"]
    horoszkop_feltolt_adatok["idopont"] = datumido_keszit()

    print(horoszkop_feltolt_adatok["idopont"])



    for bolygonev, bolygo_tulajdonsagok in kinyert_kulso_bolygo_es_haz_adatok["bolygok"].items():
        horoszkop_feltolt_adatok[ekezetnelkul(bolygonev.lower())] = \
            [ekezetnelkul(bolygo_tulajdonsagok["jegy"].lower()),
             float_fokszam(bolygo_tulajdonsagok["fokszam"])]

    for haznev, haz_tulajdonsagok in kinyert_kulso_bolygo_es_haz_adatok["hazak"].items():
        horoszkop_feltolt_adatok[str(haznev)] = \
            [ekezetnelkul(haz_tulajdonsagok["jegy"].lower()),
             float_fokszam(haz_tulajdonsagok["fokszam"])]

    return horoszkop_feltolt_adatok


def horoszkopok_feltoltese(web,kezdobolygojegyben, kezdohazjegyben):
    for tulajodonosi_adatok in tulajdonos_adat_tarolo.horoszkop_tarolo:
        egy_horoszkop_feltoltese(tulajodonosi_adatok, web, kezdobolygojegyben, kezdohazjegyben)
