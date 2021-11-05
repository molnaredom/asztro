from django.shortcuts import render
from .models import Room, Topic, Jegy, Bolygo, Haz, Message ,BolygoHazban, BolygoJegyben, HazJegyben


# konkrét oldalak( a fa levelei)
def jegy(request,nevID):
    analogia = Jegy.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/jegy.html", context)


def bolygo(request,nevID):
    analogia = Bolygo.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygo.html", context)


def haz(request,nevID):
    analogia = Haz.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/haz.html", context)


def bolygoJegyben(request,osszetett_nevID):
    analogia = BolygoJegyben.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoJegyben.html", context)


def bolygoHazban(request,osszetett_nevID):
    analogia = BolygoHazban.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoHazban.html", context)


def hazJegyben(request,osszetett_nevID):
    analogia = HazJegyben.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/hazJegyben.html", context)

