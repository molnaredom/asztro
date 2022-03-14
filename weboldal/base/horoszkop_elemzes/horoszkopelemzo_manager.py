from .alap_elemzesek import pontos_kor_szamitas, alapszamolasok, eletciklus, \
    serult_e_nap, serult_e_hold, hyleg
from .kiiratas_formatumvalto import hazura_kiiratas
from .kisegito import szuletesi_datumido
from .osszetett_elemzesek import anareta, sorstipus
from .hozzarendelesek import *


def _elemzes(adatok, osszesjegy, hazakUraHazakban):

    bolygok, hazak, pontos_kor = uj_alapanalogiak_hozzarendelese(adatok)
    # [print(i["haz"].nevID, [j["bolygo"] for j in i["bolygok"]]) for i in hazak]

    return eredmenyek_kiszamitasa(adatok, bolygok, hazak, hazakUraHazakban, osszesjegy, pontos_kor)


def eredmenyek_kiszamitasa(adatok, bolygok, hazak, hazakUraHazakban, osszesjegy, pontos_kor):
    eredmeny = dict()

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


