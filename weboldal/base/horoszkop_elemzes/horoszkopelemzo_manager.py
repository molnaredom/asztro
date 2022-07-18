from .alap_elemzesek import *
from .kiiratas_formatumvalto import hazura_kiiratas
from .kisegito import szuletesi_datumido
from .osszetett_elemzesek import anareta, sorstipus
from .hozzarendelesek import *
from .szolar_elemzes import *


def elemzes(adatok, osszesjegy, hazakUraHazakban):
    # print(111)
    bolygok, hazak, pontos_kor = uj_alapanalogiak_hozzarendelese(adatok)
    # [print(i["haz"].nevID, [j["bolygo"] for j in i["bolygok"]]) for i in hazak]

    return eredmenyek_kiszamitasa(adatok, bolygok, hazak, hazakUraHazakban, osszesjegy, pontos_kor)


def eredmenyek_kiszamitasa(adatok, bolygok, hazak, hazakUraHazakban, osszesjegy, pontos_kor):
    eredmeny = dict()
    if adatok.tipus == "radix":
        # eredmeny["BJ_id"] = bolygojegyben_id(bolygok)
        eredmeny["alapszamolasok"] = alapszamolasok(adatok, osszesjegy)
        eredmeny["pontoskor"] = pontos_kor_szamitas(pontos_kor)
        eredmeny["eletciklus"] = eletciklus(pontos_kor, adatok.neme)
        eredmeny["sorstipus"] = sorstipus(bolygok, hazak)
        eredmeny["hazakurai"] = hazura_kiiratas(hazak, hazakUraHazakban)
        eredmeny["serult_e_nap"] = serult_e_nap(bolygok, adatok)
        eredmeny["serult_e_hold"] = serult_e_hold(bolygok, adatok)
        eredmeny["hyleg"] = hyleg(bolygok)
        eredmeny["anareta"] = anareta(hyleg=eredmeny["hyleg"], bolygok=bolygok)
        eredmeny["megval_vagy_celkij"] = megval_vagy_celkij(bolygok, hazak)
    elif adatok.tipus == "szolár":
        eredmeny["naptigon"] = naptrigon(adatok)

    return eredmeny


def uj_alapanalogiak_hozzarendelese(adatok):
    pontos_kor = szuletesi_datumido(adatok)
    bolygok, hazak = fokszamhozzarendeles(adatok)
    bolygok, hazak = osszfokszam_hozzarendeles(bolygok, hazak)
    bolygok = bolygohoz_haz_rendeles(hazak, bolygok)  # megmondja egy bolygo milyen hazban van
    # todo asc hez és mchez nem kell hazat randelni
    # todo rekurziot kivenni
    bolygok = hazhoz_bolygok_rendelese(hazak, bolygok)  # megmondja egy_egy hazban milyen bolygok vannak
    bolygok = fenyszog_hozzarendeles(bolygok)
    hazura_melyik_hazaban(hazak, bolygok)
    return bolygok, hazak, pontos_kor


