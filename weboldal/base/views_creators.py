import datetime
import os
import sys

import django.utils.datetime_safe
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


# createrek
def createJegyek(request):
    return _analogiafeltoltes(request, JegyekForm, "jegyek")


def createBolygok(request):
    return _analogiafeltoltes(request, BolygokForm, "bolygok")


# job lib

def createHazak(request):
    return _analogiafeltoltes(request, HazakForm, "hazak")


def createBolygoJegyben(request):
    return _analogiafeltoltes(request, BolygoJegybenForm, "bolygoJegyben")


def createBolygoHazban(request):
    return _analogiafeltoltes(request, BolygoHazbanForm, "bolygoHazbann")


# job lib

def createHazJegyben(request):
    return _analogiafeltoltes(request, HazJegybenForm, "hazJegyben")


def createHazUraHazban(request):
    return _analogiafeltoltes(request, HazUraHazbanForm, "hazakUraHazakban")


def createHoroszkop(request):
    form = HoroszkopForm()
    if request.method == "POST":
        form = HoroszkopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("horoszkop_gyujtemeny")

    context = {'form': form}
    return render(request, "create_templates/analogia_form.html", context)


def createHoroszkopGyors(request):
    form = HoroszkopFormGyors()
    if request.method == "POST":
        form = HoroszkopFormGyors(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj)
            print(obj.idopont, type(obj.idopont))

            horoszkop_alap = ryuphi_api_adatlehivo_manager(obj)

            obj.haz_1_id = "1"
            obj.haz_2_id = "1"
            obj.haz_3_id = "1"
            obj.haz_4_id = "1"
            obj.haz_5_id = "1"
            obj.haz_6_id = "1"
            obj.haz_7_id = "1"
            obj.haz_8_id = "1"
            obj.haz_9_id = "1"
            obj.haz_10_id = "1"
            obj.haz_11_id = "1"
            obj.haz_12_id = "1"

            obj.nap_id = "1"
            obj.hold_id = "1"
            obj.merkur_id = "1"
            obj.venusz_id = "1"
            obj.mars_id = "1"
            obj.jupiter_id = "1"
            obj.szaturnusz_id = "1"
            obj.uranusz_id = "1"
            obj.neptun_id = "1"
            obj.pluto_id = "1"

            obj.fokszamok = {"analogiak" : get_fokszamok(horoszkop_alap)}
            print(obj.fokszamok)

            obj.save()
            return redirect("horoszkop_gyujtemeny")

    context = {'form': form}
    return render(request, "create_templates/analogia_form.html", context)

    # room = "kakao"  #get_object_or_404(Room, pk=room_id)
    # form = HoroszkopFormGyors(room=room, author=request.user, data=request.POST)
    # if form.is_valid():
    #     form.save()
    # return HttpResponseRedirect(reverse('chat.views.add_message', args=(p.id,)))

    # print(alapadatok["idopont"])
    # datetimeobj = datetime.datetime.strptime(alapadatok["idopont"], "%Y-%m-%d %H:%M:%S")
    # print(datetimeobj)
    # print(alapadatok["hely"])
    #
    # date = Datetime(f'{datetimeobj.year}/{datetimeobj.month}/{datetimeobj.day}', '16:42', '+02:00')
    # pos = GeoPos('38n32', '8w54')
    # chart = Chart(date, pos)
    # print(chart.isHouse10MC())
    #
    # sun = chart.get(const.SUN)
    # print(sun)
    #
    # moon = chart.get(const.MOON)
    # print(moon)
    #
    # merkury = chart.get(const.MERCURY)
    # print(merkury)
    #
    # form = HoroszkopFormGyors()
    # if form.is_valid():
    #     form.save()


#
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

def get_fokszamok(bolygo_es_haz_adatok):
    res = dict()
    for k, v in bolygo_es_haz_adatok["bolygok"].items():
        res[ekezetnelkul(str(k))] = v["fokszam"]
    for k, v in bolygo_es_haz_adatok["hazak"].items():
        res[ekezetnelkul(str(k))] = v["fokszam"]

    return res


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

from adatbazis.web_scraping.kisegito_modulok.nyelvi_kisegito import ekezetnelkul, varos_poz


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
