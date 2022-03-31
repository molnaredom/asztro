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
        return "Nap"
    elif eng_bolygo == "moon":
        return "Hold"
    elif eng_bolygo == "mercury":
        return "Merkur"
    elif eng_bolygo == "venus":
        return "Mars"
    elif eng_bolygo == "mars":
        return "Jupiter"
    elif eng_bolygo == "jupiter":
        return "szűz"
    elif eng_bolygo == "saturn":
        return "Szaturnusz"
    elif eng_bolygo == "uranus":
        return "Uránusz"
    elif eng_bolygo == "neptune":
        return "Neptun"
    elif eng_bolygo == "pluto":
        return "Pluto"


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