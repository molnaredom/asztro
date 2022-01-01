from django.shortcuts import render
import pandas as pd
from .models import Horoszkop2, Jegy2


def horoszkop(request, id):
    analogia = Horoszkop2.objects.get(id=id)
    osszesjegy = Jegy2.objects.all()
    # print(analogia.fokszamok)
    analogia.fokszamok = eval(dict(analogia.fokszamok)["analogiak"]) # eval strbol dictet csinal

    elemzes_adat = _elemzes(analogia, osszesjegy)
    context = {"analogia": analogia, "elemzes": elemzes_adat}  # ez egy objektum

    return render(request, "konkret_analogiak/horoszkop.html", context)


def _elemzes(adatok, osszesjegy):
    eredmeny = {}
    eredmeny = alapszamolasok(adatok, osszesjegy)

    adatok = fokszamhozzarendeles(adatok)

    return eredmeny

def fokszamhozzarendeles(adatok):
    bolygojegyben_adatok = [adatok.nap, adatok.hold, adatok.merkur, adatok.venusz, adatok.mars, adatok.jupiter, adatok.szaturnusz,
               adatok.uranusz, adatok.neptun, adatok.pluto]

    hazjegyben_adatok = [ adatok.haz_1, adatok.haz_2, adatok.haz_3, adatok.haz_4, adatok.haz_5, adatok.haz_6, adatok.haz_7,
                adatok.haz_8, adatok.haz_9, adatok.haz_10, adatok.haz_11, adatok.haz_12]

    bolygok, hazak = {}, {}

    for analogia in list(zip(['nap', 'hold', 'merkur', 'venusz','mars', 'jupiter', 'szaturnusz', 'uranusz', 'neptun', 'pluto'],bolygojegyben_adatok)):
        bolygok[analogia[0]] = {"jegy": analogia[1].jegy, "bolygo": analogia[1].bolygo, "fokszam": adatok.fokszamok[analogia[0]]}

    for analogia in list(zip(['haz1', 'haz2', 'haz3', 'haz4', 'haz5', 'haz6', 'haz7', 'haz8', 'haz9', 'haz10', 'haz11', 'haz12'],hazjegyben_adatok)):
        hazak[analogia[0]] = {"jegy": analogia[1].jegy, "haz": analogia[1].haz, "fokszam": adatok.fokszamok[analogia[0][3:]]}

    return pd.DataFrame(bolygok), pd.DataFrame(hazak)


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
    eredmeny["sorstípus"] = _sorstipus(bolygok)


def _altalanosfelosztas_adagolo(szetoszto, bolygok, jegynalogia, asc):
    szetoszto[asc] += 2

    for bolygok in bolygok:
        if str(bolygok) in ["nap", "hold", "merkúr"]:
            szetoszto[jegynalogia] += 2
        else:
            szetoszto[jegynalogia] += 1

    return evszakok


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


def _sorstipus(adatok):
    kiemelthazak = [1, 5, 9, 10, 11, ]
    # todo nem tudjuk az uranusz milyen hazban van - fokszam kell hozza
    return 0


if __name__ == '__main__':
    h = {adatok.nap :2, adatok.hold:3 }
    print(h[adatok.nap])












