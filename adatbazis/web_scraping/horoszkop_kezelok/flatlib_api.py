from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

def api_adatlehivo_manager(tulajdonso_adatok):
    print(tulajdonso_adatok)
    chart = init_flatlib(tulajdonso_adatok)
    return {"bolygok": get_bolygok( chart), "hazak": get_hazak(chart)}


def init_flatlib(tulajdonos_adatok):

    date = Datetime('2001/8/19', '16:54:16', '+02:00')
    # date = Datetime('1969/06/05', '10:03:00')

    pos = GeoPos('47n11', '20w12')
    chart = Chart(date, pos, hsys='Placidus')

    return chart

def get_bolygok(chart):
    bolygok = dict()

    # sun = chart.get(const.SUN)
    magyar_bolygok = ["Nap", "Hold", "Merkur", "Vénusz", "Mars", "Jupiter", "Szaturnusz", "Uránusz", "Neptun", "Pluto"]
    bolygo_objektumok = list(chart.objects)[:10]
    for i, bolygo_objektum in enumerate(bolygo_objektumok):
        bolygok[magyar_bolygok[i]] = {"jegy": jegy_eng_to_hun(bolygo_objektum.sign), "fokszam": bolygo_objektum.signlon,
                                    "összfokszám": bolygo_objektum.lon, "gyorsaság": bolygo_objektum.lonspeed}
    # print(bolygok)

    [print(i) for i in bolygok.items()]
    return bolygok


def get_hazak(chart):
    hazak = dict()

    # sun = chart.get(const.SUN)
    bolygo_objektumok = list(chart.objects)[:10]
    for i, bolygo_objektum in enumerate(chart.houses,1):
        hazak[i] = {"jegy": jegy_eng_to_hun(bolygo_objektum.sign), "fokszam": bolygo_objektum.signlon,
                                    "összfokszám": bolygo_objektum.lon, "meret": bolygo_objektum.size}

    [print(i) for i in hazak.items()]

    return hazak



def jegy_eng_to_hun(eng_jegy):
    if eng_jegy == "Aries": return "kos"
    elif eng_jegy == "Taurus": return "bika"
    elif eng_jegy == "Gemini": return "ikrek"
    elif eng_jegy == "Cancer": return "rák"
    elif eng_jegy == "Leo": return "oroszlán"
    elif eng_jegy == "Virgo": return "szűz"
    elif eng_jegy == "Libra": return "mérleg"
    elif eng_jegy == "Scorpio": return "skorpió"
    elif eng_jegy == "Sagittarius": return "nyilas"
    elif eng_jegy == "Capricorn": return "bak"
    elif eng_jegy == "Aquarius": return "vízöntő"
    elif eng_jegy == "Pisces": return "halak"



