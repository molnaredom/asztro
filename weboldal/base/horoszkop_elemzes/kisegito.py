import datetime


def nevet_privatra(nev):
    nev = str(nev)
    if len(nev.split()) == 1:
        return nev[0] + (len(nev.split()[0])-1) * "*"
    elif len(nev.split()) >= 1:
        return nev[0] + (len(nev.split()[0])-1) * "*" + " " + len(nev.split()[1]) * "*"


def hanyadik_jegy_asctol(kiindulasijegy, aktjegy):
    kiind_szam, akt_szam = jegyet_szamra_valt(kiindulasijegy), jegyet_szamra_valt(aktjegy)
    return (akt_szam - kiind_szam) % 12


def jegyet_szamra_valt(jegynev):
    jegyhezszam = {"kos": 1, "bika": 2, "ikrek": 3, "rák": 4, "oroszlán": 5, "szűz": 6, "mérleg": 7, "skorpió": 8,
                   "nyilas": 9, "bak": 10,
                   "vízöntő": 11, "halak": 12}
    return jegyhezszam[jegynev]


def szuletesi_datumido(adatok):
    szuletes = adatok.idopont.replace(tzinfo=None)

    currentDate = datetime.datetime.now()
    deadlineDate = szuletes
    # print(deadlineDate)
    daysLeft = currentDate - deadlineDate
    # print(daysLeft)

    years = ((daysLeft.total_seconds()) / (365.242199 * 24 * 3600))
    yearsInt = int(years)

    months = (years - yearsInt) * 12
    monthsInt = int(months)

    days = (months - monthsInt) * (365.242199 / 12)
    daysInt = int(days)

    hours = (days - daysInt) * 24
    hoursInt = int(hours)

    minutes = (hours - hoursInt) * 60
    minutesInt = int(minutes)

    seconds = (minutes - minutesInt) * 60
    secondsInt = int(seconds)

    pontos_kor = [yearsInt, monthsInt, daysInt, hoursInt, minutesInt, secondsInt]   # datetime.datetime(yearsInt, monthsInt, daysInt, hoursInt, minutesInt, secondsInt)

    return pontos_kor
