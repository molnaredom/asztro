
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from .models import Jegy2, Bolygo2, Haz2, BolygoHazban2, BolygoJegyben2, HazJegyben2, Message2,Room2, Horoszkop2



@login_required(login_url="login")
def deleteMessage(request, pk):
    message = Message2.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("Nem engedélyezett művelet, amíg nem vagy bejelentkezve")

    if request.method == "POST":
        message.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj":message})


@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room2.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("Nem engedélyezett művelet, amíg nem vagy bejelentkezve")

    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj":room})


def _delete_altalanos_by_id(request,pk, objetum,ide_ter_vissza:str):
    analoga_objetum = objetum.objects.get(id=pk)
    if request.method == "POST":
        analoga_objetum.delete()
        return redirect(ide_ter_vissza)
    return render(request, "base/delete.html", {"obj":analoga_objetum})


#deleterek
def deleteBolygo(request, nevID):
    bolygo = Bolygo2.objects.get(nevID=nevID)
    if request.method == "POST":
        bolygo.delete()
        return redirect("bolygok")
    return render(request, "base/delete.html", {"obj":bolygo})


def deleteJegy(request, nevID):
    jegy = Jegy2.objects.get(nevID=nevID)
    if request.method == "POST":
        jegy.delete()
        return redirect("jegyek")
    return render(request, "base/delete.html", {"obj":jegy})


def deleteHaz(request,nevID):
    haz = Haz2.objects.get(nevID=nevID)
    if request.method == "POST":
        haz.delete()
        return redirect("hazak")
    return render(request, "base/delete.html", {"obj":haz})


def deleteBolygoJegyben(request, id):
    return _delete_altalanos_by_id(request, id, BolygoJegyben2, "bolygokJegyekben")


def deleteBolygoHazban(request, id):
    return _delete_altalanos_by_id(request, id, BolygoHazban2, "bolygokHazakban")


def deleteHazJegyben(request,id):
    return _delete_altalanos_by_id(request, id, HazJegyben2, "hazakJegyekben")


def deleteHoroszkop(request,id):
    return _delete_altalanos_by_id(request, id, Horoszkop2, "horoszkop_gyujtemeny")



