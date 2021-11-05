from django.shortcuts import render
from .models import Room, Topic, Jegy_1, Bolygo_1, Haz_1, Message ,BolygoHazban_1, BolygoJegyben_1, HazJegyben_1


# konkrét oldalak( a fa levelei)
def jegy(request,nevID):
    analogia = Jegy_1.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/jegy.html", context)


def bolygo(request,nevID):
    analogia = Bolygo_1.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygo.html", context)


def haz(request,nevID):
    analogia = Haz_1.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/haz.html", context)


def bolygoJegyben(request,osszetett_nevID):
    analogia = BolygoJegyben_1.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoJegyben.html", context)


def bolygoHazban(request,osszetett_nevID):
    analogia = BolygoHazban_1.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoHazban.html", context)


def hazJegyben(request,osszetett_nevID):
    analogia = HazJegyben_1.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/hazJegyben.html", context)

