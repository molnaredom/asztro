
def get_bolygo_nevek():
    return ["nap", "hold", "merkúr", "vénusz", "mars", "jupiter", "szaturnusz", "uránusz", "neptun", "pluto"]


def get_jegy_nevek():
    return ["kos", "bika", "ikrek", "rák", "oroszlán", "szűz", "mérleg", "skorpió", "nyilas", "bak", "vízöntő", "halak"]


def bolygo_to_num(bolygo):
    bolygo = ekezetnelkul(bolygo)
    if bolygo == "nap":
        return 1
    elif bolygo == "hold":
        return 2
    elif bolygo == "merkur":
        return 3
    elif bolygo == "venusz":
        return 4
    elif bolygo == "mars":
        return 5
    elif bolygo == "jupiter":
        return 6
    elif bolygo == "szaturnusz":
        return 7
    elif bolygo == "uranusz":
        return 8
    elif bolygo == "neptun":
        return 9
    elif bolygo == "pluto":
        return 10
    else:
        raise Exception


def jegy_to_num(jegy):
    if jegy == "kos":
        return 1
    elif jegy == "bika":
        return 2
    elif jegy == "ikrek":
        return 3
    elif jegy == "rák":
        return 4
    elif jegy == "oroszlán":
        return 5
    elif jegy == "szűz":
        return 6
    elif jegy == "mérleg":
        return 7
    elif jegy == "skorpió":
        return 8
    elif jegy == "nyilas":
        return 9
    elif jegy == "bak":
        return 10
    elif jegy == "vízöntő":
        return 11
    elif jegy == "halak":
        return 12


def ekezetnelkul(szo: str):
    szo = szo.replace("á", "a")
    szo = szo.replace("ű", "u")
    szo = szo.replace("ú", "u")
    szo = szo.replace("ó", "o")
    szo = szo.replace("ö", "o")
    szo = szo.replace("ő", "o")
    szo = szo.replace("é", "e")
    szo = szo.replace("í", "i")
    szo = szo.replace(" ", "_")
    szo.replace("á", "a")
    return szo.lower()


def varos_poz(varosnev):
    if varosnev == "szolnok": return "47.11", "20.12"
    if varosnev == "vac": return "47.77518", "19.131"
    if varosnev == "budapest": return "47.472", "19.05"
    if varosnev == "siofok": return "46.923", "18.09"
    if varosnev == "szeged": return "46.255", "20.145"
    if varosnev == "pecs": return "46.073", "18.2322"
    if varosnev == "debrecen": return "47.53", "21.639"
    if varosnev == "sopron": return "47.684", "16.583"
    if varosnev == "keszthely": return "46.769", "17.248"
    if varosnev == "kecskemet": return "46.906", "19.689"
    if varosnev == "oroshaza": return "46.568", "20.654"
    if varosnev == "eger": return "47.898", "20.374"
    if varosnev == "veszprem": return "47.092", "17.913"
    if varosnev == "gyor": return "47.684", "17.634"
    if varosnev == "hodmezovasarhely" or varosnev == "vasarhely": return "46.43", "20.318"
    if varosnev == "bekescsaba" or varosnev == "csaba": return "46.679", "21.091"
    if varosnev == "nyiregyhaza": return "47.953", "21.727"
    if varosnev == "kaposvar": return "46.363", "17.782"
    if varosnev == "paks": return "46.606", "18.855"
    if varosnev == "szombathely": return "47.235", "16.621"
    if varosnev == "zalaegerszeg": return "46.839", "16.851"
    if varosnev == "nagykanizsa": return "46.45", "16.983"
    if varosnev == "mosonmagyarovar": return "47.873", "17.268"
    if varosnev == "cegled": return "47.174", "19.801"
    if varosnev == "tatabanya": return "47.570", "18.404"
    if varosnev == "dunaujvaros": return "46.961", "18.935"
    if varosnev == "papa": return "47.326", "17.469"
    if varosnev == "esztergom": return "47.785", "18.74"
    if varosnev == "szekesfehervar" or varosnev == "fehervar": return "47.188", "18.413"
    if varosnev == "mezotur": return "47.0041296", "20.6161"


def jegy_num_to_hun(eng_jegy):
    if eng_jegy == "1":
        return "kos"
    elif eng_jegy == "2":
        return "bika"
    elif eng_jegy == "3":
        return "ikrek"
    elif eng_jegy == "4":
        return "rák"
    elif eng_jegy == "5":
        return "oroszlán"
    elif eng_jegy == "6":
        return "szűz"
    elif eng_jegy == "7":
        return "mérleg"
    elif eng_jegy == "8":
        return "skorpió"
    elif eng_jegy == "9":
        return "nyilas"
    elif eng_jegy == "10":
        return "bak"
    elif eng_jegy == "11":
        return "vízöntő"
    elif eng_jegy == "12":
        return "halak"


def bolygo_to_hun(eng_bolygo):
    if eng_bolygo == "sun":
        return "nap"
    elif eng_bolygo == "moon":
        return "hold"
    elif eng_bolygo == "mercury":
        return "merkur"
    elif eng_bolygo == "venus":
        return "venusz"
    elif eng_bolygo == "saturn":
        return "szaturnusz"
    elif eng_bolygo == "uranus":
        return "uranusz"
    elif eng_bolygo == "neptune":
        return "neptun"
    else:
        return eng_bolygo  # mars , jupiter pluto ua. magyarul ékezet nélkül