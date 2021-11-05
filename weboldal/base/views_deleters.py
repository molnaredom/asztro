
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from .models import Jegy, Bolygo, Haz, BolygoHazban, BolygoJegyben, HazJegyben, Message,Room



@login_required(login_url="login")
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("Nem engedélyezett művelet, amíg nem vagy bejelentkezve")

    if request.method == "POST":
        message.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj":message})


@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("Nem engedélyezett művelet, amíg nem vagy bejelentkezve")

    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj":room})



#deleterek
def deleteBolygo(request, nevID):
    bolygo = Bolygo.objects.get(nevID=nevID)
    if request.method == "POST":
        bolygo.delete()
        return redirect("bolygok")
    return render(request, "base/delete.html", {"obj":bolygo})


def deleteJegy(request, nevID):
    jegy = Jegy.objects.get(nevID=nevID)
    if request.method == "POST":
        jegy.delete()
        return redirect("jegyek")
    return render(request, "base/delete.html", {"obj":jegy})


def deleteHaz(request,nevID):
    haz = Haz.objects.get(nevID=nevID)
    if request.method == "POST":
        haz.delete()
        return redirect("hazak")
    return render(request, "base/delete.html", {"obj":haz})


def deleteBolygoJegyben(request, nevID):
    bolygo = BolygoJegyben.objects.get(nevID=nevID)
    if request.method == "POST":
        bolygo.delete()
        return redirect("bolygokJegyekben")
    return render(request, "base/delete.html", {"obj":bolygo})


def deleteBolygoHazban(request, nevID):
    jegy = BolygoHazban.objects.get(nevID=nevID)
    if request.method == "POST":
        jegy.delete()
        return redirect("bolygokHazakban")
    return render(request, "base/delete.html", {"obj":jegy})


def deleteHazJegyben(request,nevID):
    haz = HazJegyben.objects.get(nevID=nevID)
    if request.method == "POST":
        haz.delete()
        return redirect("hazakJegyekben")
    return render(request, "base/delete.html", {"obj":haz})



