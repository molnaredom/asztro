from django.shortcuts import render
from .models import Room, Topic, Jegy, Bolygo, Haz, Message ,BolygoHazban, BolygoJegyben2, HazJegyben, Horoszkop1


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


def bolygoJegyben(request,id):
    analogia = BolygoJegyben2.objects.get(id=id)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoJegyben.html", context)


def bolygoHazban(request,id):
    analogia = BolygoHazban.objects.get(id=id)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/bolygoHazban.html", context)


def hazJegyben(request,id):
    analogia = HazJegyben.objects.get(id=id)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/hazJegyben.html", context)

def horoszkop(request,id):
    analogia = Horoszkop1.objects.get(id=id)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "konkret_analogiak/horoszkop.html", context)

