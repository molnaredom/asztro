

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
    if varosnev == "mezotur": return "47.004", "20.616"

def nyari_idoszamitas(ido):
    pass
