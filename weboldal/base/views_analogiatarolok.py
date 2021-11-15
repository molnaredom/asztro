
from django.shortcuts import render
from .models import Jegy, Bolygo, Haz,BolygoHazban, BolygoJegyben, HazJegyben, Horoszkop1

# több oldalt tartalmazo,analógiatároló felület
def jegyek_oldal(request):

    jegyek = Jegy.objects.all()
    jegy_minoseg_lekerdezes = {}
    if request.method == "POST":
        minoseg_neve = request.POST.get('minoseg')
        jegy_minoseg_lekerdezes = Jegy.objects.filter(minoseg=minoseg_neve)


    context = {'adatok': jegyek , "jegy_minoseg_lekerdezes": jegy_minoseg_lekerdezes}
    return render(request, 'analogiatarolok/jegyek.html', context )


def bolygok_oldal(request):

    bolygok = Bolygo.objects.all()
    bolygotipus_lekerdezes = {}
    if request.method == "POST":
        tipusnev = request.POST.get('bolygotipus')
        bolygotipus_lekerdezes = Bolygo.objects.filter(tipus=tipusnev)


    context = {'adatok': bolygok , "bolygotipus_lekerdezes": bolygotipus_lekerdezes}
    return render(request, 'analogiatarolok/bolygok.html', context )


def hazak_oldal(request):

    hazak = Haz.objects.all()
    haztipus_lekerdezes = {}
    if request.method == "POST":
        haztipus_lekerdezes = Haz.objects.filter(tipus=request.POST.get('tipus'))


    context = {'adatok': hazak , "haztipus_lekerdezes": haztipus_lekerdezes}
    return render(request, 'analogiatarolok/hazak.html', context )


def bolygokJegyekben(request):
    jegy_alapjan_lekeres = {}
    if request.method == "POST":
        jegyNev = request.POST.get('jegyNev')
        jegy_alapjan_lekeres = BolygoJegyben.objects.filter(jegy__nevID=jegyNev)

    jegyek = BolygoJegyben.objects.all()
    context = {'adatok': jegyek, "jegy_alapjan_lekeres": jegy_alapjan_lekeres }
    return render(request, 'analogiatarolok/bolygokJegyekben.html', context )


def bolygokHazakban(request):

    bolygokhazban = BolygoHazban.objects.all()

    context = {'adatok': bolygokhazban}
    return render(request, 'analogiatarolok/bolygokHazakban.html', context )


def hazakJegyekben(request):

    hazjegyben = HazJegyben.objects.all()
    context = {'adatok': hazjegyben}
    return render(request, 'analogiatarolok/hazakJegyekben.html', context )


def horoszkop_gyujtemeny(request):

    hp = Horoszkop1.objects.all()
    context = {'adatok': hp}
    return render(request, 'analogiatarolok/horoszkop_gyujtemeny.html', context )


