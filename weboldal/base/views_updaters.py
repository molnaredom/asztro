from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .models import Room4, Topic4, Jegy4, Bolygo4, Haz4, Message4 ,BolygoHazban4, BolygoJegyben4, HazJegyben4, Horoszkop4
from django.contrib.auth.models import User
from .forms import RoomForm, AnalogiaForm
from django.contrib.auth import authenticate, login, logout
from .forms import JegyekForm, BolygokForm, HazakForm , BolygoJegybenForm, HazJegybenForm, BolygoHazbanForm, RoomForm, HoroszkopForm




def updateAltalanos(request, nevID, AnalogiaObject, AnalogiaForm, visszateres_helye:str, rendereles_helye:str):
    analogia = AnalogiaObject.objects.get(nevID=nevID)
    form = AnalogiaForm(instance=analogia)


    if request.method == 'POST':
        form = AnalogiaForm(request.POST, instance=analogia)
        if form.is_valid():
            form.save()
            return redirect(visszateres_helye)

    context = {'form': form}
    return render(request, f"create_templates/{rendereles_helye}", context)

@login_required(login_url="login")
def updateRestrichted(request, nevID, AnalogiaObject, AnalogiaForm, visszateres_helye:str, rendereles_helye:str):
    analogia = AnalogiaObject.objects.get(nevID=nevID)
    form = AnalogiaForm(instance=analogia)

    if request.user != room.host:
        return HttpResponse("Nem engedélyezett művelet, amíg nem vagy bejelentkezve")

    if request.method == 'POST':
        form = AnalogiaForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect(visszateres_helye)

    context = {'form': form}
    return render(request, rendereles_helye, "create_templetes/"+str(context))


def updateBolygo(request, nevID):
    return updateAltalanos(request,nevID, Bolygo4, BolygokForm, "bolygok", "bolygok_form.html")


def updateJegy(request, nevID):
    return updateAltalanos(request,nevID, Jegy4, JegyekForm, "jegyek", "jegyek_form.html")


def updateHaz(request, nevID):
    return updateAltalanos(request,nevID, Haz4, HazakForm, "bolygok", "hazak_form.html")


def updateBolygoJegyben(request, osszetettNevID):
    return updateAltalanos(request,osszetettNevID, BolygoJegyben4, BolygoJegybenForm, "bolygokJegyekben", "bolygoJegyben_form.html")


def updateBolygoHazban(request, osszetettNevID):
    return updateAltalanos(request,osszetettNevID, BolygoHazban4, BolygoHazbanForm, "bolygokHazakban", "bolygoHazban_form.html")


def updateHazJegyben(request, osszetettNevID):
    return updateAltalanos(request,osszetettNevID, HazJegyben4, HazJegybenForm, "hazakJegyben", "hazJegyben_form.html")


def updateHoroszkop(request, nevID):
    return updateAltalanos(request,nevID, Horoszkop4, HoroszkopForm, "horoszkop_gyujtemeny", "horoszkop_form.html")




