from django.shortcuts import render
from ..models import Jegy2, Bolygo2, Haz2, BolygoHazban2, BolygoJegyben2, HazJegyben2, HazUraHazban
from ..kisegito.kisegito import *
import random


def altalanos_osszetett_analogia(Objektum, html_path, request, id):
    analogia = Objektum.objects.get(id=id)
    random_analogia = random.randint(1,len(Objektum.objects.all())-1)
    context = {"analogia": analogia, "random_analogia": str(random_analogia)}
    print(context)
    return render(request, f"{html_path}", context)


def altalanos_nevalapjan_kereso_analogia(Objektum, html_path, request, nevID, nevek):
    analogia = Objektum.objects.get(nevID=nevID)
    random_analogia = nevek[random.randint(0,len(Objektum.objects.all())-1)]
    context = {"analogia": analogia, "random_analogia": str(random_analogia)}

    return render(request, html_path, context)


def jegy(request, nevID):
    nevek = get_jegy_nevek()
    return altalanos_nevalapjan_kereso_analogia(Jegy2, "konkret_analogiak/jegy.html", request, nevID, nevek)


def bolygo(request, nevID):
    nevek = get_bolygo_nevek(fotengelyekkel=True)
    return altalanos_nevalapjan_kereso_analogia(Bolygo2, "konkret_analogiak/bolygo.html", request, nevID, nevek)


def haz(request, nevID):
    nevek = [str(i) for i in range(1,12)]
    return altalanos_nevalapjan_kereso_analogia(Haz2, "konkret_analogiak/haz.html", request, nevID, nevek)


def bolygoJegyben(request, id):
    return altalanos_osszetett_analogia(BolygoJegyben2,"konkret_analogiak/bolygoJegyben.html",request, id )


def bolygoHazban(request, id):
    return altalanos_osszetett_analogia(BolygoHazban2,"konkret_analogiak/bolygoHazban.html",request, id)


def hazJegyben(request, id):
    return altalanos_osszetett_analogia(HazJegyben2,"konkret_analogiak/hazJegyben.html",request, id)


def hazUraHazban(request, id):
    return altalanos_osszetett_analogia(HazUraHazban, "konkret_analogiak/hazUraHazban.html", request, id)



