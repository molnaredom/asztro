from django.shortcuts import render
from .models import Room2, Topic2, Jegy2, Bolygo2, Haz2, Message2 ,BolygoHazban2, BolygoJegyben2, HazJegyben2, Horoszkop2
import random

# konkrét oldalak( a fa levelei)
def jegy(request,nevID):
    analogia = Jegy2.objects.get(nevID=nevID)
    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/jegy.html", context)


def bolygo(request,nevID):
    analogia = Bolygo2.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygo.html", context)


def haz(request,nevID):
    analogia = Haz2.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/haz.html", context)


def bolygoJegyben(request,id):
    analogia = BolygoJegyben2.objects.get(id=id)
    randomszamok = random.randint(1,50)
    analogia

    context = {"analogia": analogia, "randomszamok" : randomszamok}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoJegyben.html", context)


def bolygoHazban(request,id):
    analogia = BolygoHazban2.objects.get(id=id)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoHazban.html", context)


def hazJegyben(request,id):
    analogia = HazJegyben2.objects.get(id=id)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/hazJegyben.html", context)


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
