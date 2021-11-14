
from django.shortcuts import render
from .models import Jegy4, Bolygo4, Haz4,BolygoHazban4, BolygoJegyben4, HazJegyben4, Horoszkop4

# több oldalt tartalmazo,analógiatároló felület
def jegyek_oldal(request):

    jegyek = Jegy4.objects.all()
    minoseg_jegyek = {}
    if request.method == "POST":
        minoseg_neve = request.POST.get('minoseg')
        print("--",minoseg_neve, type(minoseg_neve))
        minoseg_jegyek = Jegy4.objects.filter(minoseg=minoseg_neve)

    tuzes = Jegy4.objects.filter(elem="tűz")
    vizes = Jegy4.objects.filter(elem="tűz")
    foldes = Jegy4.objects.filter(elem="tűz")
    levegos = Jegy4.objects.filter(elem="tűz")

    context = {'adatok': jegyek ,"tuzes": tuzes, "vizes": vizes, "foldes" :foldes, "levegos": levegos, "minoseg_jegyek": minoseg_jegyek}
    return render(request, 'analogiatarolok/jegyek.html', context )


def bolygok_oldal(request):

    bolygok = Bolygo4.objects.all()

    context = {'adatok': bolygok}
    return render(request, 'analogiatarolok/bolygok.html', context )


def hazak_oldal(request):

    hazak = Haz4.objects.all()

    context = {'adatok': hazak}
    return render(request, 'analogiatarolok/hazak.html', context )


def bolygokJegyekben(request):

    jegyek = BolygoJegyben4.objects.all()
    context = {'adatok': jegyek}
    return render(request, 'analogiatarolok/bolygokJegyekben.html', context )


def bolygokHazakban(request):

    bolygokhazban = BolygoHazban4.objects.all()

    context = {'adatok': bolygokhazban}
    return render(request, 'analogiatarolok/bolygokHazakban.html', context )


def hazakJegyekben(request):

    hazjegyben = HazJegyben4.objects.all()
    context = {'adatok': hazjegyben}
    return render(request, 'analogiatarolok/hazakJegyekben.html', context )


def horoszkop_gyujtemeny(request):

    hp = Horoszkop4.objects.all()
    context = {'adatok': hp}
    return render(request, 'analogiatarolok/horoszkop_gyujtemeny.html', context )


