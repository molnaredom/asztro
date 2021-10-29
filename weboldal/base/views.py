from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic, Jegy1, Bolygo1, Haz1, Analogia1
from .forms import RoomForm, AnalogiaForm, JegyekForm, BolygokForm, HazakForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# rooms = [
#
#     {'id': 1 , "name":"Edgár"},
#     {'id': 2 , "name":"Elen"},
#     {'id': 3 , "name":"Póó"}
#
# ]


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(discription__icontains=q)

    )

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, "topics":topics, "room_count":room_count}
    return render(request, 'base/home.html', context )

def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created') # give us a set of messages that are related specific rooms

    context = {"room": room, "messages": room_messages}
    return render(request, "base/room.html",context)

@login_required(login_url="login")
def createroom(request):
    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form': form}
    return render(request, "base/room_form.html", context)

@login_required(login_url="login")
def updateRoom( request, pk):
    room = Room.objects.get(id= pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("Nem engedélyezett művelet, amíg nem vagy bejelentkezve")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form': form}
    return render(request, "base/room_form.html", context)

@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("Nem engedélyezett művelet, amíg nem vagy bejelentkezve")

    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj":room})


def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request , "HIBA: A felhsználó még nem létezik")

        user = authenticate(request, username= username, password= password) # hitelesito adatok

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "A Felhasználónév vagy a jelszó nem létezik")

    context = {"page": page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "ERROR: a regisztráció közben")

    return render(request, "base/login_register.html", {'form': form})






def analogia(request,nevID):
    analogia = Jegy1.objects.get(nevID=nevID)

    context = {"analogia": analogia} # ez egy objektum

    return render(request,"analogiak/analogia.html", context )


def createAnalogia(request):
    form = AnalogiaForm()

    if request.method == "POST":
        form = AnalogiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("analogia_adatbazis")

    context = {'form': form}
    return render(request, "analogiak/analogia_form.html", context)

def analogia_adatbazis(request):


    context = {}
    return render(request, 'analogiak/analogia_adatbazis.html', context )




def jegy(request,nevID):
    analogia = Jegy1.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "analogiak/jegy.html", context)

def bolygo(request,nevID):
    analogia = Bolygo1.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "analogiak/bolygo.html", context)

def haz(request,nevID):
    analogia = Haz1.objects.get(nevID=nevID)

    context = {"analogia": analogia}  # ez egy objektum

    return render(request, "analogiak/haz.html", context)




def jegyek_oldal(request):

    jegyek = Jegy1.objects.all()

    context = {'adatok': jegyek}
    return render(request, 'analogiak/jegyek.html', context )


def bolygok_oldal(request):

    bolygok = Bolygo1.objects.all()

    context = {'adatok': bolygok}
    return render(request, 'analogiak/bolygok.html', context )


def hazak_oldal(request):

    hazak = Haz1.objects.all()

    context = {'adatok': hazak}
    return render(request, 'analogiak/hazak.html', context )




def createJegyek(request):
    form = JegyekForm()

    if request.method == "POST":
        form = JegyekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jegyek")

    context = {'form': form}
    return render(request, "analogiak/jegyek_form.html", context)


def createBolygok(request):
    form = BolygokForm()

    if request.method == "POST":
        form = BolygokForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bolygok")

    context = {'form': form}
    return render(request, "analogiak/bolygok_form.html", context)


def createHazak(request):
    form = HazakForm()

    if request.method == "POST":
        form = HazakForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hazak")

    context = {'form': form}
    return render(request, "analogiak/hazak_form.html", context)


def deleteBolygo(request, nevID):
    bolygo = Bolygo1.objects.get(nevID=nevID)
    if request.method == "POST":
        bolygo.delete()
        return redirect("bolygok")
    return render(request, "base/delete.html", {"obj":bolygo})

def deleteJegy(request, nevID):
    jegy = Jegy1.objects.get(nevID=nevID)
    if request.method == "POST":
        jegy.delete()
        return redirect("jegyek")
    return render(request, "base/delete.html", {"obj":jegy})

def deleteHaz(request,nevID):
    haz = Haz1.objects.get(nevID=nevID)
    if request.method == "POST":
        haz.delete()
        return redirect("hazak")
    return render(request, "base/delete.html", {"obj":haz})







# def updateAnalogia(request, nevID):
#     analogia = Analogia.objects.get(id=nevID)
#     form = AnalogiaForm(instance=analogia)
#
#     if request.method == 'POST':
#         form = RoomForm(request.POST, instance=room)
#         if form.is_valid():
#             form.save()
#             return redirect("home") #todo ne homrea terjen vissza
#
#     context = {'form': form}
#     return render(request, "base/room_form.html", context)