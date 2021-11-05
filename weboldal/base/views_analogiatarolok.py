
from django.shortcuts import render
from .models import Jegy, Bolygo, Haz,BolygoHazban, BolygoJegyben, HazJegyben

# több oldalt tartalmazo,analógiatároló felület
def jegyek_oldal(request):

    jegyek = Jegy.objects.all()

    context = {'adatok': jegyek}
    return render(request, 'analogiatarolok/jegyek.html', context )


def bolygok_oldal(request):

    bolygok = Bolygo.objects.all()

    context = {'adatok': bolygok}
    return render(request, 'analogiatarolok/bolygok.html', context )


def hazak_oldal(request):

    hazak = Haz.objects.all()

    context = {'adatok': hazak}
    return render(request, 'analogiatarolok/hazak.html', context )


def bolygokJegyekben(request):

    jegyek = BolygoJegyben.objects.all()
    context = {'adatok': jegyek}
    return render(request, 'analogiatarolok/bolygokJegyekben.html', context )


def bolygokHazakban(request):

    bolygokhazban = BolygoHazban.objects.all()

    context = {'adatok': bolygokhazban}
    return render(request, 'analogiatarolok/bolygokHazakban.html', context )


def hazakJegyekben(request):

    hazjegyben = HazJegyben.objects.all()
    context = {'adatok': hazjegyben}
    return render(request, 'analogiatarolok/hazakJegyekben.html', context )

