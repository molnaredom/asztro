from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..models import Jegy2, Bolygo2, Haz2, BolygoHazban2, BolygoJegyben2, HazJegyben2, Horoszkop2, HazUraHazban
from ..forms import JegyekForm, BolygokForm, HazakForm , BolygoJegybenForm, HazJegybenForm, BolygoHazbanForm, RoomForm, HoroszkopForm, HazUraHazbanForm


def updateAltalanos(request, nevID, AnalogiaObject, AnalogiaForm, visszateres_helye:str):
    analogia = AnalogiaObject.objects.get(nevID=nevID)
    form = AnalogiaForm(instance=analogia)


    if request.method == 'POST':
        form = AnalogiaForm(request.POST, instance=analogia)
        if form.is_valid():
            form.save()
            return redirect(visszateres_helye)

    context = {'form': form}
    return render(request, f"create_templates/analogia_form.html", context)


def updateAltalanos_id(request, pk, AnalogiaObject, AnalogiaForm, visszateres_helye:str):
    analogia = AnalogiaObject.objects.get(id=pk)
    form = AnalogiaForm(instance=analogia)

    if request.method == 'POST':
        form = AnalogiaForm(request.POST, instance=analogia)
        if form.is_valid():
            form.save()
            return redirect(visszateres_helye)

    context = {'form': form}
    return render(request, f"create_templates/analogia_form.html", context)


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
    return updateAltalanos(request, nevID, Bolygo2, BolygokForm, "bolygok")


def updateJegy(request, nevID):
    return updateAltalanos(request, nevID, Jegy2, JegyekForm, "jegyek")


def updateHaz(request, nevID):
    return updateAltalanos(request, nevID, Haz2, HazakForm, "hazak")


def updateBolygoJegyben(request, id):
    return updateAltalanos_id(request, id, BolygoJegyben2, BolygoJegybenForm, "bolygokJegyekben")


def updateBolygoHazban(request, id):
    return updateAltalanos_id(request, id, BolygoHazban2, BolygoHazbanForm, "bolygokHazakban")


def updateHazJegyben(request, id):
    return updateAltalanos_id(request, id, HazJegyben2, HazJegybenForm, "hazakJegyekben")


def updateHazUraHazban(request, id):
    return updateAltalanos_id(request, id, HazUraHazban, HazUraHazbanForm, "hazakUraHazakban")


def updateHoroszkop(request, id):
    return updateAltalanos_id(request, id, Horoszkop2, HoroszkopForm, "horoszkop_gyujtemeny")




