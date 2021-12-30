from django.shortcuts import render

from .models import Horoszkop2


def horoszkop(request,id):
    analogia = Horoszkop2.objects.get(id=id)

    elemzes_adat = elemzes(analogia)
    context = {"analogia": analogia, "elemzes" : elemzes_adat}  # ez egy objektum

    return render(request, "konkret_analogiak/horoszkop.html", context)


def elemzes(adatok):
    elemzes_eredmeny = {}
    bolygok = [adatok.nap, adatok.hold, adatok.merkur, adatok.venusz, adatok.mars, adatok.jupiter, adatok.szaturnusz, adatok.uranusz, adatok.neptun, adatok.pluto]


    elemzes_eredmeny["évszak szerinti felosztás"] = evzsakszerinti_felosztas(bolygok)

    return elemzes_eredmeny


def evzsakszerinti_felosztas(bolygok):
    evszakok = {"tavasz": 0, "nyár": 0, "ősz": 0, "tél": 0}

    for bolygo in bolygok:
        evszakok[bolygo.jegy.evszak] +=1

    return evszakok

