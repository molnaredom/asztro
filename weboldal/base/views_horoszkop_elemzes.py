import datetime

from django.shortcuts import render
import pandas as pd
from .models import Horoszkop2, Jegy2


def horoszkop(request, id):
    analogia = Horoszkop2.objects.get(id=id)
    osszesjegy = Jegy2.objects.all()

    analogia.fokszamok = eval(dict(analogia.fokszamok)["analogiak"])  # eval strbol dictet csinal

    elemzes_adat = _elemzes(analogia, osszesjegy)
    context = {"analogia": analogia, "elemzes": elemzes_adat}  # ez egy objektum

    return render(request, "konkret_analogiak/horoszkop.html", context)


def _elemzes(adatok, osszesjegy):
    eredmeny = {}

    pontos_kor =szuletesi_datumido(adatok)

    bolygok, hazak = fokszamhozzarendeles(adatok)
    bolygok, hazak = osszfokszam_hozzarendeles(bolygok, hazak)
    bolygok = bolygohoz_haz_rendeles(hazak, bolygok)  # megmondja egy bolygo milyen hazban van
    bolygok = hazhoz_bolygok_rendelese(hazak, bolygok)  # megmondja egy_egy hazban milyen bolygok vannak

    eredmeny["alapszamolasok"] = alapszamolasok(adatok, osszesjegy)
    eredmeny["pontos kor"] = pontos_kor_szamitas(pontos_kor)
    eredmeny["életciklus"] = eletciklus(pontos_kor)
    eredmeny["sorstípus"] = _sorstipus(bolygok, hazak)

    return eredmeny


def pontos_kor_szamitas(pontoskor:datetime):
    return f'A pontos életkorod {pontoskor.year} év  ' \
           f'{pontoskor.month} hónap  ' \
           f'{pontoskor.day} nap  ' \
           f'{pontoskor.hour} óra  ' \
           f'{pontoskor.minute} perc ' \
           f'{pontoskor.second} másodperc.'


def szuletesi_datumido(adatok):
    szuletes = adatok.idopont.replace(tzinfo=None)


    currentDate = datetime.datetime.now()
    deadlineDate = szuletes
    # print(deadlineDate)
    daysLeft = currentDate - deadlineDate
    # print(daysLeft)

    years = ((daysLeft.total_seconds()) / (365.242199 * 24 * 3600))
    yearsInt = int(years)

    months = (years - yearsInt) * 12
    monthsInt = int(months)

    days = (months - monthsInt) * (365.242199 / 12)
    daysInt = int(days)

    hours = (days - daysInt) * 24
    hoursInt = int(hours)

    minutes = (hours - hoursInt) * 60
    minutesInt = int(minutes)

    seconds = (minutes - minutesInt) * 60
    secondsInt = int(seconds)

    pontos_kor = datetime.datetime(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt)


    return pontos_kor


def hazhoz_bolygok_rendelese(hazak, bolygok):
    for haz in hazak:
        haz["bolygok"] = []

    for haz in hazak:
        for bolygo in bolygok:
            if haz["haz"] == bolygo["hazszam"]["haz"]:
                haz["bolygok"].append(bolygo)

    return bolygok


def bolygohoz_haz_rendeles(hazak, bolygok):
    ujhaz = {"jegy": hazak[0]["jegy"], "haz": hazak[0]["haz"], "fokszam": hazak[0]["fokszam"], "osszfokszam": 360}
    hazak.append(ujhaz)

    for bolygo in bolygok:
        for hazszam, haz in enumerate(hazak):
            # todo keletkezett e lefedetlen resz?
            # todo ellenorizni mi van akkor ha a 12. hazbol atmegy az 1 es hazba
            if haz["haz"].tipus == "sarok" and bolygo["osszfokszam"] + 5 < hazak[hazszam + 1]["osszfokszam"]:
                bolygo["hazszam"] = haz
                break
            elif haz["haz"].tipus != "sarok" and bolygo["osszfokszam"] + 3 < hazak[hazszam + 1]["osszfokszam"]:
                bolygo["hazszam"] = haz
                break
        else:
            print("valami nincs lekezelve")
            raise Exception

    hazak.pop(-1)  # elttűntetni a plusz 1 házat

    return bolygok


def fokszamhozzarendeles(adatok):
    bolygojegyben_adatok = [adatok.nap, adatok.hold, adatok.merkur, adatok.venusz, adatok.mars, adatok.jupiter,
                            adatok.szaturnusz,
                            adatok.uranusz, adatok.neptun, adatok.pluto]

    hazjegyben_adatok = [adatok.haz_1, adatok.haz_2, adatok.haz_3, adatok.haz_4, adatok.haz_5, adatok.haz_6,
                         adatok.haz_7,
                         adatok.haz_8, adatok.haz_9, adatok.haz_10, adatok.haz_11, adatok.haz_12]

    # bolygok, hazak = {}, {} # egy regi otlet
    bolygok, hazak = [], []

    for analogia in list(
            zip(['nap', 'hold', 'merkur', 'venusz', 'mars', 'jupiter', 'szaturnusz', 'uranusz', 'neptun', 'pluto'],
                bolygojegyben_adatok)):
        bolygok.append(
            {"jegy": analogia[1].jegy, "bolygo": analogia[1].bolygo, "fokszam": adatok.fokszamok[analogia[0]]})

    for analogia in list(
            zip(['haz1', 'haz2', 'haz3', 'haz4', 'haz5', 'haz6', 'haz7', 'haz8', 'haz9', 'haz10', 'haz11', 'haz12'],
                hazjegyben_adatok)):
        hazak.append({"jegy": analogia[1].jegy, "haz": analogia[1].haz, "fokszam": adatok.fokszamok[analogia[0][3:]]})

    return bolygok, hazak  # pd.DataFrame(bolygok), pd.DataFrame(hazak)


def osszfokszam_hozzarendeles(bolygok, hazak):
    ascfok, ascjegy = float(hazak[0]["fokszam"]), hazak[0]["jegy"].nevID

    for haz in hazak:
        haz["osszfokszam"] = hanyadik_jegy_asctol(ascjegy, haz["jegy"].nevID) * 30 - ascfok + float(haz["fokszam"])
        # print(haz["haz"], haz["jegy"].nevID,haz["osszfokszam"],hanyadik_jegy_asctol(ascjegy,haz["jegy"].nevID), ascfok,float(haz["fokszam"]   ))

    for bolygo in bolygok:
        bolygo["osszfokszam"] = hanyadik_jegy_asctol(ascjegy, bolygo["jegy"].nevID) * 30 - ascfok + float(
            bolygo["fokszam"])
        # print(bolygo["bolygo"], bolygo["jegy"].nevID,bolygo["osszfokszam"],hanyadik_jegy_asctol(ascjegy,bolygo["jegy"].nevID), ascfok,float(bolygo["fokszam"]   ))

    return bolygok, hazak


def hanyadik_jegy_asctol(kiindulasijegy, aktjegy):
    kiind_szam, akt_szam = jegyet_szamra_valt(kiindulasijegy), jegyet_szamra_valt(aktjegy)
    return (akt_szam - kiind_szam) % 12


def jegyet_szamra_valt(jegynev):
    jegyhezszam = {"kos": 1, "bika": 2, "ikrek": 3, "rák": 4, "oroszlán": 5, "szűz": 6, "mérleg": 7, "skorpió": 8,
                   "nyilas": 9, "bak": 10,
                   "vízöntő": 11, "halak": 12}
    return jegyhezszam[jegynev]


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


def _sorstipus(bolygok, hazak):
    kiemelthazak = ["1", "5", "9", "10", "11"]

    kiemelthazakbolygoi = []
    for haz in hazak:
        if haz["haz"].nevID in kiemelthazak:
            for bolygo in haz["bolygok"]:
                kiemelthazakbolygoi.append(bolygo["bolygo"].nevID)


    if "uránusz" in kiemelthazakbolygoi and "neptun" not in kiemelthazakbolygoi:
        return "elsőkörös uránuszi"
    elif "neptun" in kiemelthazakbolygoi and "uránusz" not in kiemelthazakbolygoi:
        return "elsőkörös neptuni"

    if "jupiter" in kiemelthazakbolygoi and "szaturnusz" not in kiemelthazakbolygoi:
        return "második körös kiszolgáltatott"
    elif "szaturnusz" in kiemelthazakbolygoi and "jupiter" not in kiemelthazakbolygoi:
        return "második körös önfeláldozó"

    felhasznaltbolygok = ["neptun", "uránusz", "jupiter", "szaturnusz"]
    haz11pontszam = sum([i["bolygo"].pontertek for i in hazak[10]["bolygok"]
                         if i["bolygo"].nevID not in felhasznaltbolygok])
    haz12pontszam = sum([i["bolygo"].pontertek for i in hazak[11]["bolygok"]
                         if i["bolygo"].nevID not in felhasznaltbolygok])
    print("haz11pontszam, haz12pontszam", haz11pontszam, haz12pontszam)

    if haz11pontszam > haz12pontszam:
        return "haramdik körös kiszolgáltatott"
    elif haz11pontszam < haz12pontszam:
        return "harmadik körös önfeláldozó"

    # 4. kör
    halakpontszam = sum([i["bolygo"].pontertek for i in bolygok
                         if i["jegy"].nevID == "halak" and i["bolygo"].nevID not in felhasznaltbolygok])
    vizontopontszam = sum([i["bolygo"].pontertek for i in bolygok
                           if i["jegy"].nevID == "vízöntő" and i["bolygo"].nevID not in felhasznaltbolygok])
    print("halakpontszam, vizontopontszam", halakpontszam, vizontopontszam)

    if vizontopontszam > halakpontszam:
        return "negyedik körös kiszolgáltatott"
    elif halakpontszam > vizontopontszam:
        return "negyedik körös önfeláldozó"

    return "a jelenlegi adatok alapján nem lehet kiszámolni a sorstípust mert 5. körös lenne"


def eletciklus(pontos_kor):
    yearsInt =pontos_kor.year
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


if __name__ == '__main__':
    h = {adatok.nap: 2, adatok.hold: 3}
    print(h[adatok.nap])
