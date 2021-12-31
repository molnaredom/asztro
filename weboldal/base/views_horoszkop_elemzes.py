from django.shortcuts import render

from .models import Horoszkop2


def horoszkop(request, id):
    analogia = Horoszkop2.objects.get(id=id)

    elemzes_adat = _elemzes(analogia)
    context = {"analogia": analogia, "elemzes": elemzes_adat}  # ez egy objektum

    return render(request, "konkret_analogiak/horoszkop.html", context)

#todo asct is szamitasba venni rejtett ASC nel


def _elemzes(adatok):
    eredmeny = {}
    bolygok = [adatok.nap, adatok.hold, adatok.merkur, adatok.venusz, adatok.mars, adatok.jupiter, adatok.szaturnusz,
               adatok.uranusz, adatok.neptun, adatok.pluto]

    hazak = [adatok.haz_1, adatok.haz_2, adatok.haz_3, adatok.haz_4, adatok.haz_5, adatok.haz_6, adatok.haz_7
        , adatok.haz_8, adatok.haz_9, adatok.haz_10, adatok.haz_11, adatok.haz_12]

    eredmeny["évszak szerinti felosztás"] = _evszak_szerinti_felosztas(bolygok)
    eredmeny["minőség szerinti felosztás"] = _elemek_szerinti_felosztas(bolygok)
    eredmeny["elemek szerinti felosztás"] = minoseg_szarinti_felosztas(bolygok)
    eredmeny["rejtett ASC"] = rejtett_aszcendens(bolygok, eredmeny["elemek szerinti felosztás"], eredmeny["minőség szerinti felosztás"] )
    eredmeny["sorstípus"] = _sorstipus(bolygok)


    return eredmeny


def _evszak_szerinti_felosztas(bolygok):
    evszakok = {"tavasz": 0, "nyár": 0, "ősz": 0, "tél": 0}

    for bolygo in bolygok:
        print(bolygo.bolygo, evszakok)
        print(bolygo.bolygo)
        if str(bolygo.bolygo) in ["nap", "hold", "merkúr"]:
            evszakok[bolygo.jegy.evszak] += 2
        else:
            evszakok[bolygo.jegy.evszak] += 1

    return evszakok


def _elemek_szerinti_felosztas(bolygok):
    elemek = {"tűz": 0, "víz": 0, "föld": 0, "levegő": 0}

    for bolygo in bolygok:
        if str(bolygo.bolygo) in ["nap", "hold", "merkúr"]:
            elemek[bolygo.jegy.elem] += 2
        else:
            elemek[bolygo.jegy.elem] += 1

    return elemek


def minoseg_szarinti_felosztas(bolygok):
    minosegek = {"kardinális": 0, "szilárd": 0, "változó": 0}

    for bolygo in bolygok:
        if str(bolygo.bolygo) in ["nap", "hold", "merkúr"]:
            minosegek[bolygo.jegy.minoseg] += 2
        else:
            minosegek[bolygo.jegy.minoseg] += 1

    return minosegek

def rejtett_aszcendens(bolygok,elemek,minosegek):

    elem = max(elemek, key=elemek.get)
    minoseg = max(minosegek, key=minosegek.get)
    if list(elemek.values()).count(elem) == 1 and list(minosegek.values()).count(minoseg) == 1:

        return [bolygo.jegy for bolygo in bolygok if bolygo.jegy.minoseg == minoseg and bolygo.jegy.elem == elem][0]
    else:
        return "Nincs rejtett aszcendens"

def _sorstipus(adatok):
    kiemelthazak = [1, 5, 9, 10, 11, ]
    # todo nem tudjuk az uranusz milyen hazban van - fokszam kell hozza
    return 0
