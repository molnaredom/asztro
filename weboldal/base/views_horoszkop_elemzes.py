import datetime

from django.shortcuts import render
import pandas as pd
from .models import Horoszkop2, Jegy2, HazUraHazban


def horoszkop(request, id):
    analogia = Horoszkop2.objects.get(id=id)
    hazakUraHazakban = HazUraHazban.objects.all()
    osszesjegy = Jegy2.objects.all()

    analogia.fokszamok = eval(dict(analogia.fokszamok)["analogiak"])  # eval strbol dictet csinal

    elemzes_adat = _elemzes(analogia, osszesjegy, hazakUraHazakban)
    context = {"analogia": analogia, "elemzes": elemzes_adat}  # ez egy objektum

    return render(request, "konkret_analogiak/horoszkop.html", context)


def _elemzes(adatok, osszesjegy, hazakUraHazakban):
    eredmeny = {}

    pontos_kor = szuletesi_datumido(adatok)

    bolygok, hazak = fokszamhozzarendeles(adatok)
    bolygok, hazak = osszfokszam_hozzarendeles(bolygok, hazak)

    bolygok = bolygohoz_haz_rendeles(hazak, bolygok)  # megmondja egy bolygo milyen hazban van
    bolygok = hazhoz_bolygok_rendelese(hazak, bolygok)  # megmondja egy_egy hazban milyen bolygok vannak

    bolygok = fenyszog_hozzarendeles(bolygok)

    hazura_melyik_hazaban(hazak, bolygok)
    # [print(i["haz"].nevID, [j["bolygo"] for j in i["bolygok"]]) for i in hazak]

    eredmeny["alapszamolasok"] = alapszamolasok(adatok, osszesjegy)
    eredmeny["pontoskor"] = pontos_kor_szamitas(pontos_kor)
    eredmeny["eletciklus"] = eletciklus(pontos_kor)
    eredmeny["sorstipus"] = _sorstipus(bolygok, hazak)
    eredmeny["hazakurai"] = hazura_kiiratas(hazak, hazakUraHazakban)
    eredmeny["serult_e_nap"] = serult_e_nap(bolygok, adatok)
    eredmeny["serult_e_hold"] = serult_e_hold(bolygok, adatok)
    hyleg_res = hyleg(bolygok)
    eredmeny["hyleg"] = hyleg_res
    eredmeny["anareta"] = anareta(hyleg_res, bolygok)


    return eredmeny


def pontos_kor_szamitas(pontoskor: datetime):
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

    pontos_kor = datetime.datetime(yearsInt, monthsInt, daysInt, hoursInt, minutesInt, secondsInt)

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
            # todo ellenorizni mi van akkor ha a 12. hazbol atmegy az 1 es hazba
            if haz["haz"].tipus == "sarok" and bolygo["osszfokszam"] + 5 < hazak[hazszam + 1]["osszfokszam"]:
                bolygo["hazszam"] = haz
                break
            elif haz["haz"].tipus != "sarok" and bolygo["osszfokszam"] + 3 < hazak[hazszam + 1]["osszfokszam"]:
                bolygo["hazszam"] = haz
                # print(bolygo["bolygo"],bolygo["hazszam"])
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

#
# def _altalanosfelosztas_adagolo(szetoszto, bolygok, jegynalogia, asc):
#     szetoszto[asc] += 2
#
#     for bolygok in bolygok:
#         if str(bolygok) in ["nap", "hold", "merkúr"]:
#             szetoszto[jegynalogia] += 2
#         else:
#             szetoszto[jegynalogia] += 1
#
#     return evszakok


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
    # print("haz11pontszam, haz12pontszam", haz11pontszam, haz12pontszam)

    if haz11pontszam > haz12pontszam:
        return "haramdik körös kiszolgáltatott"
    elif haz11pontszam < haz12pontszam:
        return "harmadik körös önfeláldozó"

    # 4. kör
    halakpontszam = sum([i["bolygo"].pontertek for i in bolygok
                         if i["jegy"].nevID == "halak" and i["bolygo"].nevID not in felhasznaltbolygok])
    vizontopontszam = sum([i["bolygo"].pontertek for i in bolygok
                           if i["jegy"].nevID == "vízöntő" and i["bolygo"].nevID not in felhasznaltbolygok])
    # print("halakpontszam, vizontopontszam", halakpontszam, vizontopontszam)

    if vizontopontszam > halakpontszam:
        return "negyedik körös kiszolgáltatott"
    elif halakpontszam > vizontopontszam:
        return "negyedik körös önfeláldozó"

    return "a jelenlegi adatok alapján nem lehet kiszámolni a sorstípust mert 5. körös lenne"


def eletciklus(pontos_kor):
    yearsInt = pontos_kor.year
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


def hazura_melyik_hazaban(hazak, bolygok):

    def hazurnak_bolygot_talal(hazura_nev):
        for bolygo in bolygok:
            if bolygo["bolygo"].nevID == hazura_nev:
                return bolygo
        else:
            raise Exception

    def jegyvaltas(hazura_bolygo):
        konjukciok = hazura_bolygo["fenyszogek"]["konjukcio"]
        # for egyuttallo_bolygo in konjukciok:
        #     print(egyuttallo_bolygo["bolygo"].nevID)
        egyuttallo_bolygo_szam = len(konjukciok)
        if egyuttallo_bolygo_szam == 0:
            return False
        elif egyuttallo_bolygo_szam == 1:
            return True
        elif egyuttallo_bolygo_szam > 1 and "transzcendens" in [konjukcio["bolygo"]["bolygo"].tipus for konjukcio in konjukciok]:
            return False
        elif egyuttallo_bolygo_szam > 1:
            return True
        else:
            print("baj van jegyvaltas -nal")

    for haz in hazak: # 12
        hazura_nev = haz["jegy"].uralkodo_bolygo
        hazura_bolygo = hazurnak_bolygot_talal(hazura_nev)
        for belso_haz in hazak: # 12
            for belso_bolygo in belso_haz["bolygok"]: # 0-10
                if hazura_nev == belso_bolygo["bolygo"].nevID:
                    # print(haz["haz"], haz["jegy"].nevID, haz["jegy"].paritas)
                    # print(belso_haz["haz"],belso_bolygo["jegy"].nevID,belso_bolygo["bolygo"].nevID, belso_bolygo["jegy"].paritas)
                    # print("hazura:", hazura_nev)
                    # print()
                    if belso_bolygo["bolygo"].nevID == "hold" or belso_bolygo["bolygo"].nevID == "nap":# nap/hold
                        haz["hazura"] = belso_haz["haz"]

                    if jegyvaltas(hazura_bolygo):
                        if haz["jegy"].paritas != belso_bolygo["jegy"].paritas:  # ellentétes a polaritás
                            haz["hazura"] = belso_haz["haz"]

                    else:
                        if haz["jegy"].paritas == belso_bolygo["jegy"].paritas:  # megyegyezik a polaritás
                            haz["hazura"] = belso_haz["haz"]

        if "hazura" not in haz: # ugy fut le hogy nem talalt hazurat
            haz["hazura"] = "nincs hazur"


def hazura_kiiratas(hazak, hazakUraHazakban):

    def hazur_kiiratas(haz, ura):
        if ura in ["1", "2", "4", "7", "9", '10', '11', "12"]:
            return f"{haz}.ház ura az {ura}-es házban"
        elif ura in ["3","8"]:
            return f"{haz}.ház ura az {ura}-as házban"
        elif ura in ["6"]:
            return f"{haz}.ház ura az {ura}-os házban"
        elif ura in ["5"]:
            return f"{haz}.ház ura az {ura}-ös házban"
        elif ura == "nincs hazur":
            return f"{haz}.háznak nincs ura"
        else:
            print("HIBA")
            print(ura)

    haz_urak_kiiratva = []

    for i in hazak:
        for hazurahazban in hazakUraHazakban:
            # print(hazurahazban.alap_haz, str(i["haz"]) ,"--", hazurahazban.ura_melyik_hazban ,str(i["hazura"]))
            if str(hazurahazban.alap_haz) == str(i["haz"]) and str(hazurahazban.ura_melyik_hazban) == str(i["hazura"]):
                # print("házura")
                haz_urak_kiiratva.append({hazur_kiiratas(haz=str(i["haz"]), ura=str(i["hazura"])) : hazurahazban.tulajdonsagok })


    return haz_urak_kiiratva
    # [print(hazur_kiiratas(haz=str(i["haz"]), ura=str(i["hazura"]))) for i in hazak]


def fenyszog_hozzarendeles(bolygok, orbisz=8):
    for bolygo in bolygok:
        bolygo["fenyszogek"] = {}
        bolygo["fenyszogek"]["konjukcio"] = []
        bolygo["fenyszogek"]["oppozicio"] = []
        bolygo["fenyszogek"]["kvadrat"] = []
        bolygo["fenyszogek"]["trigon"] = []


    for kulso_bolygo in bolygok:
        for belso_bolygo in bolygok:
            kulso_osszfok = float(kulso_bolygo["osszfokszam"])
            belso_osszfok = float(belso_bolygo["osszfokszam"])

            debug = True
            # konjukció
            fenyszog_szamol(belso_bolygo, belso_osszfok, kulso_bolygo, kulso_osszfok, orbisz,
                            fenyszogtipus="konjukcio", fok_kilenges=0, debug=debug)
            # oppozicio
            fenyszog_szamol(belso_bolygo, belso_osszfok, kulso_bolygo, kulso_osszfok, orbisz,
                            fenyszogtipus="oppozicio", fok_kilenges=180, debug=debug)
            # kvadrat
            fenyszog_szamol(belso_bolygo, belso_osszfok, kulso_bolygo, kulso_osszfok, orbisz,
                            fenyszogtipus="kvadrat", fok_kilenges=90, debug=debug)
            # trigon
            fenyszog_szamol(belso_bolygo, belso_osszfok, kulso_bolygo, kulso_osszfok, orbisz,
                            fenyszogtipus="trigon", fok_kilenges=120, debug=debug)

    bolygok = lancolt_egyuttallas(bolygok)
    return bolygok


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

    kiemelt_vilagos_hazak = [1,5,9,10,11]
    kiemelt_sotet_hazak = [4,8,12]

    hold = bolygok[1]
    neme = adatok.neme
    # print(neme, int(hold["hazszam"]["haz"].nevID))
    if neme == "férfi" and int(hold["hazszam"]["haz"].nevID) in kiemelt_vilagos_hazak:
        return "+ hold"
    elif neme == "nő" and int(hold["hazszam"]["haz"].nevID) in kiemelt_sotet_hazak:
        return "- hold"
    else:
        return "a hold nem sérült"


def fenyszog_szamol(belso_bolygo, belso_osszfok, kulso_bolygo, kulso_osszfok, orbisz, fenyszogtipus, fok_kilenges,
                    debug):

    # jobb oldali fényszög
    if (kulso_osszfok + orbisz > belso_osszfok + fok_kilenges > kulso_osszfok - orbisz
            and belso_bolygo["bolygo"] != kulso_bolygo["bolygo"]):

        fokelteres = abs(belso_osszfok + fok_kilenges - kulso_osszfok)

        if debug:
            print(fenyszogtipus)
            print(belso_bolygo["bolygo"], kulso_bolygo["bolygo"])

        belso_bolygo["fenyszogek"][fenyszogtipus].append({"bolygo":kulso_bolygo, "fokelteres":fokelteres })

    # bal oldali fényszög
    elif (kulso_osszfok + orbisz > belso_osszfok - fok_kilenges > kulso_osszfok - orbisz
            and belso_bolygo["bolygo"] != kulso_bolygo["bolygo"]):

        fokelteres = abs(belso_osszfok + fok_kilenges - kulso_osszfok)

        if debug:
            print(fenyszogtipus)
            print(belso_bolygo["bolygo"], kulso_bolygo["bolygo"])

        belso_bolygo["fenyszogek"][fenyszogtipus].append({"bolygo":kulso_bolygo, "fokelteres":fokelteres })


def lancolt_egyuttallas(bolygok):
    for kulso_bolygo in bolygok:
        # hold
        for belso_bolygo in bolygok:
            if kulso_bolygo != belso_bolygo:
                kulso_konjukcios_bolygok = [i["bolygo"] for i in kulso_bolygo["fenyszogek"]["konjukcio"]]
                belso_konjukcios_bolygok = [i["bolygo"] for i in belso_bolygo["fenyszogek"]["konjukcio"]]

                for kulso_konjukcios_bolygo in kulso_konjukcios_bolygok:
                    # print(kulso_bolygo)
                    if kulso_konjukcios_bolygo not in belso_konjukcios_bolygok and \
                            kulso_bolygo["bolygo"].nevID in [i["bolygo"].nevID for i in belso_konjukcios_bolygok] and \
                            belso_bolygo["bolygo"].nevID != kulso_konjukcios_bolygo["bolygo"].nevID:
                        belso_konjukcios_bolygok.append(kulso_konjukcios_bolygo)
                        # print(kulso_konjukcios_bolygo["bolygo"].nevID, belso_bolygo["bolygo"].nevID)
                        # print(kulso_bolygo["bolygo"], belso_bolygo["bolygo"])
                        # print()
    return bolygok


def hyleg(bolygok):

    kiemelt_hazak = [7,9,10,11]
    if int(bolygok[0]["hazszam"]["haz"].nevID) in kiemelt_hazak:
        return "nap"
    elif int(bolygok[1]["hazszam"]["haz"].nevID) in kiemelt_hazak:
        return "hold"
    else:
        return "ASC"


def anareta(hyleg, bolygok):

    if hyleg == "nap":
        print("NAP")
        oppoziciok = bolygok[0]["fenyszogek"]["oppozicio"]
        kvadratok = bolygok[0]["fenyszogek"]["kvadrat"]
        if oppoziciok:
            oppoziciok.sort(key=lambda x: float(x["fokelteres"]))
            return str(oppoziciok[0]["bolygo"]["bolygo"].nevID) + " (oppozíció)"

        elif kvadratok:
            #print("KVAD", len(kvadratok))
            # print( [[i["bolygo"]["bolygo"].nevID,i["fokelteres"]] for i in kvadratok ])
            # print(kvadratok.sort())

            kvadratok.sort(key=lambda x: float(x["fokelteres"]))
            return str(kvadratok[0]["bolygo"]["bolygo"].nevID) + " (kvadrát)"
            # [print(i) for i in kvadratok]
        else:
            return "Nincs anaréta"

    elif hyleg == "hold":
        print("HOLD")
        # print(bolygok[1]["fenyszogek"])
        oppoziciok = bolygok[1]["fenyszogek"]["oppozicio"]
        kvadratok = bolygok[1]["fenyszogek"]["kvadrat"]

        if oppoziciok:
            oppoziciok.sort(key=lambda x: float(x["fokelteres"]))
            return str(oppoziciok[0]["bolygo"]["bolygo"].nevID) + " (oppozíció)"

        elif kvadratok:
            kvadratok.sort(key=lambda x: float(x["fokelteres"]))
            return str(kvadratok[0]["bolygo"]["bolygo"].nevID) + " (kvadrát)"
        else:
            return "Nincs anaréta"

    elif hyleg == "ASC":
        return "Nincs anaréta"
        # [print(i) for i in bolygok[0]["fenyszogek"]]
