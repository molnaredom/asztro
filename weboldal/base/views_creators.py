import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *


@login_required(login_url="login")
def createroom(request):
    form = RoomForm()

    if request.method == "POST":

        if 'bolygo_es_jegy_lekerdezes' in request.POST:
            jegyNev = request.POST.get('jegyNev')
            bolygoNev = request.POST.get('bolygoNev')
            jegy_alapjan_lekeres = bolygo_alapjan_lekeres(bolygoNev, jegyNev)

        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            return redirect("home")

    context = {'form': form}
    return render(request, "create_templates/room_form.html", context)


def _analogiafeltoltes(request, Osztalyform, analogia):
    form = Osztalyform()
    if request.method == "POST":

        if "megse" in request.POST:
            return redirect(f"{analogia}")

        form = Osztalyform(request.POST)
        if form.is_valid():
            form.save()

        if 'ujabb_fevitel' in request.POST:
            return redirect(f"create-{analogia}")

        elif "mentes_es_foolal" in request.POST:
            return redirect(f"{analogia}")

    context = {'form': form}
    return render(request, "create_templates/analogia_form.html", context)

#createrek
def createJegyek(request):
    return _analogiafeltoltes(request, JegyekForm, "jegyek")


def createBolygok(request):
    return _analogiafeltoltes(request, BolygokForm, "bolygok")

 #job lib

def createHazak(request):
    return _analogiafeltoltes(request, HazakForm, "hazak")


def createBolygoJegyben(request):
    return _analogiafeltoltes(request, BolygoJegybenForm, "bolygoJegyben")


def createBolygoHazban(request):
    return _analogiafeltoltes(request, BolygoHazbanForm, "bolygoHazbann")


 #job lib

def createHazJegyben(request):
    return _analogiafeltoltes(request, HazJegybenForm, "hazJegyben")


def createHazUraHazban(request):
    return _analogiafeltoltes(request, HazUraHazbanForm, "hazakUraHazakban")


def createHoroszkop(request):
    form = HoroszkopForm()
    if request.method == "POST":

        if "megse" in request.POST:
            return redirect(f"horoszkop_gyujtemeny")

        form = HoroszkopForm(request.POST)
        if form.is_valid():
            form.save()

        if 'ujabb_fevitel' in request.POST:
            return redirect(f"create-horoszkop")

        elif "mentes_es_foolal" in request.POST:
            return redirect(f"horoszkop_gyujtemeny")


    context = {'form': form}
    return render(request, "create_templates/analogia_form.html", context)


# def createHoroszkopAdatok(request):
#     form = HoroszkopAdatokForm()
#     if request.method == "POST":
#         form = HoroszkopAdatokForm(request.POST)
#         if form.is_valid():
#             form.save()
#             createHoroszkopGyors(request, alapadatok=form.data)
#
#             return redirect("horoszkop_gyujtemeny")
#
#     context = {'form': form}
#     return render(request, "create_templates/analogia_form.html", context)


def createHoroszkopGyors(request):
    form = HoroszkopFormGyors()
    if request.method == "POST":
        form = HoroszkopFormGyors(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj)
            print(obj.idopont, type(obj.idopont))

            horoszkop_alap = ryuphi_api_adatlehivo_manager(obj)

            print("***********",horoszkop_alap)


            obj.haz_1_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][1]["jegy"],haz="1")
            obj.haz_2_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][2]["jegy"],haz="2")
            obj.haz_3_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][3]["jegy"],haz="3")
            obj.haz_4_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][4]["jegy"],haz="4")
            obj.haz_5_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][5]["jegy"],haz="5")
            obj.haz_6_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][6]["jegy"],haz="6")
            obj.haz_7_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][7]["jegy"],haz="7")
            obj.haz_8_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][8]["jegy"],haz="8")
            obj.haz_9_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][9]["jegy"],haz="9")
            obj.haz_10_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][10]["jegy"],haz="10")
            obj.haz_11_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][11]["jegy"],haz="11")
            obj.haz_12_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["hazak"][12]["jegy"],haz="12")

            obj.nap_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["bolygok"]["Nap"]["jegy"],bolygo= "nap")
            obj.hold_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["bolygok"]["Hold"]["jegy"], bolygo="hold")
            obj.merkur_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["bolygok"]["Merkur"]["jegy"], bolygo="merkur")
            obj.venusz_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["bolygok"]["Vénusz"]["jegy"], bolygo="venusz")
            obj.mars_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["bolygok"]["Mars"]["jegy"], bolygo="mars")
            obj.jupiter_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["bolygok"]["Jupiter"]["jegy"], bolygo="jupiter")
            obj.szaturnusz_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["bolygok"]["Szaturnusz"]["jegy"], bolygo="szaturnusz")
            obj.uranusz_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["bolygok"]["Uránusz"]["jegy"], bolygo="uranusz")
            obj.neptun_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["bolygok"]["Neptun"]["jegy"], bolygo="neptun")
            obj.pluto_id = get_id_to_horoszkopalapadat(jegy= horoszkop_alap["bolygok"]["Pluto"]["jegy"], bolygo="pluto")

            obj.fokszamok = {"analogiak" : get_fokszamok(horoszkop_alap)}
            print("\n*******",obj.fokszamok)

            obj.save()
            return redirect("horoszkop_gyujtemeny")

    context = {'form': form}
    return render(request, "create_templates/analogia_form.html", context)


def get_fokszamok(bolygo_es_haz_adatok):
    res = dict()
    for k, v in bolygo_es_haz_adatok["bolygok"].items():
        res[ekezetnelkul(str(k))] = v["fokszam"]
    for k, v in bolygo_es_haz_adatok["hazak"].items():
        res[ekezetnelkul(str(k))] = v["fokszam"]

    return res


def get_id_to_horoszkopalapadat(jegy=None, bolygo=None, haz=None):
    # bolygojegyben
    print("haz= ",haz," jegy= ", jegy, " bolygo= ",bolygo)

    if haz == None:
        return jegy_to_num(jegy) + (bolygo_to_num(bolygo)-1)*12
    elif bolygo == None:
        return jegy_to_num(jegy) + (int(haz)-1)*12
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




"""
{"analogiak": "{'nap': '26.7', 'hold': '3.8166666666666664', 'merkur': '9.9',
 'venusz': '21.083333333333332', 'mars': '21.116666666666667',
  'jupiter': '7.766666666666667', 'szaturnusz': '13.683333333333334',
   'uranusz': '22.7', 'neptun': '6.866666666666666',
    'pluto': '12.5', '1': '3.55', '2': '17.6', '3': '2.183333333333333', 
    '4': '3.95', '5': '26.566666666666666', '6': '15.166666666666666', '7': '3.55', '8': '17.6', 
    '9': '2.183333333333333', '10': '3.95', '11': '26.566666666666666', '12': '15.166666666666666'}"}"""

import datetime
import requests

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



## todo timezone


def ryuphi_api_adatlehivo_manager(tulajdonso_adatok):
    # print("tulajdonos adatok",tulajdonso_adatok)
    kinyert_adatok = init_api(tulajdonso_adatok)
    # print("kinyert adatok",kinyert_adatok)
    return {"bolygok": get_bolygok(kinyert_adatok), "hazak": get_hazak(kinyert_adatok)}


def char2(char):
    if len(char) == 1:
        return "0" + char
    return char


def init_api(obj):
    ev = char2(str(obj.idopont.year))
    honap = char2(str(obj.idopont.month))
    nap = char2(str(obj.idopont.day))
    ora = char2(str(obj.idopont.hour))
    perc = char2(str(obj.idopont.minute))
    mp = char2(str(obj.idopont.second))
    varos = str(obj.hely)

    szelesseg, hosszusag = varos_poz(varosnev=ekezetnelkul(varos.lower()))

    start = datetime.datetime.now()
    adat = requests.get(
        # f'https://dev-astrology-api.herokuapp.com/'
        f'http://127.0.0.1:3000/'
        f'horoscope?time={ev}-{honap}-{nap}T{ora}:{perc}:{mp}%2B02:00&latitude={szelesseg}&longitude={hosszusag}')

    end = datetime.datetime.now()
    print("runtime api", end - start)

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
        return "Nap"
    elif eng_bolygo == "moon":
        return "Hold"
    elif eng_bolygo == "mercury":
        return "Merkur"
    elif eng_bolygo == "venus":
        return "Vénusz"
    elif eng_bolygo == "mars":
        return "Mars"
    elif eng_bolygo == "jupiter":
        return "Jupiter"
    elif eng_bolygo == "saturn":
        return "Szaturnusz"
    elif eng_bolygo == "uranus":
        return "Uránusz"
    elif eng_bolygo == "neptune":
        return "Neptun"
    elif eng_bolygo == "pluto":
        return "Pluto"

#
# print(get_basic_datas("2001", "08", "19", "16", "54", "00", "Szolnok"))
