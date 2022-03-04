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


def sorstipus(bolygok, hazak):
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
