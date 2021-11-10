from django.shortcuts import render
from .models import Room4, Topic4, Jegy4, Bolygo4, Haz4, Message4 ,BolygoHazban4, BolygoJegyben4, HazJegyben4, Horoszkop4


# konkrét oldalak( a fa levelei)
def jegy(request,nevID):
    analogia = Jegy4.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/jegy.html", context)


def bolygo(request,nevID):
    analogia = Bolygo4.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygo.html", context)


def haz(request,nevID):
    analogia = Haz4.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/haz.html", context)


def bolygoJegyben(request,osszetett_nevID):
    analogia = BolygoJegyben4.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoJegyben.html", context)


def bolygoHazban(request,osszetett_nevID):
    analogia = BolygoHazban4.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoHazban.html", context)


def hazJegyben(request,osszetett_nevID):
    analogia = HazJegyben4.objects.get(osszetett_nevID=osszetett_nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/hazJegyben.html", context)

def horoszkop(request,nevID):
    analogia = Horoszkop4.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/horoszkop.html", context)

