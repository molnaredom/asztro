def munka_osztalyozas(oszatlozas_alap):
    munka_tarolo = {}


    with open("../munka_osztalyok.csv") as munkatabla:
        munkatabla.readline()
        for munka in munkatabla:
            munka = munka.strip().split(";")
            if oszatlozas_alap== "irodai":
                munka_tarolo[munka[0]] = int(munka[1])

    return munka_tarolo

