from django.shortcuts import render
from ..models import Room2, Topic2, Jegy2, Bolygo2, Haz2, Message2, BolygoHazban2, BolygoJegyben2, HazJegyben2, HazUraHazban
import random


# konkrét oldalak( a fa levelei)
def jegy(request, nevID):
    analogia = Jegy2.objects.get(nevID=nevID)
    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/jegy.html", context)


def bolygo(request, nevID):
    analogia = Bolygo2.objects.get(nevID=nevID)
    # print(analogia.leiras["analogiak"])
    analogia.leiras = eval(analogia.leiras["analogiak"])
    randomszam = random.randint(0, 12)
    print(randomszam)

    context = {"analogia": analogia, }  # ez egy objektum

    return render(request, "konkret_analogiak/bolygo.html", context)


def haz(request, nevID):
    analogia = Haz2.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/haz.html", context)


def bolygoJegyben(request, id):
    analogia = BolygoJegyben2.objects.get(id=id)
    randomszamok = random.randint(1, 50)

    context = {"analogia": analogia, "randomszamok": randomszamok}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoJegyben.html", context)


def bolygoHazban(request, id):
    analogia = BolygoHazban2.objects.get(id=id)

    random_analogia = random.randint(1,len(BolygoHazban2.objects.all()))

    context = {"analogia": analogia, "random_analogia": str(random_analogia)}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoHazban.html", context)


def hazJegyben(request, id):
    analogia = HazJegyben2.objects.get(id=id)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/hazJegyben.html", context)


def hazUraHazban(request, id):
    analogia = HazUraHazban.objects.get(id=id)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/hazUraHazban.html", context)


