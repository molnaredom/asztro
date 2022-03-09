import datetime

from ..default_parameters import *


def pontos_kor_szamitas(pontoskor: datetime):
    return f'A pontos életkorod {pontoskor[0]} év  ' \
           f'{pontoskor[1]} hónap  ' \
           f'{pontoskor[2]} nap  ' \
           f'{pontoskor[3]} óra  ' \
           f'{pontoskor[4]} perc ' \
           f'{pontoskor[5]} másodperc.'


def alapszamolasok(adatok, osszesjegy):
    eredmeny = {}
    bolygok = [adatok.nap, adatok.hold, adatok.merkur, adatok.venusz, adatok.mars, adatok.jupiter, adatok.szaturnusz,
               adatok.uranusz, adatok.neptun, adatok.pluto]
    # hazak = [adatok.haz_1, adatok.haz_2, adatok.haz_3, adatok.haz_4, adatok.haz_5, adatok.haz_6, adatok.haz_7
    #     , adatok.haz_8, adatok.haz_9, adatok.haz_10, adatok.haz_11, adatok.haz_12]

    eredmeny["évszak szerinti felosztás"] = _evszak_szerinti_felosztas(bolygok, adatok)
    eredmeny["minőség szerinti felosztás"] = minoseg_szarinti_felosztas(bolygok, adatok)
    eredmeny["elemek szerinti felosztás"] = _elemek_szerinti_felosztas(bolygok, adatok)
    eredmeny["rejtett ASC"] = rejtett_aszcendens(eredmeny["elemek szerinti felosztás"],
                                                 eredmeny["minőség szerinti felosztás"], osszesjegy)

    return eredmeny


def _evszak_szerinti_felosztas(bolygok, adatok):
    evszakok = {"tavasz": 0, "nyár": 0, "ősz": 0, "tél": 0}
    evszakok[adatok.haz_1.jegy.evszak] += 2
    for bolygo in bolygok:
        if str(bolygo.bolygo) in ["nap", "hold", "merkúr"]:
            evszakok[bolygo.jegy.evszak] += 2
        else:
            evszakok[bolygo.jegy.evszak] += 1

    return evszakok


def _elemek_szerinti_felosztas(bolygok, adatok):
    elemek = {"tűz": 0, "víz": 0, "föld": 0, "levegő": 0}
    elemek[adatok.haz_1.jegy.elem] += 2

    for bolygo in bolygok:
        if str(bolygo.bolygo) in ["nap", "hold", "merkúr"]:
            elemek[bolygo.jegy.elem] += 2
        else:
            elemek[bolygo.jegy.elem] += 1

    return elemek


def minoseg_szarinti_felosztas(bolygok, adatok):
    minosegek = {"kardinális": 0, "szilárd": 0, "változó": 0}
    minosegek[adatok.haz_1.jegy.minoseg] += 2

    for bolygo in bolygok:
        if str(bolygo.bolygo) in ["nap", "hold", "merkúr"]:
            minosegek[bolygo.jegy.minoseg] += 2
        else:
            minosegek[bolygo.jegy.minoseg] += 1

    return minosegek


def rejtett_aszcendens(elemek, minosegek, osszesjegy):
    maxelem_key, maxminoseg_key = str(max(elemek, key=elemek.get)), str(max(minosegek, key=minosegek.get))
    maxelem_value, max_minoseg_value = max(list(elemek.values())), max(list(minosegek.values()))

    if list(elemek.values()).count(maxelem_value) == 1 and list(minosegek.values()).count(max_minoseg_value) == 1:
        return [jegy.nevID for jegy in osszesjegy if maxelem_key == jegy.elem and maxminoseg_key == jegy.minoseg][0]
    else:
        return "Nincs rejtett aszcendens"


def eletciklus(pontos_kor):
    yearsInt = pontos_kor[0]
    eletciklus = ""
    if yearsInt > 63:
        eletciklus = "szaturnusz"
    elif yearsInt > 56:
        eletciklus = "jupiter-szaturnusz"
    elif yearsInt > 56:
        eletciklus = "jupiter"
    elif yearsInt > 42:
        eletciklus = "nap-mars"
    elif yearsInt > 35:
        eletciklus = "nap-jupiter"
    elif yearsInt > 28:
        eletciklus = "nap"
    elif yearsInt > 21:
        eletciklus = "ha férfi NAP, ha nő HOLD"
    elif yearsInt > 14:
        eletciklus = "ha fiú hold-mars, ha lány hold vénusz"
    elif yearsInt > 7:
        eletciklus = "hold-merkúr"
    elif yearsInt > 0:
        eletciklus = "hold"
    else:
        eletciklus = "még nem született meg"

    return eletciklus


def serult_e_nap(bolygok, adatok):

    kiemelt_vilagos_hazak = [1,5,9,10,11]
    kiemelt_sotet_hazak = [4,8,12]

    nap = bolygok[0]
    # print(nap)
    neme = adatok.neme
    # print(neme, int(nap["hazszam"]["haz"].nevID))

    if neme == "férfi" and int(nap["hazszam"]["haz"].nevID) in kiemelt_sotet_hazak:
        return "- nap"
    elif neme == "nő" and int(nap["hazszam"]["haz"].nevID) in kiemelt_vilagos_hazak:
        return "+ nap"
    else:
        return "a nap nem sérült"


def serult_e_hold(bolygok, adatok):
    fgv_nev = "serult_e_hold"
    kiemelt_vilagos_hazak = [1,5,9,10,11]
    kiemelt_sotet_hazak = [4,8,12]

    hold = bolygok[1]
    neme = adatok.neme
    printd(neme, int(hold["hazszam"]["haz"].nevID),problema=fgv_nev)
    if neme == "férfi" and int(hold["hazszam"]["haz"].nevID) in kiemelt_vilagos_hazak:
        return "+ hold"
    elif neme == "nő" and int(hold["hazszam"]["haz"].nevID) in kiemelt_sotet_hazak:
        return "- hold"
    else:
        return "a hold nem sérült"


def hyleg(bolygok):

    kiemelt_hazak = [7,9,10,11]
    if int(bolygok[0]["hazszam"]["haz"].nevID) in kiemelt_hazak:
        return "nap"
    elif int(bolygok[1]["hazszam"]["haz"].nevID) in kiemelt_hazak:
        return "hold"
    else:
        return "ASC"
