def munka_osztalyozas(irodai=False):
    munka_tarolo = {}


    with open("../munka_osztalyok.csv") as munkatabla:
        munkatabla.readline()
        for munka in munkatabla:
            munka = munka.strip().split(";")
            if irodai:
                munka_tarolo[munka[0]] = int(munka[1])

    return munka_tarolo
