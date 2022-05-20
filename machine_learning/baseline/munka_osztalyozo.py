def munka_osztalyozas(oszatlozas_alap):
    munka_tarolo = {}

    with open("../munka_osztalyok.csv") as munkatabla:
        munkatabla.readline()
        for munka in munkatabla:
            munka = munka.strip().split(";")
            if oszatlozas_alap == "irodai":
                if munka[1].isdigit():
                    munka_tarolo[munka[0]] = int(munka[1])
    # print("----",munka_tarolo)
    return munka_tarolo

