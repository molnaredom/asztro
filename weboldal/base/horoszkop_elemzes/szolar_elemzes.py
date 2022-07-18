def naptrigon(adatok):
    """
    :param adatok:  a nap házának kinyerése céljából az adatok
    :return: egy tömb ami tartalmaz 3 házat, ami megfelel a nap házhelyzetének és 2 további trigonális házával
            ez a 3 ház 3 integer
    """

    return [int(adatok.nap_h.haz.__str__()),
            (int(adatok.nap_h.haz.__str__()) + 4) % 12,
            (int(adatok.nap_h.haz.__str__()) + 8) % 12]
