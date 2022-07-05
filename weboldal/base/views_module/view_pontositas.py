import datetime
import requests
from django.shortcuts import redirect, render
from ..forms import HoroszkopFormGyorsPontositas
from ..kisegito import kisegito, idoszamitas
from ..horoszkop_elemzes import horoszkopelemzo_manager
import socket
from ..models import Jegy2, HazUraHazban, Munkatipus, Horoszkop2

def pontositas_kerdoiv(request):
    form = HoroszkopFormGyorsPontositas()

    if request.method == "POST":

        if 'megse' in request.POST:
            return redirect(f"horoszkop_gyujtemeny")

        form = HoroszkopFormGyorsPontositas(request.POST)
        if form.is_valid():
            print("+ horoszkop pontosítás")
            obj = form.save(commit=False)
            # print(obj.munka)
            obj = set_bolygo_es_haz_objektumok(obj)
            obj.save()

            if 'tovabb1' in request.POST:
                return redirect(f"create-horoszkop")

            last_horoscope = Horoszkop2.objects.last()


    context = {'form': form}
    return render(request, "pontositas/pontositas_kerdoiv.html", context)


def pontositas_adatfelvitel(request):
    form = HoroszkopFormGyorsPontositas()

    if request.method == "POST":

        if 'megse' in request.POST:
            return redirect(f"horoszkop_gyujtemeny")

        form = HoroszkopFormGyorsPontositas(request.POST)
        if form.is_valid():
            print("+ horoszkop pontosítás")
            # obj = form.save(commit=False)
            # # print(obj.munka)
            # obj = set_bolygo_es_haz_objektumok(obj)
            # obj.save()

            if 'tovabb1' in request.POST:
                print(request.POST.get("pontossag"))
                if request.POST.get("pontossag") == "nem meghatározott":
                    # todo
                    pass

                    return redirect(f"pontositas_kerdoiv")
                if request.POST.get("pontossag") == "pontosított":
                    # todo
                    pass

                    return redirect(f"pontositas_kerdoiv")

            last_horoscope = Horoszkop2.objects.last()


    context = {'form': form}
    return render(request, "pontositas/pontositas_adatfelvitel.html", context)


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


def ryuphi_api_adatlehivo_manager(tulajdonso_adatok):
    kinyert_adatok = init_api(tulajdonso_adatok)
    return {"bolygok": get_bolygok(kinyert_adatok), "hazak": get_hazak(kinyert_adatok)}


def char2(char):
    if len(str(char)) == 1:
        return "0" + str(char)
    return char


def init_api(obj):
    datumido = obj.idopont

    szelesseg, hosszusag = kisegito.varos_poz(varosnev=kisegito.ekezetnelkul(str(obj.hely).lower()))

    start = datetime.datetime.now()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 3000))

    datumido_teljes_str = f'{char2(datumido.year)}-{char2(datumido.month)}-{char2(datumido.day)}T' \
                          f'{char2(datumido.hour)}:{char2(datumido.minute)}:{char2(datumido.second)}'

    idozona = idoszamitas.idoszamitas(datumido)

    if result == 0:
        print("Port is open : 3000")
        adat = requests.get(
            f'http://127.0.0.1:3000/'
            f'horoscope?time='
            f'{datumido_teljes_str}'
            f'%2B0{idozona}:00&latitude={szelesseg}&longitude={hosszusag}')
    else:
        print("Port is not open --> web api")
        adat = requests.get(
            f'https://dev-astrology-api.herokuapp.com/'
            f'horoscope?time='
            f'{datumido_teljes_str}'
            f'%2B0{idozona}:00&latitude={szelesseg}&longitude={hosszusag}')

    sock.close()

    end = datetime.datetime.now()
    print("API Futásidő: ", end - start)

    return adat.json()


def get_bolygok(chart):
    bolygok = dict()

    bolygo_objektumok = chart["data"]["astros"]
    for key, value in bolygo_objektumok.items():
        if key == "chiron":
            break

        fokszam = float(get_fokszam(value["position"]))
        print(key,fokszam)
        tizedesresz = (fokszam-int(fokszam))/10*6
        korrigalt_fokszam = int(fokszam) + tizedesresz
        print(key,korrigalt_fokszam)
        bolygok[kisegito.bolygo_to_hun(key)] = {
            "jegy": kisegito.jegy_num_to_hun(str(value["sign"])),
            "fokszam": korrigalt_fokszam,
            "retográd": value["retrograde"],
            "gyorsaság": value["speed"]
        }
    # [print(i) for i in bolygok.items()]
    return bolygok


def get_fokszam(position):
    return str(float(position["longitude"]) % 30)


def get_hazak(chart):
    hazak = dict()

    hazakiter = chart["data"]["houses"]
    for i, value in enumerate(hazakiter, 1):
        hazak[i] = {"jegy": kisegito.jegy_num_to_hun(str(value["sign"])),
                    "fokszam": get_fokszam(value["position"])}
        print(hazak[i])

    # [print(i) for i in hazak.items()]
    return hazak


def set_bolygo_es_haz_objektumok(obj):
    obj.tipus = "radix"

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
