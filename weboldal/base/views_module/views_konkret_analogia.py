from django.shortcuts import render
from ..models import Room2, Topic2, Jegy2, Bolygo2, Haz2, Message2, BolygoHazban2, BolygoJegyben2, HazJegyben2, HazUraHazban
import random

def altalanos_osszetett_analogia(Objektum, html_path, request, id):
    analogia = Objektum.objects.get(id=id)

    random_analogia = random.randint(1,len(Objektum.objects.all()))

    context = {"analogia": analogia, "random_analogia": str(random_analogia)}  # ez egy objektum

    return render(request, f"{html_path}", context)


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
    return altalanos_osszetett_analogia(BolygoJegyben2,"konkret_analogiak/bolygoJegyben.html",request, id )


def bolygoHazban(request, id):
    return altalanos_osszetett_analogia(BolygoHazban2,"konkret_analogiak/bolygoHazban.html",request, id)


def hazJegyben(request, id):
    analogia = HazJegyben2.objects.get(id=id)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/hazJegyben.html", context)


def hazUraHazban(request, id):
    analogia = HazUraHazban.objects.get(id=id)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/hazUraHazban.html", context)


