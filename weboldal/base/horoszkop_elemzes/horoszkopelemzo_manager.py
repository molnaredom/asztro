from .alap_elemzesek import pontos_kor_szamitas, alapszamolasok, eletciklus, \
    serult_e_nap, serult_e_hold, hyleg
from .kisegito import szuletesi_datumido
from .osszetett_elemzesek import anareta, sorstipus
from .hozzarendelesek import hazhoz_bolygok_rendelese, bolygohoz_haz_rendeles, \
    fokszamhozzarendeles, osszfokszam_hozzarendeles, hazura_melyik_hazaban, fenyszog_hozzarendeles


def _elemzes(adatok, osszesjegy, hazakUraHazakban):
    eredmeny = {}
    pontos_kor = szuletesi_datumido(adatok)

    bolygok, hazak = fokszamhozzarendeles(adatok)
    bolygok, hazak = osszfokszam_hozzarendeles(bolygok, hazak)

    bolygok = bolygohoz_haz_rendeles(hazak, bolygok)  # megmondja egy bolygo milyen hazban van
    bolygok = hazhoz_bolygok_rendelese(hazak, bolygok)  # megmondja egy_egy hazban milyen bolygok vannak

    bolygok = fenyszog_hozzarendeles(bolygok)

    hazura_melyik_hazaban(hazak, bolygok)
    # [print(i["haz"].nevID, [j["bolygo"] for j in i["bolygok"]]) for i in hazak]

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


def hazura_kiiratas(hazak, hazakUraHazakban):

    def hazur_kiiratas(haz, ura):
        if ura in ["1", "2", "4", "7", "9", '10', '11', "12"]:
            return f"{haz}.ház ura az {ura}-es házban"
        elif ura in ["3","8"]:
            return f"{haz}.ház ura az {ura}-as házban"
        elif ura in ["6"]:
            return f"{haz}.ház ura az {ura}-os házban"
        elif ura in ["5"]:
            return f"{haz}.ház ura az {ura}-ös házban"
        elif ura == "nincs hazur":
            return f"{haz}.háznak nincs ura"
        else:
            print("HIBA")
            print(ura)

    haz_urak_kiiratva = []

    for i in hazak:
        for hazurahazban in hazakUraHazakban:
            # print(hazurahazban.alap_haz, str(i["haz"]) ,"--", hazurahazban.ura_melyik_hazban ,str(i["hazura"]))
            if str(hazurahazban.alap_haz) == str(i["haz"]) and str(hazurahazban.ura_melyik_hazban) == str(i["hazura"]):
                # print("házura")
                haz_urak_kiiratva.append({hazur_kiiratas(haz=str(i["haz"]), ura=str(i["hazura"])) : hazurahazban.tulajdonsagok })


    return haz_urak_kiiratva
    # [print(hazur_kiiratas(haz=str(i["haz"]), ura=str(i["hazura"]))) for i in hazak]


