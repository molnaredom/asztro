from django.shortcuts import redirect, render

from .ryuphi_api import ryuphi_api_adatlehivo_manager
from .flatlib_api import get_solar
from ..forms import HoroszkopFormGyors, MunkatipusModelFormset
from ..kisegito import kisegito, idoszamitas
from ..horoszkop_elemzes import horoszkopelemzo_manager
from ..models import Jegy2, HazUraHazban, Munkatipus, Horoszkop2
from datetime import datetime
import re


def createHoroszkopGyors(request):
    """
    :return:  RADIX hp
    """
    form = HoroszkopFormGyors()
    formset = MunkatipusModelFormset()
    Munkatipus.objects.all().delete()

    if request.method == 'GET':
        formset = MunkatipusModelFormset(request.GET or None)

    if request.method == "POST":

        if 'megse' in request.POST:
            return redirect(f"horoszkop_gyujtemeny")

        formset = MunkatipusModelFormset(request.POST)
        if formset.is_valid() and 'munkahozzaadas' in request.POST:
            print("+munka", formset.forms)
            for form in formset:
                print("munkanev",munkanev)
                if form.cleaned_data.get('munkanev'):
                    form.save()
                    print('save')
                return redirect(f"create-horoszkop")

        form = HoroszkopFormGyors(request.POST)
        if form.is_valid() and formset.is_valid() and 'munkahozzaadas' not in request.POST:
            print("+horoszkop")
            obj = form.save(commit=False)
            obj.munka = {"munkak": [i.__getitem__("munkanev").value() for i in formset ]}
            # print(obj.munka)
            obj.tipus = "radix"
            obj = set_bolygo_es_haz_objektumok(obj)
            obj.save()

            if 'ujabb_fevitel' in request.POST:
                return redirect(f"create-horoszkop")

            elif "mentes_es_foolal" in request.POST:
                return redirect(f"horoszkop_gyujtemeny")

            elif "horozkop_megnyitas" in request.POST:
                last_horoscope = Horoszkop2.objects.last()
                return redirect(f"horoszkop", str(last_horoscope.id))


    context = {'form': form, "formset": formset}
    return render(request, "create_templates/horoszkop_keszito_form.html", context)


def createHoroszkopSolar(radix_hp, visszateresi_ev):
    form = HoroszkopFormGyors()

    radix_idopont_str = str(radix_hp.idopont)[:-6]
    print("radix_idopont_str", radix_idopont_str)
    ri_dashsplit = radix_idopont_str.split("-")
    ri_colonsplit = radix_idopont_str.split(":")
    # print(ri_colonsplit[0],ri_colonsplit[0][-2:])
    datum = ri_dashsplit[0] + "/" +ri_dashsplit[1] + "/" +ri_dashsplit[2][:2]
    ido = ri_colonsplit[0][-2:] + ":" +ri_colonsplit[1] + ":" +ri_colonsplit[2]
    print("datum, ido", datum, ido)

    datumido_ = datetime.strptime(radix_idopont_str, "%Y-%m-%d %H:%M:%S")
    idozona = idoszamitas.idoszamitas(datumido_)

    geopos_lat, geopos_lon = kisegito.varos_poz(radix_hp.hely)

    geopos_lat = geopos_lat.split(".")[0]+"n"+str(int(float("0."+geopos_lat.split(".")[1])*600))[-2:]
    geopos_lon = geopos_lon.split(".")[0]+"e"+str(int(float("0."+geopos_lon.split(".")[1])*600))[-2:]
    print("[1]", datum, ido)
    idopont = get_solar(
        visszateresi_ev=visszateresi_ev,
        datum=datum,
        ido=ido,
        idozona=idozona,
        geopos_lat=geopos_lat,
        geopos_lon=geopos_lon
    )

    idopont = str(idopont).replace(' ', ":")
    ip_split = re.split("/|:",str(idopont))
    print("[2]", ip_split)
    form.idopont = f"{ip_split[0][1:]}-{ip_split[1]}-{ip_split[2]} {ip_split[3]}:{ip_split[4]}:{ip_split[5]}"
    print("form idp ", form.idopont)
    form.hely = radix_hp.hely # todo beallithato szolar hp hely
    form.neme = radix_hp.neme
    print("[3]", form.idopont)
    form.pontossag = radix_hp.pontossag
    form.tulajdonos_neve = radix_hp.tulajdonos_neve

    obj = form.save(commit=False)
    obj.tipus = "szolár"
    obj.munka = {"munkak": []}
    obj.idopont = datetime.strptime(form.idopont, "%Y-%m-%d %H:%M:%S")
    print("[4]", obj.idopont)
    obj = set_bolygo_es_haz_objektumok(obj)
    obj.save()

    return obj


def get_fokszamok(bolygo_es_haz_adatok):
    res = dict()
    for k, v in bolygo_es_haz_adatok["bolygok"].items():
        res[kisegito.ekezetnelkul(str(k))] = v["fokszam"]
    for k, v in bolygo_es_haz_adatok["hazak"].items():
        res[kisegito.ekezetnelkul(str(k))] = v["fokszam"]

    return res


def fokszamhozzarendeles(obj, horoszkop_alap):
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
                range(1, 13))):
        hazak.append(
            {"jegy": horoszkop_alap["hazak"][analogia[1]]["jegy"],
             "haz": analogia[1],
             "fokszam": obj.fokszamok[str(analogia[1])]})
    return bolygok, hazak


def bolygohoz_haz_rendeles(bolygok, hazak):
    ujhaz = {"jegy": hazak[0]["jegy"], "haz": hazak[0]["haz"], "fokszam": hazak[0]["fokszam"], "osszfokszam": 360}
    hazak.append(ujhaz)

    for bolygo in bolygok:
        for hazszam, haz in enumerate(hazak):
            # todo ellenorizni mi van akkor ha a 12. hazbol atmegy az 1 es hazba
            if get_haz_tipus(haz["haz"]) == "sarok" and bolygo["osszfokszam"] + 5 < hazak[hazszam + 1]["osszfokszam"]:
                bolygo["hazszam"] = haz
                break
            elif get_haz_tipus(haz["haz"]) != "sarok" and bolygo["osszfokszam"] + 3 < hazak[hazszam + 1]["osszfokszam"]:
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


def bolygo_hazban_hozzarendelesek(b_nevek, hp_alap, obj):
    bolygok, hazak = fokszamhozzarendeles(obj, hp_alap)
    bolygok, hazak = osszfokszam_hozzarendeles(bolygok, hazak)
    bolygok, hazak = bolygohoz_haz_rendeles(bolygok, hazak)
    obj.nap_h_id = get_id_hp_alapadat(haz=str(bolygok[0]["hazszam"]["haz"]), bolygo=b_nevek[0])
    obj.hold_h_id = get_id_hp_alapadat(haz=str(bolygok[1]["hazszam"]["haz"]), bolygo=b_nevek[1])
    obj.merkur_h_id = get_id_hp_alapadat(haz=str(bolygok[2]["hazszam"]["haz"]), bolygo=b_nevek[2])
    obj.venusz_h_id = get_id_hp_alapadat(haz=str(bolygok[3]["hazszam"]["haz"]), bolygo=b_nevek[3])
    obj.mars_h_id = get_id_hp_alapadat(haz=str(bolygok[4]["hazszam"]["haz"]), bolygo=b_nevek[4])
    obj.jupiter_h_id = get_id_hp_alapadat(haz=str(bolygok[5]["hazszam"]["haz"]), bolygo=b_nevek[5])
    obj.szaturnusz_h_id = get_id_hp_alapadat(haz=str(bolygok[6]["hazszam"]["haz"]), bolygo=b_nevek[6])
    obj.uranusz_h_id = get_id_hp_alapadat(haz=str(bolygok[7]["hazszam"]["haz"]), bolygo=b_nevek[7])
    obj.neptun_h_id = get_id_hp_alapadat(haz=str(bolygok[8]["hazszam"]["haz"]), bolygo=b_nevek[8])
    obj.pluto_h_id = get_id_hp_alapadat(haz=str(bolygok[9]["hazszam"]["haz"]), bolygo=b_nevek[9])


def bolygo_jegyben_hozzarendelesek(b_nevek, hp_alap, obj):
    obj.nap_id = get_id_hp_alapadat(jegy=hp_alap["bolygok"][b_nevek[0]]["jegy"], bolygo=b_nevek[0])
    obj.hold_j_id = get_id_hp_alapadat(jegy=hp_alap["bolygok"][b_nevek[1]]["jegy"], bolygo=b_nevek[1])
    obj.merkur_j_id = get_id_hp_alapadat(jegy=hp_alap["bolygok"][b_nevek[2]]["jegy"], bolygo=b_nevek[2])
    obj.venusz_j_id = get_id_hp_alapadat(jegy=hp_alap["bolygok"][b_nevek[3]]["jegy"], bolygo=b_nevek[3])
    obj.mars_j_id = get_id_hp_alapadat(jegy=hp_alap["bolygok"][b_nevek[4]]["jegy"], bolygo=b_nevek[4])
    obj.jupiter_j_id = get_id_hp_alapadat(jegy=hp_alap["bolygok"][b_nevek[5]]["jegy"], bolygo=b_nevek[5])
    obj.szaturnusz_j_id = get_id_hp_alapadat(jegy=hp_alap["bolygok"][b_nevek[6]]["jegy"], bolygo=b_nevek[6])
    obj.uranusz_j_id = get_id_hp_alapadat(jegy=hp_alap["bolygok"][b_nevek[7]]["jegy"], bolygo=b_nevek[7])
    obj.neptun_j_id = get_id_hp_alapadat(jegy=hp_alap["bolygok"][b_nevek[8]]["jegy"], bolygo=b_nevek[8])
    obj.pluto_j_id = get_id_hp_alapadat(jegy=hp_alap["bolygok"][b_nevek[9]]["jegy"], bolygo=b_nevek[9])
    # # főtengelyek bolygóként
    obj.asc_j_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][1]["jegy"], bolygo="asc")
    obj.mc_j_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][10]["jegy"], bolygo="mc")


def haz_jegyben_hozzarendelesek(hp_alap, obj):
    obj.haz_1_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][1]["jegy"], haz=str(1))
    obj.haz_2_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][2]["jegy"], haz=str(2))
    obj.haz_3_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][3]["jegy"], haz=str(3))
    obj.haz_4_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][4]["jegy"], haz=str(4))
    obj.haz_5_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][5]["jegy"], haz=str(5))
    obj.haz_6_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][6]["jegy"], haz=str(6))
    obj.haz_7_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][7]["jegy"], haz=str(7))
    obj.haz_8_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][8]["jegy"], haz=str(8))
    obj.haz_9_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][9]["jegy"], haz=str(9))
    obj.haz_10_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][10]["jegy"], haz=str(10))
    obj.haz_11_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][11]["jegy"], haz=str(11))
    obj.haz_12_id = get_id_hp_alapadat(jegy=hp_alap["hazak"][12]["jegy"], haz=str(12))


def get_id_hp_alapadat(jegy=None, bolygo=None, haz=None):
    if haz is None:  # bolygo jegyben
        return str(kisegito.jegy_to_num(jegy) + (kisegito.bolygo_to_num(bolygo) - 1) * 12)
    elif bolygo is None:  # haz jegyben
        return str(kisegito.jegy_to_num(jegy) + (int(haz) - 1) * 12)
    elif jegy is None:  # bolygo hazban
        return str((kisegito.bolygo_to_num(bolygo) - 1) * 12 + int(haz))
    else:
        raise Exception


def set_bolygo_es_haz_objektumok(obj):

    api_mode = "ryuphi"
    hp_alap = None

    if api_mode == "flatlib":
        # hp_alap = flatlib_api_adatlehivo_manager(obj)
        pass
    elif api_mode == "ryuphi":
        hp_alap = ryuphi_api_adatlehivo_manager(obj)

    b_nevek = [kisegito.ekezetnelkul(i) for i in kisegito.get_bolygo_nevek()]

    obj.fokszamok = get_fokszamok(hp_alap)

    haz_jegyben_hozzarendelesek(hp_alap, obj)
    bolygo_jegyben_hozzarendelesek(b_nevek, hp_alap, obj)
    bolygo_hazban_hozzarendelesek(b_nevek, hp_alap, obj)

    hazakUraHazakban = HazUraHazban.objects.all()
    for i in hazakUraHazakban:
        i.tulajdonsagok =  i.tulajdonsagok["analogiak"][2:-2].split("', '")

    obj.elemzes_adat = horoszkopelemzo_manager.elemzes(obj,
                                                       hazakUraHazakban=hazakUraHazakban,
                                                       osszesjegy = Jegy2.objects.all()
                                                       )

    return obj
