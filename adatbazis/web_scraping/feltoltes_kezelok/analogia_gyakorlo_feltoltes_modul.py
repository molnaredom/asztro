import time

from selenium.webdriver.support.select import Select

from adatbazis.web_scraping.kisegito_modulok.feltoltes_kisegito_modul import feltoltes


def analogiagyakorlo_feltoltes(web,  domain):

    kvizek = [{"név":"Bolygójegyben gyakorló",
               "leírás":"ez egy közepes nehézségű teszt",
               "kérdésszám" : "10",
               "idő": "200",
               "kviz_value": 0
               }]

    bejelentkezes_adminkent(web, domain)

    kvizek_hozzaadasa(domain, web, kvizek)

    bolygojegyben_kozepes_kviz_kerdesfeltoltes(web,domain, kviz_value="13")


def bejelentkezes_adminkent(web, domain):
    time.sleep(0.5)
    web.get(f'{domain}/admin')
    szoveg_kitoltes(web, xpath= '//*[@id="id_username"]', tartalom= "1")
    szoveg_kitoltes(web, xpath= '//*[@id="id_password"]', tartalom= "1")
    raklikkeles(web, xpath='/html/body/div/div[2]/div/div[1]/div/form/div[3]/input')
    time.sleep(0.5)


def kvizek_hozzaadasa(domain, web, kvizek):
    web.get(f'{domain}/admin/home/quiz/add/')

    for kviz in kvizek:
        szoveg_kitoltes(web, '//*[@id="id_name"]',kviz["név"])
        szoveg_kitoltes(web, '//*[@id="id_desc"]',kviz["leírás"])
        szoveg_kitoltes(web, '//*[@id="id_number_of_questions"]',kviz["kérdésszám"])
        szoveg_kitoltes(web, '//*[@id="id_time"]',kviz["idő"])
        # mentés
        raklikkeles(web, xpath='/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]')


def bolygojegyben_kozepes_kviz_kerdesfeltoltes(web,domain, kviz_value):
    web.get(f'{domain}/admin/home/question/add/')
    kerdesek = kerdes_generator()

    for kerdes in kerdesek:
        egy_kerdes_hozzaadasa(web,
                              kerdes_neve= kerdes["kerdesnev"],
                              valasz_opciok=kerdes["valasz_opciok"],
                              hozzatartozo_kviz_value= kviz_value
                              )

def kerdes_generator():

    kerdesek = []

    kerdesek.append({
        "kerdesnev": "kerdes --- ez a neve",
        "valasz_opciok": [
            {"opcio": "igaz e h igaz", "helyes_e":"igaz"},
            {"opcio": "igaz e h hamis", "helyes_e":"haims"},
            {"opcio": "hamis ez tuti hamis", "helyes_e":"haims"}
        ]})
    kerdesek.append({
        "kerdesnev": "kerdes --- ez a neve",
        "valasz_opciok": [
            {"opcio": "igaz e h igaz", "helyes_e":"igaz"},
            {"opcio": "igaz e h hamis", "helyes_e":"haims"},
            {"opcio": "hamis ez tuti hamis", "helyes_e":"haims"}
        ]})
    kerdesek.append({
        "kerdesnev": "kerdes --- ez a neve2",
        "valasz_opciok": [
            {"opcio": "igaz e h igaz", "helyes_e":"igaz"},
            {"opcio": "igaz e h hamis", "helyes_e":"haims"},
            {"opcio": "hamis ez tuti hamis", "helyes_e":"haims"}
        ]})
    kerdesek.append({
        "kerdesnev": "kerdes --- ez a neve3",
        "valasz_opciok": [
            {"opcio": "igaz e h igaz", "helyes_e":"igaz"},
            {"opcio": "igaz e h hamis", "helyes_e":"haims"},
            {"opcio": "hamis ez tuti hamis", "helyes_e":"haims"}
        ]})
    kerdesek.append({
        "kerdesnev": "kerdes --- ez a neve4",
        "valasz_opciok": [
            {"opcio": "igaz e h igaz", "helyes_e":"igaz"},
            {"opcio": "igaz e h hamis", "helyes_e":"haims"},
            {"opcio": "hamis ez tuti hamis", "helyes_e":"haims"}
        ]})


    return kerdesek


def egy_kerdes_hozzaadasa(web, kerdes_neve, hozzatartozo_kviz_value, valasz_opciok):
    szoveg_kitoltes(web, xpath='//*[@id="id_content"]',tartalom= kerdes_neve )
    # value ---> hozzatartozo kviz
    value_alapjan_kivalasztas(web, xpath='//*[@id="id_quiz"]', value=hozzatartozo_kviz_value) # tudni kell mi a vauleja

    for hanyadik_valaszlehetoseg, opcio in enumerate(valasz_opciok):
        egy_valasz_opcio_hozzaadas(web,
                                   valasz_nev = opcio["opcio"],
                                   helyes_e = opcio["helyes_e"],
                                   hanyadik_valaszlehetoseg = hanyadik_valaszlehetoseg)
    # mentés és újabb hozzáadása
    raklikkeles(web, xpath='/html/body/div/div[3]/div/div[1]/div/form/div/div[2]/input[2]')


def egy_valasz_opcio_hozzaadas(web, valasz_nev:str, helyes_e:bool, hanyadik_valaszlehetoseg:int):
    if hanyadik_valaszlehetoseg <= 3:
        szoveg_kitoltes(web,
                        xpath=f'//*[@id="id_answer_set-{hanyadik_valaszlehetoseg}-content"]',
                        tartalom= valasz_nev)
        # CHECKBOX
        if helyes_e:
            raklikkeles(web, xpath= f'//*[@id="id_answer_set-{hanyadik_valaszlehetoseg}-correct"]')
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

def szoveg_kitoltes(web,xpath,tartalom):
    select = web.find_element_by_xpath(xpath)
    select.clear()
    select.send_keys(tartalom)


def value_alapjan_kivalasztas(web, xpath, value):
    select = Select(web.find_element_by_xpath(xpath))
    select.select_by_value(value)
