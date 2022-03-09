from ..default_parameters import *


def hazura_kiiratas(hazak, hazakUraHazakban):
    fgv_nev = "hazura_kiiratas"

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
            printw(ura,problema=fgv_nev)

    haz_urak_kiiratva = []

    for i in hazak:
        for hazurahazban in hazakUraHazakban:
            # print(hazurahazban.alap_haz, str(i["haz"]) ,"--", hazurahazban.ura_melyik_hazban ,str(i["hazura"]))
            if str(hazurahazban.alap_haz) == str(i["haz"]) and str(hazurahazban.ura_melyik_hazban) == str(i["hazura"]):
                # print("házura")
                haz_urak_kiiratva.append({hazur_kiiratas(haz=str(i["haz"]), ura=str(i["hazura"])) : hazurahazban.tulajdonsagok })


    return haz_urak_kiiratva
    # [print(hazur_kiiratas(haz=str(i["haz"]), ura=str(i["hazura"]))) for i in hazak]
