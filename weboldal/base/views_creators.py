from django.contrib.auth.decorators import login_required
from .forms import JegyekForm, BolygokForm, HazakForm , BolygoJegybenForm, HazJegybenForm, BolygoHazbanForm, RoomForm
from django.shortcuts import render, redirect



@login_required(login_url="login")
def createroom(request):
    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            return redirect("home")

    context = {'form': form}
    return render(request, "create_templates/room_form.html", context)


#createrek
def createJegyek(request):
    form = JegyekForm()

    if request.method == "POST":
        form = JegyekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jegyek")

    context = {'form': form}
    return render(request, "create_templates/jegyek_form.html", context)


def createBolygok(request):
    form = BolygokForm()

    if request.method == "POST":
        form = BolygokForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bolygok")

    context = {'form': form}
    return render(request, "create_templates/bolygok_form.html", context)


 #job lib

def createHazak(request):
    form = HazakForm()

    if request.method == "POST":
        form = HazakForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hazak")

    context = {'form': form}
    return render(request, "create_templates/hazak_form.html", context)


def createBolygoJegyben(request):
    form = BolygoJegybenForm()

    if request.method == "POST":
        form = BolygoJegybenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bolygokJegyekben")

    context = {'form': form}
    return render(request, "create_templates/bolygoJegyben_form.html", context)


def createBolygoHazban(request):
    form = BolygoHazbanForm()

    if request.method == "POST":
        form = BolygoHazbanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bolygokHazakban")

    context = {'form': form}
    return render(request, "create_templates/bolygoHazban_form.html", context)


 #job lib

def createHazJegyben(request):
    form = HazJegybenForm()

    if request.method == "POST":
        form = HazJegybenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hazakJegyekben")

    context = {'form': form}
    return render(request, "create_templates/hazJegyben_form.html", context)

