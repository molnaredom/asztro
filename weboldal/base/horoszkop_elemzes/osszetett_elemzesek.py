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
            return  "Nincs anaréta"

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
    felhasznaltbolygok = ["neptun", "uránusz", "jupiter", "szaturnusz"]
    kiemelthazakbolygoi = get_kiemelthazak_bolygoi(hazak, kiemelthazak)
    print(kiemelthazakbolygoi)
    korok = [
        elso_kor_eldontes(kiemelthazakbolygoi),
        masodik_kor_eldontes(kiemelthazakbolygoi),
        harmadik_kor(hazak, felhasznaltbolygok),
        negyedik_kor(bolygok, felhasznaltbolygok),
        otodik_kor()
    ]

    for kor_eredmeny in korok:
        if kor_eredmeny != False:
            return kor_eredmeny


def get_kiemelthazak_bolygoi(hazak, kiemelthazak):
    kiemelthazakbolygoi = []
    for haz in hazak:
        if haz["haz"].nevID in kiemelthazak:
            for bolygo in haz["bolygok"]:
                kiemelthazakbolygoi.append(bolygo["bolygo"].nevID)
    return kiemelthazakbolygoi


def otodik_kor():
    return altalanos_kor_eldontes(korszam=5, bolygo="még nem tudjuk", sorstipus="még nem tudjuk kiszámolni")


def negyedik_kor(bolygok, felhasznaltbolygok):
    halakpontszam = sum([i["bolygo"].pontertek for i in bolygok
                         if i["jegy"].nevID == "halak" and i["bolygo"].nevID not in felhasznaltbolygok])
    vizontopontszam = sum([i["bolygo"].pontertek for i in bolygok
                           if i["jegy"].nevID == "vízöntő" and i["bolygo"].nevID not in felhasznaltbolygok])
    if vizontopontszam > halakpontszam:
        return altalanos_kor_eldontes(korszam=4, bolygo="uránuszi", sorstipus="kiszolgáltatott")
    elif halakpontszam > vizontopontszam:
        return altalanos_kor_eldontes(korszam=4, bolygo="neptuni", sorstipus="önfeláldozó")
    else:
        return False


def harmadik_kor(hazak, felhasznaltbolygok):
    haz11pontszam = sum([i["bolygo"].pontertek for i in hazak[10]["bolygok"]
                         if i["bolygo"].nevID not in felhasznaltbolygok])
    haz12pontszam = sum([i["bolygo"].pontertek for i in hazak[11]["bolygok"]
                         if i["bolygo"].nevID not in felhasznaltbolygok])

    if haz11pontszam > haz12pontszam:
        return altalanos_kor_eldontes(korszam=3, bolygo="uránuszi", sorstipus="kiszolgáltatott")
    elif haz11pontszam < haz12pontszam:
        return altalanos_kor_eldontes(korszam=3, bolygo="neptuni", sorstipus="önfeláldozó")
    else:
        return False


def masodik_kor_eldontes(kiemelthazakbolygoi):
    if "jupiter" in kiemelthazakbolygoi and "szaturnusz" not in kiemelthazakbolygoi:
        return altalanos_kor_eldontes(korszam=2, bolygo="uránuszi", sorstipus="kiszolgáltatott")
    elif "szaturnusz" in kiemelthazakbolygoi and "jupiter" not in kiemelthazakbolygoi:
        return altalanos_kor_eldontes(korszam=2, bolygo="neptuni", sorstipus="önfeláldozó")
    else:
        return False


def elso_kor_eldontes(kiemelthazakbolygoi):
    if "uránusz" in kiemelthazakbolygoi and "neptun" not in kiemelthazakbolygoi:
        return altalanos_kor_eldontes(korszam=1, bolygo="uránuszi", sorstipus="független vagy kiszolgáltatott")
    elif "neptun" in kiemelthazakbolygoi and "uránusz" not in kiemelthazakbolygoi:
        return altalanos_kor_eldontes(korszam=1, bolygo="neptuni", sorstipus="önfeláldozó vagy áldozat")
    else:
        return False


def altalanos_kor_eldontes(korszam,bolygo, sorstipus):
    eredmeny = dict()
    eredmeny["korszam"] = str(korszam)
    eredmeny["bolygoja"] = bolygo
    eredmeny["sorstipus"] = sorstipus
    return eredmeny
