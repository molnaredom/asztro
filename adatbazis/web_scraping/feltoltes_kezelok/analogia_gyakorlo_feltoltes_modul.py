import time

from selenium.webdriver.support.select import Select

def analogiagyakorlo_feltoltes(web, domain, feltoltendo_adatok):
    kvizek = [{"név": "Bolygójegyben gyakorló",
               "leírás": "ez egy nehéz nehézségű teszt",
               "kérdésszám": "15",
               "idő": "200",
               "kviz_value": "49"
               },{"név": "Bolygójegyben gyakorló",
               "leírás": "ez egy közepes nehézségű teszt",
               "kérdésszám": "10",
               "idő": "250",
               "kviz_value": "50"
               },{"név": "Bolygójegyben gyakorló",
               "leírás": "ez egy könnyű nehézségű teszt",
               "kérdésszám": "8",
               "idő": "400",
               "kviz_value": "51"
               },


              ]

    bejelentkezes_adminkent(web, domain)

    # kvizek_hozzaadasa(domain, web, kvizek)
    for kviz in kvizek:
        if kviz["név"] == "Bolygójegyben gyakorló":
            bolygojegyben_kozepes_kviz_kerdesfeltoltes(web, domain, feltoltendo_adatok, kviz)


def bejelentkezes_adminkent(web, domain):
    time.sleep(0.5)
    web.get(f'{domain}/admin')
    szoveg_kitoltes(web, xpath='//*[@id="id_username"]', tartalom="1")
    szoveg_kitoltes(web, xpath='//*[@id="id_password"]', tartalom="1")
    raklikkeles(web, xpath='/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')
    time.sleep(0.5)


def kvizek_hozzaadasa(domain, web, kvizek):
    web.get(f'{domain}/admin/home/quiz/add/')

    for kviz in kvizek:
        szoveg_kitoltes(web, '//*[@id="id_name"]', kviz["név"])
        szoveg_kitoltes(web, '//*[@id="id_desc"]', kviz["leírás"])
        szoveg_kitoltes(web, '//*[@id="id_number_of_questions"]', kviz["kérdésszám"])
        szoveg_kitoltes(web, '//*[@id="id_time"]', kviz["idő"])
        # mentés
        raklikkeles(web, xpath='/html/body/div/div[3]/div/div[1]/div/form/div/div/input[2]')


def bolygojegyben_kozepes_kviz_kerdesfeltoltes(web, domain, feltoltendo_adatok, kviz_adatok):
    web.get(f'{domain}/admin/home/question/add/')
    kerdesek = kerdes_generator(feltoltendo_adatok, kviz_adatok)

    for kerdes in kerdesek:
        egy_kerdes_hozzaadasa(web,
                              kerdes_neve=kerdes["kerdesnev"],
                              valasz_opciok=kerdes["valasz_opciok"],
                              hozzatartozo_kviz_value=kviz_adatok["kviz_value"]
                              )


def kerdes_generator(feltoltendo_adatok, kviz_adatok):
    bolygojegyben_kerdesbank = []
    opciok = set()
    for bolygo_nev, bolygo_values in feltoltendo_adatok["bolygojegyben"]["analogiak"].items():
        szempontok = bolygo_values["szempontok"]
        for jegy_nev, jegy_values in bolygo_values.items():
            if jegy_nev != "szempontok" and jegy_nev != "bolygo_leiras":
                for szempont_nev, szempont_array in jegy_values.items():
                    for analogia in szempont_array:
                        opciok.add("-".join([jegy_nev, bolygo_nev]))
                        if analogia != "" and szempont_nev != "munka":
                            bolygojegyben_kerdesbank.append({
                                "kerdes": str(szempont_nev) + ": " + str(analogia),
                                "valasz": "-".join([jegy_nev, bolygo_nev])
                            })
                        # print(,analogia,sep="-" )
    kerdesbank_meret = len(bolygojegyben_kerdesbank)
    # for i in bolygojegyben_kerdesbank:
    #     print(i)

    kerdesek = []
    import random

    for _ in range(int(kviz_adatok["kérdésszám"])):
        # print(kerdesek)
        kivalasztott_kerdes_valasz = bolygojegyben_kerdesbank[random.randint(0, kerdesbank_meret-1)]

        valasz_opciok = [
                {"opcio": kivalasztott_kerdes_valasz["valasz"], "helyes_e": "igaz"},
                {"opcio": bolygojegyben_kerdesbank[random.randint(0, kerdesbank_meret)]["valasz"], "helyes_e": "haims"},
                {"opcio": bolygojegyben_kerdesbank[random.randint(0, kerdesbank_meret)]["valasz"], "helyes_e": "haims"}
            ]
        random.shuffle(valasz_opciok)
        kerdesek.append({
            "kerdesnev": kivalasztott_kerdes_valasz["kerdes"],

            "valasz_opciok": valasz_opciok})
    print("kérdések")
    print(kerdesek)
    return kerdesek


def egy_kerdes_hozzaadasa(web, kerdes_neve, hozzatartozo_kviz_value, valasz_opciok):
    szoveg_kitoltes(web, xpath='//*[@id="id_content"]', tartalom=kerdes_neve)
    # value ---> hozzatartozo kviz
    value_alapjan_kivalasztas(web, xpath='//*[@id="id_quiz"]', value=hozzatartozo_kviz_value)  # tudni kell mi a vauleja
    print(valasz_opciok)
    for hanyadik_valaszlehetoseg, opcio in enumerate(valasz_opciok):
        egy_valasz_opcio_hozzaadas(web,
                                   valasz_nev=opcio["opcio"],
                                   helyes_e=opcio["helyes_e"],
                                   hanyadik_valaszlehetoseg=hanyadik_valaszlehetoseg)
    # mentés és újabb hozzáadása
    raklikkeles(web, xpath='/html/body/div/div[3]/div/div[1]/div/form/div/div[2]/input[2]')


def egy_valasz_opcio_hozzaadas(web, valasz_nev: str, helyes_e, hanyadik_valaszlehetoseg: int):
    if hanyadik_valaszlehetoseg <= 3:
        szoveg_kitoltes(web,
                        xpath=f'//*[@id="id_answer_set-{hanyadik_valaszlehetoseg}-content"]',
                        tartalom=valasz_nev)
        # CHECKBOX
        if helyes_e == "igaz":
            raklikkeles(web, xpath=f'//*[@id="id_answer_set-{hanyadik_valaszlehetoseg}-correct"]')


    if hanyadik_valaszlehetoseg > 3:
        # todo uj opciot hozzaadni
        pass


def raklikkeles(web, xpath):
    web.find_element_by_xpath(xpath).click()


#
# def kerdes_kitoltes(web, hanyadikkerdes, kerdes, igaze):
#     select = Select(web.find_element_by_xpath(f'//*[@id="id_answer_set-{hanyadikkerdes}-content"]'))
#     select.select_by_value(kerdes)
#     # todo igaze kockát bepipáltatni

def szoveg_kitoltes(web, xpath, tartalom):
    select = web.find_element_by_xpath(xpath)
    select.clear()
    select.send_keys(tartalom)


def value_alapjan_kivalasztas(web, xpath, value):
    select = Select(web.find_element_by_xpath(xpath))
    select.select_by_value(value)
