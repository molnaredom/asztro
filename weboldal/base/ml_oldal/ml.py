from django.shortcuts import render
from ..models import Horoszkop2, Jegy2, HazUraHazban
from  ..horoszkop_elemzes.alap_elemzesek import pontos_kor_szamitas, alapszamolasok, eletciklus, \
    serult_e_nap, serult_e_hold, hyleg
from ..horoszkop_elemzes.kiiratas_formatumvalto import hazura_kiiratas
from ..horoszkop_elemzes.kisegito import szuletesi_datumido
from ..horoszkop_elemzes.osszetett_elemzesek import anareta, sorstipus
from ..horoszkop_elemzes.hozzarendelesek import *


def ml_fooldal(request):
    context = {"analogia": {} }

    return render(request, "ml_oldalak/ml_fooldal.html", context)


def generalt_adatok(request):

    horoszkopok = Horoszkop2.objects.all()
    hazakUraHazakban = HazUraHazban.objects.all()
    osszesjegy = Jegy2.objects.all()

    kinyert_adatok = []

    for i, horoszkop in enumerate(horoszkopok,1):
        if "analogiak" not in horoszkop.fokszamok:
            horoszkop.fokszamok = eval(dict(horoszkop.fokszamok)["analogiak"])  # eval strbol dictet csinal
        else:
            horoszkop.fokszamok = horoszkop.fokszamok["analogiak"]
        elemzes_adat = _elemzes(horoszkop, osszesjegy, hazakUraHazakban)
        elemzes_adat["sorszam"] = str(i)
        elemzes_adat.pop("nev")
        kinyert_adatok.append(elemzes_adat)

    csv_keszites(kinyert_adatok)

    context = {"analogia": kinyert_adatok}  # ez egy objektum

    return render(request, "ml_oldalak/generalt_adatok.html", context)



def _elemzes(adatok, osszesjegy, hazakUraHazakban):

    bolygok, hazak, pontos_kor = uj_alapanalogiak_hozzarendelese(adatok)
    # [print(i["haz"].nevID, [j["bolygo"] for j in i["bolygok"]]) for i in hazak]

    return eredmenyek_kiszamitasa(adatok, bolygok, hazak, hazakUraHazakban, osszesjegy, pontos_kor)


def eredmenyek_kiszamitasa(adatok, bolygok, hazak, hazakUraHazakban, osszesjegy, pontos_kor):
    eredmeny = dict()

    eredmeny["nev"] = str(adatok.tulajdonos_neve)
    eredmeny["munka"] = str(adatok.munka)
    eredmeny["neme"] = str(adatok.neme)
    eredmeny["alapszamolasok"] = alapszamolasok(adatok, osszesjegy)
    eredmeny["pontoskor"] = pontos_kor_szamitas(pontos_kor)
    eredmeny["eletciklus"] = eletciklus(pontos_kor)
    eredmeny["sorstipus"] = sorstipus(bolygok, hazak)
    eredmeny["hazakurai"] = hazura_kiiratas(hazak, hazakUraHazakban)
    eredmeny["serult_e_nap"] = serult_e_nap(bolygok, adatok)
    eredmeny["serult_e_hold"] = serult_e_hold(bolygok, adatok)
    hyleg_res = hyleg(bolygok)
    eredmeny["hyleg"] = hyleg_res
    eredmeny["anareta"] = anareta(hyleg_res, bolygok)

    return eredmeny


def uj_alapanalogiak_hozzarendelese(adatok):
    pontos_kor = szuletesi_datumido(adatok)
    bolygok, hazak = fokszamhozzarendeles(adatok)
    bolygok, hazak = osszfokszam_hozzarendeles(bolygok, hazak)
    bolygok = bolygohoz_haz_rendeles(hazak, bolygok)  # megmondja egy bolygo milyen hazban van
    bolygok = hazhoz_bolygok_rendelese(hazak, bolygok)  # megmondja egy_egy hazban milyen bolygok vannak
    bolygok = fenyszog_hozzarendeles(bolygok)
    hazura_melyik_hazaban(hazak, bolygok)
    return bolygok, hazak, pontos_kor



def csv_keszites(kinyert_adatok):
    with open("kinyert_adatok.csv", "w") as f:
        # f.write("sorszam;nev;sorstipus;kor;nem;eletciklus;munkai\n")
        f.write("sorszam;sorstipus;kor;nem;eletciklus;munkai\n")

        for adat in kinyert_adatok:
            f.write(f"{adat['sorszam']};")
            # f.write(f"{adat['nev']};")
            f.write(f"{adat['sorstipus']};")
            f.write(f"{adat['pontoskor']};")
            f.write(f"{adat['neme']};")
            f.write(f"{adat['eletciklus']};")
            f.write(f"{adat['munka']};")
            f.write("\n")
