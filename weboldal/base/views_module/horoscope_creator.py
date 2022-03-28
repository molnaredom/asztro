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

            obj.save()

        if 'ujabb_fevitel' in request.POST:
            return redirect(f"create-horoszkop")

        elif "mentes_es_foolal" in request.POST:
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


def set_bolygo_es_haz_objektumok(obj):
    horoszkop_alap = ryuphi_api_adatlehivo_manager(obj)

    bolygok = ["nap", "hold", "merkur", "venusz", "mars", "jupiter", "szaturnusz", "uranusz", "neptun", "pluto"]

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

    obj.nap_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygok[0]]["jegy"], bolygo=bolygok[0])
    obj.hold_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygok[1]]["jegy"], bolygo=bolygok[1])
    obj.merkur_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygok[2]]["jegy"], bolygo=bolygok[2])
    obj.venusz_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygok[3]]["jegy"], bolygo=bolygok[3])
    obj.mars_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygok[4]]["jegy"], bolygo=bolygok[4])
    obj.jupiter_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygok[5]]["jegy"], bolygo=bolygok[5])
    obj.szaturnusz_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygok[6]]["jegy"],
                                                    bolygo=bolygok[6])
    obj.uranusz_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygok[7]]["jegy"], bolygo=bolygok[7])
    obj.neptun_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygok[8]]["jegy"], bolygo=bolygok[8])
    obj.pluto_id = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["bolygok"][bolygok[9]]["jegy"], bolygo=bolygok[9])

    # for i,objektum in enumerate([obj.haz_1_id,obj.haz_2_id,obj.haz_3_id,obj.haz_4_id, obj.haz_5_id,obj.haz_6_id,
    #                            obj.haz_7_id,obj.haz_8_id,obj.haz_9_id,obj.haz_10_id,obj.haz_11_id,obj.haz_12_id],1):
    #     print(objektum)
    #     print(obj.haz_1_id)
    #     objektum = get_id_to_horoszkopalapadat(jegy=horoszkop_alap["hazak"][i]["jegy"], haz=str(i))
    #     print(objektum)
    #     print(obj.haz_1_id)
    # for objektum0_bolygonev1 in zip([obj.nap_id, obj.hold_id, obj.merkur_id, obj.venusz_id, obj.mars_id,obj.jupiter_id,
    #                         obj.szaturnusz_id, obj.uranusz_id, obj.neptun_id, obj.pluto_id],
    #                        ["nap", "hold", "merkur", "venusz", "mars", "jupiter", "szaturnusz", "uranusz", "neptun", "pluto"]
    #                        ):
    #     objektum0_bolygonev1= list(objektum0_bolygonev1)
    #     objektum0_bolygonev1[0] = get_id_to_horoszkopalapadat(
    #         jegy=horoszkop_alap["bolygok"][objektum0_bolygonev1[1]]["jegy"],
    #         bolygo=objektum0_bolygonev1[1])
    # obj.hazzal is baj van
    obj.fokszamok = {"analogiak": get_fokszamok(horoszkop_alap)}

    return obj


def get_id_to_horoszkopalapadat(jegy=None, bolygo=None, haz=None):
    # bolygojegyben
    print("haz= ", haz, " jegy= ", jegy, " bolygo= ", bolygo)

    if haz is None:
        return str(jegy_to_num(jegy) + (bolygo_to_num(bolygo) - 1) * 12)
    elif bolygo is None:
        return str(jegy_to_num(jegy) + (int(haz) - 1) * 12)
    else:
        raise Exception


def bolygo_to_num(bolygo):
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
        print ("Port is open")
        adat = requests.get(
            f'http://127.0.0.1:3000/'
            f'horoscope?time={ev}-{honap}-{nap}T{ora}:{perc}:{mp}%2B02:00&latitude={szelesseg}&longitude={hosszusag}')
    else:
        print("Port is not open")
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
        hazak[i] = {"jegy": jegy_num_to_hun(str(value["sign"])), "fokszam": get_fokszam(value["position"])}

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
