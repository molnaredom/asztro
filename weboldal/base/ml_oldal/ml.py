from django.shortcuts import render
from ..models import Horoszkop2, Jegy2, HazUraHazban
from ..horoszkop_elemzes.alap_elemzesek import *
from ..horoszkop_elemzes.kiiratas_formatumvalto import hazura_kiiratas
from ..horoszkop_elemzes.kisegito import szuletesi_datumido
from ..horoszkop_elemzes.osszetett_elemzesek import anareta, sorstipus
from ..horoszkop_elemzes.hozzarendelesek import *


def ml_fooldal(request):
    context = {"analogia": {}}

    return render(request, "ml_oldalak/ml_fooldal.html", context)


def generalt_adatok(request):
    horoszkopok = Horoszkop2.objects.all()
    hazakUraHazakban = HazUraHazban.objects.all()
    osszesjegy = Jegy2.objects.all()

    kinyert_adatok = []

    for i, horoszkop in enumerate(horoszkopok, 1):
        if "analogiak" not in horoszkop.fokszamok:
            horoszkop.fokszamok = eval(dict(horoszkop.fokszamok)["analogiak"])  # eval strbol dictet csinal
        else:
            horoszkop.fokszamok = horoszkop.fokszamok["analogiak"]

        elemzes_adat = _elemzes(horoszkop, osszesjegy, hazakUraHazakban, sorszam=i)

        kinyert_adatok.append(elemzes_adat)

    csv_keszites(kinyert_adatok)

    context = {"analogia": kinyert_adatok}  # ez egy objektum

    return render(request, "ml_oldalak/generalt_adatok.html", context)


def _elemzes(adatok, osszesjegy, hazakUraHazakban, sorszam):
    bolygok, hazak, pontos_kor = uj_alapanalogiak_hozzarendelese(adatok)
    # [print(i["haz"].nevID, [j["bolygo"] for j in i["bolygok"]]) for i in hazak]

    return eredmenyek_kiszamitasa(adatok, bolygok, hazak, hazakUraHazakban, osszesjegy, pontos_kor, sorszam)


def eredmenyek_kiszamitasa(adatok, bolygok, hazak, hazakUraHazakban, osszesjegy, pontos_kor, sorszam):
    eredmeny = dict()

    # eredmeny["nev"] = str(adatok.tulajdonos_neve)
    eredmeny["Sorszám"] = str(sorszam)
    eredmeny["Munka"] = str(adatok.munka)
    eredmeny["Neme"] = str(adatok.neme)
    # eredmeny["alapszamolasok"] = alapszamolasok(adatok, osszesjegy)
    eredmeny["Életkor"] = pontos_kor[0]
    eredmeny["Életciklus"] = eletciklus(pontos_kor, adatok.neme)
    eredmeny["Sorstípus"] = sorstipus(bolygok, hazak)
    #eredmeny["Házak urai"] = hazura_kiiratas(hazak, hazakUraHazakban)
    eredmeny["Sérult-e Nap"] = serult_e_nap(bolygok, adatok)
    eredmeny["Sérült-e a Hold"] = serult_e_hold(bolygok, adatok)
    hyleg_res = hyleg(bolygok)
    eredmeny["Hyleg"] = hyleg_res
    eredmeny["Anaréta"] = anareta(hyleg_res, bolygok)

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
        jellemzovektorok = [k for k in kinyert_adatok[0].keys()]
        f.write(";".join(jellemzovektorok) + "\n")

        for adat in kinyert_adatok:
            sor = []
            for oszlop in jellemzovektorok:
                sor.append(str(adat[oszlop]))
            f.write(";".join(sor) + "\n")
