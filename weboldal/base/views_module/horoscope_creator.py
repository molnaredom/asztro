import datetime

import requests
from django.shortcuts import redirect, render

from ..forms import HoroszkopFormGyors


def createHoroszkopGyors(request):
    form = HoroszkopFormGyors()

    if "megse" in request.POST:
        return redirect(f"horoszkop_gyujtemeny")

    if request.method == "POST":
        form = HoroszkopFormGyors(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

            obj = set_bolygo_es_haz_objektumok(obj)
            print(f'{obj.haz_1_id=}')

            if 'ujabb_fevitel' in request.POST:
                obj.save()
                return redirect(f"create-horoszkop")

            elif "mentes_es_foolal" in request.POST:
                obj.save()
                return redirect(f"horoszkop_gyujtemeny")

    context = {'form': form}
    return render(request, "create_templates/analogia_form.html", context)


def get_fokszamok(bolygo_es_haz_adatok):
    res = dict()
    for k, v in bolygo_es_haz_adatok["bolygok"].items():
        res[ekezetnelkul(str(k))] = v["fokszam"]
    for k, v in bolygo_es_haz_adatok["hazak"].items():
        res[ekezetnelkul(str(k))] = v["fokszam"]

    return res


def fokszamhozzarendeles(obj,horoszkop_alap):

    # bolygok, hazak = {}, {} # egy regi otlet
    bolygok, hazak = [], []

    for analogia in list(
            zip(['nap', 'hold', 'merkur', 'venusz', 'mars', 'jupiter', 'szaturnusz', 'uranusz', 'neptun', 'pluto'],
                range(12))):
        bolygok.append(
            {"jegy": horoszkop_alap["bolygok"][analogia[0]]["jegy"],
             "bolygo": analogia[0],
             "fokszam": obj.fokszamok[analogia[0]]})


    for analogia in list(
            zip(['haz1', 'haz2', 'haz3', 'haz4', 'haz5', 'haz6', 'haz7', 'haz8', 'haz9', 'haz10', 'haz11', 'haz12'],
                range(1,13))):
        hazak.append(
            {"jegy": horoszkop_alap["hazak"][analogia[1]]["jegy"],
             "haz": analogia[1],
             "fokszam": obj.fokszamok[str(analogia[1])]})
    return bolygok,hazak


def bolygohoz_haz_rendeles(bolygok, hazak):
    ujhaz = {"jegy": hazak[0]["jegy"], "haz": hazak[0]["haz"], "fokszam": hazak[0]["fokszam"], "osszfokszam": 360}
    hazak.append(ujhaz)

    for bolygo in bolygok:
        for hazszam, haz in enumerate(hazak):
            # todo ellenorizni mi van akkor ha a 12. hazbol atmegy az 1 es hazba
            if get_haz_tipus(haz["haz"]) == "sarok" and bolygo["osszfokszam"] + 5 < hazak[hazszam + 1]["osszfokszam"]:
                bolygo["hazszam"] = haz
                break
            elif get_haz_tipus( haz["haz"]) != "sarok" and bolygo["osszfokszam"] + 3 < hazak[hazszam + 1]["osszfokszam"]:
                bolygo["hazszam"] = haz
                break
        else:
            printe("valami nincs lekezelve", problema=bolygohoz_haz_rendeles.__name__)
            raise Exception

    hazak.pop(-1)  # elttűntetni a plusz 1 házat

    return bolygok, hazak


def get_haz_tipus(haz_szam):
    if haz_szam in [1, 4, 7, 10]:
        return "sarok"
    elif haz_szam in [2, 5, 8, 11]:
        return "hanyatló"
    elif haz_szam in [3, 6, 9, 12]:
        return "követő"


def hanyadik_jegy_asctol(kiindulasijegy, aktjegy):
    kiind_szam, akt_szam = jegyet_szamra_valt(kiindulasijegy), jegyet_szamra_valt(aktjegy)
    return (akt_szam - kiind_szam) % 12


def jegyet_szamra_valt(jegynev):
    jegyhezszam = {"kos": 1, "bika": 2, "ikrek": 3, "rák": 4, "oroszlán": 5, "szűz": 6, "mérleg": 7, "skorpió": 8,
                   "nyilas": 9, "bak": 10,
                   "vízöntő": 11, "halak": 12}
    return jegyhezszam[jegynev]


def osszfokszam_hozzarendeles(bolygok, hazak):
    ascfok, ascjegy = float(hazak[0]["fokszam"]), hazak[0]["jegy"]

    for haz in hazak:
        haz["osszfokszam"] = hanyadik_jegy_asctol(ascjegy, haz["jegy"]) * 30 - ascfok + float(haz["fokszam"])
        # print(haz["haz"], haz["jegy"].nevID,haz["osszfokszam"],hanyadik_jegy_asctol(ascjegy,haz["jegy"].nevID), ascfok,float(haz["fokszam"]   ))

    for bolygo in bolygok:
        bolygo["osszfokszam"] = hanyadik_jegy_asctol(ascjegy, bolygo["jegy"]) * 30 - ascfok + float(
            bolygo["fokszam"])
        # print(bolygo["bolygo"], bolygo["jegy"].nevID,bolygo["osszfokszam"],hanyadik_jegy_asctol(ascjegy,bolygo["jegy"].nevID), ascfok,float(bolygo["fokszam"]   ))

    return bolygok, hazak




def set_bolygo_es_haz_objektumok(obj):
    horoszkop_alap = ryuphi_api_adatlehivo_manager(obj)

    bolygo_nevek = ["nap", "hold", "merkur", "venusz", "mars", "jupiter", "szaturnusz", "uranusz", "neptun", "pluto"]

    obj.fokszamok = get_fokszamok(horoszkop_alap)

    #haz jegyben
    obj.haz_1_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][1]["jegy"], haz=str(1))
    obj.haz_2_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][2]["jegy"], haz=str(2))
    obj.haz_3_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][3]["jegy"], haz=str(3))
    obj.haz_4_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][4]["jegy"], haz=str(4))
    obj.haz_5_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][5]["jegy"], haz=str(5))
    obj.haz_6_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][6]["jegy"], haz=str(6))
    obj.haz_7_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][7]["jegy"], haz=str(7))
    obj.haz_8_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][8]["jegy"], haz=str(8))
    obj.haz_9_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][9]["jegy"], haz=str(9))
    obj.haz_10_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][10]["jegy"], haz=str(10))
    obj.haz_11_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][11]["jegy"], haz=str(11))
    obj.haz_12_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][12]["jegy"], haz=str(12))

    # bolygo jegyben
    obj.nap_j_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygo_nevek[0]]["jegy"], bolygo=bolygo_nevek[0])
    obj.hold_j_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygo_nevek[1]]["jegy"], bolygo=bolygo_nevek[1])
    obj.merkur_j_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygo_nevek[2]]["jegy"], bolygo=bolygo_nevek[2])
    obj.venusz_j_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygo_nevek[3]]["jegy"], bolygo=bolygo_nevek[3])
    obj.mars_j_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygo_nevek[4]]["jegy"], bolygo=bolygo_nevek[4])
    obj.jupiter_j_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygo_nevek[5]]["jegy"], bolygo=bolygo_nevek[5])
    obj.szaturnusz_j_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygo_nevek[6]]["jegy"],bolygo=bolygo_nevek[6])
    obj.uranusz_j_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygo_nevek[7]]["jegy"], bolygo=bolygo_nevek[7])
    obj.neptun_j_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygo_nevek[8]]["jegy"], bolygo=bolygo_nevek[8])
    obj.pluto_j_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygo_nevek[9]]["jegy"], bolygo=bolygo_nevek[9])

    # bolygo hazban
    bolygok, hazak = fokszamhozzarendeles(obj,horoszkop_alap)
    bolygok, hazak = osszfokszam_hozzarendeles(bolygok, hazak)

    bolygok, hazak = bolygohoz_haz_rendeles(bolygok, hazak)
    print(f"{str(hazak[0]['haz'])}")
    obj.nap_h_id = get_id_to_horoszkopalapadat(haz=str(hazak[0]["haz"]), bolygo=bolygo_nevek[0])
    obj.hold_h_id = get_id_to_horoszkopalapadat(haz=str(hazak[1]["haz"]), bolygo=bolygo_nevek[1])
    obj.merkur_h_id = get_id_to_horoszkopalapadat(haz=str(hazak[2]["haz"]), bolygo=bolygo_nevek[2])
    obj.venusz_h_id = get_id_to_horoszkopalapadat(haz=str(hazak[3]["haz"]), bolygo=bolygo_nevek[3])
    obj.mars_h_id = get_id_to_horoszkopalapadat(haz=str(hazak[4]["haz"]), bolygo=bolygo_nevek[4])
    obj.jupiter_h_id = get_id_to_horoszkopalapadat(haz=str(hazak[5]["haz"]), bolygo=bolygo_nevek[5])
    obj.szaturnusz_h_id = get_id_to_horoszkopalapadat(haz=str(hazak[6]["haz"]), bolygo=bolygo_nevek[6])
    obj.uranusz_h_id = get_id_to_horoszkopalapadat(haz=str(hazak[7]["haz"]), bolygo=bolygo_nevek[7])
    obj.neptun_h_id = get_id_to_horoszkopalapadat(haz=str(hazak[8]["haz"]), bolygo=bolygo_nevek[8])
    obj.pluto_h_id = get_id_to_horoszkopalapadat(haz=str(hazak[9]["haz"]), bolygo=bolygo_nevek[9])

    return obj


def get_id_to_horoszkopalapadat(jegy=None, bolygo=None, haz=None):
    # bolygojegyben
    print("haz= ", haz, " jegy= ", jegy, " bolygo= ", bolygo)

    if haz is None: # bolygo jegyben
        return str(jegy_to_num(jegy) + (bolygo_to_num(bolygo) - 1) * 12)
    elif bolygo is None: # haz jegyben
        return str(jegy_to_num(jegy) + (int(haz) - 1) * 12)
    elif jegy is None: # bolygo hazban
        return str((bolygo_to_num(bolygo) - 1) * 12 + ((int(haz) - 1) * 12))
    else:
        raise Exception


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


def ryuphi_api_adatlehivo_manager(tulajdonso_adatok):
    # print("tulajdonos adatok",tulajdonso_adatok)
    kinyert_adatok = init_api(tulajdonso_adatok)
    # print("kinyert adatok",kinyert_adatok)
    return {"bolygok": get_bolygok(kinyert_adatok), "hazak": get_hazak(kinyert_adatok)}


def char2(char):
    if len(str(char)) == 1:
        return "0" + str(char)
    return char


def init_api(obj):
    datumido = obj.idopont

    szelesseg, hosszusag = varos_poz(varosnev=ekezetnelkul(str(obj.hely).lower()))

    start = datetime.datetime.now()

    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 3000))
    if result == 0:
        print("Port is open : 3000")
        adat = requests.get(
            f'http://127.0.0.1:3000/'
            f'horoscope?time='
            f'{char2(datumido.year)}-{char2(datumido.month)}-{char2(datumido.day)}T'
            f'{char2(datumido.hour)}:{char2(datumido.minute)}:{char2(datumido.second)}'
            f'%2B02:00&latitude={szelesseg}&longitude={hosszusag}')
    else:
        print("Port is not open --> web api")
        adat = requests.get(
            f'https://dev-astrology-api.herokuapp.com/'
            f'horoscope?time='
            f'{char2(datumido.year)}-{char2(datumido.month)}-{char2(datumido.day)}T'
            f'{char2(datumido.hour)}:{char2(datumido.minute)}:{char2(datumido.second)}'
            f'%2B02:00&latitude={szelesseg}&longitude={hosszusag}')

    sock.close()

    end = datetime.datetime.now()
    print("API Futásidő: ", end - start)

    return adat.json()


def get_bolygok(chart):
    bolygok = dict()

    bolygo_objektumok = chart["data"]["astros"]
    for key, value in bolygo_objektumok.items():
        # print(key, value, )
        if key == "chiron":
            break
        bolygok[bolygo_to_hun(key)] = {"jegy": jegy_num_to_hun(str(value["sign"])),
                                       "fokszam": get_fokszam(value["position"]),
                                       "retográd": value["retrograde"],
                                       "gyorsaság": value["speed"]
                                       }
    # print(bolygok)

    # [print(i) for i in bolygok.items()]
    return bolygok


def get_fokszam(position):
    return str(float(position["longitude"]) % 30)


def get_hazak(chart):
    hazak = dict()

    hazakiter = chart["data"]["houses"]
    for i, value in enumerate(hazakiter, 1):
        hazak[i] = {"jegy": jegy_num_to_hun(str(value["sign"])),
                    "fokszam": get_fokszam(value["position"])}

    # [print(i) for i in hazak.items()]

    return hazak


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
