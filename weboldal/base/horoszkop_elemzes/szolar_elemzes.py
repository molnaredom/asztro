def naptrigon(adatok):
    """
    :param adatok:  a nap házának kinyerése céljából az adatok
    :return: egy tömb ami tartalmaz 3 házat, ami megfelel a nap házhelyzetének és 2 további trigonális házával
            ez a 3 ház 3 integer
    """

    return [int(adatok.nap_h.haz.__str__()),
            (int(adatok.nap_h.haz.__str__()) + 4) % 12,
            (int(adatok.nap_h.haz.__str__()) + 8) % 12]


def transzcenens_bolygok_tamadottak_e(bolygok):
    """
    3 transzcendens bolygó van: Uránusz, Neptunusz, Plútó
    Ezeknek vizsgáljuk, hogy kapnak-e támadó fényszöget, azaz kvadrátot vagy oppozíciót
    :return: egy szótár ami a 3 bolygónak a támadásait tárolja tömbökben:
        példa: {'plútó' : ['mars oppozíció', 'pluto kvadrát']}
        általánso forma: {'vizsgalt_bolygó': ['támadó_bolygó fényszög_típus', ...], ...}
    """

    tamadottsag_tomb = {}

    def bolygovizsgalo(bolygo_szama:int):
        tamadasok = []
        oppoziciok = bolygok[bolygo_szama]["fenyszogek"]["oppozicio"]
        kvadratok = bolygok[bolygo_szama]["fenyszogek"]["kvadrat"]
        for opp in oppoziciok:
            tamadasok.append(f'{opp["bolygo"]["bolygo"].nevID} oppozíció')
        for opp in kvadratok:
            tamadasok.append(f'{opp["bolygo"]["bolygo"].nevID} kvadrát')
        return tamadasok

    tamadottsag_tomb["Uránusz"] = bolygovizsgalo(7)
    tamadottsag_tomb["Neptun"] = bolygovizsgalo(8)
    tamadottsag_tomb["Pluto"] = bolygovizsgalo(9)

    return tamadottsag_tomb
