from .kisegito import hanyadik_jegy_asctol
from ..default_parameters import *



def ekezetnelkul(szo: str):
    szo =szo.replace("á", "a")
    szo =szo.replace("ű", "u")
    szo =szo.replace("ú", "u")
    szo =szo.replace("ó", "o")
    szo =szo.replace("ö", "o")
    szo =szo.replace("ő", "o")
    szo =szo.replace("é", "e")
    szo =szo.replace("í", "i")
    szo =szo.replace(" ", "_")
    szo.replace("á", "a")
    return szo

def bolygojegyben_id(bolygok):

    bolygojegyben_id_dict= dict()

    for adat in bolygok:
        print(adat["bolygo"].nevID, adat["hazszam"]["haz"].nevID, )
        bolygojegyben_id_dict[ekezetnelkul(adat["bolygo"].nevID)] = \
            {"value": ekezetnelkul( adat["hazszam"]["haz"].nevID),
            "name": str(adat["hazszam"]["haz"].nevID) + " - " + str(adat["bolygo"].nevID) }

    return bolygojegyben_id_dict


def hazhoz_bolygok_rendelese(hazak, bolygok):
    for haz in hazak:
        haz["bolygok"] = []

    for haz in hazak:
        for bolygo in bolygok:
            # if bolygo["bolygo"].nevID == "asc" or "mc":
            #     continue
            if haz["haz"] == bolygo["hazszam"]["haz"]:
                haz["bolygok"].append(bolygo)

    return bolygok


def bolygohoz_haz_rendeles(hazak, bolygok):
    ujhaz = {"jegy": hazak[0]["jegy"], "haz": hazak[0]["haz"], "fokszam": hazak[0]["fokszam"], "osszfokszam": 360}
    hazak.append(ujhaz)

    for bolygo in bolygok:
        # if bolygo["bolygo"].nevID == "asc" or "mc":
        #     continue todo

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
            printe("valami nincs lekezelve", problema=bolygohoz_haz_rendeles.__name__)
            raise Exception

    hazak.pop(-1)  # elttűntetni a plusz 1 házat

    return bolygok


def fokszamhozzarendeles(adatok):
    bolygojegyben_adatok = [adatok.nap, adatok.hold_j, adatok.merkur_j, adatok.venusz_j, adatok.mars_j, adatok.jupiter_j,
                            adatok.szaturnusz_j,adatok.uranusz_j, adatok.neptun_j, adatok.pluto_j,
                            adatok.asc_j, adatok.mc_j
                            ]

    hazjegyben_adatok = [adatok.haz_1, adatok.haz_2, adatok.haz_3, adatok.haz_4, adatok.haz_5, adatok.haz_6,
                         adatok.haz_7,
                         adatok.haz_8, adatok.haz_9, adatok.haz_10, adatok.haz_11, adatok.haz_12]
    print("..............", adatok.fokszamok)
    # bolygok, hazak = {}, {} # egy regi otlet
    bolygok, hazak = [], []
    # printd(bolygojegyben_adatok, problema=fokszamhozzarendeles.__name__)
    # printd(adatok.fokszamok, problema=fokszamhozzarendeles.__name__)

    for bolygonev, bj_obj in zip(['nap', 'hold', 'merkur', 'venusz', 'mars', 'jupiter', 'szaturnusz',
                 'uranusz', 'neptun', 'pluto', "asc", "mc"], bolygojegyben_adatok):
        # printd(bj_obj.jegy, problema=fokszamhozzarendeles.__name__)
        # printd(bj_obj.bolygo, problema=fokszamhozzarendeles.__name__)
        # print("fokszamok", adatok.fokszamok)
        if bolygonev == "asc":
            bolygok.append(
                {"jegy": bj_obj.jegy, "bolygo": bj_obj.bolygo, "fokszam": adatok.fokszamok["1"]})
        elif bolygonev == "mc":
            bolygok.append(
                {"jegy": bj_obj.jegy, "bolygo": bj_obj.bolygo, "fokszam": adatok.fokszamok["10"]})
        else:
            bolygok.append(
                {"jegy": bj_obj.jegy, "bolygo": bj_obj.bolygo, "fokszam": adatok.fokszamok[bolygonev]})

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


def hazura_melyik_hazaban(hazak, bolygok):
    def hazurnak_bolygot_talal(hazura_nev):
        for bolygo in bolygok:
            printd(bolygo["bolygo"].nevID, hazura_nev, problema=hazura_melyik_hazaban.__name__)
            if bolygo["bolygo"].nevID == hazura_nev:
                return bolygo
        # else:
        #     raise Exception

    def jegyvaltas(hazura_bolygo):
        konjukciok = hazura_bolygo["fenyszogek"]["konjukcio"]
        # for egyuttallo_bolygo in konjukciok:
        #     print(egyuttallo_bolygo["bolygo"].nevID)
        egyuttallo_bolygo_szam = len(konjukciok)
        if egyuttallo_bolygo_szam == 0:
            return False
        elif egyuttallo_bolygo_szam == 1:
            return True
        elif egyuttallo_bolygo_szam > 1 and "transzcendens" in [konjukcio["bolygo"]["bolygo"].tipus for konjukcio in
                                                                konjukciok]:
            return False
        elif egyuttallo_bolygo_szam > 1:
            return True
        else:
            printe("baj van jegyvaltas -nal", problema=jegyvaltas.__name__)

    for haz in hazak:  # 12
        hazura_nev = haz["jegy"].uralkodo_bolygo
        hazura_bolygo = hazurnak_bolygot_talal(hazura_nev)
        for belso_haz in hazak:  # 12
            for belso_bolygo in belso_haz["bolygok"]:  # 0-10
                if hazura_nev == belso_bolygo["bolygo"].nevID:
                    # print(haz["haz"], haz["jegy"].nevID, haz["jegy"].paritas)
                    # print(belso_haz["haz"],belso_bolygo["jegy"].nevID,belso_bolygo["bolygo"].nevID, belso_bolygo["jegy"].paritas)
                    # print("hazura:", hazura_nev)
                    # print()
                    if belso_bolygo["bolygo"].nevID == "hold" or belso_bolygo["bolygo"].nevID == "nap":  # nap/hold
                        haz["hazura"] = belso_haz["haz"]

                    if jegyvaltas(hazura_bolygo):
                        if haz["jegy"].paritas != belso_bolygo["jegy"].paritas:  # ellentétes a polaritás
                            haz["hazura"] = belso_haz["haz"]

                    else:
                        if haz["jegy"].paritas == belso_bolygo["jegy"].paritas:  # megyegyezik a polaritás
                            haz["hazura"] = belso_haz["haz"]

        if "hazura" not in haz:  # ugy fut le hogy nem talalt hazurat
            haz["hazura"] = "nincs hazur"


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

            debug = False
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


def fenyszog_szamol(belso_bolygo, belso_osszfok, kulso_bolygo, kulso_osszfok, orbisz, fenyszogtipus, fok_kilenges,
                    debug):
    # jobb oldali fényszög
    if (kulso_osszfok + orbisz > belso_osszfok + fok_kilenges > kulso_osszfok - orbisz
            and belso_bolygo["bolygo"] != kulso_bolygo["bolygo"]):

        fokelteres = abs(belso_osszfok + fok_kilenges - kulso_osszfok)

        if debug:
            print(fenyszogtipus)
            print(belso_bolygo["bolygo"], kulso_bolygo["bolygo"])

        belso_bolygo["fenyszogek"][fenyszogtipus].append({"bolygo": kulso_bolygo, "fokelteres": fokelteres})

    # bal oldali fényszög
    elif (kulso_osszfok + orbisz > belso_osszfok - fok_kilenges > kulso_osszfok - orbisz
          and belso_bolygo["bolygo"] != kulso_bolygo["bolygo"]):

        fokelteres = abs(belso_osszfok + fok_kilenges - kulso_osszfok)

        if debug:
            print(fenyszogtipus)
            print(belso_bolygo["bolygo"], kulso_bolygo["bolygo"])

        belso_bolygo["fenyszogek"][fenyszogtipus].append({"bolygo": kulso_bolygo, "fokelteres": fokelteres})


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
