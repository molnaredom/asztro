from django.contrib.auth.decorators import login_required
from .forms import JegyekForm, BolygokForm, HazakForm , BolygoJegybenForm, HazJegybenForm, BolygoHazbanForm, RoomForm, HoroszkopForm, HazUraHazbanForm
from django.shortcuts import render, redirect

@login_required(login_url="login")
def createroom(request):
    form = RoomForm()

    if request.method == "POST":

        if 'bolygo_es_jegy_lekerdezes' in request.POST:
            jegyNev = request.POST.get('jegyNev')
            bolygoNev = request.POST.get('bolygoNev')
            jegy_alapjan_lekeres = bolygo_alapjan_lekeres(bolygoNev, jegyNev)

        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            return redirect("home")

    context = {'form': form}
    return render(request, "create_templates/room_form.html", context)


def _analogiafeltoltes(request,Osztalyform, analogia):
    form = Osztalyform()
    if request.method == "POST":

        if "megse" in request.POST:
            return redirect(f"{analogia}")

        form = Osztalyform(request.POST)
        if form.is_valid():
            form.save()

        if 'ujabb_fevitel' in request.POST:
            return redirect(f"create-{analogia}")

        elif "mentes_es_foolal" in request.POST:
            return redirect(f"{analogia}")

    context = {'form': form}
    return render(request, "create_templates/analogia_form.html", context)

#createrek
def createJegyek(request):
    return _analogiafeltoltes(request, JegyekForm, "jegyek")


def createBolygok(request):
    return _analogiafeltoltes(request, BolygokForm, "bolygok")

 #job lib

def createHazak(request):
    return _analogiafeltoltes(request, HazakForm, "hazak")


def createBolygoJegyben(request):
    return _analogiafeltoltes(request, BolygoJegybenForm, "bolygoJegyben")


def createBolygoHazban(request):
    return _analogiafeltoltes(request, BolygoHazbanForm, "bolygoHazbann")


 #job lib

def createHazJegyben(request):
    return _analogiafeltoltes(request, HazJegybenForm, "hazJegyben")


def createHazUraHazban(request):
    return _analogiafeltoltes(request, HazUraHazbanForm, "hazakUraHazakban")


def createHoroszkop(request):
    form = HoroszkopForm()
    if request.method == "POST":
        form = HoroszkopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("horoszkop_gyujtemeny")

    context = {'form': form}
    return render(request, "create_templates/analogia_form.html", context)

