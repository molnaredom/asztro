from .kisegito import hanyadik_jegy_asctol


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
    print("------", bolygojegyben_adatok)
    print("------", adatok.fokszamok)
    for analogia in list(
            zip(['nap', 'hold', 'merkur', 'venusz', 'mars', 'jupiter', 'szaturnusz', 'uranusz', 'neptun', 'pluto'],
                bolygojegyben_adatok)):
        print(analogia[1].jegy)
        print(analogia[1].bolygo)
        # print("fokszamok", adatok.fokszamok)
        # print("fokszamok", analogia[0])
        # print(adatok.fokszamok[analogia[0]])

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


def hazura_melyik_hazaban(hazak, bolygok):

    def hazurnak_bolygot_talal(hazura_nev):
        for bolygo in bolygok:
            print( bolygo["bolygo"].nevID ,hazura_nev)
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
