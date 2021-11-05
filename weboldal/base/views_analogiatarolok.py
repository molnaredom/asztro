
from django.shortcuts import render
from .models import Jegy_1, Bolygo_1, Haz_1,BolygoHazban_1, BolygoJegyben_1, HazJegyben_1

# több oldalt tartalmazo,analógiatároló felület
def jegyek_oldal(request):

    jegyek = Jegy_1.objects.all()

    context = {'adatok': jegyek}
    return render(request, 'analogiatarolok/jegyek.html', context )


def bolygok_oldal(request):

    bolygok = Bolygo_1.objects.all()

    context = {'adatok': bolygok}
    return render(request, 'analogiatarolok/bolygok.html', context )


def hazak_oldal(request):

    hazak = Haz_1.objects.all()

    context = {'adatok': hazak}
    return render(request, 'analogiatarolokk/hazak.html', context )


def bolygokJegyekben(request):

    jegyek = BolygoJegyben_1.objects.all()

    context = {'adatok': jegyek}
    return render(request, 'analogiatarolok/bolygokJegyekben.html', context )


def bolygokHazakban(request):

    bolygok = BolygoHazban_1.objects.all()

    context = {'adatok': bolygok}
    return render(request, 'analogiatarolok/bolygokHazakban.html', context )


def hazakJegyekben(request):

    hazak = HazJegyben_1.objects.all()
    context = {'adatok': hazak}
    return render(request, 'analogiatarolok/hazakJegyekben.html', context )

