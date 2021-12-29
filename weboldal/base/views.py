from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .models import Room2, Topic2, Jegy2, Bolygo2, Haz2, Message2 ,BolygoHazban2, BolygoJegyben2, HazJegyben2
from django.contrib.auth.models import User
from .forms import RoomForm, AnalogiaForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'base/kezdolap.html', {} )


def room(request, pk):
    room = Room2.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created') # give us a set of messages that are related specific rooms
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message2.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get("body"),
        )
        room.participants.add(request.user)

        return redirect('room', pk=room.id)

    context = {"room": room, "messages": room_messages, 'participants': participants}
    return render(request, "base/room.html",context)



@login_required(login_url="login")
def updateRoom( request, pk):
    room = Room2.objects.get(id= pk)
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


def analogia_adatbazis(request):

    context = {}
    return render(request, 'base/analogia_adatbazis.html', context )


def titkosSzoba(request):
    return render(request, "base/titkosSzoba.html", {})


def rolunk(request):
    return render(request, "base/rolunk.html", {})


